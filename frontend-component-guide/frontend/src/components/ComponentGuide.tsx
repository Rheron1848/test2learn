import React, { useState, useEffect } from 'react';
import {
  Layout,
  Menu,
  Card,
  Typography,
  Space,
  Tag,
  Button,
  Input,
  Row,
  Col,
  Table,
  Modal,
  Form,
  Divider,
  Tabs,
  Alert,
  Switch,
  Select,
  Radio,
  Checkbox,
  DatePicker,
  Slider,
  Progress,
  Badge,
  Avatar,
  Breadcrumb,
  Dropdown,
  Pagination,
  Spin,
  message,
  notification
} from 'antd';
import {
  AppstoreOutlined,
  CodeOutlined,
  EyeOutlined,
  BookOutlined,
  TranslationOutlined,
  SearchOutlined
} from '@ant-design/icons';
import { componentApi } from '../services/api';
import { Component, Category } from '../types';
import ComponentPreview from './ComponentPreview';
import ComponentPropsTable from './ComponentPropsTable';
import CodeEditor from './CodeEditor';

const { Header, Sider, Content } = Layout;
const { Title, Text, Paragraph } = Typography;
const { TabPane } = Tabs;

const ComponentGuide: React.FC = () => {
  const [categories, setCategories] = useState<Record<string, Category>>({});
  const [selectedCategory, setSelectedCategory] = useState<string>('basic');
  const [selectedComponent, setSelectedComponent] = useState<Component | null>(null);
  const [language, setLanguage] = useState<'zh' | 'en'>('zh');
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadComponents();
  }, []);

  const loadComponents = async () => {
    try {
      setLoading(true);
      const data = await componentApi.getAllComponents();
      setCategories(data.categories);
      // 默认选择第一个组件
      const firstCategory = Object.keys(data.categories)[0];
      if (firstCategory && data.categories[firstCategory].components.length > 0) {
        setSelectedCategory(firstCategory);
        setSelectedComponent(data.categories[firstCategory].components[0]);
      }
    } catch (error) {
      console.error('Failed to load components:', error);
      message.error('加载组件数据失败');
    } finally {
      setLoading(false);
    }
  };

  const handleCategorySelect = (categoryKey: string) => {
    setSelectedCategory(categoryKey);
    if (categories[categoryKey]?.components.length > 0) {
      setSelectedComponent(categories[categoryKey].components[0]);
    }
  };

  const handleComponentSelect = (component: Component) => {
    setSelectedComponent(component);
  };

  const toggleLanguage = () => {
    setLanguage(language === 'zh' ? 'en' : 'zh');
  };

  const filteredComponents = categories[selectedCategory]?.components.filter(component =>
    component.name[language].toLowerCase().includes(searchTerm.toLowerCase()) ||
    component.description[language].toLowerCase().includes(searchTerm.toLowerCase())
  ) || [];

  const menuItems = Object.entries(categories).map(([key, category]) => ({
    key,
    icon: React.createElement(AppstoreOutlined),
    label: category.title,
  }));

  if (loading) {
    return (
      <Layout style={{ minHeight: '100vh' }}>
        <Content style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
          <Spin size="large" />
        </Content>
      </Layout>
    );
  }

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header style={{ background: '#fff', padding: '0 24px', display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderBottom: '1px solid #f0f0f0' }}>
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <BookOutlined style={{ fontSize: '24px', marginRight: '16px' }} />
          <Title level={3} style={{ margin: 0 }}>
            {language === 'zh' ? '前端组件中英文对照' : 'Frontend Components Guide'}
          </Title>
        </div>
        <Space>
          <Input
            placeholder={language === 'zh' ? '搜索组件...' : 'Search components...'}
            prefix={<SearchOutlined />}
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{ width: 200 }}
          />
          <Button
            icon={<TranslationOutlined />}
            onClick={toggleLanguage}
          >
            {language === 'zh' ? 'EN' : '中文'}
          </Button>
        </Space>
      </Header>

      <Layout>
        <Sider width={280} style={{ background: '#fff', borderRight: '1px solid #f0f0f0' }}>
          <div style={{ padding: '16px' }}>
            <Menu
              mode="inline"
              selectedKeys={[selectedCategory]}
              items={menuItems}
              onClick={({ key }) => handleCategorySelect(key)}
              style={{ border: 'none' }}
            />

            <Divider />

            <div style={{ padding: '8px 16px' }}>
              <Text strong>
                {language === 'zh' ? '组件列表' : 'Component List'}
              </Text>
            </div>

            <div style={{ maxHeight: 'calc(100vh - 300px)', overflowY: 'auto' }}>
              {filteredComponents.map((component) => (
                <div
                  key={component.id}
                  onClick={() => handleComponentSelect(component)}
                  style={{
                    padding: '12px 16px',
                    cursor: 'pointer',
                    backgroundColor: selectedComponent?.id === component.id ? '#e6f7ff' : 'transparent',
                    borderLeft: selectedComponent?.id === component.id ? '3px solid #1890ff' : '3px solid transparent',
                    transition: 'all 0.3s'
                  }}
                >
                  <div style={{ fontWeight: 500 }}>{component.name[language]}</div>
                  <Text type="secondary" style={{ fontSize: '12px' }}>
                    {component.description[language]}
                  </Text>
                </div>
              ))}
            </div>
          </div>
        </Sider>

        <Content style={{ padding: '24px', background: '#f5f5f5' }}>
          {selectedComponent && (
            <Card>
              <div style={{ marginBottom: '24px' }}>
                <Space align="center" style={{ marginBottom: '16px' }}>
                  <Title level={2} style={{ margin: 0 }}>
                    {selectedComponent.name[language]}
                  </Title>
                  <Tag color="blue">{selectedComponent.id}</Tag>
                </Space>
                <Paragraph>
                  {selectedComponent.description[language]}
                </Paragraph>
              </div>

              <Tabs defaultActiveKey="preview">
                <TabPane
                  tab={
                    <span>
                      <EyeOutlined />
                      {language === 'zh' ? ' 组件预览' : ' Component Preview'}
                    </span>
                  }
                  key="preview"
                >
                  <ComponentPreview component={selectedComponent} language={language} />
                </TabPane>

                <TabPane
                  tab={
                    <span>
                      <CodeOutlined />
                      {language === 'zh' ? ' 代码示例' : ' Code Example'}
                    </span>
                  }
                  key="code"
                >
                  <CodeEditor code={selectedComponent.codeExample} language={language} />
                </TabPane>

                <TabPane
                  tab={
                    <span>
                      <BookOutlined />
                      {language === 'zh' ? ' 属性说明' : ' Props Documentation'}
                    </span>
                  }
                  key="props"
                >
                  <ComponentPropsTable component={selectedComponent} language={language} />
                </TabPane>
              </Tabs>
            </Card>
          )}
        </Content>
      </Layout>
    </Layout>
  );
};

export default ComponentGuide;