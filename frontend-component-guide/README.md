# 前端组件中英文对照学习系统

一个交互式的前端组件学习工具，帮助开发者快速掌握常用前端组件的中英文名称、使用方法和属性说明。

## 🚀 功能特性

- **组件分类展示**: 基础组件、布局组件、导航组件、数据录入组件、数据展示组件、反馈组件
- **中英文切换**: 支持中文和英文界面切换，方便学习组件的专业术语
- **交互式预览**: 每个组件都有实时预览，可以交互体验
- **代码示例**: 提供完整的代码示例，支持一键复制
- **属性说明**: 详细的组件属性表格，包含类型、默认值、可选值等
- **搜索功能**: 快速搜索组件名称和描述

## 🛠️ 技术栈

### 后端
- **FastAPI**: 高性能 Python Web 框架
- **Pydantic**: 数据验证和序列化
- **Uvicorn**: ASGI 服务器

### 前端
- **React 18**: 现代化前端框架
- **TypeScript**: 类型安全的 JavaScript
- **Ant Design**: 企业级 UI 设计语言和 React 组件库
- **Axios**: HTTP 客户端

## 📦 安装和运行

### 1. 克隆项目
```bash
git clone <项目地址>
cd frontend-component-guide
```

### 2. 启动项目

#### Windows
```bash
start.bat
```

#### macOS/Linux
```bash
chmod +x start.sh
./start.sh
```

### 3. 手动启动（可选）

#### 后端
```bash
cd backend
pip install -r requirements.txt
python main.py
```

#### 前端
```bash
cd frontend
npm install
npm start
```

## 🌐 访问地址

- 前端应用: http://localhost:3000
- 后端 API: http://localhost:8000
- API 文档: http://localhost:8000/docs

## 📋 组件列表

### 基础组件 (Basic Components)
- Button 按钮
- Input 输入框
- Select 选择器
- Radio 单选框
- Checkbox 多选框
- Switch 开关
- Slider 滑块

### 布局组件 (Layout Components)
- Grid 栅格
- Layout 布局
- Space 间距
- Divider 分割线

### 导航组件 (Navigation Components)
- Menu 菜单
- Breadcrumb 面包屑
- Dropdown 下拉菜单
- Pagination 分页

### 数据录入组件 (Data Entry Components)
- Form 表单
- Upload 上传
- DatePicker 日期选择框
- TimePicker 时间选择框
- Cascader 级联选择

### 数据展示组件 (Data Display Components)
- Table 表格
- List 列表
- Card 卡片
- Calendar 日历
- Tree 树形控件

### 反馈组件 (Feedback Components)
- Modal 对话框
- Progress 进度条
- Message 全局提示
- Notification 通知提醒框
- Popconfirm 气泡确认框

## 🔧 开发指南

### 添加新组件

1. **后端**: 在 `backend/main.py` 的 `COMPONENTS_DATA` 中添加新组件数据
2. **前端**: 在 `ComponentPreview.tsx` 中添加对应的预览逻辑

### 组件数据格式
```typescript
{
  id: 'component-id',
  name: { zh: '中文名', en: 'English Name' },
  description: { zh: '中文描述', en: 'English Description' },
  category: 'basic',
  props: [
    {
      name: 'propName',
      type: 'string',
      default: 'defaultValue',
      description: { zh: '属性说明', en: 'Property Description' },
      options: ['option1', 'option2'] // 可选
    }
  ],
  codeExample: '代码示例'
}
```

## 📱 界面预览

### 主界面
- 左侧分类导航
- 中间组件列表
- 右侧详细展示

### 组件详情页
- 预览标签页：交互式组件展示
- 代码标签页：可复制的代码示例
- 属性标签页：详细的属性说明表格

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 📝 许可证

MIT License

## 👥 作者

- 项目创建者: Claude AI Assistant

## 🙏 致谢

- [Ant Design](https://ant.design/) - 优秀的 React UI 组件库
- [FastAPI](https://fastapi.tiangolo.com/) - 现代、快速的 Web 框架
- [React](https://reactjs.org/) - 用于构建用户界面的 JavaScript 库

---

如果你有任何问题或建议，欢迎提交 Issue 或 Pull Request！

Happy Coding! 🎉