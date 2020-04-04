module.exports = {
  env: {
    es6: true,
    node: true,
  },
  extends: [
    'airbnb-base',
    "prettier",
    "prettier/@typescript-eslint",
    "plugin:import/typescript",
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
    project: "./tsconfig.json"
  },
  plugins: [
    '@typescript-eslint',
  ],
  ignorePatterns: ["rollup.config.js", "node_modules/"],
  rules: {
    'import/extensions': [
      'error', 'ignorePackages', {
      js: 'never',
      mjs: 'never',
      ts: 'never',
    }]
  },
};
