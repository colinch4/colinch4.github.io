---
layout: post
title: "Package.json을 활용하여 JavaScript 프로젝트 환경 변수 설정하기"
description: " "
date: 2023-11-06
tags: [package]
comments: true
share: true
---

JavaScript 프로젝트에서 환경 변수를 설정하는 것은 중요합니다. 이를 통해 프로젝트의 설정값을 유지하고 배포 환경에 따라 다른 값을 사용할 수 있습니다. Package.json 파일을 사용하여 간단하게 환경 변수를 설정하는 방법을 알아보겠습니다.

## 1. Package.json 파일 생성하기

프로젝트 루트 디렉토리에 있는 Package.json 파일은 프로젝트의 메타 데이터 및 의존성을 정의합니다. 만약 Package.json 파일이 없다면, 다음 명령어를 사용하여 생성할 수 있습니다:

```bash
npm init
```

위 명령어를 실행하면 몇 가지 질문이 나타납니다. 원하는 대로 답변을 입력하고, Package.json 파일을 생성할 수 있습니다.

## 2. 환경 변수 설정하기

Package.json 파일을 열어 `scripts` 속성 아래에 원하는 환경 변수를 설정할 수 있습니다. 예를 들어, `development` 환경에서는 `ENV` 변수에 `dev` 값을 설정하고, `production` 환경에서는 `ENV` 변수에 `prod` 값을 설정하고 싶다면 다음과 같이 작성할 수 있습니다:

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "scripts": {
    "start": "ENV=dev node index.js",
    "build": "ENV=prod node index.js"
  }
}
```

위 예시에서는 `start` 스크립트를 실행할 때 `ENV` 변수에 `dev` 값을 설정하고, `build` 스크립트를 실행할 때 `ENV` 변수에 `prod` 값을 설정하도록 정의하였습니다.

## 3. 환경 변수 사용하기

프로젝트 소스 코드에서 환경 변수를 사용할 때는 `process.env` 객체를 활용합니다. 위에서 설정한 `ENV` 변수를 사용하려면 다음과 같이 코드를 작성할 수 있습니다:

```javascript
if (process.env.ENV === 'dev') {
  console.log('Development environment');
} else if (process.env.ENV === 'prod') {
  console.log('Production environment');
} else {
  console.log('Unknown environment');
}
```

위 코드는 `process.env.ENV` 값에 따라서 실행되는 로그 메시지가 달라집니다.

## 마무리

이렇게 Package.json 파일을 활용하여 JavaScript 프로젝트의 환경 변수를 설정하는 방법에 대해 알아보았습니다. 환경 변수를 이용하여 프로젝트의 설정 값을 유지하고 다양한 환경에서 일관되게 동작하도록 설정할 수 있습니다.

- 참고 문서: [npm 개발자 가이드](https://docs.npmjs.com/cli/v7/configuring-npm/package-json)