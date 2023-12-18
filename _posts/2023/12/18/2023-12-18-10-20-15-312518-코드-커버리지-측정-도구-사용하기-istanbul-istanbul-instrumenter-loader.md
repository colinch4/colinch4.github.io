---
layout: post
title: "[typescript] 코드 커버리지 측정 도구 사용하기 (Istanbul, istanbul-instrumenter-loader)"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

코드 커버리지(Coverage)란 소프트웨어가 테스트된 기능의 얼마나 많은 부분을 포함하는지를 나타내는 지표입니다. 코드 커버리지를 측정하고 관리하는 것은 소프트웨어의 품질을 향상시키는 데 도움이 됩니다. TypeScript 프로젝트에서 코드 커버리지를 측정하기 위해 Istanbul과 istanbul-instrumenter-loader를 사용할 수 있습니다.

## Istanbul이란?

[Istanbul](https://istanbul.js.org/)은 JavaScript와 TypeScript를 위한 코드 커버리지 도구입니다. 프로젝트의 소스 코드를 분석하여 각 줄의 실행 여부를 추적하고 커버리지 보고서를 생성합니다.

## istanbul-instrumenter-loader란?

[istanbul-instrumenter-loader](https://github.com/deepsweet/istanbul-instrumenter-loader)는 Webpack을 위한 Istanbul 인스트루먼터입니다. 이 로더를 사용하면 소스 코드를 테스트하기 전에 Istanbul을 사용하여 코드를 instrument(센싱, 감시)할 수 있어 테스트용 소스 코드에 대해 커버리지를 측정할 수 있습니다.

## Istanbul 및 istanbul-instrumenter-loader 사용하기

먼저 프로젝트에 Istanbul 및 istanbul-instrumenter-loader 패키지를 설치합니다.

```bash
npm install --save-dev istanbul istanbul-instrumenter-loader
```

그런 다음, Webpack 구성 파일에 `istanbul-instrumenter-loader`를 추가하고 설정합니다.

```javascript
module.exports = {
  // ... 다른 구성 설정
  module: {
    rules: [
      {
        test: /\.(ts|tsx)$/,
        enforce: 'post',
        use: {
          loader: 'istanbul-instrumenter-loader',
          options: { esModules: true }
        }
      }
    ]
  }
};
```

이제 테스트를 실행하고 Istanbul을 사용하여 코드 커버리지를 측정할 준비가 되었습니다.

이를 통해 코드 커버리지를 통해 소프트웨어 품질을 향상시키고 실수를 미리 방지할 수 있습니다.

## 결론
Istanbul과 istanbul-instrumenter-loader를 사용하면 TypeScript 프로젝트에서 코드 커버리지를 효과적으로 측정하고 관리할 수 있습니다. 올바른 테스트와 코드 커버리지 측정은 안정적이고 견고한 소프트웨어를 만드는 데 도움이 됩니다.