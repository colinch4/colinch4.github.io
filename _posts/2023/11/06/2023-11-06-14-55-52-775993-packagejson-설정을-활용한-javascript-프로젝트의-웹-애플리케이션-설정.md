---
layout: post
title: "Package.json 설정을 활용한 JavaScript 프로젝트의 웹 애플리케이션 설정"
description: " "
date: 2023-11-06
tags: [Package]
comments: true
share: true
---

이번 글에서는 JavaScript 프로젝트의 웹 애플리케이션 설정을 위해 `package.json` 파일을 사용하는 방법에 대해 알아보겠습니다. 

## package.json 파일이란?

`package.json` 파일은 JavaScript 프로젝트의 설정과 의존성을 정의하는데 사용되는 JSON 형식의 파일입니다. 이 파일은 프로젝트의 루트 디렉토리에 위치하며, 프로젝트에 필요한 의존성 패키지, 스크립트, 버전, 저작자 등의 정보를 담고 있습니다.

## package.json 파일 생성하기

1. 프로젝트의 루트 디렉토리에서 터미널을 열고 `npm init` 명령어를 실행합니다.
2. 명령어를 실행하면 프로젝트 정보를 입력하는 프롬프트가 나타납니다.
3. 프롬프트에 따라 프로젝트의 이름, 버전, 설명 등의 정보를 입력합니다.

## 의존성 패키지 추가하기

`package.json` 파일을 사용하면 프로젝트에 필요한 의존성 패키지를 손쉽게 관리할 수 있습니다.

1. 프로젝트 디렉토리에서 터미널을 열고 `npm install <패키지 이름>` 명령어를 실행합니다.
2. 명령어를 실행하면 해당 패키지를 프로젝트의 `node_modules` 디렉토리에 설치하고, `package.json` 파일의 `dependencies` 항목에 패키지 정보가 추가됩니다.

## 스크립트 설정하기

`package.json` 파일을 사용하면 프로젝트에서 사용하는 스크립트를 정의할 수도 있습니다.

```json
{
  "scripts": {
    "start": "node app.js",
    "build": "webpack"
  }
}
```

위 예시에서는 `start` 스크립트에 `node app.js` 명령어를, `build` 스크립트에는 `webpack` 명령어를 설정한 것을 볼 수 있습니다. 이렇게 설정된 스크립트는 `npm run` 명령어와 함께 사용하여 실행할 수 있습니다.

```bash
npm run start
npm run build
```

## 버전 및 저작자 등 정보 설정하기

`package.json` 파일에는 프로젝트의 버전, 저작자, 라이선스 등의 정보를 설정할 수 있습니다.

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "description": "My JavaScript project",
  "author": "John Doe",
  "license": "MIT"
}
```

이외에도 `package.json` 파일을 사용하여 프로젝트의 환경 설정, 테스트 스크립트 등을 정의할 수도 있습니다.

## 결론

`package.json` 파일은 JavaScript 프로젝트의 웹 애플리케이션 설정을 관리하는데 유용한 도구입니다. 이 파일을 활용하여 의존성 관리, 스크립트 실행, 버전 정보 등을 효과적으로 관리할 수 있습니다.

## 참고 자료

- [npm 공식 문서](https://docs.npmjs.com/cli/v7/configuring-npm/package-json)
- [Understanding package.json in Node.js](https://www.digitalocean.com/community/tutorials/nodejs-package-json)