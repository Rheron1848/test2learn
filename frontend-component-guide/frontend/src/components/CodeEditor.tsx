import React, { useState } from 'react';
import { Card, Button, Space, Typography, message } from 'antd';
import { CopyOutlined, CheckOutlined } from '@ant-design/icons';

const { Text, Paragraph } = Typography;

interface CodeEditorProps {
  code: string;
  language: 'zh' | 'en';
}

const CodeEditor: React.FC<CodeEditorProps> = ({ code, language }) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      message.success(language === 'zh' ? '代码已复制到剪贴板！' : 'Code copied to clipboard!');
      setTimeout(() => setCopied(false), 2000);
    } catch (error) {
      message.error(language === 'zh' ? '复制失败！' : 'Copy failed!');
    }
  };

  return (
    <div style={{ padding: '24px' }}>
      <Card
        title={
          <Space style={{ width: '100%', justifyContent: 'space-between' }}>
            <span>{language === 'zh' ? '代码示例' : 'Code Example'}</span>
            <Button
              icon={copied ? <CheckOutlined /> : <CopyOutlined />}
              onClick={handleCopy}
              type={copied ? 'default' : 'primary'}
            >
              {copied ? (language === 'zh' ? '已复制' : 'Copied') : (language === 'zh' ? '复制代码' : 'Copy Code')}
            </Button>
          </Space>
        }
        style={{ marginBottom: 16 }}
      >
        <pre
          style={{
            backgroundColor: '#f5f5f5',
            padding: '16px',
            borderRadius: '6px',
            overflow: 'auto',
            fontFamily: 'Consolas, Monaco, "Courier New", monospace',
            fontSize: '14px',
            lineHeight: '1.5',
            margin: 0,
            whiteSpace: 'pre-wrap',
            wordBreak: 'break-all'
          }}
        >
          <code>{code}</code>
        </pre>
      </Card>

      <Card title={language === 'zh' ? '使用说明' : 'Usage Instructions'}>
        <Paragraph>
          {language === 'zh' ? (
            <>
              <Text>1. 复制上面的代码到你的 React 组件中</Text><br />
              <Text>2. 确保你已经正确导入了所需的 Ant Design 组件</Text><br />
              <Text>3. 根据你的需求修改属性和事件处理函数</Text><br />
              <Text>4. 运行你的应用查看效果</Text>
            </>
          ) : (
            <>
              <Text>1. Copy the code above to your React component</Text><br />
              <Text>2. Make sure you have properly imported the required Ant Design components</Text><br />
              <Text>3. Modify properties and event handlers according to your needs</Text><br />
              <Text>4. Run your application to see the effect</Text>
            </>
          )}
        </Paragraph>
      </Card>
    </div>
  );
};

export default CodeEditor;