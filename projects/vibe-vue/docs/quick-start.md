# 快速开始指南

## 目录

- [1. 环境准备](#1-环境准备)
- [2. 安装依赖](#2-安装依赖)
- [3. 配置编辑器](#3-配置编辑器)
- [4. 使用工具](#4-使用工具)
- [5. 开发流程](#5-开发流程)
- [6. 常见问题](#6-常见问题)
- [7. 进阶配置](#7-进阶配置)

---

## 1. 环境准备

### 1.1 系统要求

- **Node.js**: >= 16.0.0
- **npm**: >= 7.0.0 或 **pnpm**: >= 6.0.0 或 **yarn**: >= 1.22.0
- **操作系统**: Windows, macOS, Linux

### 1.2 检查环境

```bash
# 检查Node.js版本
node --version

# 检查npm版本
npm --version

# 检查pnpm版本（如果使用）
pnpm --version

# 检查yarn版本（如果使用）
yarn --version
```

### 1.3 安装Node.js

如果未安装Node.js，请访问 [Node.js官网](https://nodejs.org/) 下载并安装LTS版本。

---

## 2. 安装依赖

### 2.1 进入项目目录

```bash
cd /Users/sk/projects/vibe-coding/projects/vibe-vue
```

### 2.2 安装依赖

```bash
# 使用npm
npm install

# 使用pnpm
pnpm install

# 使用yarn
yarn install
```

### 2.3 验证安装

```bash
# 检查package.json中的依赖
cat package.json

# 检查node_modules目录
ls node_modules | grep eslint
ls node_modules | grep prettier
ls node_modules | grep stylelint
```

---

## 3. 配置编辑器

### 3.1 VS Code

#### 安装扩展

1. 打开VS Code
2. 按 `Cmd+Shift+X` (macOS) 或 `Ctrl+Shift+X` (Windows/Linux) 打开扩展面板
3. 搜索并安装以下扩展：

   - **ESLint** - `dbaeumer.vscode-eslint`
   - **Prettier** - `esbenp.prettier-vscode`
   - **Stylelint** - `stylelint.vscode-stylelint`
   - **Vetur** 或 **Volar** - `Vue.volar` (推荐Volar)

#### 配置设置

创建或编辑 `.vscode/settings.json`：

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  "editor.formatOnType": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit",
    "source.fixAll.stylelint": "explicit"
  },
  "eslint.validate": [
    "javascript",
    "javascriptreact",
    "typescript",
    "typescriptreact",
    "vue"
  ],
  "stylelint.validate": [
    "css",
    "scss",
    "less",
    "vue"
  ],
  "vue.codeActions.enabled": true,
  "vue.complete.casing.tags": "pascal",
  "vue.complete.casing.props": "camel",
  "files.eol": "\n",
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.exclude": {
    "**/.git": true,
    "**/.DS_Store": true,
    "**/node_modules": true,
    "**/dist": true
  }
}
```

#### 推荐扩展

```json
{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "stylelint.vscode-stylelint",
    "Vue.volar",
    "bradlc.vscode-tailwindcss",
    "eamodio.gitlens",
    "ms-python.python"
  ]
}
```

### 3.2 WebStorm

#### 配置ESLint

1. 打开 `Preferences` > `Languages & Frameworks` > `JavaScript` > `Code Quality Tools` > `ESLint`
2. 选择 `Automatic ESLint configuration`
3. 勾选 `Run eslint --fix on save`

#### 配置Prettier

1. 打开 `Preferences` > `Languages & Frameworks` > `JavaScript` > `Prettier`
2. 设置 `Prettier package` 为项目中的 `node_modules/prettier`
3. 勾选 `Run on save for files`

#### 配置Stylelint

1. 打开 `Preferences` > `Languages & Frameworks` > `Style Sheets` > `Stylelint`
2. 选择 `Automatic search`
3. 勾选 `Run stylelint --fix on save`

### 3.3 Vim/Neovim

#### 安装插件

使用 `vim-plug`：

```vim
" ~/.vimrc 或 ~/.config/nvim/init.vim

call plug#begin('~/.vim/plug')

" ESLint
Plug 'dense-analysis/ale'

" Prettier
Plug 'prettier/vim-prettier', {
  \ 'do': 'yarn install',
  \ 'for': ['javascript', 'typescript', 'css', 'less', 'scss', 'json', 'graphql', 'markdown', 'vue', 'yaml', 'html'] }

" Vue
Plug 'leafOfTree/vim-vue-plugin'

call plug#end()
```

#### 配置ALE

```vim
" ~/.vimrc 或 ~/.config/nvim/init.vim

let g:ale_linters = {
\   'javascript': ['eslint'],
\   'typescript': ['eslint'],
\   'vue': ['eslint', 'stylelint'],
\}

let g:ale_fixers = {
\   'javascript': ['prettier', 'eslint'],
\   'typescript': ['prettier', 'eslint'],
\   'vue': ['prettier', 'eslint', 'stylelint'],
\   'css': ['prettier', 'stylelint'],
\   'scss': ['prettier', 'stylelint'],
\}

let g:ale_fix_on_save = 1
```

---

## 4. 使用工具

### 4.1 ESLint

#### 基本用法

```bash
# 检查所有文件
npm run lint

# 检查特定文件
npx eslint src/App.vue

# 自动修复问题
npm run lint -- --fix

# 检查并显示详细输出
npm run lint -- --verbose

# 只显示错误，不显示警告
npm run lint -- --quiet
```

#### 高级用法

```bash
# 使用特定配置文件
npx eslint --config .eslintrc.cjs src/

# 指定文件扩展名
npx eslint --ext .js,.vue src/

# 忽略特定规则
npx eslint --rule 'no-console:off' src/

# 使用缓存提高速度
npx eslint --cache src/

# 格式化输出为JSON
npx eslint --format json src/
```

### 4.2 Prettier

#### 基本用法

```bash
# 格式化所有文件
npm run format

# 格式化特定文件
npx prettier --write src/App.vue

# 检查文件格式（不修改）
npx prettier --check src/

# 显示格式化差异
npx prettier --list-different src/
```

#### 高级用法

```bash
# 使用特定配置文件
npx prettier --config .prettierrc.json --write src/

# 格式化特定类型文件
npx prettier --write "src/**/*.vue"

# 忽略配置文件
npx prettier --no-config --write src/

# 使用不同的解析器
npx prettier --parser vue --write src/App.vue

# 显示调试信息
npx prettier --debug-check src/
```

### 4.3 Stylelint

#### 基本用法

```bash
# 检查所有样式文件
npm run lint:style

# 检查特定文件
npx stylelint src/style.css

# 自动修复问题
npm run lint:style -- --fix

# 检查并显示详细输出
npm run lint:style -- --verbose
```

#### 高级用法

```bash
# 使用特定配置文件
npx stylelint --config .stylelintrc.cjs "src/**/*.css"

# 指定文件扩展名
npx stylelint -- "*.css" "*.scss"

# 忽略特定规则
npx stylelint --rule 'color-named: null' src/

# 使用缓存提高速度
npx stylelint --cache src/

# 格式化输出为JSON
npx stylelint --format json src/
```

---

## 5. 开发流程

### 5.1 日常开发流程

#### 1. 启动开发服务器

```bash
npm run dev
```

#### 2. 编写代码

- 创建新组件
- 编写样式
- 实现功能

#### 3. 代码检查

编辑器会自动显示错误和警告，也可以手动运行：

```bash
# 检查代码
npm run lint

# 检查样式
npm run lint:style

# 格式化代码
npm run format
```

#### 4. 自动修复

```bash
# 自动修复ESLint问题
npm run lint -- --fix

# 自动修复Stylelint问题
npm run lint:style -- --fix

# 格式化代码
npm run format
```

#### 5. 提交代码

```bash
git add .
git commit -m "feat: add new feature"
```

### 5.2 Git Hooks配置（可选）

#### 安装Husky

```bash
npm install --save-dev husky lint-staged
```

#### 初始化Husky

```bash
npx husky install
npx husky add .husky/pre-commit "npx lint-staged"
```

#### 配置lint-staged

在 `package.json` 中添加：

```json
{
  "lint-staged": {
    "*.{js,jsx,ts,tsx,vue}": [
      "eslint --fix",
      "prettier --write"
    ],
    "*.{css,scss,less,vue}": [
      "stylelint --fix",
      "prettier --write"
    ],
    "*.{json,md}": [
      "prettier --write"
    ]
  }
}
```

### 5.3 CI/CD集成

#### GitHub Actions

创建 `.github/workflows/ci.yml`：

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run ESLint
        run: npm run lint

      - name: Run Stylelint
        run: npm run lint:style

      - name: Check Prettier
        run: npm run format:check
```

#### 添加检查脚本

在 `package.json` 中添加：

```json
{
  "scripts": {
    "format:check": "prettier --check src/"
  }
}
```

---

## 6. 常见问题

### 6.1 安装问题

#### 问题：依赖安装失败

**解决方案**：

```bash
# 清除缓存
npm cache clean --force

# 删除node_modules和lock文件
rm -rf node_modules package-lock.json

# 重新安装
npm install
```

#### 问题：权限错误

**解决方案**：

```bash
# 使用sudo（不推荐）
sudo npm install

# 或修复npm权限
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
```

### 6.2 ESLint问题

#### 问题：ESLint找不到配置文件

**解决方案**：

```bash
# 检查配置文件是否存在
ls -la .eslintrc.cjs

# 使用绝对路径指定配置文件
npx eslint --config /path/to/.eslintrc.cjs src/
```

#### 问题：ESLint规则冲突

**解决方案**：

```bash
# 安装eslint-config-prettier
npm install --save-dev eslint-config-prettier

# 在.eslintrc.cjs中添加
{
  "extends": [
    "eslint:recommended",
    "plugin:vue/vue3-recommended",
    "prettier"
  ]
}
```

### 6.3 Prettier问题

#### 问题：Prettier和ESLint冲突

**解决方案**：

```bash
# 安装eslint-config-prettier
npm install --save-dev eslint-config-prettier

# 在.eslintrc.cjs中添加
{
  "extends": [
    "eslint:recommended",
    "plugin:vue/vue3-recommended",
    "prettier"
  ]
}
```

#### 问题：Prettier不格式化文件

**解决方案**：

```bash
# 检查文件是否在.prettierignore中
cat .prettierignore

# 强制格式化
npx prettier --write --no-ignore src/
```

### 6.4 Stylelint问题

#### 问题：Stylelint不支持特定语法

**解决方案**：

```bash
# 在.stylelintrc.cjs中禁用特定规则
{
  "rules": {
    "at-rule-no-unknown": null
  }
}
```

#### 问题：Stylelint不检查Vue文件

**解决方案**：

```bash
# 确保安装了stylelint-config-recommended-vue
npm install --save-dev stylelint-config-recommended-vue

# 检查配置文件
cat .stylelintrc.cjs
```

### 6.5 编辑器问题

#### 问题：VS Code不自动格式化

**解决方案**：

1. 检查扩展是否安装
2. 检查设置是否正确
3. 重启VS Code
4. 尝试手动格式化：`Shift+Alt+F` (Windows/Linux) 或 `Shift+Option+F` (macOS)

#### 问题：WebStorm不自动检查

**解决方案**：

1. 检查配置是否正确
2. 重启WebStorm
3. 清除缓存：`File` > `Invalidate Caches / Restart`

---

## 7. 进阶配置

### 7.1 自定义规则

#### 自定义ESLint规则

创建 `.eslintrc.cjs`：

```javascript
module.exports = {
  rules: {
    'no-console': 'off',
    'no-debugger': 'off',
    'prefer-const': 'error'
  }
}
```

#### 自定义Prettier规则

创建 `.prettierrc.json`：

```json
{
  "semi": false,
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2
}
```

#### 自定义Stylelint规则

创建 `.stylelintrc.cjs`：

```javascript
module.exports = {
  rules: {
    'indentation': 2,
    'string-quotes': 'single',
    'color-hex-case': 'lower'
  }
}
```

### 7.2 文件特定配置

#### ESLint文件特定配置

```javascript
// .eslintrc.cjs
module.exports = {
  overrides: [
    {
      files: ['*.vue'],
      rules: {
        'no-console': 'off'
      }
    },
    {
      files: ['*.test.js'],
      rules: {
        'no-unused-vars': 'off'
      }
    }
  ]
}
```

#### Prettier文件特定配置

```json
{
  "overrides": [
    {
      "files": "*.vue",
      "options": {
        "parser": "vue"
      }
    },
    {
      "files": "*.md",
      "options": {
        "proseWrap": "preserve"
      }
    }
  ]
}
```

#### Stylelint文件特定配置

```javascript
// .stylelintrc.cjs
module.exports = {
  overrides: [
    {
      files: ['*.scss'],
      rules: {
        'at-rule-no-unknown': null
      }
    },
    {
      files: ['*.vue'],
      rules: {
        'selector-pseudo-class-no-unknown': [
          true,
          {
            ignorePseudoClasses: ['deep', 'global']
          }
        ]
      }
    }
  ]
}
```

### 7.3 性能优化

#### 使用缓存

```bash
# ESLint缓存
npx eslint --cache src/

# Stylelint缓存
npx stylelint --cache src/
```

#### 并行处理

```bash
# 安装npm-run-all
npm install --save-dev npm-run-all

# 在package.json中添加
{
  "scripts": {
    "lint:all": "npm-run-all lint lint:style"
  }
}
```

#### 增量检查

```bash
# 只检查修改的文件
npx eslint $(git diff --name-only --diff-filter=ACM | grep -E '\.(js|jsx|ts|tsx|vue)$')
```

### 7.4 团队协作

#### 共享配置

创建共享配置包：

```bash
mkdir eslint-config-custom
cd eslint-config-custom
npm init -y
```

创建 `index.js`：

```javascript
module.exports = {
  extends: ['eslint:recommended', 'plugin:vue/vue3-recommended'],
  rules: {
    'no-console': 'off'
  }
}
```

发布并使用：

```bash
npm publish
```

在项目中使用：

```bash
npm install --save-dev eslint-config-custom
```

```javascript
// .eslintrc.cjs
module.exports = {
  extends: ['custom']
}
```

#### 文档规范

创建 `docs/` 目录，包含：

- `development-standards.md` - 开发规范
- `eslint-rules.md` - ESLint规则
- `prettier-rules.md` - Prettier规则
- `stylelint-rules.md` - Stylelint规则
- `quick-start.md` - 快速开始指南

---

## 附录

### A. 快速参考

| 任务 | 命令 |
|------|------|
| 检查代码 | `npm run lint` |
| 检查样式 | `npm run lint:style` |
| 格式化代码 | `npm run format` |
| 自动修复代码 | `npm run lint -- --fix` |
| 自动修复样式 | `npm run lint:style -- --fix` |

### B. 配置文件清单

| 文件 | 说明 |
|------|------|
| `.eslintrc.cjs` | ESLint配置 |
| `.prettierrc.json` | Prettier配置 |
| `.stylelintrc.cjs` | Stylelint配置 |
| `.editorconfig` | 编辑器配置 |
| `.eslintignore` | ESLint忽略文件 |
| `.prettierignore` | Prettier忽略文件 |
| `.stylelintignore` | Stylelint忽略文件 |
| `.vscode/settings.json` | VS Code配置 |

### C. 相关文档

- [Vue 3开发规范](./development-standards.md)
- [ESLint规则文档](./eslint-rules.md)
- [Prettier规则文档](./prettier-rules.md)
- [Stylelint规则文档](./stylelint-rules.md)

### D. 有用链接

- [Vue 3官方文档](https://vuejs.org/)
- [ESLint官方文档](https://eslint.org/)
- [Prettier官方文档](https://prettier.io/)
- [Stylelint官方文档](https://stylelint.io/)
- [Volar插件](https://marketplace.visualstudio.com/items?itemName=Vue.volar)

---

**文档维护**：开发团队
**最后更新**：2026-02-27
**文档版本**：1.0.0
