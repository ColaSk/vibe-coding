# Prettier 规则文档

## 目录

- [1. 概述](#1-概述)
- [2. 配置文件](#2-配置文件)
- [3. 格式化规则](#3-格式化规则)
- [4. 语言特定规则](#4-语言特定规则)
- [5. 集成配置](#5-集成配置)
- [6. 常见问题](#6-常见问题)

---

## 1. 概述

Prettier是一个代码格式化工具，支持多种编程语言，能够自动统一代码风格，减少团队协作中的格式争议。

### 1.1 主要特性

- **自动格式化**：一键格式化代码
- **统一风格**：强制执行一致的代码风格
- **多语言支持**：支持JavaScript、Vue、CSS、JSON等
- **可配置**：提供丰富的配置选项
- **编辑器集成**：支持主流编辑器

### 1.2 与ESLint的关系

- **Prettier**：负责代码格式化（空格、缩进、引号等）
- **ESLint**：负责代码质量检查（语法错误、潜在问题等）
- **配合使用**：先使用Prettier格式化，再使用ESLint检查

---

## 2. 配置文件

### 2.1 配置文件格式

Prettier支持多种配置文件格式：

- `.prettierrc` - JSON格式
- `.prettierrc.json` - JSON格式
- `.prettierrc.yaml` / `.prettierrc.yml` - YAML格式
- `.prettierrc.js` / `.prettierrc.cjs` - JavaScript格式
- `prettier.config.js` / `prettier.config.cjs` - JavaScript格式
- `.prettierrc.toml` - TOML格式

### 2.2 当前配置

```json
{
  "semi": false,
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "trailingComma": "none",
  "bracketSpacing": true,
  "bracketSameLine": false,
  "arrowParens": "always",
  "endOfLine": "lf",
  "htmlWhitespaceSensitivity": "css",
  "vueIndentScriptAndStyle": false,
  "singleAttributePerLine": false,
  "overrides": [
    {
      "files": "*.vue",
      "options": {
        "parser": "vue"
      }
    },
    {
      "files": "*.json",
      "options": {
        "tabWidth": 2
      }
    },
    {
      "files": "*.md",
      "options": {
        "proseWrap": "preserve",
        "printWidth": 80
      }
    }
  ]
}
```

### 2.3 配置选项说明

| 选项 | 值 | 说明 |
|------|-----|------|
| `semi` | `false` | 不使用分号 |
| `singleQuote` | `true` | 使用单引号 |
| `printWidth` | `100` | 每行最多100字符 |
| `tabWidth` | `2` | 2空格缩进 |
| `useTabs` | `false` | 使用空格而非制表符 |
| `trailingComma` | `"none"` | 不使用尾随逗号 |
| `bracketSpacing` | `true` | 对象字面量括号内添加空格 |
| `bracketSameLine` | `false` | JSX标签的`>`另起一行 |
| `arrowParens` | `"always"` | 箭头函数参数始终使用括号 |
| `endOfLine` | `"lf"` | 使用LF换行符 |
| `htmlWhitespaceSensitivity` | `"css"` | HTML空格敏感度为CSS |
| `vueIndentScriptAndStyle` | `false` | Vue的script和style不缩进 |
| `singleAttributePerLine` | `false` | HTML标签属性不强制单行 |

---

## 3. 格式化规则

### 3.1 分号

#### semi: false

不使用分号。

```javascript
// 格式化后
const a = 1
const b = 2
function test() {
  return a + b
}

// 如果设置为true
const a = 1;
const b = 2;
function test() {
  return a + b;
}
```

### 3.2 引号

#### singleQuote: true

使用单引号。

```javascript
// 格式化后
const str = 'string'
const template = `template string`

// 如果设置为false
const str = "string"
const template = `template string`
```

### 3.3 行宽度

#### printWidth: 100

每行最多100字符。

```javascript
// 格式化后
const longString = 'This is a very long string that will be wrapped at 100 characters to maintain readability'

// 如果行超过100字符，会自动换行
const result = someVeryLongFunctionName(
  firstParameter,
  secondParameter,
  thirdParameter
)
```

### 3.4 缩进

#### tabWidth: 2, useTabs: false

使用2空格缩进。

```javascript
// 格式化后
function test() {
  if (condition) {
    doSomething()
  }
}

// 如果tabWidth: 4
function test() {
    if (condition) {
        doSomething();
    }
}
```

### 3.5 尾随逗号

#### trailingComma: "none"

不使用尾随逗号。

```javascript
// 格式化后
const obj = {
  a: 1,
  b: 2
}

const arr = [1, 2, 3]

// 如果设置为"all"
const obj = {
  a: 1,
  b: 2,
}

const arr = [1, 2, 3,]
```

### 3.6 括号空格

#### bracketSpacing: true

对象字面量括号内添加空格。

```javascript
// 格式化后
const obj = { a: 1, b: 2 }

// 如果设置为false
const obj = {a: 1, b: 2}
```

### 3.7 JSX标签

#### bracketSameLine: false

JSX标签的`>`另起一行。

```javascript
// 格式化后
const element = (
  <div>
    <span>Content</span>
  </div>
)

// 如果设置为true
const element = (
  <div>
    <span>Content</span>
  </div>)
```

### 3.8 箭头函数

#### arrowParens: "always"

箭头函数参数始终使用括号。

```javascript
// 格式化后
const add = (a, b) => a + b
const square = (x) => x * x

// 如果设置为"avoid"
const add = (a, b) => a + b
const square = x => x * x
```

### 3.9 换行符

#### endOfLine: "lf"

使用LF换行符（Unix风格）。

```javascript
// 格式化后
const a = 1
const b = 2

// 如果设置为"crlf"（Windows风格）
const a = 1
const b = 2
```

---

## 4. 语言特定规则

### 4.1 JavaScript/TypeScript

#### 基本格式化

```javascript
// 格式化前
const obj={a:1,b:2};const arr=[1,2,3];function test(x,y){return x+y;}

// 格式化后
const obj = { a: 1, b: 2 }
const arr = [1, 2, 3]
function test(x, y) {
  return x + y
}
```

#### 对象和数组

```javascript
// 格式化前
const user={name:'John',age:30,city:'New York'}

// 格式化后
const user = { name: 'John', age: 30, city: 'New York' }

// 长对象自动换行
const longObject = {
  firstName: 'John',
  lastName: 'Doe',
  age: 30,
  email: 'john.doe@example.com',
  address: '123 Main St',
  city: 'New York',
  country: 'USA'
}
```

#### 函数

```javascript
// 格式化前
function add(a,b){return a+b}
const multiply=function(x,y){return x*y}
const divide=(x,y)=>x/y

// 格式化后
function add(a, b) {
  return a + b
}
const multiply = function (x, y) {
  return x * y
}
const divide = (x, y) => x / y
```

#### 条件语句

```javascript
// 格式化前
if(condition){doSomething()}else{doSomethingElse()}

// 格式化后
if (condition) {
  doSomething()
} else {
  doSomethingElse()
}
```

### 4.2 Vue组件

#### 模板格式化

```vue
<!-- 格式化前 -->
<template><div class="container"><h1>Title</h1><p>Content</p></div></template>

<!-- 格式化后 -->
<template>
  <div class="container">
    <h1>Title</h1>
    <p>Content</p>
  </div>
</template>
```

#### 属性格式化

```vue
<!-- 格式化前 -->
<template><div id="app" class="container" :data-id="id" @click="handleClick">Content</div></template>

<!-- 格式化后 -->
<template>
  <div id="app" class="container" :data-id="id" @click="handleClick">
    Content
  </div>
</template>

<!-- 长属性列表自动换行 -->
<template>
  <div
    id="app"
    class="container"
    :data-id="id"
    :data-name="name"
    @click="handleClick"
    @mouseover="handleMouseOver"
  >
    Content
  </div>
</template>
```

#### Script格式化

```vue
<!-- 格式化前 -->
<script setup>
import{ref,computed}from'vue'
const count=ref(0)
const doubled=computed(()=>count.value*2)
</script>

<!-- 格式化后 -->
<script setup>
import { ref, computed } from 'vue'
const count = ref(0)
const doubled = computed(() => count.value * 2)
</script>
```

#### Style格式化

```vue
<!-- 格式化前 -->
<style scoped>
.container{display:flex;align-items:center;justify-content:center;}
</style>

<!-- 格式化后 -->
<style scoped>
.container {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
```

### 4.3 CSS/SCSS

#### 选择器格式化

```css
/* 格式化前 */
.container{display:flex;align-items:center;justify-content:center;}

/* 格式化后 */
.container {
  display: flex;
  align-items: center;
  justify-content: center;
}
```

#### 属性格式化

```css
/* 格式化前 */
.button{background:#1890ff;color:#fff;padding:10px 20px;border:none;border-radius:4px;}

/* 格式化后 */
.button {
  background: #1890ff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
}
```

#### 嵌套规则

```scss
// 格式化前
.container{.header{.title{font-size:24px;font-weight:bold;}}}

// 格式化后
.container {
  .header {
    .title {
      font-size: 24px;
      font-weight: bold;
    }
  }
}
```

### 4.4 JSON

#### 对象格式化

```json
// 格式化前
{"name":"John","age":30,"city":"New York"}

// 格式化后
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

#### 数组格式化

```json
// 格式化前
[1,2,3,4,5]

// 格式化后
[1, 2, 3, 4, 5]
```

### 4.5 Markdown

#### 代码块

```markdown
<!-- 格式化前 -->
```javascript
const a=1
const b=2
```

<!-- 格式化后 -->
```javascript
const a = 1
const b = 2
```
```

#### 列表

```markdown
<!-- 格式化前 -->
- Item 1
- Item 2
  - Subitem 1
  - Subitem 2

<!-- 格式化后 -->
- Item 1
- Item 2
  - Subitem 1
  - Subitem 2
```

---

## 5. 集成配置

### 5.1 文件特定配置

#### overrides配置

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
      "files": "*.json",
      "options": {
        "tabWidth": 2
      }
    },
    {
      "files": "*.md",
      "options": {
        "proseWrap": "preserve",
        "printWidth": 80
      }
    }
  ]
}
```

### 5.2 忽略文件

#### .prettierignore

```
# 忽略目录
dist/
build/
node_modules/

# 忽略文件
*.min.js
*.min.css
package-lock.json

# 忽略特定模式
coverage/
*.log
```

### 5.3 编辑器集成

#### VS Code

安装Prettier扩展并配置：

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[vue]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[css]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

#### WebStorm

1. 安装Prettier插件
2. 配置Prettier路径
3. 启用"Run Prettier on save"

#### Vim/Neovim

使用vim-prettier插件：

```vim
Plug 'prettier/vim-prettier', {
  \ 'do': 'yarn install',
  \ 'for': ['javascript', 'typescript', 'css', 'less', 'scss', 'json', 'graphql', 'markdown', 'vue', 'yaml', 'html'] }
```

---

## 6. 常见问题

### 6.1 Prettier和ESLint冲突怎么办？

**问题**：Prettier和ESLint对某些代码格式有不同要求。

**解决方案**：

1. 使用`eslint-config-prettier`禁用ESLint中与Prettier冲突的规则

```bash
npm install --save-dev eslint-config-prettier
```

2. 在`.eslintrc.cjs`中添加：

```javascript
{
  extends: [
    'eslint:recommended',
    'plugin:vue/vue3-recommended',
    'prettier'
  ]
}
```

### 6.2 如何格式化特定文件？

**解决方案**：

```bash
# 格式化单个文件
npx prettier --write src/App.vue

# 格式化特定目录
npx prettier --write src/

# 格式化特定类型文件
npx prettier --write "src/**/*.vue"
```

### 6.3 如何检查文件是否已格式化？

**解决方案**：

```bash
# 检查文件格式
npx prettier --check src/

# 如果文件未格式化，会显示差异
npx prettier --list-different src/
```

### 6.4 如何自定义配置？

**解决方案**：

1. 修改`.prettierrc.json`文件
2. 使用`overrides`为特定文件类型配置不同规则
3. 使用`.prettierignore`忽略特定文件

### 6.5 如何在CI/CD中使用？

**解决方案**：

在CI/CD配置中添加：

```yaml
# .github/workflows/ci.yml
- name: Run Prettier
  run: npm run format:check

# package.json
{
  "scripts": {
    "format": "prettier --write src/",
    "format:check": "prettier --check src/"
  }
}
```

### 6.6 如何处理HTML空格？

**问题**：HTML中的空格处理可能导致意外的格式变化。

**解决方案**：

```json
{
  "htmlWhitespaceSensitivity": "css"
}
```

选项说明：
- `css`：遵循CSS显示规则
- `strict`：严格保留空格
- `ignore`：忽略空格

### 6.7 如何处理Vue文件中的script和style缩进？

**问题**：Vue文件中的`<script>`和`<style>`标签内容缩进问题。

**解决方案**：

```json
{
  "vueIndentScriptAndStyle": false
}
```

- `true`：缩进script和style内容
- `false`：不缩进script和style内容

---

## 附录

### A. 配置选项速查表

| 选项 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `printWidth` | number | `80` | 行宽度 |
| `tabWidth` | number | `2` | 缩进宽度 |
| `useTabs` | boolean | `false` | 使用制表符 |
| `semi` | boolean | `true` | 使用分号 |
| `singleQuote` | boolean | `false` | 使用单引号 |
| `quoteProps` | string | `'as-needed'` | 对象属性引号 |
| `jsxSingleQuote` | boolean | `false` | JSX使用单引号 |
| `trailingComma` | string | `'es5'` | 尾随逗号 |
| `bracketSpacing` | boolean | `true` | 对象括号空格 |
| `bracketSameLine` | boolean | `false` | JSX括号同行 |
| `arrowParens` | string | `'always'` | 箭头函数括号 |
| `endOfLine` | string | `'lf'` | 换行符 |

### B. 相关文档

- [Prettier官方文档](https://prettier.io/)
- [Prettier选项](https://prettier.io/docs/en/options.html)
- [Prettier与ESLint集成](https://prettier.io/docs/en/integrating-with-linters.html)

### C. 有用的命令

```bash
# 格式化所有文件
npx prettier --write .

# 检查文件格式
npx prettier --check .

# 显示格式化差异
npx prettier --list-different .

# 使用配置文件
npx prettier --config .prettierrc.json --write src/

# 忽略配置文件
npx prettier --no-config --write src/
```

---

**文档维护**：开发团队
**最后更新**：2026-02-27
**文档版本**：1.0.0
