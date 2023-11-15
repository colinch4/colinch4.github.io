---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 실행 환경 설정하기"
description: " "
date: 2023-11-06
tags: [javascript]
comments: true
share: true
---

JavaScript 프로젝트를 시작할 때 가장 먼저 해야 할 일은 실행 환경을 설정하는 것입니다. Package.json 파일은 JavaScript 프로젝트의 실행 환경을 정의하는 데 사용되는 중요한 파일입니다. 이 파일을 사용하여 프로젝트의 종속성, 스크립트, 환경 변수 등을 설정할 수 있습니다.

## Package.json 파일 생성하기

먼저 새로운 프로젝트 폴더를 만든 후, 해당 폴더에서 터미널을 열어 다음 명령을 실행하여 Package.json 파일을 생성합니다:

```shell
$ npm init
```

위 명령을 실행하면 일련의 질문이 나타나게 됩니다. 이 질문에 응답하면서 프로젝트에 대한 기본 설정을 입력할 수 있습니다.

## 종속성 관리하기

Package.json 파일에서 프로젝트에 필요한 종속성(dependency)을 관리할 수 있습니다. 종속성은 프로젝트를 실행하기 위해 필요한 외부 패키지들을 의미합니다.

종속성을 추가하기 위해서는 `npm install` 명령을 사용합니다. 예를 들어, `lodash` 패키지를 종속성에 추가하고 싶다면 다음 명령을 실행합니다:

```shell
$ npm install lodash --save
```

위 명령을 실행하면 lodash 패키지가 프로젝트의 종속성으로 추가됩니다. 이때, `--save` 옵션을 사용하여 Package.json 파일에 종속성 정보를 자동으로 추가할 수 있습니다.

## 스크립트 설정하기

Package.json 파일은 프로젝트에서 사용할 수 있는 스크립트(script)를 설정하는 데에도 사용됩니다. 예를 들어, 프로젝트를 실행하기 위한 스크립트를 설정한다면 다음과 같이 작성할 수 있습니다:

```json
{
  "scripts": {
    "start": "node index.js"
  }
}
```

위 예제에서는 `start` 스크립트를 정의하고 있으며, 해당 스크립트를 실행하면 `index.js` 파일이 실행됩니다.

스크립트를 실행하기 위해서는 `npm run` 명령을 사용합니다.

```shell
$ npm run start
```

## 환경 변수 설정하기

Package.json 파일을 사용하여 프로젝트에 필요한 환경 변수(environment variable)를 설정할 수도 있습니다. 환경 변수는 프로젝트에서 사용되는 개별 변수들을 의미합니다.

환경 변수를 설정하기 위해서는 `env` 속성을 사용합니다. 예를 들어, `PORT` 환경 변수를 3000으로 설정하고 싶다면 다음과 같이 작성할 수 있습니다:

```json
{
  "env": {
    "PORT": "3000"
  }
}
```

위 예제에서는 `PORT` 환경 변수를 3000으로 설정하고 있습니다.

## 결론

Package.json 파일은 JavaScript 프로젝트의 실행 환경을 설정하는 데에 필수적인 역할을 합니다. 이 파일을 통해 종속성, 스크립트, 환경 변수 등을 설정하여 프로젝트를 관리할 수 있습니다.

---

References:
- [npm Documentation](https://docs.npmjs.com/getting-started/using-a-package.json)
- [How to Use package.json, the Core of Any Node.js Project or npm Package](https://www.freecodecamp.org/news/how-to-use-package-json-the-core-of-any-node-js-project-npm-package/)

[#JavaScript](en) [#Node.js](en)