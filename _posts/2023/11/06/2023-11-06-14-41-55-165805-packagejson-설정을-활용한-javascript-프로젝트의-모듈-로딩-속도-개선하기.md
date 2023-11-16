---
layout: post
title: "Package.json 설정을 활용한 JavaScript 프로젝트의 모듈 로딩 속도 개선하기"
description: " "
date: 2023-11-06
tags: [Package]
comments: true
share: true
---

JavaScript 프로젝트를 개발하면서 모듈 로딩 속도는 매우 중요한 요소입니다. 모듈 로딩 시간이 길다면 사용자 경험에 지장을 줄 수 있고, 애플리케이션의 성능에도 영향을 미칠 수 있습니다. 이에 따라 Package.json 파일에 몇 가지 설정을 추가하여 모듈 로딩 속도를 개선할 수 있습니다.

## 1. "module" 필드 사용하기

Package.json 파일의 "module" 필드는 ES6 모듈을 지원하는 브라우저에서 사용할 모듈 파일의 경로를 지정합니다. 이를 이용하여 자바스크립트 번들러(Webpack, Rollup 등)를 사용해 번들링된 모듈이 아닌 개별 모듈 파일을 로딩할 수 있습니다. 이는 번들링된 파일보다 더 적은 사이즈의 개별 모듈 파일을 로딩하여 초기 로딩 속도를 개선할 수 있습니다.

```json
{
  "module": "dist/main.js",
  "browser": {
    "dist/main.js": "./src/main.js"
  }
}
```

위 예시에서 "module" 필드에는 번들링된 모듈 파일의 경로를 지정하고, "browser" 필드에는 개별 모듈 파일의 경로를 지정하여 브라우저 환경에서 모듈을 로딩할 수 있도록 설정합니다.

## 2. "browser" 필드 사용하기

Package.json 파일의 "browser" 필드는 모듈 번들러가 아닌 브라우저 환경에서 모듈을 로딩할 때 사용됩니다. 이를 이용하여 번들링된 파일 대신 오리지널 모듈 파일을 로딩하도록 설정할 수 있습니다. 이는 로딩된 파일의 사이즈를 줄이고 초기 로딩 속도를 개선할 수 있습니다.

```json
{
  "browser": {
    "lodash": "lodash-es"
  }
}
```

위 예시에서는 "lodash" 모듈을 브라우저에서 "lodash-es" 모듈로 로딩하도록 설정하였습니다. "lodash-es"는 Tree Shaking을 지원하는 ES6 버전의 lodash 모듈이며, 이를 사용하여 필요한 코드만 로딩하게 됩니다.

## 결론

Package.json 파일의 "module" 및 "browser" 필드를 적절하게 설정하여 JavaScript 프로젝트의 모듈 로딩 속도를 개선할 수 있습니다. "module" 필드를 사용하여 개별 모듈 파일을 로딩하거나, "browser" 필드를 사용하여 번들링된 파일 대신 오리지널 모듈 파일을 로딩하도록 설정하는 등의 방법을 활용할 수 있습니다. 이를 통해 사용자 경험을 향상시키고 애플리케이션의 성능을 개선할 수 있습니다.

### 참고 자료
- [What is `package.module` field for?](https://stackoverflow.com/questions/50669362/what-is-package-module-field-for)
- [package browser field](https://docs.npmjs.com/cli/v7/configuring-npm/package-json#browser)