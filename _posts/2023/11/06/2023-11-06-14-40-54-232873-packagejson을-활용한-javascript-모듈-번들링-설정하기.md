---
layout: post
title: "Package.json을 활용한 JavaScript 모듈 번들링 설정하기"
description: " "
date: 2023-11-06
tags: [javascript]
comments: true
share: true
---

JavaScript 개발에서 모듈 번들링은 코드를 하나의 파일로 결합하여 웹 애플리케이션의 성능을 향상시키는 방법입니다. JavaScript 모듈 번들링 도구 중에서 가장 인기있는 도구인 Webpack을 사용하여, Package.json 파일을 활용하여 프로젝트의 모듈 번들링 설정을 관리할 수 있습니다.

## Package.json 파일 생성하기

프로젝트 루트 폴더에서 다음 npm 명령어를 실행하여 Package.json 파일을 생성합니다.

```bash
npm init -y
```

위 명령어를 실행하면 기본적인 Package.json 파일이 생성됩니다.

## Webpack 설치하기

Webpack을 사용하기 위해 다음 npm 명령어로 Webpack 패키지를 설치합니다.

```bash
npm install webpack webpack-cli --save-dev
```

위 명령어를 실행하면 프로젝트의 package.json 파일에 devDependencies 항목으로 Webpack 패키지가 추가됩니다.

## Webpack 구성 파일 생성하기

Webpack 구성 파일은 프로젝트 루트 폴더에 webpack.config.js라는 이름으로 생성됩니다. 이 파일은 Webpack이 프로젝트를 번들링할 때 어떠한 동작을 수행해야 하는지를 정의합니다.

```javascript
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
};
```

위 예제에서는 entry 속성을 사용하여 번들링할 진입점 파일을 지정하고, output 속성을 사용하여 번들링된 파일의 이름과 경로를 설정합니다.

## 번들링 실행하기

Webpack 구성 파일이 준비되었다면, 다음 npm 명령어로 번들링을 실행할 수 있습니다.

```bash
npx webpack
```

위 명령어를 실행하면 Webpack이 entry로 지정된 파일을 기반으로 번들링을 수행하고, output으로 지정된 경로에 번들링된 파일을 생성합니다.

## 결론

Package.json을 활용하여 Webpack을 사용한 JavaScript 모듈 번들링 설정을 관리할 수 있습니다. 이를 통해 프로젝트의 의존성 관리와 번들링 과정을 간편하게 수행할 수 있습니다. 자세한 내용은 [Webpack 공식 문서](https://webpack.js.org/)를 참고하십시오.

*#javascript #webpack*