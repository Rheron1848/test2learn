"""
一个集成工具调用、RAG、输出解析与记忆的 LangChain Agent 示例
"""
import os, uuid
from typing import List
from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.tools import Tool

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.tools import StructuredTool
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

# ---------- 1. 初始化 LLM ----------
llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)

# ---------- 2. 工具 ----------
# 2.1 搜索工具（使用 SerpAPI；也可换成 DuckDuckGoSearchRun）
search = SerpAPIWrapper()

# 2.2 计算工具
def calculator(expression: str) -> str:
    """
    计算数学表达式并返回字符串结果
    例如: "3**5 / 7"
    """
    try:
        ans = eval(expression, {"__builtins__": None}, {})
        return str(ans)
    except Exception as e:
        return f"计算错误: {e}"

calc_tool = StructuredTool.from_function(
    func=calculator,
    name="Calculator",
    description="执行数学表达式，例如 2+3*4 或 3**5/7"
)

tools = [
    Tool(name="Search", func=search.run, description="实时互联网搜索"),
    calc_tool
]

# ---------- 3. RAG ----------
# 3.1 加载并切分文档（这里用 LangChain 官方博客做示例）
loader = WebBaseLoader(["https://blog.langchain.dev/"])
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
splits = text_splitter.split_documents(docs)

# 3.2 向量存储
embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(
    documents=splits,
    embedding=embedding,
    collection_name="langchain_blog",
    persist_directory="./chroma_db"
)
retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# 3.3 RAG chain（独立检索器，供 Agent 调用）
rag_chain = (
    {"context": retriever | (lambda docs: "\n".join(d.page_content for d in docs)),
     "question": RunnablePassthrough()}
    | ChatPromptTemplate.from_template(
        "你是 LangChain 助手，根据以下上下文回答用户问题：\n{context}\n用户问题：{question}")
    | llm
    | StrOutputParser()
)

# 把检索器封装成工具，使 Agent 可以调用
def rag_tool_func(query: str) -> str:
    return rag_chain.invoke(query)

rag_tool = Tool(
    name="LangChainBlogRetriever",
    func=rag_tool_func,
    description="从 LangChain 官方博客检索相关信息，回答技术问题"
)
tools.append(rag_tool)

# ---------- 4. 记忆 ----------
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# ---------- 5. 输出解析 ----------
class AgentOutput(BaseModel):
    answer: str = Field(description="最终给用户看的答案")
    sources: List[str] = Field(default_factory=list, description="参考来源链接")

# 5.1 定义系统提示
system_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "你是全能助手，可使用工具：搜索、计算、知识库检索。请按以下 JSON 格式回答：\n"
     '{"answer": "...", "sources": ["..."]}'),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# 5.2 创建 agent
agent = create_openai_tools_agent(llm, tools, system_prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    return_intermediate_steps=True
)

# ---------- 6. 封装运行函数 ----------
def run_agent(query: str) -> AgentOutput:
    result = agent_executor.invoke({"input": query})
    # 简单解析：把 LLM 输出当 json
    import json
    try:
        data = json.loads(result["output"])
    except Exception:
        # 如果 LLM 没返回合法 JSON，就兜底
        data = {"answer": result["output"], "sources": []}
    return AgentOutput(**data)

# ---------- 7. 测试 ----------
if __name__ == "__main__":
    while True:
        q = input("\n用户> ")
        if q in {"exit", "quit"}:
            break
        resp = run_agent(q)
        print("助手> ", resp.answer)
        if resp.sources:
            print("来源> ", resp.sources)