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
    'vue/multi-word-component-names': 'off',
    'vue/no-v-html': 'warn',
    'vue/require-default-prop': 'off',
    'vue/require-explicit-emits': 'off',
    'vue/html-self-closing': ['error', {
      html: {
        void: 'always',
        normal: 'never',
        component: 'always'
      },
      svg: 'always',
      math: 'always'
    }],
    'vue/max-attributes-per-line': ['error', {
      singleline: 3,
      multiline: 1
    }],
    'vue/html-closing-bracket-newline': ['error', {
      singleline: 'never',
      multiline: 'always'
    }],
    'vue/first-attribute-linebreak': ['error', {
      singleline: 'ignore',
      multiline: 'below'
    }],
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-unused-vars': ['warn', {
      argsIgnorePattern: '^_',
      varsIgnorePattern: '^_'
    }],
    'prefer-const': 'warn',
    'no-var': 'error',
    'eqeqeq': ['error', 'always'],
    'curly': ['error', 'all'],
    'no-else-return': 'warn',
    'no-nested-ternary': 'error',
    'no-unneeded-ternary': 'error',
    'arrow-body-style': ['warn', 'as-needed'],
    'prefer-arrow-callback': 'warn',
    'prefer-template': 'warn',
    'template-curly-spacing': ['error', 'never'],
    'object-shorthand': ['warn', 'always'],
    'prefer-destructuring': ['warn', {
      array: true,
      object: true
    }, {
      enforceForRenamedProperties: false
    }],
    'no-duplicate-imports': 'error',
    'no-useless-rename': 'error',
    'no-param-reassign': ['warn', {
      props: true,
      ignorePropertyModificationsFor: ['state', 'acc', 'e']
    }],
    'no-shadow': 'warn',
    'no-return-await': 'warn',
    'require-await': 'warn',
    'no-promise-executor-return': 'error',
    'prefer-promise-reject-errors': 'error',
    'no-async-promise-executor': 'warn',
    'no-throw-literal': 'error',
    'prefer-rest-params': 'warn',
    'prefer-spread': 'warn',
    'no-array-constructor': 'error',
    'no-new-object': 'error',
    'no-lone-blocks': 'error',
    'no-empty-function': 'warn',
    'no-implied-eval': 'error',
    'no-eval': 'error',
    'no-with': 'error',
    'no-delete-var': 'error',
    'no-undef-init': 'warn',
    'no-multi-spaces': 'error',
    'no-multiple-empty-lines': ['error', {
      max: 1,
      maxEOF: 1,
      maxBOF: 0
    }],
    'no-trailing-spaces': 'error',
    'no-mixed-spaces-and-tabs': 'error',
    'indent': 'off',
    'quotes': ['error', 'single', {
      avoidEscape: true,
      allowTemplateLiterals: true
    }],
    'semi': ['error', 'never'],
    'comma-dangle': ['error', 'never'],
    'comma-spacing': ['error', {
      before: false,
      after: true
    }],
    'comma-style': ['error', 'last'],
    'key-spacing': ['error', {
      beforeColon: false,
      afterColon: true
    }],
    'keyword-spacing': ['error', {
      before: true,
      after: true
    }],
    'space-before-blocks': ['error', 'always'],
    'space-before-function-paren': ['error', {
      anonymous: 'always',
      named: 'never',
      asyncArrow: 'always'
    }],
    'space-in-parens': ['error', 'never'],
    'space-infix-ops': 'error',
    'space-unary-ops': ['error', {
      words: true,
      nonwords: false
    }],
    'spaced-comment': ['warn', 'always', {
      markers: ['/']
    }],
    'brace-style': ['error', '1tbs', {
      allowSingleLine: true
    }],
    'object-curly-spacing': ['error', 'always'],
    'array-bracket-spacing': ['error', 'never'],
    'computed-property-spacing': ['error', 'never'],
    'func-call-spacing': ['error', 'never'],
    'no-whitespace-before-property': 'error',
    'no-irregular-whitespace': 'error',
    'lines-between-class-members': ['warn', 'always', {
      exceptAfterSingleLine: true
    }],
    'padding-line-between-statements': [
      'error',
      { blankLine: 'always', prev: '*', next: 'return' },
      { blankLine: 'always', prev: ['const', 'let', 'var'], next: '*' },
      { blankLine: 'any', prev: ['const', 'let', 'var'], next: ['const', 'let', 'var'] },
      { blankLine: 'always', prev: 'directive', next: '*' },
      { blankLine: 'any', prev: 'directive', next: 'directive' },
      { blankLine: 'always', prev: ['case', 'default'], next: '*' }
    ],
    'vue/component-name-in-template-casing': ['error', 'PascalCase', {
      registeredComponentsOnly: false,
      ignores: []
    }],
    'vue/component-definition-name-casing': ['error', 'PascalCase'],
    'vue/define-macros-order': ['warn', {
      order: ['defineProps', 'defineEmits']
    }],
    'vue/no-setup-props-destructure': 'warn',
    'vue/no-unused-vars': ['warn', {
      ignorePattern: '^_'
    }],
    'vue/no-unused-properties': 'warn',
    'vue/no-unused-components': 'warn',
    'vue/order-in-components': 'warn',
    'vue/this-in-template': 'warn',
    'vue/v-on-event-hyphenation': ['warn', 'always', {
      autofix: true,
      ignore: []
    }],
    'vue/attribute-hyphenation': ['warn', 'always', {
      ignore: []
    }],
    'vue/prop-name-casing': ['error', 'camelCase'],
    'vue/component-tags-order': ['error', {
      order: ['script', 'template', 'style']
    }],
    'vue/block-tag-newline': ['error', {
      singleline: 'always',
      multiline: 'always'
    }],
    'vue/html-indent': ['error', 2],
    'vue/html-quotes': ['error', 'double'],
    'vue/no-template-shadow': 'warn',
    'vue/no-duplicate-attr-inheritance': 'warn',
    'vue/no-multiple-template-root': 'off',
    'vue/require-v-for-key': 'error',
    'vue/valid-v-for': 'error',
    'vue/valid-v-if': 'error',
    'vue/valid-v-show': 'error',
    'vue/valid-v-bind': 'error',
    'vue/valid-v-on': 'error',
    'vue/valid-v-model': 'error',
    'vue/valid-v-slot': 'error',
    'vue/valid-v-text': 'error',
    'vue/valid-v-html': 'error',
    'vue/valid-v-pre': 'error',
    'vue/valid-v-cloak': 'error',
    'vue/valid-v-once': 'error',
    'vue/valid-v-is': 'error',
    'vue/valid-v-memo': 'error',
    'vue/valid-v-else-if': 'error',
    'vue/valid-v-else': 'error'
  }
}
