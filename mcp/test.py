# from https://modelcontextprotocol.io/docs/concepts/transports#python-client

# Standard Input/Output (stdio):
# server:
app = Server("example-server")

async with stdio_server() as streams:
    await app.run(
        streams[0],
        streams[1],
        app.create_initialization_options()
    )
    
    
#client:
params = StdioServerParameters(
    command="./server",
    args=["--option", "value"]
)

async with stdio_client(params) as streams:
    async with ClientSession(streams[0], streams[1]) as session:
        await session.initialize()
        

#streamable HTTP:
# server:
from mcp.server.http import HttpServerTransport
from starlette.applications import Starlette
from starlette.routing import Route

app = Server("example-server")

async def handle_mcp(scope, receive, send):
    if scope["method"] == "POST":
        # Handle JSON-RPC request
        response = await app.handle_request(request_body)

        if needs_streaming:
            # Return SSE stream
            await send_sse_response(send, response)
        else:
            # Return JSON response
            await send_json_response(send, response)

    elif scope["method"] == "GET":
        # Optional: Support server-initiated SSE streams
        await send_sse_stream(send)

starlette_app = Starlette(
    routes=[
        Route("/mcp", endpoint=handle_mcp, methods=["POST", "GET"]),
    ]
)

# client:
async with http_client("http://localhost:8000/mcp") as transport:
    async with ClientSession(transport[0], transport[1]) as session:
        await session.initialize()
        
        
        
'''
Streamable HTTP
The Streamable HTTP transport uses HTTP POST requests for client-to-server communication and optional Server-Sent Events (SSE) streams for server-to-client communication.

Use Streamable HTTP when:

Building web-based integrations
Needing client-server communication over HTTP
Requiring stateful sessions
Supporting multiple concurrent clients
Implementing resumable connections
​
How it Works
Client-to-Server Communication: Every JSON-RPC message from client to server is sent as a new HTTP POST request to the MCP endpoint
Server Responses: The server can respond either with:
A single JSON response (Content-Type: application/json)
An SSE stream (Content-Type: text/event-stream) for multiple messages
Server-to-Client Communication: Servers can send requests/notifications to clients via:
SSE streams initiated by client requests
SSE streams from HTTP GET requests to the MCP endpoint

可流式传输的HTTP
传输使用HTTP POST请求进行客户端到服务器的通信，并使用可选的服务器发送事件（SSE）流进行服务器到客户端的通信。

在以下情况下使用可流式传输的HTTP：
- 构建基于Web的集成
- 需要通过HTTP进行客户端 - 服务器通信
- 需要有状态会话
- 支持多个并发客户端
- 实现可恢复连接

其工作原理如下：
- **客户端到服务器通信**：从客户端到服务器的每个JSON - RPC消息都作为一个新的HTTP POST请求发送到MCP端点。
- **服务器响应**：服务器可以通过以下方式进行响应：
    - 单个JSON响应（Content-Type: application/json）
    - 用于多个消息的SSE流（Content-Type: text/event-stream）
- **服务器到客户端通信**：服务器可以通过以下方式向客户端发送请求/通知：
    - 由客户端请求发起的SSE流
    - 来自对MCP端点的HTTP GET请求的SSE流
'''

