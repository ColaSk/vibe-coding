# Vue 3 开发规范文档

欢迎使用Vue 3开发规范文档。本文档提供了完整的开发规范、工具配置和最佳实践指南。

## 文档目录

### 核心文档

- **[开发规范](./development-standards.md)** - 完整的Vue 3开发规范文档
  - 概述和适用范围
  - 开发工具配置
  - 代码风格规范
  - 最佳实践
  - 工作流程
  - 常见问题

### 工具规则文档

- **[ESLint规则](./eslint-rules.md)** - ESLint代码检查规则
  - 配置文件说明
  - Vue组件规则
  - JavaScript规则
  - 代码风格规则
  - 最佳实践

- **[Prettier规则](./prettier-rules.md)** - Prettier代码格式化规则
  - 配置文件说明
  - 格式化规则
  - 语言特定规则
  - 集成配置
  - 常见问题

- **[Stylelint规则](./stylelint-rules.md)** - Stylelint样式检查规则
  - 配置文件说明
  - 基础规则
  - 代码风格规则
  - 属性排序规则
  - Vue特定规则

### 快速开始

- **[快速开始指南](./quick-start.md)** - 快速上手指南
  - 环境准备
  - 安装依赖
  - 配置编辑器
  - 使用工具
  - 开发流程
  - 常见问题

## 快速导航

### 按主题查找

#### Vue组件开发
- [组件命名规范](./development-standards.md#32-vue组件规范)
- [组件结构规范](./development-standards.md#322-组件结构)
- [Props定义](./development-standards.md#323-props定义)
- [Emits定义](./development-standards.md#324-emits定义)

#### JavaScript/TypeScript
- [变量声明](./development-standards.md#311-变量声明)
- [函数定义](./development-standards.md#312-函数定义)
- [对象和数组](./development-standards.md#313-对象和数组)
- [异步编程](./development-standards.md#315-异步编程)

#### CSS样式
- [命名规范](./development-standards.md#331-命名规范)
- [属性排序](./development-standards.md#332-属性排序)
- [选择器规范](./development-standards.md#333-选择器规范)
- [颜色规范](./development-standards.md#334-颜色规范)

#### 工具使用
- [ESLint使用](./quick-start.md#41-eslint)
- [Prettier使用](./quick-start.md#42-prettier)
- [Stylelint使用](./quick-start.md#43-stylelint)

### 按问题查找

#### 配置问题
- [如何禁用ESLint规则](./eslint-rules.md#7-常见问题)
- [Prettier和ESLint冲突](./prettier-rules.md#61-prettier和eslint冲突怎么办)
- [Stylelint不支持特定语法](./stylelint-rules.md#8-常见问题)

#### 编辑器配置
- [VS Code配置](./quick-start.md#31-vs-code)
- [WebStorm配置](./quick-start.md#32-webstorm)
- [Vim/Neovim配置](./quick-start.md#33-vimneovim)

#### 开发流程
- [日常开发流程](./quick-start.md#51-日常开发流程)
- [Git Hooks配置](./quick-start.md#52-git-hooks配置可选)
- [CI/CD集成](./quick-start.md#53-cicd集成)

## 工具概览

### ESLint
- **作用**：JavaScript和Vue代码检查
- **配置文件**：`.eslintrc.cjs`
- **命令**：`npm run lint`
- **文档**：[ESLint规则文档](./eslint-rules.md)

### Prettier
- **作用**：代码格式化
- **配置文件**：`.prettierrc.json`
- **命令**：`npm run format`
- **文档**：[Prettier规则文档](./prettier-rules.md)

### Stylelint
- **作用**：CSS样式检查
- **配置文件**：`.stylelintrc.cjs`
- **命令**：`npm run lint:style`
- **文档**：[Stylelint规则文档](./stylelint-rules.md)

### EditorConfig
- **作用**：统一编辑器配置
- **配置文件**：`.editorconfig`
- **文档**：[开发规范文档](./development-standards.md#24-editorconfig)

## 常用命令

```bash
# 安装依赖
npm install

# 检查代码
npm run lint

# 检查样式
npm run lint:style

# 格式化代码
npm run format

# 自动修复代码
npm run lint -- --fix

# 自动修复样式
npm run lint:style -- --fix

# 启动开发服务器
npm run dev

# 构建项目
npm run build
```

## 配置文件

| 文件 | 说明 |
|------|------|
| `.eslintrc.cjs` | ESLint配置文件 |
| `.prettierrc.json` | Prettier配置文件 |
| `.stylelintrc.cjs` | Stylelint配置文件 |
| `.editorconfig` | EditorConfig配置文件 |
| `.eslintignore` | ESLint忽略文件 |
| `.prettierignore` | Prettier忽略文件 |
| `.stylelintignore` | Stylelint忽略文件 |

## 最佳实践

### 组件设计
- [单一职责原则](./development-standards.md#411-单一职责)
- [组件复用](./development-standards.md#412-组件复用)
- [Props设计](./development-standards.md#413-props设计)

### 性能优化
- [使用计算属性](./development-standards.md#421-使用计算属性)
- [使用v-show和v-if](./development-standards.md#422-使用v-show和v-if)
- [列表渲染优化](./development-standards.md#423-列表渲染优化)
- [懒加载组件](./development-standards.md#424-懒加载组件)

### 安全性
- [避免XSS攻击](./development-standards.md#431-避免xss攻击)
- [验证用户输入](./development-standards.md#432-验证用户输入)
- [使用HTTPS](./development-standards.md#433-使用https)

## 常见问题

### 安装问题
- [依赖安装失败](./quick-start.md#61-安装问题)
- [权限错误](./quick-start.md#61-安装问题)

### 工具问题
- [ESLint找不到配置文件](./quick-start.md#62-eslint问题)
- [Prettier和ESLint冲突](./quick-start.md#63-prettier问题)
- [Stylelint不支持特定语法](./quick-start.md#64-stylelint问题)

### 编辑器问题
- [VS Code不自动格式化](./quick-start.md#65-编辑器问题)
- [WebStorm不自动检查](./quick-start.md#65-编辑器问题)

## 进阶配置

- [自定义规则](./quick-start.md#71-自定义规则)
- [文件特定配置](./quick-start.md#72-文件特定配置)
- [性能优化](./quick-start.md#73-性能优化)
- [团队协作](./quick-start.md#74-团队协作)

## 外部资源

### 官方文档
- [Vue 3官方文档](https://vuejs.org/)
- [ESLint官方文档](https://eslint.org/)
- [Prettier官方文档](https://prettier.io/)
- [Stylelint官方文档](https://stylelint.io/)

### 社区资源
- [Vue风格指南](https://vuejs.org/style-guide/)
- [JavaScript最佳实践](https://github.com/ryanmcdermott/clean-code-javascript)
- [CSS技巧](https://css-tricks.com/)

## 文档维护

- **维护团队**：开发团队
- **最后更新**：2026-02-27
- **文档版本**：1.0.0

## 贡献指南

如果您发现文档中的错误或有改进建议，欢迎提交Issue或Pull Request。

## 许可证

本文档遵循项目的许可证。

---

**开始使用**：建议从[快速开始指南](./quick-start.md)开始，了解如何配置和使用这些工具。

**深入学习**：阅读[开发规范文档](./development-standards.md)了解完整的开发规范和最佳实践。

**问题解决**：查看各工具规则文档中的[常见问题](./eslint-rules.md#7-常见问题)部分，解决遇到的问题。
