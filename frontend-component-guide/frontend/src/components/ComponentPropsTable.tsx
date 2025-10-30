import React from 'react';
import { Table, Tag, Typography } from 'antd';
import { Component } from '../types';

const { Text } = Typography;

interface ComponentPropsTableProps {
  component: Component;
  language: 'zh' | 'en';
}

const ComponentPropsTable: React.FC<ComponentPropsTableProps> = ({ component, language }) => {
  const columns = [
    {
      title: language === 'zh' ? '属性名' : 'Property Name',
      dataIndex: 'name',
      key: 'name',
      width: 150,
      render: (text: string) => <Text code>{text}</Text>,
    },
    {
      title: language === 'zh' ? '说明' : 'Description',
      dataIndex: 'description',
      key: 'description',
      render: (description: any) => description[language],
    },
    {
      title: language === 'zh' ? '类型' : 'Type',
      dataIndex: 'type',
      key: 'type',
      width: 120,
      render: (type: string) => <Tag color="blue">{type}</Tag>,
    },
    {
      title: language === 'zh' ? '默认值' : 'Default Value',
      dataIndex: 'default',
      key: 'default',
      width: 120,
      render: (defaultValue: string) => {
        if (defaultValue === '-') {
          return <Text type="secondary">-</Text>;
        }
        return <Text code>{defaultValue}</Text>;
      },
    },
    {
      title: language === 'zh' ? '可选值' : 'Options',
      dataIndex: 'options',
      key: 'options',
      width: 150,
      render: (options: string[] | undefined) => {
        if (!options || options.length === 0) {
          return <Text type="secondary">-</Text>;
        }
        return (
          <div>
            {options.map((option, index) => (
              <Tag key={index} style={{ marginBottom: 4 }}>{option}</Tag>
            ))}
          </div>
        );
      },
    },
  ];

  return (
    <div style={{ padding: '24px' }}>
      <Table
        columns={columns}
        dataSource={component.props}
        rowKey="name"
        pagination={false}
        bordered
        size="middle"
      />
    </div>
  );
};

export default ComponentPropsTable;