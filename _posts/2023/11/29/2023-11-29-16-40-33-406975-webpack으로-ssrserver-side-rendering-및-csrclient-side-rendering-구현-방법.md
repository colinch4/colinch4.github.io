---
layout: post
title: "[javascript] Webpack으로 SSR(Server-side Rendering) 및 CSR(Client-Side Rendering) 구현 방법"
description: " "
date: 2023-11-29
tags: [javascript]
comments: true
share: true
---

이번 글에서는 Webpack을 사용하여 서버 사이드 렌더링(SSR) 및 클라이언트 사이드 렌더링(CSR)을 구현하는 방법에 대해 알아보겠습니다.

## 1. SSR(Server-side Rendering) 구현

서버 사이드 렌더링은 웹 페이지의 초기 로딩 속도를 개선하기 위해 사용됩니다. 서버에서 페이지의 HTML을 렌더링하여 클라이언트에게 전달하는 방식입니다.

Webpack에서 SSR을 구현하기 위해 다음과 같은 단계를 따르면 됩니다.

### 1.1. Entry 및 Output 설정

Webpack 설정 파일에서 entry 및 output을 설정해야 합니다. entry는 서버 사이드 렌더링을 시작할 파일을 가리키고, output은 빌드된 파일의 경로와 이름을 지정합니다.

```javascript
module.exports = {
  entry: './src/server.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'server.bundle.js',
  },
};
```

### 1.2. Loaders 설정

서버 사이드 렌더링을 위해 필요한 파일들을 로드하기 위해 필요한 로더를 설정해야 합니다. 주로 Babel 로더를 사용하여 ES6+ 코드를 변환하는 작업이 필요합니다.

```javascript
module.exports = {
  // ...
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
    ],
  },
};
```

### 1.3. External 관리

서버 사이드 렌더링 시에는 클라이언트와 달리 브라우저 환경이 없기 때문에 일부 라이브러리를 외부에서 가져와야 할 수도 있습니다. 이를 위해 externals 설정을 사용하여 필요한 라이브러리를 외부에서 가져올 수 있습니다.

```javascript
module.exports = {
  // ...
  externals: {
    react: 'commonjs react',
    'react-dom': 'commonjs react-dom',
  },
};
```

### 1.4. 서버 빌드 및 실행

위 설정들을 모두 적용한 후, Webpack을 사용하여 서버를 빌드하고 실행할 수 있습니다.

```bash
$ webpack --config webpack.config.js
$ node dist/server.bundle.js
```

이제 서버 사이드 렌더링이 구현되었습니다.


## 2. CSR(Client-Side Rendering) 구현

클라이언트 사이드 렌더링은 서버에서 받은 초기 HTML을 기반으로 클라이언트에서 동적으로 렌더링하는 방식입니다. Webpack을 사용하여 CSR을 구현하기 위해 다음과 같은 단계를 따르면 됩니다.

### 2.1. Entry 및 Output 설정

SSR과 마찬가지로 Webpack 설정 파일에서 entry와 output을 설정해야 합니다. 다만, 이번에는 클라이언트 사이드 렌더링을 시작할 파일을 가리키는 entry와 빌드된 파일의 이름을 포함한 output을 설정해야 합니다.

```javascript
module.exports = {
  entry: './src/client.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'client.bundle.js',
  },
};
```

### 2.2. Loaders 설정

CSR을 위해서도 필요한 파일들을 로드하기 위해 loaders를 설정해줍니다. 주로 Babel 로더를 사용하여 ES6+ 코드를 변환하는 작업이 필요합니다.

```javascript
module.exports = {
  // ...
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
    ],
  },
};
```

### 2.3. HTML 템플릿 설정

CSR을 구현하기 위해서는 빌드된 JS 파일을 HTML 파일에 넣어주어야 합니다. 이를 위해 HtmlWebpackPlugin을 사용하여 HTML 템플릿을 생성하고 빌드된 JS 파일을 자동으로 삽입할 수 있습니다.

```bash
$ npm install --save-dev html-webpack-plugin
```

```javascript
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  // ...
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
    }),
  ],
};
```

### 2.4. 클라이언트 빌드 및 실행

위 설정들을 모두 적용한 후, Webpack을 사용하여 클라이언트를 빌드하고 실행할 수 있습니다.

```bash
$ webpack --config webpack.config.js
$ npx serve dist
```

이제 클라이언트 사이드 렌더링이 구현되었습니다.

---

이제 Webpack을 사용하여 SSR 및 CSR을 구현하는 방법에 대해 알아보았습니다. Webpack은 강력한 모듈 번들러로서 다양한 기능과 설정을 제공하므로 프로젝트에 적절하게 활용하면 보다 효율적이고 유연한 웹 애플리케이션을 구축할 수 있습니다.

참고 자료:

- [Webpack Documentation](https://webpack.js.org/)
- [Babel Documentation](https://babeljs.io/docs/)
- [HtmlWebpackPlugin Documentation](https://webpack.js.org/plugins/html-webpack-plugin/)