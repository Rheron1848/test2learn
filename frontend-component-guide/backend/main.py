from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import json

app = FastAPI(title="前端组件中英文对照API", version="1.0.0")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 组件数据
COMPONENTS_DATA = {
    "general": {
        "title": "通用组件 General Components",
        "components": [
            {
                "id": "button",
                "name": {"zh": "按钮", "en": "Button"},
                "description": {"zh": "用于触发操作的基础组件", "en": "Basic component for triggering actions"},
                "category": "general",
                "props": [
                    {"name": "type", "type": "string", "default": "default", "description": {"zh": "按钮类型", "en": "Button type"}, "options": ["primary", "default", "dashed", "text", "link"]},
                    {"name": "size", "type": "string", "default": "middle", "description": {"zh": "按钮尺寸", "en": "Button size"}, "options": ["large", "middle", "small"]},
                    {"name": "disabled", "type": "boolean", "default": "false", "description": {"zh": "是否禁用", "en": "Whether disabled"}},
                    {"name": "loading", "type": "boolean", "default": "false", "description": {"zh": "是否加载中", "en": "Whether loading"}},
                    {"name": "onClick", "type": "function", "default": "-", "description": {"zh": "点击事件", "en": "Click event handler"}}
                ],
                "codeExample": """<Button type="primary" size="large" onClick={() => console.log('clicked')}>
  主要按钮
</Button>"""
            },
            {
                "id": "icon",
                "name": {"zh": "图标", "en": "Icon"},
                "description": {"zh": "语义化的矢量图形", "en": "Semantic vector graphics"},
                "category": "general",
                "props": [
                    {"name": "type", "type": "string", "default": "-", "description": {"zh": "图标类型", "en": "Icon type"}},
                    {"name": "style", "type": "CSSProperties", "default": "-", "description": {"zh": "图标样式", "en": "Icon style"}},
                    {"name": "spin", "type": "boolean", "default": "false", "description": {"zh": "是否旋转", "en": "Whether to spin"}},
                    {"name": "rotate", "type": "number", "default": "-", "description": {"zh": "旋转角度", "en": "Rotate degrees"}}
                ],
                "codeExample": """<Icon type="home" style={{ fontSize: '16px', color: '#08c' }} />"""
            },
            {
                "id": "typography",
                "name": {"zh": "排版", "en": "Typography"},
                "description": {"zh": "文本的基本格式", "en": "Basic text formatting"},
                "category": "general",
                "props": [
                    {"name": "type", "type": "string", "default": "primary", "description": {"zh": "文本类型", "en": "Text type"}, "options": ["secondary", "success", "warning", "danger"]},
                    {"name": "disabled", "type": "boolean", "default": "false", "description": {"zh": "是否禁用", "en": "Whether disabled"}},
                    {"name": "delete", "type": "boolean", "default": "false", "description": {"zh": "添加删除线样式", "en": "Deleted line style"}},
                    {"name": "mark", "type": "boolean", "default": "false", "description": {"zh": "添加标记样式", "en": "Mark style"}},
                    {"name": "underline", "type": "boolean", "default": "false", "description": {"zh": "添加下划线样式", "en": "Underline style"}},
                    {"name": "strong", "type": "boolean", "default": "false", "description": {"zh": "是否加粗", "en": "Whether bold"}}
                ],
                "codeExample": """<Text type="danger" strong>危险文本</Text>"""
            }
        ]
    },
    "basic": {
        "title": "基础组件 Basic Components",
        "components": [
            {
                "id": "input",
                "name": {"zh": "输入框", "en": "Input"},
                "description": {"zh": "基础的输入框组件", "en": "Basic input component"},
                "category": "basic",
                "props": [
                    {"name": "placeholder", "type": "string", "default": "-", "description": {"zh": "占位符", "en": "Placeholder text"}},
                    {"name": "value", "type": "string", "default": "-", "description": {"zh": "输入值", "en": "Input value"}},
                    {"name": "disabled", "type": "boolean", "default": "false", "description": {"zh": "是否禁用", "en": "Whether disabled"}},
                    {"name": "size", "type": "string", "default": "middle", "description": {"zh": "输入框尺寸", "en": "Input size"}, "options": ["large", "middle", "small"]},
                    {"name": "onChange", "type": "function", "default": "-", "description": {"zh": "值改变事件", "en": "Value change event"}}
                ],
                "codeExample": """<Input
  placeholder="请输入内容"
  value={value}
  onChange={(e) => setValue(e.target.value)}
/>"""
            },
            {
                "id": "select",
                "name": {"zh": "选择器", "en": "Select"},
                "description": {"zh": "下拉选择器", "en": "Dropdown selector"},
                "category": "basic",
                "props": [
                    {"name": "placeholder", "type": "string", "default": "-", "description": {"zh": "占位符", "en": "Placeholder text"}},
                    {"name": "value", "type": "string|string[]", "default": "-", "description": {"zh": "选中值", "en": "Selected value"}},
                    {"name": "mode", "type": "string", "default": "-", "description": {"zh": "选择模式", "en": "Selection mode"}, "options": ["multiple", "tags"]},
                    {"name": "disabled", "type": "boolean", "default": "false", "description": {"zh": "是否禁用", "en": "Whether disabled"}},
                    {"name": "onChange", "type": "function", "default": "-", "description": {"zh": "值改变事件", "en": "Value change event"}}
                ],
                "codeExample": """<Select placeholder="请选择" onChange={handleChange}>
  <Option value="option1">选项1</Option>
  <Option value="option2">选项2</Option>
</Select>"""
            },
            {
                "id": "checkbox",
                "name": {"zh": "复选框", "en": "Checkbox"},
                "description": {"zh": "复选框组件", "en": "Checkbox component"},
                "category": "basic",
                "props": [
                    {"name": "checked", "type": "boolean", "default": "false", "description": {"zh": "是否选中", "en": "Whether checked"}},
                    {"name": "disabled", "type": "boolean", "default": "false", "description": {"zh": "是否禁用", "en": "Whether disabled"}},
                    {"name": "onChange", "type": "function", "default": "-", "description": {"zh": "值改变事件", "en": "Value change event"}}
                ],
                "codeExample": """<Checkbox onChange={onChange}>复选框</Checkbox>"""
            },
            {
                "id": "radio",
                "name": {"zh": "单选框", "en": "Radio"},
                "description": {"zh": "单选框组件", "en": "Radio component"},
                "category": "basic",
                "props": [
                    {"name": "checked", "type": "boolean", "default": "false", "description": {"zh": "是否选中", "en": "Whether checked"}},
                    {"name": "disabled", "type": "boolean", "default": "false", "description": {"zh": "是否禁用", "en": "Whether disabled"}},
                    {"name": "value", "type": "string", "default": "-", "description": {"zh": "单选框的值", "en": "Radio value"}}
                ],
                "codeExample": """<Radio.Group onChange={onChange} value={value}>
  <Radio value="a">A</Radio>
  <Radio value="b">B</Radio>
</Radio.Group>"""
            },
            {
                "id": "switch",
                "name": {"zh": "开关", "en": "Switch"},
                "description": {"zh": "开关选择器", "en": "Switch selector"},
                "category": "basic",
                "props": [
                    {"name": "checked", "type": "boolean", "default": "false", "description": {"zh": "是否选中", "en": "Whether checked"}},
                    {"name": "disabled", "type": "boolean", "default": "false", "description": {"zh": "是否禁用", "en": "Whether disabled"}},
                    {"name": "loading", "type": "boolean", "default": "false", "description": {"zh": "加载中的开关", "en": "Loading switch"}},
                    {"name": "onChange", "type": "function", "default": "-", "description": {"zh": "值改变事件", "en": "Value change event"}}
                ],
                "codeExample": """<Switch checked={checked} onChange={setChecked} />"""
            }
        ]
    },
    "layout": {
        "title": "布局组件 Layout Components",
        "components": [
            {
                "id": "grid",
                "name": {"zh": "栅格", "en": "Grid"},
                "description": {"zh": "24栅格系统", "en": "24-column grid system"},
                "category": "layout",
                "props": [
                    {"name": "span", "type": "number", "default": "-", "description": {"zh": "栅格占位格数", "en": "Number of column the grid spans"}},
                    {"name": "offset", "type": "number", "default": "0", "description": {"zh": "栅格左侧间隔格数", "en": "Number of spacing on the left side"}},
                    {"name": "gutter", "type": "number", "default": "0", "description": {"zh": "栅格间隔", "en": "Grid spacing"}}
                ],
                "codeExample": """<Row gutter={16}>
  <Col span={12}>col-12</Col>
  <Col span={12}>col-12</Col>
</Row>"""
            },
            {
                "id": "space",
                "name": {"zh": "间距", "en": "Space"},
                "description": {"zh": "设置组件之间的间距", "en": "Set spacing between components"},
                "category": "layout",
                "props": [
                    {"name": "size", "type": "string|number", "default": "small", "description": {"zh": "间距大小", "en": "Spacing size"}, "options": ["small", "middle", "large"]},
                    {"name": "direction", "type": "string", "default": "horizontal", "description": {"zh": "间距方向", "en": "Spacing direction"}, "options": ["horizontal", "vertical"]},
                    {"name": "align", "type": "string", "default": "-", "description": {"zh": "对齐方式", "en": "Alignment"}, "options": ["start", "end", "center", "baseline"]},
                    {"name": "wrap", "type": "boolean", "default": "false", "description": {"zh": "是否自动换行", "en": "Whether to wrap automatically"}}
                ],
                "codeExample": """<Space size="large" direction="vertical">
  <Button>按钮1</Button>
  <Button>按钮2</Button>
</Space>"""
            },
            {
                "id": "divider",
                "name": {"zh": "分割线", "en": "Divider"},
                "description": {"zh": "区隔内容的分割线", "en": "Divider to separate content"},
                "category": "layout",
                "props": [
                    {"name": "orientation", "type": "string", "default": "center", "description": {"zh": "分割线标题的位置", "en": "Position of divider title"}, "options": ["left", "right", "center"]},
                    {"name": "type", "type": "string", "default": "horizontal", "description": {"zh": "水平还是垂直类型", "en": "Horizontal or vertical type"}, "options": ["horizontal", "vertical"]},
                    {"name": "dashed", "type": "boolean", "default": "false", "description": {"zh": "是否虚线", "en": "Whether dashed"}},
                    {"name": "plain", "type": "boolean", "default": "false", "description": {"zh": "文字是否显示为普通正文样式", "en": "Whether text is displayed as plain body text style"}}
                ],
                "codeExample": """<Divider orientation="left">左侧标题</Divider>"""
            }
        ]
    },
    "navigation": {
        "title": "导航组件 Navigation Components",
        "components": [
            {
                "id": "menu",
                "name": {"zh": "菜单", "en": "Menu"},
                "description": {"zh": "为页面和功能提供导航的菜单列表", "en": "Navigation menu for pages and functions"},
                "category": "navigation",
                "props": [
                    {"name": "mode", "type": "string", "default": "vertical", "description": {"zh": "菜单类型", "en": "Menu type"}, "options": ["vertical", "horizontal", "inline"]},
                    {"name": "selectedKeys", "type": "string[]", "default": "[]", "description": {"zh": "选中的菜单项", "en": "Selected menu items"}},
                    {"name": "onClick", "type": "function", "default": "-", "description": {"zh": "点击事件", "en": "Click event handler"}}
                ],
                "codeExample": """<Menu mode="horizontal" onClick={handleClick}>
  <Menu.Item key="home">首页</Menu.Item>
  <Menu.Item key="about">关于</Menu.Item>
</Menu>"""
            },
            {
                "id": "breadcrumb",
                "name": {"zh": "面包屑", "en": "Breadcrumb"},
                "description": {"zh": "显示当前页面在系统层级结构中的位置", "en": "Show the position of the current page in the system hierarchy"},
                "category": "navigation",
                "props": [
                    {"name": "separator", "type": "string", "default": "/", "description": {"zh": "分隔符", "en": "Separator"}},
                    {"name": "routes", "type": "array", "default": "-", "description": {"zh": "路由栈信息", "en": "Route stack information"}},
                    {"name": "itemRender", "type": "function", "default": "-", "description": {"zh": "自定义链接函数", "en": "Custom link function"}}
                ],
                "codeExample": """<Breadcrumb>
  <Breadcrumb.Item>首页</Breadcrumb.Item>
  <Breadcrumb.Item>用户管理</Breadcrumb.Item>
  <Breadcrumb.Item>详情</Breadcrumb.Item>
</Breadcrumb>"""
            },
            {
                "id": "dropdown",
                "name": {"zh": "下拉菜单", "en": "Dropdown"},
                "description": {"zh": "向下弹出的列表", "en": "Dropdown list that pops down"},
                "category": "navigation",
                "props": [
                    {"name": "trigger", "type": "string[]", "default": "[hover]", "description": {"zh": "触发行为", "en": "Trigger behavior"}, "options": ["hover", "click", "contextMenu"]},
                    {"name": "placement", "type": "string", "default": "bottomLeft", "description": {"zh": "菜单弹出位置", "en": "Menu popup position"}},
                    {"name": "disabled", "type": "boolean", "default": "false", "description": {"zh": "菜单是否禁用", "en": "Whether menu is disabled"}},
                    {"name": "overlay", "type": "Menu", "default": "-", "description": {"zh": "菜单", "en": "Menu"}}
                ],
                "codeExample": """<Dropdown overlay={menu} placement="bottomCenter">
  <Button>下拉菜单 <DownOutlined /></Button>
</Dropdown>"""
            },
            {
                "id": "pagination",
                "name": {"zh": "分页", "en": "Pagination"},
                "description": {"zh": "采用分页的形式分隔长列表", "en": "Separate long lists using pagination"},
                "category": "navigation",
                "props": [
                    {"name": "current", "type": "number", "default": "1", "description": {"zh": "当前页数", "en": "Current page number"}},
                    {"name": "total", "type": "number", "default": "0", "description": {"zh": "数据总数", "en": "Total number of data"}},
                    {"name": "pageSize", "type": "number", "default": "10", "description": {"zh": "每页条数", "en": "Number of items per page"}},
                    {"name": "showSizeChanger", "type": "boolean", "default": "false", "description": {"zh": "是否展示 pageSize 切换器", "en": "Whether to show pageSize changer"}},
                    {"name": "onChange", "type": "function", "default": "-", "description": {"zh": "页码改变的回调", "en": "Callback when page number changes"}}
                ],
                "codeExample": """<Pagination current={current} total={50} onChange={onChange} />"""
            }
        ]
    },
    "data_entry": {
        "title": "数据录入组件 Data Entry Components",
        "components": [
            {
                "id": "form",
                "name": {"zh": "表单", "en": "Form"},
                "description": {"zh": "高性能表单控件，自带数据域管理", "en": "High performance form control with data management"},
                "category": "data_entry",
                "props": [
                    {"name": "form", "type": "FormInstance", "default": "-", "description": {"zh": "表单实例", "en": "Form instance"}},
                    {"name": "layout", "type": "string", "default": "horizontal", "description": {"zh": "表单布局", "en": "Form layout"}, "options": ["horizontal", "vertical", "inline"]},
                    {"name": "onFinish", "type": "function", "default": "-", "description": {"zh": "提交成功事件", "en": "Submit success event"}}
                ],
                "codeExample": """<Form form={form} onFinish={onFinish}>
  <Form.Item name="username" rules={[{required: true}]}>
    <Input placeholder="用户名" />
  </Form.Item>
  <Form.Item>
    <Button type="primary" htmlType="submit">提交</Button>
  </Form.Item>
</Form>"""
            },
            {
                "id": "datepicker",
                "name": {"zh": "日期选择器", "en": "DatePicker"},
                "description": {"zh": "输入或选择日期的控件", "en": "Control for inputting or selecting dates"},
                "category": "data_entry",
                "props": [
                    {"name": "value", "type": "moment", "default": "-", "description": {"zh": "日期", "en": "Date"}},
                    {"name": "format", "type": "string", "default": "YYYY-MM-DD", "description": {"zh": "展示的日期格式", "en": "Display date format"}},
                    {"name": "disabled", "type": "boolean", "default": "false", "description": {"zh": "是否禁用", "en": "Whether disabled"}},
                    {"name": "placeholder", "type": "string", "default": "-", "description": {"zh": "输入框提示文字", "en": "Input placeholder text"}},
                    {"name": "onChange", "type": "function", "default": "-", "description": {"zh": "时间发生变化的回调", "en": "Callback when time changes"}}
                ],
                "codeExample": """<DatePicker onChange={onChange} placeholder="选择日期" />"""
            },
            {
                "id": "slider",
                "name": {"zh": "滑动输入条", "en": "Slider"},
                "description": {"zh": "滑动型输入器", "en": "Slide type input"},
                "category": "data_entry",
                "props": [
                    {"name": "min", "type": "number", "default": "0", "description": {"zh": "最小值", "en": "Minimum value"}},
                    {"name": "max", "type": "number", "default": "100", "description": {"zh": "最大值", "en": "Maximum value"}},
                    {"name": "step", "type": "number", "default": "1", "description": {"zh": "步长", "en": "Step size"}},
                    {"name": "value", "type": "number", "default": "-", "description": {"zh": "设置当前取值", "en": "Set current value"}},
                    {"name": "disabled", "type": "boolean", "default": "false", "description": {"zh": "是否禁用", "en": "Whether disabled"}},
                    {"name": "onChange", "type": "function", "default": "-", "description": {"zh": "回调函数", "en": "Callback function"}}
                ],
                "codeExample": """<Slider defaultValue={30} onChange={onChange} />"""
            },
            {
                "id": "upload",
                "name": {"zh": "上传", "en": "Upload"},
                "description": {"zh": "文件上传", "en": "File upload"},
                "category": "data_entry",
                "props": [
                    {"name": "action", "type": "string", "default": "-", "description": {"zh": "上传的地址", "en": "Upload URL"}},
                    {"name": "accept", "type": "string", "default": "-", "description": {"zh": "接受上传的文件类型", "en": "Accepted file types"}},
                    {"name": "multiple", "type": "boolean", "default": "false", "description": {"zh": "是否支持多选文件", "en": "Whether to support multiple file selection"}},
                    {"name": "disabled", "type": "boolean", "default": "false", "description": {"zh": "是否禁用", "en": "Whether disabled"}},
                    {"name": "onChange", "type": "function", "default": "-", "description": {"zh": "上传文件改变时的状态", "en": "Status when upload file changes"}}
                ],
                "codeExample": """<Upload action="/upload" onChange={handleChange}>
  <Button icon=<UploadOutlined />>点击上传</Button>
</Upload>"""
            }
        ]
    },
    "data_display": {
        "title": "数据展示组件 Data Display Components",
        "components": [
            {
                "id": "table",
                "name": {"zh": "表格", "en": "Table"},
                "description": {"zh": "展示行列数据", "en": "Display tabular data"},
                "category": "data_display",
                "props": [
                    {"name": "dataSource", "type": "array", "default": "[]", "description": {"zh": "数据数组", "en": "Data array"}},
                    {"name": "columns", "type": "array", "default": "[]", "description": {"zh": "表格列配置", "en": "Table column configuration"}},
                    {"name": "pagination", "type": "object|boolean", "default": "-", "description": {"zh": "分页配置", "en": "Pagination configuration"}}
                ],
                "codeExample": """<Table
  dataSource={data}
  columns={columns}
  pagination={{pageSize: 10}}
/>"""
            },
            {
                "id": "list",
                "name": {"zh": "列表", "en": "List"},
                "description": {"zh": "通用列表", "en": "General list"},
                "category": "data_display",
                "props": [
                    {"name": "dataSource", "type": "array", "default": "[]", "description": {"zh": "列表数据源", "en": "List data source"}},
                    {"name": "renderItem", "type": "function", "default": "-", "description": {"zh": "当使用 dataSource 时，可以用 renderItem 自定义渲染列表项", "en": "When using dataSource, you can use renderItem to customize the rendering of list items"}},
                    {"name": "size", "type": "string", "default": "default", "description": {"zh": "列表的尺寸", "en": "Size of list"}, "options": ["default", "large", "small"]},
                    {"name": "split", "type": "boolean", "default": "true", "description": {"zh": "是否展示分割线", "en": "Whether to show split line"}},
                    {"name": "loading", "type": "boolean", "default": "false", "description": {"zh": "当卡片内容还在加载中时，可以用 loading 展示一个占位", "en": "When the card content is still loading, you can use loading to display a placeholder"}}
                ],
                "codeExample": """<List
  dataSource={data}
  renderItem={item => (
    <List.Item>
      <List.Item.Meta
        title={item.title}
        description={item.description}
      />
    </List.Item>
  )}
/>"""
            },
            {
                "id": "card",
                "name": {"zh": "卡片", "en": "Card"},
                "description": {"zh": "通用卡片容器", "en": "General card container"},
                "category": "data_display",
                "props": [
                    {"name": "title", "type": "string|ReactNode", "default": "-", "description": {"zh": "卡片标题", "en": "Card title"}},
                    {"name": "extra", "type": "string|ReactNode", "default": "-", "description": {"zh": "卡片右上角的操作区域", "en": "Operation area in the upper right corner of the card"}},
                    {"name": "bordered", "type": "boolean", "default": "true", "description": {"zh": "是否有边框", "en": "Whether there is a border"}},
                    {"name": "loading", "type": "boolean", "default": "false", "description": {"zh": "当卡片内容还在加载中时，可以用 loading 展示一个占位", "en": "When the card content is still loading, you can use loading to display a placeholder"}},
                    {"name": "size", "type": "string", "default": "default", "description": {"zh": "卡片的尺寸", "en": "Card size"}, "options": ["default", "small"]}
                ],
                "codeExample": """<Card title="卡片标题" extra={<a href="#">更多</a>} style={{ width: 300 }}>
  <p>卡片内容</p>
</Card>"""
            },
            {
                "id": "calendar",
                "name": {"zh": "日历", "en": "Calendar"},
                "description": {"zh": "按照日历形式展示数据的容器", "en": "Container for displaying data in calendar format"},
                "category": "data_display",
                "props": [
                    {"name": "value", "type": "moment", "default": "-", "description": {"zh": "展示日期", "en": "Display date"}},
                    {"name": "mode", "type": "string", "default": "month", "description": {"zh": "初始模式", "en": "Initial mode"}, "options": ["month", "year"]},
                    {"name": "fullscreen", "type": "boolean", "default": "true", "description": {"zh": "是否全屏显示", "en": "Whether to display in full screen"}},
                    {"name": "onChange", "type": "function", "default": "-", "description": {"zh": "日期变化回调", "en": "Date change callback"}},
                    {"name": "onPanelChange", "type": "function", "default": "-", "description": {"zh": "面板变化回调", "en": "Panel change callback"}}
                ],
                "codeExample": """<Calendar onPanelChange={onPanelChange} />"""
            }
        ]
    },
    "feedback": {
        "title": "反馈组件 Feedback Components",
        "components": [
            {
                "id": "modal",
                "name": {"zh": "对话框", "en": "Modal"},
                "description": {"zh": "模态对话框", "en": "Modal dialog"},
                "category": "feedback",
                "props": [
                    {"name": "visible", "type": "boolean", "default": "false", "description": {"zh": "是否显示", "en": "Whether visible"}},
                    {"name": "title", "type": "string", "default": "-", "description": {"zh": "标题", "en": "Modal title"}},
                    {"name": "onOk", "type": "function", "default": "-", "description": {"zh": "确认事件", "en": "OK button click event"}},
                    {"name": "onCancel", "type": "function", "default": "-", "description": {"zh": "取消事件", "en": "Cancel button click event"}}
                ],
                "codeExample": """<Modal
  title="标题"
  visible={visible}
  onOk={handleOk}
  onCancel={handleCancel}
>
  <p>对话框内容</p>
</Modal>"""
            },
            {
                "id": "alert",
                "name": {"zh": "警告提示", "en": "Alert"},
                "description": {"zh": "警告提示，展现需要关注的信息", "en": "Alert messages to show information that needs attention"},
                "category": "feedback",
                "props": [
                    {"name": "message", "type": "string|ReactNode", "default": "-", "description": {"zh": "警告提示内容", "en": "Alert message content"}},
                    {"name": "type", "type": "string", "default": "info", "description": {"zh": "指定警告提示的样式", "en": "Specify the style of alert message"}, "options": ["success", "info", "warning", "error"]},
                    {"name": "closable", "type": "boolean", "default": "false", "description": {"zh": "默认不显示关闭按钮", "en": "Close button is not displayed by default"}},
                    {"name": "closeText", "type": "string|ReactNode", "default": "-", "description": {"zh": "自定义关闭按钮", "en": "Custom close button"}},
                    {"name": "onClose", "type": "function", "default": "-", "description": {"zh": "关闭时触发的回调函数", "en": "Callback function triggered when closing"}}
                ],
                "codeExample": """<Alert message="成功提示" type="success" showIcon />"""
            },
            {
                "id": "message",
                "name": {"zh": "全局提示", "en": "Message"},
                "description": {"zh": "全局展示操作反馈信息", "en": "Display operation feedback information globally"},
                "category": "feedback",
                "props": [
                    {"name": "content", "type": "string|ReactNode", "default": "-", "description": {"zh": "提示内容", "en": "Message content"}},
                    {"name": "duration", "type": "number", "default": "3", "description": {"zh": "自动关闭的延时", "en": "Delay before auto close"}},
                    {"name": "icon", "type": "ReactNode", "default": "-", "description": {"zh": "自定义图标", "en": "Custom icon"}},
                    {"name": "onClose", "type": "function", "default": "-", "description": {"zh": "关闭时触发的回调函数", "en": "Callback function triggered when closing"}}
                ],
                "codeExample": """message.success('操作成功');"""
            },
            {
                "id": "notification",
                "name": {"zh": "通知提醒框", "en": "Notification"},
                "description": {"zh": "全局展示通知提醒信息", "en": "Display notification information globally"},
                "category": "feedback",
                "props": [
                    {"name": "message", "type": "string|ReactNode", "default": "-", "description": {"zh": "通知提醒标题", "en": "Notification title"}},
                    {"name": "description", "type": "string|ReactNode", "default": "-", "description": {"zh": "通知提醒内容", "en": "Notification content"}},
                    {"name": "duration", "type": "number", "default": "4.5", "description": {"zh": "默认自动关闭延时", "en": "Default auto close delay"}},
                    {"name": "placement", "type": "string", "default": "topRight", "description": {"zh": "弹出位置", "en": "Popup position"}, "options": ["topLeft", "topRight", "bottomLeft", "bottomRight"]},
                    {"name": "type", "type": "string", "default": "info", "description": {"zh": "图标类型", "en": "Icon type"}, "options": ["success", "info", "warning", "error"]},
                    {"name": "onClose", "type": "function", "default": "-", "description": {"zh": "关闭时触发的回调函数", "en": "Callback function triggered when closing"}}
                ],
                "codeExample": """notification.open({
  message: '通知标题',
  description: '通知内容',
  placement: 'topRight'
});"""
            },
            {
                "id": "progress",
                "name": {"zh": "进度条", "en": "Progress"},
                "description": {"zh": "展示操作的当前进度", "en": "Show the current progress of operations"},
                "category": "feedback",
                "props": [
                    {"name": "percent", "type": "number", "default": "-", "description": {"zh": "百分比", "en": "Percentage"}},
                    {"name": "status", "type": "string", "default": "-", "description": {"zh": "状态", "en": "Status"}, "options": ["success", "exception", "normal", "active"]},
                    {"name": "type", "type": "string", "default": "line", "description": {"zh": "类型", "en": "Type"}, "options": ["line", "circle", "dashboard"]},
                    {"name": "strokeWidth", "type": "number", "default": "8", "description": {"zh": "进度条线的宽度", "en": "Progress bar line width"}},
                    {"name": "showInfo", "type": "boolean", "default": "true", "description": {"zh": "是否显示进度数值或状态图标", "en": "Whether to display progress value or status icon"}}
                ],
                "codeExample": """<Progress percent={30} status="active" />"""
            }
        ]
    }
}

class ComponentResponse(BaseModel):
    categories: Dict[str, Any]
    allComponents: List[Dict[str, Any]]

@app.get("/")
async def root():
    return {"message": "前端组件中英文对照API服务", "version": "1.0.0"}

@app.get("/api/components", response_model=ComponentResponse)
async def get_components():
    """获取所有组件信息"""
    all_components = []
    for category_data in COMPONENTS_DATA.values():
        all_components.extend(category_data["components"])

    return {
        "categories": COMPONENTS_DATA,
        "allComponents": all_components
    }

@app.get("/api/components/{component_id}")
async def get_component(component_id: str):
    """获取特定组件信息"""
    for category_data in COMPONENTS_DATA.values():
        for component in category_data["components"]:
            if component["id"] == component_id:
                return component

    raise HTTPException(status_code=404, detail="组件未找到")

@app.get("/api/categories")
async def get_categories():
    """获取所有分类"""
    return list(COMPONENTS_DATA.keys())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)