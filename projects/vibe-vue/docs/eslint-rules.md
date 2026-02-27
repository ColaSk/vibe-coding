# ESLint 规则文档

## 目录

- [1. 概述](#1-概述)
- [2. 配置文件](#2-配置文件)
- [3. Vue组件规则](#3-vue组件规则)
- [4. JavaScript规则](#4-javascript规则)
- [5. 代码风格规则](#5-代码风格规则)
- [6. 最佳实践](#6-最佳实践)
- [7. 常见问题](#7-常见问题)

---

## 1. 概述

ESLint是一个可配置的JavaScript代码检查工具，用于发现代码中的错误和潜在问题，并强制执行代码风格规范。

### 1.1 主要功能

- **语法检查**：检测语法错误
- **代码质量**：发现潜在问题
- **风格统一**：强制执行代码风格
- **自动修复**：自动修复部分问题

### 1.2 配置优先级

ESLint配置按以下优先级加载：

1. `.eslintrc.js` 或 `.eslintrc.cjs`
2. `.eslintrc.json`
3. `.eslintrc.yaml` 或 `.eslintrc.yml`
4. `package.json` 中的 `eslintConfig` 字段

---

## 2. 配置文件

### 2.1 基本配置

```javascript
module.exports = {
  root: true,
  env: {
    browser: true,
    es2021: true,
    node: true
  },
  extends: [
    'eslint:recommended',
    'plugin:vue/vue3-recommended',
    'plugin:@typescript-eslint/recommended'
  ],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module'
  },
  plugins: ['vue'],
  rules: {
    // 自定义规则
  }
}
```

### 2.2 配置选项说明

| 选项 | 说明 | 示例 |
|------|------|------|
| `root` | 标记为根配置 | `true` |
| `env` | 指定环境变量 | `browser: true` |
| `extends` | 继承规则集 | `'eslint:recommended'` |
| `parserOptions` | 解析器选项 | `{ ecmaVersion: 'latest' }` |
| `plugins` | 使用插件 | `['vue']` |
| `rules` | 自定义规则 | `{ 'no-console': 'warn' }` |

### 2.3 规则级别

- `off` 或 `0` - 关闭规则
- `warn` 或 `1` - 警告（不会导致构建失败）
- `error` 或 `2` - 错误（会导致构建失败）

---

## 3. Vue组件规则

### 3.1 组件命名

#### vue/component-name-in-template-casing

强制组件在模板中使用PascalCase命名。

```vue
<!-- 推荐 -->
<template>
  <UserProfile />
  <UserAvatar />
</template>

<!-- 不推荐 -->
<template>
  <user-profile />
  <user-avatar />
</template>
```

#### vue/component-definition-name-casing

强制组件定义使用PascalCase命名。

```javascript
// 推荐
export default {
  name: 'UserProfile'
}

// 不推荐
export default {
  name: 'user-profile'
}
```

#### vue/multi-word-component-names

允许单词组件名称（已禁用）。

```javascript
// 允许
export default {
  name: 'Home'
}

export default {
  name: 'UserProfile'
}
```

### 3.2 组件结构

#### vue/component-tags-order

强制组件标签顺序：`<script>`、`<template>`、`<style>`。

```vue
<!-- 推荐 -->
<script setup>
// ...
</script>

<template>
  <!-- ... -->
</template>

<style scoped>
/* ... */
</style>
```

#### vue/block-tag-newline

强制块标签换行。

```vue
<!-- 推荐 -->
<script setup>
// ...
</script>

<template>
  <!-- ... -->
</template>
```

### 3.3 模板规则

#### vue/require-v-for-key

强制v-for必须使用key。

```vue
<!-- 推荐 -->
<template>
  <li v-for="item in items" :key="item.id">
    {{ item.name }}
  </li>
</template>

<!-- 不推荐 -->
<template>
  <li v-for="item in items">
    {{ item.name }}
  </li>
</template>
```

#### vue/no-v-html

警告使用v-html（可能存在XSS风险）。

```vue
<!-- 警告 -->
<template>
  <div v-html="userInput"></div>
</template>

<!-- 推荐 -->
<template>
  <div>{{ userInput }}</div>
</template>
```

#### vue/html-self-closing

强制自闭合标签的使用。

```vue
<!-- 推荐 -->
<template>
  <img src="logo.png" />
  <input type="text" />
  <UserProfile />
</template>

<!-- 不推荐 -->
<template>
  <img src="logo.png">
  <input type="text">
</template>
```

#### vue/max-attributes-per-line

限制每行最大属性数量。

```vue
<!-- 推荐：单行最多3个属性 -->
<template>
  <div id="app" class="container" :data-id="id">
    <!-- ... -->
  </div>

  <!-- 多行每行1个属性 -->
  <div
    id="app"
    class="container"
    :data-id="id"
    @click="handleClick"
  >
    <!-- ... -->
  </div>
</template>
```

### 3.4 Props和Emits

#### vue/require-default-prop

允许props不提供默认值（已禁用）。

```javascript
// 允许
const props = defineProps({
  title: String
})
```

#### vue/require-explicit-emits

允许隐式emits（已禁用）。

```javascript
// 允许
const emit = defineEmits()

emit('update')
```

#### vue/define-macros-order

强制define宏的顺序：`defineProps`、`defineEmits`。

```javascript
// 推荐
const props = defineProps({
  title: String
})
const emit = defineEmits(['update'])

// 不推荐
const emit = defineEmits(['update'])
const props = defineProps({
  title: String
})
```

### 3.5 代码质量

#### vue/no-setup-props-destructure

警告解构props（可能失去响应性）。

```javascript
// 警告
const props = defineProps({
  title: String
})
const { title } = props

// 推荐
const props = defineProps({
  title: String
})
const title = computed(() => props.title)
```

#### vue/no-unused-vars

警告未使用的变量。

```javascript
// 警告
const unused = ref(0)

// 推荐
const used = ref(0)
console.log(used.value)
```

#### vue/no-unused-properties

警告未使用的属性。

```javascript
// 警告
export default {
  data() {
    return {
      unusedProp: 'value'
    }
  }
}

// 推荐
export default {
  data() {
    return {
      usedProp: 'value'
    }
  },
  methods: {
    useProp() {
      console.log(this.usedProp)
    }
  }
}
```

---

## 4. JavaScript规则

### 4.1 变量声明

#### no-var

禁止使用var，使用let或const。

```javascript
// 推荐
const constant = 'value'
let variable = 'value'

// 不推荐
var oldStyle = 'value'
```

#### prefer-const

优先使用const声明常量。

```javascript
// 推荐
const constant = 'value'

// 不推荐
let constant = 'value'
constant = 'new value'
```

#### no-unused-vars

警告未使用的变量。

```javascript
// 警告
const unused = 'value'

// 推荐
const used = 'value'
console.log(used)
```

### 4.2 函数

#### arrow-body-style

箭头函数体风格。

```javascript
// 推荐：单行
const add = (a, b) => a + b

// 推荐：多行
const multiply = (a, b) => {
  return a * b
}

// 不推荐：不必要的花括号
const add = (a, b) => {
  return a + b
}
```

#### prefer-arrow-callback

优先使用箭头函数作为回调。

```javascript
// 推荐
array.map(item => item * 2)

// 不推荐
array.map(function(item) {
  return item * 2
})
```

#### space-before-function-paren

函数括号前的空格。

```javascript
// 推荐：匿名函数
const add = function (a, b) {
  return a + b
}

// 推荐：箭头函数
const add = (a, b) => {
  return a + b
}

// 推荐：命名函数
function add(a, b) {
  return a + b
}
```

### 4.3 对象和数组

#### object-shorthand

对象属性简写。

```javascript
// 推荐
const name = 'John'
const age = 30
const person = { name, age }

// 不推荐
const name = 'John'
const age = 30
const person = { name: name, age: age }
```

#### prefer-destructuring

优先使用解构赋值。

```javascript
// 推荐
const { name, age } = person
const [first, second] = array

// 不推荐
const name = person.name
const age = person.age
const first = array[0]
const second = array[1]
```

#### no-duplicate-imports

禁止重复导入。

```javascript
// 推荐
import { a, b } from 'module'

// 不推荐
import { a } from 'module'
import { b } from 'module'
```

### 4.4 字符串

#### quotes

强制使用单引号。

```javascript
// 推荐
const str = 'string'

// 不推荐
const str = "string"
```

#### prefer-template

优先使用模板字符串。

```javascript
// 推荐
const message = `Hello, ${name}`

// 不推荐
const message = 'Hello, ' + name
```

### 4.5 异步编程

#### no-return-await

警告不必要的await。

```javascript
// 警告
async function getData() {
  return await fetchData()
}

// 推荐
async function getData() {
  return fetchData()
}

// 推荐：需要await的情况
async function getData() {
  const data = await fetchData()
  return processData(data)
}
```

#### require-await

警告没有await的async函数。

```javascript
// 警告
async function getData() {
  return fetchData()
}

// 推荐
async function getData() {
  return await fetchData()
}
```

### 4.6 比较和逻辑

#### eqeqeq

强制使用严格相等。

```javascript
// 推荐
if (a === b) { }

// 不推荐
if (a == b) { }
```

#### no-nested-ternary

禁止嵌套三元表达式。

```javascript
// 推荐
const result = condition1 ? value1 : condition2 ? value2 : value3

// 不推荐
const result = condition1 ? value1 : (condition2 ? value2 : value3)
```

#### no-unneeded-ternary

禁止不必要的三元表达式。

```javascript
// 推荐
const result = condition ? value : defaultValue

// 不推荐
const result = condition ? value : value
```

---

## 5. 代码风格规则

### 5.1 缩进和空格

#### indent

缩进规则（已禁用，由Prettier处理）。

#### no-multiple-empty-lines

禁止多个空行。

```javascript
// 推荐
const a = 1

const b = 2

// 不推荐
const a = 1


const b = 2
```

#### no-trailing-spaces

禁止行尾空格。

```javascript
// 推荐
const a = 1

// 不推荐
const a = 1   
```

### 5.2 分号和逗号

#### semi

禁止分号。

```javascript
// 推荐
const a = 1
const b = 2

// 不推荐
const a = 1;
const b = 2;
```

#### comma-dangle

禁止尾随逗号。

```javascript
// 推荐
const obj = {
  a: 1,
  b: 2
}

// 不推荐
const obj = {
  a: 1,
  b: 2,
}
```

### 5.3 行长度

#### max-len

最大行长度（由Prettier处理）。

### 5.4 代码块

#### brace-style

花括号风格。

```javascript
// 推荐
if (condition) {
  // ...
}

// 推荐：单行
if (condition) { /* ... */ }

// 不推荐
if (condition)
{
  // ...
}
```

#### curly

强制使用花括号。

```javascript
// 推荐
if (condition) {
  doSomething()
}

// 不推荐
if (condition)
  doSomething()
```

### 5.5 空行

#### padding-line-between-statements

语句间的空行。

```javascript
// 推荐：return前空行
function test() {
  const a = 1

  return a
}

// 推荐：声明后空行
const a = 1
const b = 2

doSomething()
```

---

## 6. 最佳实践

### 6.1 代码组织

#### lines-between-class-members

类成员间的空行。

```javascript
// 推荐
class MyClass {
  constructor() {
    this.value = 0
  }

  getValue() {
    return this.value
  }

  setValue(value) {
    this.value = value
  }
}
```

#### no-shadow

警告变量遮蔽。

```javascript
// 警告
function test() {
  const value = 1
  {
    const value = 2
  }
}

// 推荐
function test() {
  const value = 1
  {
    const newValue = 2
  }
}
```

### 6.2 性能

#### no-param-reassign

警告参数重新赋值。

```javascript
// 警告
function process(obj) {
  obj.value = 1
}

// 推荐
function process(obj) {
  return { ...obj, value: 1 }
}
```

#### prefer-rest-params

优先使用剩余参数。

```javascript
// 推荐
function sum(...args) {
  return args.reduce((a, b) => a + b, 0)
}

// 不推荐
function sum() {
  return Array.from(arguments).reduce((a, b) => a + b, 0)
}
```

### 6.3 安全性

#### no-eval

禁止使用eval。

```javascript
// 不推荐
eval('console.log("dangerous")')

// 推荐
const func = new Function('console.log("safer")')
```

#### no-implied-eval

禁止隐式eval。

```javascript
// 不推荐
setTimeout('console.log("dangerous")', 1000)

// 推荐
setTimeout(() => {
  console.log('safer')
}, 1000)
```

---

## 7. 常见问题

### 7.1 如何禁用规则？

在`.eslintrc.cjs`中设置规则为'off'：

```javascript
{
  rules: {
    'no-console': 'off'
  }
}
```

### 7.2 如何在文件中临时禁用规则？

使用注释：

```javascript
// eslint-disable-next-line no-console
console.log('debug message')

/* eslint-disable no-console */
console.log('debug message')
/* eslint-enable no-console */

/* eslint-disable */
console.log('debug message')
/* eslint-enable */
```

### 7.3 如何自动修复问题？

使用`--fix`选项：

```bash
npm run lint -- --fix
```

### 7.4 如何忽略特定文件？

在`.eslintignore`中添加文件路径：

```
dist/
node_modules/
*.min.js
```

### 7.5 如何配置特定文件的规则？

使用`overrides`：

```javascript
{
  overrides: [
    {
      files: ['*.vue'],
      rules: {
        'no-console': 'off'
      }
    }
  ]
}
```

---

## 附录

### A. 规则列表

| 规则 | 级别 | 说明 |
|------|------|------|
| `vue/multi-word-component-names` | off | 允许单词组件名称 |
| `vue/no-v-html` | warn | 警告v-html使用 |
| `vue/require-default-prop` | off | 允许props无默认值 |
| `vue/require-explicit-emits` | off | 允许隐式emits |
| `no-console` | warn | 警告console使用 |
| `no-debugger` | warn | 警告debugger使用 |
| `no-var` | error | 禁止var |
| `eqeqeq` | error | 强制严格相等 |
| `semi` | error | 禁止分号 |
| `quotes` | error | 强制单引号 |

### B. 相关文档

- [ESLint官方文档](https://eslint.org/)
- [Vue ESLint插件](https://eslint.vuejs.org/)
- [ESLint规则列表](https://eslint.org/docs/latest/rules/)

---

**文档维护**：开发团队
**最后更新**：2026-02-27
**文档版本**：1.0.0
