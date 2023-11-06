---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 동적인 컴포넌트 로딩 설정하기"
description: " "
date: 2023-11-06
tags: []
comments: true
share: true
---

이번 블로그 포스트에서는 JavaScript 프로젝트에서 동적으로 컴포넌트를 로딩하는 방법을 Package.json 파일을 사용하여 설정하는 방법에 대해 알아보겠습니다.

## 1. 패키지 설치

먼저, 프로젝트의 루트 디렉토리에서 패키지를 설치해야 합니다. 아래 명령을 실행하여 필요한 패키지를 설치합니다.

```shell
npm install --save react-router-dom
```

이 명령은 `react-router-dom` 패키지를 설치하고, 패키지 정보를 Package.json 파일의 `dependencies` 항목에 추가합니다.

## 2. Webpack 설정

다음으로, Webpack을 사용하여 동적 컴포넌트 로딩을 설정해야 합니다. 프로젝트의 루트 디렉토리에 `webpack.config.js` 파일을 만들고 아래 코드를 추가합니다.

```javascript
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: 'babel-loader',
      },
    ],
  },
  resolve: {
    extensions: ['.js'],
  },
};
```

이 코드는 Webpack의 진입점을 `index.js`로 설정하고, 번들된 파일을 `bundle.js`로 출력합니다. 또한, Babel을 사용하여 JavaScript 파일을 변환하는데 사용할 `babel-loader`를 설정합니다.

## 3. 컴포넌트 로딩 설정

이제 Package.json 파일을 열고, 아래 코드를 추가합니다.

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "scripts": {
    "start": "webpack --mode development",
    "build": "webpack --mode production"
  },
  "dependencies": {
    "react-router-dom": "^5.2.0"
  }
}
```

이 코드는 프로젝트의 이름과 버전을 설정합니다. 그리고, `scripts` 항목은 프로젝트를 개발 모드로 실행하거나 번들링할 때 사용할 명령어를 설정합니다. `dependencies` 항목은 방금 설치한 패키지인 `react-router-dom`을 포함하고 있습니다.

## 4. 컴포넌트 로딩 사용

이제 설정이 완료되었습니다. JavaScript 파일에서 동적으로 컴포넌트를 로딩하는 방법은 `import()` 함수를 사용하는 것입니다. 예를 들어, 아래 코드는 `About` 컴포넌트를 로딩하는 예입니다.

```javascript
import React from 'react';

class App extends React.Component {
  state = {
    component: null,
  };

  componentDidMount() {
    import('./About').then((module) => {
      this.setState({ component: module.default });
    });
  }

  render() {
    const { component: Component } = this.state;

    return Component ? <Component /> : '로딩 중...';
  }
}

export default App;
```

이 코드는 `component` 상태를 사용하여 로딩된 컴포넌트를 저장하고, `componentDidMount` 라이프사이클 메서드에서 `import()` 함수를 사용하여 `About` 컴포넌트를 동적으로 로딩합니다. 로딩이 완료되면, 컴포넌트를 렌더링하고 그렇지 않으면 "로딩 중..."이라는 텍스트를 표시합니다.

## 마치며

이제 JavaScript 프로젝트에서 Package.json 파일을 사용하여 동적 컴포넌트 로딩을 설정하는 방법에 대해 알아보았습니다. 이러한 설정을 통해 프로젝트의 유연성과 성능을 향상시킬 수 있습니다. 그러므로 동적 컴포넌트 로딩이 필요한 경우, 위의 단계를 따라 진행하세요.

참고 자료:

- [Webpack 공식 문서](https://webpack.js.org/)
- [React Router DOM 공식 문서](https://reactrouter.com/web/guides/quick-start)
- [Babel 공식 문서](https://babeljs.io/)