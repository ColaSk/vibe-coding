# Stylelint 规则文档

## 目录

- [1. 概述](#1-概述)
- [2. 配置文件](#2-配置文件)
- [3. 基础规则](#3-基础规则)
- [4. 代码风格规则](#4-代码风格规则)
- [5. 属性排序规则](#5-属性排序规则)
- [6. Vue特定规则](#6-vue特定规则)
- [7. 最佳实践](#7-最佳实践)
- [8. 常见问题](#8-常见问题)

---

## 1. 概述

Stylelint是一个CSS样式检查工具，用于检测样式代码中的语法错误、风格问题，并强制执行CSS编码规范。

### 1.1 主要功能

- **语法检查**：检测CSS语法错误
- **风格统一**：强制执行统一的代码风格
- **最佳实践**：遵循CSS最佳实践
- **自动修复**：自动修复部分问题
- **Vue支持**：支持.vue文件中的`<style>`标签

### 1.2 支持的语法

- CSS
- SCSS
- Less
- SugarSS
- Vue单文件组件

---

## 2. 配置文件

### 2.1 配置文件格式

Stylelint支持多种配置文件格式：

- `.stylelintrc` - JSON格式
- `.stylelintrc.json` - JSON格式
- `.stylelintrc.yaml` / `.stylelintrc.yml` - YAML格式
- `.stylelintrc.js` / `.stylelintrc.cjs` - JavaScript格式
- `stylelint.config.js` / `stylelint.config.cjs` - JavaScript格式

### 2.2 当前配置

```javascript
module.exports = {
  extends: [
    'stylelint-config-standard',
    'stylelint-config-recommended-vue'
  ],
  plugins: [
    'stylelint-order'
  ],
  rules: {
    // 基础规则
    'indentation': 2,
    'string-quotes': 'single',
    'no-duplicate-selectors': true,
    'color-hex-case': 'lower',
    'color-hex-length': 'short',
    'color-named': 'never',

    // 选择器规则
    'selector-class-pattern': null,
    'selector-id-pattern': null,
    'selector-pseudo-class-no-unknown': [
      true,
      {
        ignorePseudoClasses: ['deep', 'global']
      }
    ],
    'selector-pseudo-element-no-unknown': [
      true,
      {
        ignorePseudoElements: ['v-deep', 'v-global', 'v-slotted']
      }
    ],

    // Vue特定规则
    'at-rule-no-unknown': [
      true,
      {
        ignoreAtRules: ['tailwind', 'apply', 'layer', 'variants', 'responsive', 'screen']
      }
    ],

    // 代码质量规则
    'block-no-empty': true,
    'declaration-block-no-duplicate-properties': true,
    'declaration-block-no-shorthand-property-overrides': true,
    'font-family-no-duplicate-names': true,
    'font-family-no-missing-generic-family-keyword': true,
    'function-calc-no-unspaced-operator': true,
    'function-linear-gradient-no-nonstandard-direction': true,
    'keyframe-declaration-no-important': true,
    'media-feature-name-no-unknown': true,
    'no-descending-specificity': null,
    'no-duplicate-at-import-rules': true,
    'no-empty-source': true,
    'no-invalid-double-slash-comments': true,
    'no-unknown-animations': true,
    'property-no-unknown': true,
    'selector-pseudo-class-parentheses-space-inside': 'never',
    'selector-pseudo-element-no-unknown': [
      true,
      {
        ignorePseudoElements: ['v-deep', 'v-global', 'v-slotted']
      }
    ],
    'selector-type-no-unknown': [
      true,
      {
        ignoreTypes: ['/^page/']
      }
    ],
    'unit-no-unknown': true,

    // 格式化规则
    'declaration-block-trailing-semicolon': 'always',
    'declaration-colon-space-after': 'always',
    'declaration-colon-space-before': 'never',
    'function-comma-space-after': 'always',
    'function-comma-space-before': 'never',
    'function-url-quotes': 'always',
    'number-leading-zero': 'always',
    'number-no-trailing-zeros': true,
    'length-zero-no-unit': true,
    'selector-attribute-brackets-space-inside': 'never',
    'selector-attribute-operator-space-after': 'never',
    'selector-attribute-operator-space-before': 'never',
    'selector-combinator-space-after': 'always',
    'selector-combinator-space-before': 'always',
    'selector-descendant-combinator-no-non-space': true,
    'selector-list-comma-newline-after': 'always',
    'selector-list-comma-space-before': 'never',
    'selector-max-id': 0,
    'selector-max-type': 3,
    'selector-max-universal': 1,
    'value-list-comma-newline-after': 'never-multi-line',
    'value-list-comma-space-after': 'always-single-line',
    'value-list-comma-space-before': 'never-single-line',
    'value-list-max-empty-lines': 0,

    // 块规则
    'block-closing-brace-empty-line-before': 'never',
    'block-closing-brace-newline-after': 'always',
    'block-closing-brace-newline-before': 'always-multi-line',
    'block-closing-brace-space-before': 'always-single-line',
    'block-opening-brace-newline-after': 'always-multi-line',
    'block-opening-brace-space-after': 'always-single-line',
    'block-opening-brace-space-before': 'always',

    // 声明规则
    'declaration-block-no-redundant-longhand-properties': true,
    'declaration-block-single-line-max-declarations': 1,
    'declaration-empty-line-before': [
      'always',
      {
        except: ['after-declaration', 'first-nested'],
        ignore: ['after-comment', 'inside-single-line-block']
      }
    ],

    // 规则规则
    'rule-empty-line-before': [
      'always-multi-line',
      {
        except: ['first-nested'],
        ignore: ['after-comment']
      }
    ],

    // 排序规则
    'order/order': [
      'custom-properties',
      'declarations'
    ],
    'order/properties-order': [
      'position',
      'top',
      'right',
      'bottom',
      'left',
      'z-index',
      'display',
      'flex-direction',
      'flex-wrap',
      'justify-content',
      'align-items',
      'align-content',
      'align-self',
      'flex',
      'flex-grow',
      'flex-shrink',
      'flex-basis',
      'grid-template-columns',
      'grid-template-rows',
      'grid-template-areas',
      'grid-column',
      'grid-row',
      'grid-area',
      'grid-gap',
      'gap',
      'width',
      'min-width',
      'max-width',
      'height',
      'min-height',
      'max-height',
      'margin',
      'margin-top',
      'margin-right',
      'margin-bottom',
      'margin-left',
      'padding',
      'padding-top',
      'padding-right',
      'padding-bottom',
      'padding-left',
      'border',
      'border-width',
      'border-style',
      'border-color',
      'border-top',
      'border-right',
      'border-bottom',
      'border-left',
      'border-radius',
      'border-top-left-radius',
      'border-top-right-radius',
      'border-bottom-right-radius',
      'border-bottom-left-radius',
      'box-sizing',
      'box-shadow',
      'opacity',
      'visibility',
      'overflow',
      'overflow-x',
      'overflow-y',
      'background',
      'background-color',
      'background-image',
      'background-repeat',
      'background-position',
      'background-size',
      'background-attachment',
      'background-clip',
      'background-origin',
      'color',
      'font',
      'font-family',
      'font-size',
      'font-weight',
      'font-style',
      'font-variant',
      'line-height',
      'letter-spacing',
      'text-align',
      'text-decoration',
      'text-transform',
      'text-indent',
      'text-overflow',
      'white-space',
      'word-spacing',
      'word-wrap',
      'word-break',
      'list-style',
      'list-style-type',
      'list-style-position',
      'list-style-image',
      'table-layout',
      'border-collapse',
      'border-spacing',
      'caption-side',
      'empty-cells',
      'cursor',
      'pointer-events',
      'transition',
      'transform',
      'animation',
      'filter'
    ],

    // 复杂性规则
    'selector-max-compound-selectors': 4,
    'selector-max-specificity': '0,4,0',
    'max-nesting-depth': 3,

    // 其他规则
    'shorthand-property-no-redundant-values': true,
    'comment-no-empty': true,
    'comment-whitespace-inside': 'always',
    'comment-empty-line-before': [
      'always',
      {
        except: ['first-nested'],
        ignore: ['stylelint-commands', 'after-comment']
      }
    ],
    'rule-non-nested-empty-line-before': [
      'always-multi-line',
      {
        except: ['first-nested'],
        ignore: ['after-comment']
      }
    ],
    'declaration-block-no-duplicate-custom-properties': true,
    'custom-property-no-missing-var-function': true,
    'custom-property-pattern': null,
    'keyframes-name-pattern': null,
    'alpha-value-notation': 'number',
    'color-function-notation': 'modern',
    'hue-degree-notation': 'angle'
  }
}
```

### 2.3 配置选项说明

| 选项 | 说明 |
|------|------|
| `extends` | 继承的规则集 |
| `plugins` | 使用的插件 |
| `rules` | 自定义规则 |
| `overrides` | 特定文件的覆盖配置 |

---

## 3. 基础规则

### 3.1 缩进

#### indentation: 2

使用2空格缩进。

```css
/* 推荐 */
.container {
  display: flex;
  align-items: center;
}

/* 不推荐 */
.container {
    display: flex;
    align-items: center;
}
```

### 3.2 引号

#### string-quotes: single

使用单引号。

```css
/* 推荐 */
.content::before {
  content: 'Hello';
}

/* 不推荐 */
.content::before {
  content: "Hello";
}
```

### 3.3 颜色

#### color-hex-case: lower

使用小写十六进制颜色。

```css
/* 推荐 */
.button {
  background: #1890ff;
}

/* 不推荐 */
.button {
  background: #1890FF;
}
```

#### color-hex-length: short

使用简短的十六进制颜色。

```css
/* 推荐 */
.button {
  background: #fff;
}

/* 不推荐 */
.button {
  background: #ffffff;
}
```

#### color-named: never

不使用命名颜色。

```css
/* 推荐 */
.button {
  background: #ff0000;
}

/* 不推荐 */
.button {
  background: red;
}
```

### 3.4 数字

#### number-leading-zero: always

小数点前始终加零。

```css
/* 推荐 */
.button {
  opacity: 0.5;
}

/* 不推荐 */
.button {
  opacity: .5;
}
```

#### number-no-trailing-zeros: true

不使用尾随零。

```css
/* 推荐 */
.button {
  margin: 10px;
}

/* 不推荐 */
.button {
  margin: 10.0px;
}
```

#### length-zero-no-unit: true

零值不使用单位。

```css
/* 推荐 */
.button {
  margin: 0;
}

/* 不推荐 */
.button {
  margin: 0px;
}
```

---

## 4. 代码风格规则

### 4.1 声明

#### declaration-block-trailing-semicolon: always

声明块末尾使用分号。

```css
/* 推荐 */
.button {
  background: #1890ff;
  color: #fff;
}

/* 不推荐 */
.button {
  background: #1890ff;
  color: #fff
}
```

#### declaration-colon-space-after: always

冒号后添加空格。

```css
/* 推荐 */
.button {
  background: #1890ff;
}

/* 不推荐 */
.button {
  background:#1890ff;
}
```

#### declaration-colon-space-before: never

冒号前不添加空格。

```css
/* 推荐 */
.button {
  background: #1890ff;
}

/* 不推荐 */
.button {
  background : #1890ff;
}
```

### 4.2 选择器

#### selector-combinator-space-after: always

组合符后添加空格。

```css
/* 推荐 */
.parent > .child {
  /* ... */
}

/* 不推荐 */
.parent >.child {
  /* ... */
}
```

#### selector-combinator-space-before: always

组合符前添加空格。

```css
/* 推荐 */
.parent > .child {
  /* ... */
}

/* 不推荐 */
.parent>.child {
  /* ... */
}
```

#### selector-list-comma-newline-after: always

选择器列表逗号后换行。

```css
/* 推荐 */
.button,
.link,
.icon {
  /* ... */
}

/* 不推荐 */
.button, .link, .icon {
  /* ... */
}
```

#### selector-list-comma-space-before: never

选择器列表逗号前不添加空格。

```css
/* 推荐 */
.button,
.link {
  /* ... */
}

/* 不推荐 */
.button , .link {
  /* ... */
}
```

### 4.3 函数

#### function-comma-space-after: always

函数参数逗号后添加空格。

```css
/* 推荐 */
.button {
  background: linear-gradient(to right, #1890ff, #36cfc9);
}

/* 不推荐 */
.button {
  background: linear-gradient(to right,#1890ff,#36cfc9);
}
```

#### function-comma-space-before: never

函数参数逗号前不添加空格。

```css
/* 推荐 */
.button {
  background: linear-gradient(to right, #1890ff, #36cfc9);
}

/* 不推荐 */
.button {
  background: linear-gradient(to right , #1890ff , #36cfc9);
}
```

#### function-url-quotes: always

URL使用引号。

```css
/* 推荐 */
.icon {
  background: url('icon.png');
}

/* 不推荐 */
.icon {
  background: url(icon.png);
}
```

### 4.4 块

#### block-opening-brace-space-before: always

开括号前添加空格。

```css
/* 推荐 */
.button {
  /* ... */
}

/* 不推荐 */
.button{
  /* ... */
}
```

#### block-closing-brace-newline-after: always

闭括号后换行。

```css
/* 推荐 */
.button {
  background: #1890ff;
}

.link {
  color: #1890ff;
}

/* 不推荐 */
.button {
  background: #1890ff;
}
.link {
  color: #1890ff;
}
```

---

## 5. 属性排序规则

### 5.1 排序顺序

属性按以下顺序排列：

1. **定位属性**：position, top, right, bottom, left, z-index
2. **显示属性**：display, flex-direction, flex-wrap, justify-content, align-items等
3. **盒模型**：width, height, margin, padding, border等
4. **背景**：background, background-color, background-image等
5. **颜色**：color
6. **字体**：font, font-size, font-weight, line-height等
7. **文本**：text-align, text-decoration等
8. **列表**：list-style等
9. **表格**：table-layout, border-collapse等
10. **其他**：cursor, transition, transform, animation等

### 5.2 示例

```css
/* 推荐的属性排序 */
.button {
  /* 定位 */
  position: relative;
  top: 0;
  left: 0;
  z-index: 1;

  /* 显示 */
  display: inline-flex;
  justify-content: center;
  align-items: center;

  /* 盒模型 */
  width: 100px;
  height: 40px;
  padding: 10px 20px;
  margin: 0;
  border: 1px solid #1890ff;
  border-radius: 4px;

  /* 背景 */
  background: #1890ff;

  /* 颜色 */
  color: #fff;

  /* 字体 */
  font-size: 14px;
  font-weight: 500;
  line-height: 1.5;

  /* 文本 */
  text-align: center;
  text-decoration: none;

  /* 其他 */
  cursor: pointer;
  transition: all 0.3s;
}
```

---

## 6. Vue特定规则

### 6.1 深度选择器

#### selector-pseudo-class-no-unknown

支持Vue的深度选择器。

```vue
<style scoped>
/* 推荐 */
.parent :deep(.child) {
  /* ... */
}

/* 推荐 */
.parent >>> .child {
  /* ... */
}

/* 推荐 */
.parent /deep/ .child {
  /* ... */
}
</style>
```

### 6.2 全局样式

#### selector-pseudo-element-no-unknown

支持Vue的全局样式伪元素。

```vue
<style scoped>
/* 推荐 */
:global(.global-class) {
  /* ... */
}

/* 推荐 */
:global(.global-class) .scoped-class {
  /* ... */
}
</style>
```

### 6.3 插槽样式

```vue
<style scoped>
/* 推荐 */
:slotted(.slot-class) {
  /* ... */
}
</style>
```

### 6.4 Tailwind CSS

#### at-rule-no-unknown

支持Tailwind CSS的@规则。

```vue
<style>
/* 推荐 */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* 推荐 */
@layer components {
  .button {
    @apply px-4 py-2 bg-blue-500 text-white rounded;
  }
}

/* 推荐 */
@variants hover, focus {
  .button {
    /* ... */
  }
}

/* 推荐 */
@responsive {
  .container {
    /* ... */
  }
}
</style>
```

---

## 7. 最佳实践

### 7.1 选择器规范

#### selector-max-id: 0

不使用ID选择器。

```css
/* 不推荐 */
#header {
  /* ... */
}

/* 推荐 */
.header {
  /* ... */
}
```

#### selector-max-type: 3

限制类型选择器数量。

```css
/* 推荐 */
.container .header .title {
  /* ... */
}

/* 不推荐 */
.container .header .content .section .title {
  /* ... */
}
```

#### selector-max-universal: 1

限制通用选择器数量。

```css
/* 推荐 */
.container * {
  /* ... */
}

/* 不推荐 */
.container * * {
  /* ... */
}
```

#### selector-max-compound-selectors: 4

限制复合选择器复杂度。

```css
/* 推荐 */
.container .header .title .text {
  /* ... */
}

/* 不推荐 */
.container .header .content .section .title .text {
  /* ... */
}
```

#### selector-max-specificity: '0,4,0'

限制选择器特异性。

```css
/* 推荐 */
.container .header .title {
  /* ... */
}

/* 不推荐 */
.container .header .content .section .title {
  /* ... */
}
```

### 7.2 嵌套规则

#### max-nesting-depth: 3

限制嵌套深度。

```scss
/* 推荐 */
.container {
  .header {
    .title {
      /* ... */
    }
  }
}

/* 不推荐 */
.container {
  .header {
    .content {
      .section {
        .title {
          /* ... */
        }
      }
    }
  }
}
```

### 7.3 代码质量

#### no-duplicate-selectors: true

不使用重复选择器。

```css
/* 不推荐 */
.button {
  background: #1890ff;
}

.button {
  color: #fff;
}

/* 推荐 */
.button {
  background: #1890ff;
  color: #fff;
}
```

#### declaration-block-no-duplicate-properties: true

不使用重复属性。

```css
/* 不推荐 */
.button {
  background: #1890ff;
  background: #36cfc9;
}

/* 推荐 */
.button {
  background: #1890ff;
}
```

#### block-no-empty: true

不使用空块。

```css
/* 不推荐 */
.button {
}

/* 推荐 */
.button {
  background: #1890ff;
}
```

### 7.4 现代CSS

#### alpha-value-notation: 'number'

使用数字表示透明度。

```css
/* 推荐 */
.button {
  background: rgba(24, 144, 255, 0.5);
}

/* 不推荐 */
.button {
  background: rgba(24, 144, 255, 50%);
}
```

#### color-function-notation: 'modern'

使用现代颜色函数。

```css
/* 推荐 */
.button {
  background: rgb(24 144 255);
  background: rgba(24 144 255 / 0.5);
}

/* 不推荐 */
.button {
  background: rgb(24, 144, 255);
  background: rgba(24, 144, 255, 0.5);
}
```

#### hue-degree-notation: 'angle'

使用角度表示色相。

```css
/* 推荐 */
.button {
  background: hsl(210deg 100% 50%);
}

/* 不推荐 */
.button {
  background: hsl(210 100% 50%);
}
```

---

## 8. 常见问题

### 8.1 如何禁用某条规则？

在`.stylelintrc.cjs`中设置规则为`null`：

```javascript
{
  rules: {
    'selector-class-pattern': null
  }
}
```

### 8.2 如何在文件中临时禁用规则？

使用注释：

```css
/* stylelint-disable */
.button {
  background: #1890ff;
}
/* stylelint-enable */

/* stylelint-disable color-named */
.button {
  background: red;
}
/* stylelint-enable color-named */

/* stylelint-disable-next-line color-named */
.button {
  background: red;
}
```

### 8.3 如何自动修复问题？

使用`--fix`选项：

```bash
npm run lint:style -- --fix
```

### 8.4 如何忽略特定文件？

在`.stylelintignore`中添加文件路径：

```
dist/
node_modules/
*.min.css
```

### 8.5 如何配置特定文件的规则？

使用`overrides`：

```javascript
{
  overrides: [
    {
      files: ['*.scss'],
      rules: {
        'at-rule-no-unknown': null
      }
    }
  ]
}
```

### 8.6 如何支持自定义CSS属性？

在`.stylelintrc.cjs`中配置：

```javascript
{
  rules: {
    'custom-property-pattern': null
  }
}
```

### 8.7 如何支持Tailwind CSS？

在`.stylelintrc.cjs`中配置：

```javascript
{
  rules: {
    'at-rule-no-unknown': [
      true,
      {
        ignoreAtRules: ['tailwind', 'apply', 'layer', 'variants', 'responsive', 'screen']
      }
    ]
  }
}
```

---

## 附录

### A. 规则列表

| 规则 | 级别 | 说明 |
|------|------|------|
| `indentation` | 2 | 2空格缩进 |
| `string-quotes` | `single` | 使用单引号 |
| `no-duplicate-selectors` | `true` | 不使用重复选择器 |
| `color-hex-case` | `lower` | 使用小写十六进制 |
| `color-hex-length` | `short` | 使用简短十六进制 |
| `color-named` | `never` | 不使用命名颜色 |
| `selector-max-id` | `0` | 不使用ID选择器 |
| `selector-max-type` | `3` | 限制类型选择器数量 |
| `selector-max-universal` | `1` | 限制通用选择器数量 |
| `max-nesting-depth` | `3` | 限制嵌套深度 |

### B. 相关文档

- [Stylelint官方文档](https://stylelint.io/)
- [Stylelint规则列表](https://stylelint.io/user-guide/rules/)
- [Stylelint Vue插件](https://github.com/ota-meshi/stylelint-config-recommended-vue)
- [Stylelint Order插件](https://github.com/hudochenkov/stylelint-order)

### C. 有用的命令

```bash
# 检查样式
npm run lint:style

# 自动修复问题
npm run lint:style -- --fix

# 检查特定文件
npx stylelint "src/**/*.css"

# 使用配置文件
npx stylelint --config .stylelintrc.cjs "src/**/*.css"

# 忽略配置文件
npx stylelint --no-config "src/**/*.css"

# 显示详细输出
npx stylelint --verbose "src/**/*.css"
```

---

**文档维护**：开发团队
**最后更新**：2026-02-27
**文档版本**：1.0.0
