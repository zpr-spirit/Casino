# CSMAR 智能财经报告分析平台

这是一个基于Vue 3的智能财经报告分析平台前端项目，实现了类似CSMAR平台的功能界面。

## 功能特性

- 🏠 **首页** - 平台概览和功能导航
- 📊 **智能分析** - 个股分析和投资组合管理
- 📄 **我的报告** - 报告管理（开发中）
- 🔢 **量化分析** - 量化投资分析（开发中）

## 技术栈

- Vue 3
- Vue Router 4
- Element Plus
- Vite
- Sass

## 项目结构

```
src/
├── components/          # 公共组件
│   └── Sidebar.vue     # 左侧导航栏
├── views/              # 页面组件
│   ├── Home.vue        # 首页
│   ├── StockAnalysis.vue # 个股分析页面
│   ├── Reports.vue     # 我的报告
│   └── Quantitative.vue # 量化分析
├── router/             # 路由配置
│   └── index.js
├── App.vue             # 根组件
├── main.js             # 入口文件
└── style.css           # 全局样式
```

## 安装和运行

1. 安装依赖：
```bash
npm install
```

2. 启动开发服务器：
```bash
npm run dev
```

3. 构建生产版本：
```bash
npm run build
```

## 主要功能

### 投资组合分析
- 支持输入2-5只股票进行组合分析
- 历史组合管理
- 快速生成报告功能
- 组合删除功能

### 界面设计
- 响应式布局
- 现代化UI设计
- 深蓝色主题配色
- 卡片式布局

## 开发说明

项目使用Vue 3 Composition API开发，采用Element Plus作为UI组件库，使用Vite作为构建工具。

左侧导航栏包含四个主要模块，其中智能分析模块已实现个股分析功能，其他模块预留了接口供后续开发。
