---
layout: post
title: "Package.json을 사용하여 JavaScript 프로젝트의 사전 빌드 작업 설정하기"
description: " "
date: 2023-11-06
tags: [Package]
comments: true
share: true
---

JavaScript 프로젝트를 개발할 때 사전 빌드 작업을 설정하는 것은 매우 중요합니다. 이를 통해 자동화된 작업을 수행하고 코드의 품질을 향상시킬 수 있습니다. Package.json 파일을 사용하여 사전 빌드 작업을 설정하는 방법을 알아보겠습니다.

## Package.json 파일 생성하기

먼저 프로젝트 루트 디렉토리에서 다음 명령어를 사용하여 Package.json 파일을 생성합니다.

```bash
$ npm init
```

이 명령어를 실행하면 프로젝트에 대한 정보를 입력하는 프롬프트가 나타납니다. 입력이 완료되면 `package.json` 파일이 생성됩니다.

## 사전 빌드 작업을 위한 스크립트 추가하기

Package.json 파일에는 `scripts` 항목이 있습니다. 이 항목을 사용하여 사전 빌드 작업에 대한 스크립트를 추가할 수 있습니다. 다음은 예시입니다.

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "scripts": {
    "build": "npm run lint && npm run test"
  },
  "devDependencies": {
    "eslint": "^7.0.0",
    "mocha": "^8.0.0"
  }
}
```

위 예시에서는 `build`라는 스크립트를 추가했습니다. 이 스크립트는 `npm run lint` 명령어와 `npm run test` 명령어를 차례로 실행합니다. 따라서 사전 빌드 작업으로 코드의 문법 검사(`lint`)와 테스트(`test`)를 수행할 수 있습니다.

## 스크립트 실행하기

`npm run` 명령어를 사용하여 스크립트를 실행할 수 있습니다. 위의 예시에서는 다음과 같이 `build` 스크립트를 실행합니다.

```bash
$ npm run build
```

이를 통해 `npm run lint`와 `npm run test`가 차례로 실행되며, 사전 빌드 작업이 수행됩니다.

## 결론

Package.json을 사용하여 JavaScript 프로젝트의 사전 빌드 작업을 설정하는 방법을 알아보았습니다. `scripts` 항목을 이용하여 필요한 스크립트를 추가하고, `npm run` 명령어로 스크립트를 실행할 수 있습니다. 이를 통해 코드의 품질을 향상시키고 개발 과정을 자동화할 수 있습니다.

_**참고 자료:**_
- [npm 공식 문서](https://docs.npmjs.com/)