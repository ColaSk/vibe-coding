# Vue 3 开发规范文档

## 目录

- [1. 概述](#1-概述)
- [2. 开发工具配置](#2-开发工具配置)
  - [2.1 ESLint](#21-eslint)
  - [2.2 Prettier](#22-prettier)
  - [2.3 Stylelint](#23-stylelint)
  - [2.4 EditorConfig](#24-editorconfig)
- [3. 代码风格规范](#3-代码风格规范)
  - [3.1 JavaScript/TypeScript规范](#31-javascripttypescript规范)
  - [3.2 Vue组件规范](#32-vue组件规范)
  - [3.3 CSS样式规范](#33-css样式规范)
- [4. 最佳实践](#4-最佳实践)
  - [4.1 组件设计原则](#41-组件设计原则)
  - [4.2 性能优化建议](#42-性能优化建议)
  - [4.3 安全性建议](#43-安全性建议)
- [5. 工作流程](#5-工作流程)
- [6. 常见问题](#6-常见问题)
- [7. 参考资料](#7-参考资料)

---

## 1. 概述

本文档定义了Vue 3项目的开发规范，包括代码风格、最佳实践、工具配置等内容。遵循这些规范有助于：

- 保持代码风格统一
- 提高代码质量和可维护性
- 减少代码审查时间
- 提升团队协作效率

### 1.1 适用范围

本规范适用于所有Vue 3项目，包括：

- 单文件组件（.vue）
- JavaScript/TypeScript文件
- CSS/SCSS/Less样式文件
- 配置文件

### 1.2 核心原则

- **一致性**：保持代码风格和结构的一致性
- **可读性**：代码应易于理解和维护
- **简洁性**：避免不必要的复杂性
- **性能**：注重代码执行效率
- **安全性**：遵循安全最佳实践

---

## 2. 开发工具配置

### 2.1 ESLint

ESLint是JavaScript代码检查工具，用于检测代码中的语法错误和潜在问题。

#### 配置文件

- **文件位置**：`.eslintrc.cjs`
- **配置类型**：CommonJS模块

#### 主要规则

- **Vue组件规则**：遵循Vue 3最佳实践
- **JavaScript规则**：ES6+语法和最佳实践
- **代码风格**：强制执行统一的代码风格

#### 使用方法

```bash
# 检查代码
npm run lint

# 自动修复问题
npm run lint -- --fix
```

详细规则请参考：[ESLint规则文档](./eslint-rules.md)

---

### 2.2 Prettier

Prettier是代码格式化工具，用于统一代码格式。

#### 配置文件

- **文件位置**：`.prettierrc.json`
- **配置类型**：JSON格式

#### 主要配置

- **引号**：使用单引号
- **分号**：不使用分号
- **缩进**：2空格
- **行宽**：100字符
- **换行符**：LF

#### 使用方法

```bash
# 格式化代码
npm run format

# 格式化特定文件
npx prettier --write src/components/*.vue
```

详细规则请参考：[Prettier规则文档](./prettier-rules.md)

---

### 2.3 Stylelint

Stylelint是CSS样式检查工具，用于检测样式代码中的语法错误和风格问题。

#### 配置文件

- **文件位置**：`.stylelintrc.cjs`
- **配置类型**：CommonJS模块

#### 主要规则

- **CSS语法**：标准CSS语法检查
- **属性排序**：按类型分组排序
- **Vue支持**：支持.vue文件中的`<style>`标签
- **预处理器**：支持SCSS/Less

#### 使用方法

```bash
# 检查样式
npm run lint:style

# 自动修复问题
npm run lint:style -- --fix
```

详细规则请参考：[Stylelint规则文档](./stylelint-rules.md)

---

### 2.4 EditorConfig

EditorConfig是编辑器配置工具，用于统一不同编辑器的编码风格。

#### 配置文件

- **文件位置**：`.editorconfig`
- **配置类型**：INI格式

#### 主要配置

- **编码**：UTF-8
- **缩进**：2空格
- **换行符**：LF
- **行尾空格**：删除

#### 支持的编辑器

- VS Code
- WebStorm
- Sublime Text
- Atom
- Vim/Neovim

---

## 3. 代码风格规范

### 3.1 JavaScript/TypeScript规范

#### 3.1.1 变量声明

```javascript
// 推荐：使用const声明常量
const API_URL = 'https://api.example.com'

// 推荐：使用let声明可变变量
let count = 0

// 不推荐：使用var
var name = 'John'
```

#### 3.1.2 函数定义

```javascript
// 推荐：箭头函数
const add = (a, b) => a + b

// 推荐：函数声明
function fetchData() {
  // ...
}

// 推荐：方法简写
const obj = {
  method() {
    // ...
  }
}
```

#### 3.1.3 对象和数组

```javascript
// 推荐：对象简写
const name = 'John'
const age = 30
const person = { name, age }

// 推荐：解构赋值
const { name, age } = person
const [first, second] = array

// 推荐：展开运算符
const newObj = { ...oldObj, newProp: 'value' }
const newArray = [...oldArray, newItem]
```

#### 3.1.4 字符串

```javascript
// 推荐：模板字符串
const message = `Hello, ${name}`

// 推荐：单引号
const str = 'string'

// 不推荐：字符串拼接
const message = 'Hello, ' + name
```

#### 3.1.5 异步编程

```javascript
// 推荐：async/await
async function getData() {
  try {
    const response = await fetch(url)
    const data = await response.json()
    return data
  } catch (error) {
    console.error(error)
  }
}

// 推荐：Promise链
fetch(url)
  .then(response => response.json())
  .then(data => processData(data))
  .catch(error => handleError(error))
```

---

### 3.2 Vue组件规范

#### 3.2.1 组件命名

```vue
<!-- 推荐：PascalCase -->
<template>
  <UserProfile />
</template>

<script>
export default {
  name: 'UserProfile'
}
</script>
```

#### 3.2.2 组件结构

```vue
<template>
  <!-- 模板内容 -->
</template>

<script setup>
// 导入
import { ref, computed } from 'vue'

// Props
const props = defineProps({
  title: String
})

// Emits
const emit = defineEmits(['update'])

// 响应式数据
const count = ref(0)

// 计算属性
const doubled = computed(() => count.value * 2)

// 方法
const increment = () => {
  count.value++
}
</script>

<style scoped>
/* 样式内容 */
</style>
```

#### 3.2.3 Props定义

```javascript
// 推荐：使用defineProps
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  count: {
    type: Number,
    default: 0
  },
  items: {
    type: Array,
    default: () => []
  }
})

// 推荐：使用TypeScript
interface Props {
  title: string
  count?: number
  items?: any[]
}

const props = withDefaults(defineProps<Props>(), {
  count: 0,
  items: () => []
})
```

#### 3.2.4 Emits定义

```javascript
// 推荐：使用defineEmits
const emit = defineEmits(['update', 'delete', 'change'])

// 触发事件
emit('update', newValue)
```

#### 3.2.5 模板语法

```vue
<template>
  <!-- 推荐：使用v-bind简写 -->
  <div :class="{ active: isActive }"></div>

  <!-- 推荐：使用v-on简写 -->
  <button @click="handleClick">Click</button>

  <!-- 推荐：使用v-model -->
  <input v-model="inputValue" />

  <!-- 推荐：v-for必须使用key -->
  <li v-for="item in items" :key="item.id">
    {{ item.name }}
  </li>
</template>
```

---

### 3.3 CSS样式规范

#### 3.3.1 命名规范

```css
/* 推荐：kebab-case */
.user-profile {
  /* ... */
}

.user-profile__header {
  /* ... */
}

.user-profile--active {
  /* ... */
}
```

#### 3.3.2 属性排序

```css
.component {
  /* 定位 */
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;

  /* 盒模型 */
  display: flex;
  width: 100%;
  height: 100%;
  padding: 10px;
  margin: 0;

  /* 排版 */
  font-size: 14px;
  line-height: 1.5;
  text-align: center;

  /* 颜色 */
  color: #333;
  background-color: #fff;

  /* 其他 */
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

#### 3.3.3 选择器规范

```css
/* 推荐：使用类选择器 */
.button {
  /* ... */
}

/* 不推荐：使用标签选择器 */
div {
  /* ... */
}

/* 推荐：限制选择器嵌套层级 */
.user-profile {
  &__header {
    /* ... */
  }

  &__content {
    /* ... */
  }
}

/* 不推荐：过深的嵌套 */
.user-profile .header .title .text {
  /* ... */
}
```

#### 3.3.4 颜色规范

```css
/* 推荐：使用十六进制颜色 */
.primary-color {
  color: #1890ff;
}

/* 推荐：使用CSS变量 */
:root {
  --primary-color: #1890ff;
  --success-color: #52c41a;
  --warning-color: #faad14;
  --error-color: #f5222d;
}

.button {
  color: var(--primary-color);
}
```

---

## 4. 最佳实践

### 4.1 组件设计原则

#### 4.1.1 单一职责

每个组件应该只负责一个功能。

```vue
<!-- 推荐：职责单一 -->
<UserAvatar :user="user" />
<UserInfo :user="user" />

<!-- 不推荐：职责过多 -->
<UserProfile :user="user" />
```

#### 4.1.2 组件复用

```vue
<!-- 推荐：可复用的组件 -->
<BaseButton type="primary" @click="handleClick">
  Submit
</BaseButton>

<BaseInput v-model="inputValue" placeholder="Enter text" />
```

#### 4.1.3 Props设计

```javascript
// 推荐：明确的数据类型
const props = defineProps({
  user: {
    type: Object,
    required: true
  },
  loading: {
    type: Boolean,
    default: false
  }
})

// 推荐：提供默认值
const props = defineProps({
  items: {
    type: Array,
    default: () => []
  }
})
```

---

### 4.2 性能优化建议

#### 4.2.1 使用计算属性

```javascript
// 推荐：使用计算属性缓存结果
const filteredList = computed(() => {
  return items.value.filter(item => item.active)
})

// 不推荐：在模板中使用方法
<template>
  <div v-for="item in filterItems()" :key="item.id">
    {{ item.name }}
  </div>
</template>
```

#### 4.2.2 使用v-show和v-if

```vue
<!-- 推荐：频繁切换使用v-show -->
<div v-show="isVisible">Content</div>

<!-- 推荐：条件渲染使用v-if -->
<div v-if="isLoggedIn">User content</div>
```

#### 4.2.3 列表渲染优化

```vue
<!-- 推荐：使用唯一的key -->
<li v-for="item in items" :key="item.id">
  {{ item.name }}
</li>

<!-- 推荐：避免使用index作为key -->
<li v-for="(item, index) in items" :key="index">
  {{ item.name }}
</li>
```

#### 4.2.4 懒加载组件

```javascript
// 推荐：异步组件加载
const UserProfile = defineAsyncComponent(() =>
  import('./components/UserProfile.vue')
)
```

---

### 4.3 安全性建议

#### 4.3.1 避免XSS攻击

```vue
<!-- 不推荐：使用v-html -->
<div v-html="userInput"></div>

<!-- 推荐：使用文本插值 -->
<div>{{ userInput }}</div>

<!-- 如果必须使用v-html，确保内容可信 -->
<div v-html="sanitizedContent"></div>
```

#### 4.3.2 验证用户输入

```javascript
// 推荐：验证Props
const props = defineProps({
  email: {
    type: String,
    validator: value => {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)
    }
  }
})
```

#### 4.3.3 使用HTTPS

```javascript
// 推荐：使用HTTPS API
const API_URL = 'https://api.example.com'

// 不推荐：使用HTTP
const API_URL = 'http://api.example.com'
```

---

## 5. 工作流程

### 5.1 开发流程

1. **创建分支**
   ```bash
   git checkout -b feature/your-feature
   ```

2. **编写代码**
   - 遵循代码规范
   - 使用ESLint和Stylelint检查
   - 使用Prettier格式化

3. **代码检查**
   ```bash
   # 检查代码
   npm run lint

   # 检查样式
   npm run lint:style

   # 格式化代码
   npm run format
   ```

4. **提交代码**
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

5. **推送代码**
   ```bash
   git push origin feature/your-feature
   ```

### 5.2 代码审查

- 检查代码是否符合规范
- 检查是否有潜在问题
- 提供改进建议
- 确保代码质量

### 5.3 测试

- 编写单元测试
- 编写集成测试
- 运行测试套件
- 确保测试通过

---

## 6. 常见问题

### 6.1 ESLint问题

**Q: 如何禁用某条规则？**

A: 在.eslintrc.cjs中设置规则为'off'：

```javascript
{
  rules: {
    'no-console': 'off'
  }
}
```

**Q: 如何在文件中临时禁用规则？**

A: 使用注释：

```javascript
// eslint-disable-next-line no-console
console.log('debug message')
```

### 6.2 Prettier问题

**Q: Prettier和ESLint冲突怎么办？**

A: 确保Prettier配置与ESLint配置一致，或使用eslint-config-prettier。

### 6.3 Stylelint问题

**Q: 如何支持自定义CSS属性？**

A: 在.stylelintrc.cjs中配置：

```javascript
{
  rules: {
    'custom-property-pattern': null
  }
}
```

---

## 7. 参考资料

- [Vue 3官方文档](https://vuejs.org/)
- [ESLint文档](https://eslint.org/)
- [Prettier文档](https://prettier.io/)
- [Stylelint文档](https://stylelint.io/)
- [JavaScript最佳实践](https://github.com/ryanmcdermott/clean-code-javascript)
- [Vue风格指南](https://vuejs.org/style-guide/)

---

## 附录

### A. 快速参考

| 工具 | 命令 | 说明 |
|------|------|------|
| ESLint | `npm run lint` | 检查代码 |
| Prettier | `npm run format` | 格式化代码 |
| Stylelint | `npm run lint:style` | 检查样式 |

### B. 配置文件清单

- `.eslintrc.cjs` - ESLint配置
- `.prettierrc.json` - Prettier配置
- `.stylelintrc.cjs` - Stylelint配置
- `.editorconfig` - 编辑器配置
- `.eslintignore` - ESLint忽略文件
- `.prettierignore` - Prettier忽略文件
- `.stylelintignore` - Stylelint忽略文件

### C. 版本历史

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0.0 | 2026-02-27 | 初始版本 |

---

**文档维护**：开发团队
**最后更新**：2026-02-27
**文档版本**：1.0.0
