---
layout: post
title: "npm 을 활용한 배포 자동화 (Deployment automation with npm)"
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

소프트웨어 개발에서 배포 단계는 매우 중요합니다. 애플리케이션을 실제 사용자에게 전달하는 과정은 정확하고 신뢰할 수 있어야 합니다. npm을 사용하여 배포 과정을 자동화하는 방법을 알아보겠습니다.

## 1. npm 스크립트 작성하기

우선, package.json 파일의 scripts 섹션에 배포에 필요한 명령어를 작성합니다. 예를 들어, 아래와 같이 배포 스크립트를 작성할 수 있습니다.

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "scripts": {
    "build": "npm run lint && npm run test && npm run compile",
    "lint": "eslint src",
    "test": "mocha test",
    "compile": "babel src -d dist",
    "deploy": "npm run build && npm publish"
  },
  "dependencies": {
    "eslint": "^7.10.0",
    "mocha": "^8.2.1",
    "babel-cli": "^6.26.0"
  },
  "devDependencies": {
    "babel-preset-env": "^1.7.0"
  }
}
```

위의 예제에서는 빌드(build), lint, 테스트(test), 컴파일(compile) 단계를 포함하고 있습니다. `deploy` 스크립트를 사용하여 이전 단계들을 실행한 뒤, 최종적으로 앱을 배포합니다.

## 2. 배포 과정 자동화하기

npm 스크립트를 사용하여 배포 과정을 자동화할 수 있습니다. 다음 명령어를 실행하여 앱을 배포합니다.

```bash
npm run deploy
```

위 명령어는 `deploy` 스크립트에 정의된 모든 단계들을 실행합니다. 빌드(build), lint, 테스트(test), 컴파일(compile)이 순차적으로 실행되며, 마지막으로 앱이 배포됩니다.

## 3. 추가 설정하기

배포 자동화를 위해 추가적인 설정이 필요할 수 있습니다. 예를 들어, 배포 이전에 환경 변수를 설정하거나, 배포 후에 서버를 재시작하는 등의 작업을 수행할 수 있습니다. 이러한 설정들은 `deploy` 스크립트에 추가하여 원하는 작업을 수행할 수 있습니다.

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "scripts": {
    "build": "npm run lint && npm run test && npm run compile",
    "lint": "eslint src",
    "test": "mocha test",
    "compile": "babel src -d dist",
    "deploy": "npm run build && npm publish && node restart-server.js"
  },
  "dependencies": {
    "eslint": "^7.10.0",
    "mocha": "^8.2.1",
    "babel-cli": "^6.26.0"
  },
  "devDependencies": {
    "babel-preset-env": "^1.7.0"
  }
}
```

위의 예제에서는 `deploy` 스크립트에 `node restart-server.js`를 추가하여 배포 후 서버를 재시작하는 작업을 수행하도록 설정하였습니다.

## 마무리

npm을 활용하여 배포 자동화를 구현할 수 있습니다. 이를 통해 애플리케이션의 배포 과정을 자동화하고, 효율적인 개발과 배포를 달성할 수 있습니다.

#npm #배포 #자동화