import React, { useState } from 'react';
import {
  Space,
  Button,
  Input,
  Form,
  Row,
  Col,
  Table,
  Modal,
  Menu,
  Card,
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
  message,
  notification,
  Typography
} from 'antd';
import { UserOutlined } from '@ant-design/icons';
import { Component } from '../types';

const { Title, Text } = Typography;
const { Option } = Select;
const { RangePicker } = DatePicker;

interface ComponentPreviewProps {
  component: Component;
  language: 'zh' | 'en';
}

const ComponentPreview: React.FC<ComponentPreviewProps> = ({ component, language }) => {
  const [modalVisible, setModalVisible] = useState(false);
  const [inputValue, setInputValue] = useState('');
  const [switchChecked, setSwitchChecked] = useState(false);
  const [selectedValue, setSelectedValue] = useState('option1');
  const [checkboxValues, setCheckboxValues] = useState(['A']);
  const [dateValue, setDateValue] = useState(null);
  const [sliderValue, setSliderValue] = useState(30);

  const handleButtonClick = () => {
    message.success(language === 'zh' ? '按钮被点击了！' : 'Button clicked!');
  };

  const showModal = () => {
    setModalVisible(true);
  };

  const handleModalOk = () => {
    setModalVisible(false);
    message.success(language === 'zh' ? '确认操作' : 'Confirmed');
  };

  const handleModalCancel = () => {
    setModalVisible(false);
  };

  const handleFormFinish = (values: any) => {
    console.log('Form values:', values);
    message.success(language === 'zh' ? '表单提交成功！' : 'Form submitted successfully!');
  };

  const menuItems = [
    { key: '1', label: language === 'zh' ? '菜单项 1' : 'Menu Item 1' },
    { key: '2', label: language === 'zh' ? '菜单项 2' : 'Menu Item 2' },
    { key: '3', label: language === 'zh' ? '菜单项 3' : 'Menu Item 3' },
  ];

  const tableData = [
    { key: '1', name: 'John Brown', age: 32, address: 'New York No. 1 Lake Park' },
    { key: '2', name: 'Jim Green', age: 42, address: 'London No. 1 Lake Park' },
    { key: '3', name: 'Joe Black', age: 32, address: 'Sidney No. 1 Lake Park' },
  ];

  const tableColumns = [
    { title: language === 'zh' ? '姓名' : 'Name', dataIndex: 'name', key: 'name' },
    { title: language === 'zh' ? '年龄' : 'Age', dataIndex: 'age', key: 'age' },
    { title: language === 'zh' ? '地址' : 'Address', dataIndex: 'address', key: 'address' },
  ];

  const renderPreview = () => {
    switch (component.id) {
      case 'button':
        return (
          <Space wrap>
            <Button type="primary" onClick={handleButtonClick}>
              {language === 'zh' ? '主要按钮' : 'Primary Button'}
            </Button>
            <Button>{language === 'zh' ? '默认按钮' : 'Default Button'}</Button>
            <Button type="dashed">{language === 'zh' ? '虚线按钮' : 'Dashed Button'}</Button>
            <Button type="text">{language === 'zh' ? '文字按钮' : 'Text Button'}</Button>
            <Button type="link">{language === 'zh' ? '链接按钮' : 'Link Button'}</Button>
            <Button type="primary" loading>
              {language === 'zh' ? '加载中' : 'Loading'}
            </Button>
            <Button type="primary" disabled>
              {language === 'zh' ? '禁用按钮' : 'Disabled Button'}
            </Button>
          </Space>
        );

      case 'input':
        return (
          <Space direction="vertical" style={{ width: '100%' }}>
            <Input
              placeholder={language === 'zh' ? '请输入内容' : 'Please input'}
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
            />
            <Input.TextArea
              placeholder={language === 'zh' ? '请输入多行文本' : 'Please input multiple lines'}
              rows={4}
            />
            <Input.Search
              placeholder={language === 'zh' ? '搜索' : 'Search'}
              onSearch={(value) => message.info(`${language === 'zh' ? '搜索' : 'Search'}: ${value}`)}
            />
            <Input.Password
              placeholder={language === 'zh' ? '请输入密码' : 'Please input password'}
            />
          </Space>
        );

      case 'grid':
        return (
          <div>
            <Row gutter={16} style={{ marginBottom: 16 }}>
              <Col span={12}>
                <Card>{language === 'zh' ? 'col-12' : 'col-12'}</Card>
              </Col>
              <Col span={12}>
                <Card>{language === 'zh' ? 'col-12' : 'col-12'}</Card>
              </Col>
            </Row>
            <Row gutter={16}>
              <Col span={8}>
                <Card>{language === 'zh' ? 'col-8' : 'col-8'}</Card>
              </Col>
              <Col span={8}>
                <Card>{language === 'zh' ? 'col-8' : 'col-8'}</Card>
              </Col>
              <Col span={8}>
                <Card>{language === 'zh' ? 'col-8' : 'col-8'}</Card>
              </Col>
            </Row>
          </div>
        );

      case 'menu':
        return (
          <div>
            <Menu
              mode="horizontal"
              defaultSelectedKeys={['1']}
              items={menuItems}
              style={{ marginBottom: 24 }}
            />
            <Menu
              mode="vertical"
              defaultSelectedKeys={['1']}
              items={menuItems}
              style={{ width: 200 }}
            />
          </div>
        );

      case 'form':
        return (
          <Form onFinish={handleFormFinish} layout="vertical" style={{ maxWidth: 400 }}>
            <Form.Item
              label={language === 'zh' ? '用户名' : 'Username'}
              name="username"
              rules={[{ required: true, message: language === 'zh' ? '请输入用户名!' : 'Please input username!' }]}
            >
              <Input placeholder={language === 'zh' ? '请输入用户名' : 'Please input username'} />
            </Form.Item>
            <Form.Item
              label={language === 'zh' ? '密码' : 'Password'}
              name="password"
              rules={[{ required: true, message: language === 'zh' ? '请输入密码!' : 'Please input password!' }]}
            >
              <Input.Password placeholder={language === 'zh' ? '请输入密码' : 'Please input password'} />
            </Form.Item>
            <Form.Item>
              <Button type="primary" htmlType="submit">
                {language === 'zh' ? '提交' : 'Submit'}
              </Button>
            </Form.Item>
          </Form>
        );

      case 'table':
        return <Table dataSource={tableData} columns={tableColumns} pagination={{ pageSize: 2 }} />;

      case 'modal':
        return (
          <div>
            <Button type="primary" onClick={showModal}>
              {language === 'zh' ? '显示对话框' : 'Show Modal'}
            </Button>
            <Modal
              title={language === 'zh' ? '对话框标题' : 'Modal Title'}
              visible={modalVisible}
              onOk={handleModalOk}
              onCancel={handleModalCancel}
            >
              <p>{language === 'zh' ? '这是一个对话框的内容' : 'This is modal content'}</p>
            </Modal>
          </div>
        );

      default:
        return (
          <Space direction="vertical" style={{ width: '100%' }}>
            <Alert
              message={language === 'zh' ? '组件预览' : 'Component Preview'}
              description={
                language === 'zh'
                  ? `这是 ${component.name.zh} 组件的交互式预览`
                  : `This is an interactive preview of ${component.name.en} component`
              }
              type="info"
            />
            <Card title={language === 'zh' ? '基础控件展示' : 'Basic Controls Display'}>
              <Space direction="vertical" style={{ width: '100%' }}>
                <Switch
                  checked={switchChecked}
                  onChange={setSwitchChecked}
                  checkedChildren={language === 'zh' ? '开' : 'On'}
                  unCheckedChildren={language === 'zh' ? '关' : 'Off'}
                />
                <Select
                  value={selectedValue}
                  onChange={setSelectedValue}
                  style={{ width: 200 }}
                >
                  <Option value="option1">{language === 'zh' ? '选项1' : 'Option 1'}</Option>
                  <Option value="option2">{language === 'zh' ? '选项2' : 'Option 2'}</Option>
                  <Option value="option3">{language === 'zh' ? '选项3' : 'Option 3'}</Option>
                </Select>
                <Checkbox.Group
                  options={[
                    { label: language === 'zh' ? '选项A' : 'Option A', value: 'A' },
                    { label: language === 'zh' ? '选项B' : 'Option B', value: 'B' },
                    { label: language === 'zh' ? '选项C' : 'Option C', value: 'C' },
                  ]}
                  value={checkboxValues}
                  onChange={setCheckboxValues}
                />
                <DatePicker
                  value={dateValue}
                  onChange={setDateValue}
                  placeholder={language === 'zh' ? '选择日期' : 'Select date'}
                />
                <div>
                  <Text>{language === 'zh' ? '滑块值: ' : 'Slider value: '}{sliderValue}</Text>
                  <Slider
                    value={sliderValue}
                    onChange={setSliderValue}
                    style={{ width: 200 }}
                  />
                </div>
                <Progress percent={sliderValue} />
                <Badge count={5}>
                  <a href="#" className="head-example" />
                </Badge>
                <Avatar size="large" icon={<UserOutlined />} />
              </Space>
            </Card>
          </Space>
        );
    }
  };

  return (
    <div style={{ padding: '24px' }}>
      {renderPreview()}
    </div>
  );
};

export default ComponentPreview;