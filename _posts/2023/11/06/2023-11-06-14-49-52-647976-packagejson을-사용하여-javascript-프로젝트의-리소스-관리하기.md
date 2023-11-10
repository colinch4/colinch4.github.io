---
layout: post
title: "Package.json을 사용하여 JavaScript 프로젝트의 리소스 관리하기"
description: " "
date: 2023-11-06
tags: [Package]
comments: true
share: true
---

자바스크립트 프로젝트를 개발하다보면 다양한 종속성 관리와 리소스 관리가 필요합니다. 하지만 이러한 작업은 수동으로 하기에는 많은 시간과 노력이 필요합니다. 이를 해결하기 위해 패키지.json 파일을 사용하여 프로젝트의 리소스를 관리해보는 방법을 알아보겠습니다.

### 패키지.json 파일이란?

패키지.json 파일은 자바스크립트 프로젝트에서 사용되는 모듈 및 종속성을 정의하는 파일입니다. 이 파일을 사용하여 프로젝트의 종속성을 명시하고, 버전 관리, 라이브러리 다운로드 등을 자동화할 수 있습니다.

### 패키지.json 파일 생성하기

패키지.json 파일은 다음과 같이 명령어를 사용하여 생성할 수 있습니다.

```shell
npm init
```

위 명령어를 실행하면 프로젝트의 정보를 입력하라는 메시지가 표시됩니다. 해당 정보를 입력하면 패키지.json 파일이 생성됩니다.

### 패키지.json 파일 수정하기

패키지.json 파일은 다음과 같은 정보를 포함합니다.

#### dependencies

프로젝트에서 사용하는 다른 패키지의 종속성을 정의하는 부분입니다. 다른 패키지를 사용하기 위해서는 해당 패키지를 패키지.json 파일에 추가해야 합니다. 종속성을 추가하는 방법은 다음과 같습니다.

```json
"dependencies": {
  "패키지명": "버전"
}
```

예를 들어, lodash 패키지를 추가하려면 다음과 같이 입력합니다.

```json
"dependencies": {
  "lodash": "^4.17.21"
}
```

#### scripts

프로젝트에서 사용하는 스크립트 명령어를 정의하는 부분입니다. 자주 사용하는 스크립트를 패키지.json 파일에 추가하여 간편하게 실행할 수 있습니다. 스크립트를 추가하는 방법은 다음과 같습니다.

```json
"scripts": {
  "스크립트명": "실행할 명령어"
}
```

예를 들어, `start`라는 스크립트에 `node app.js` 명령어를 실행하도록 설정하려면 다음과 같이 입력합니다.

```json
"scripts": {
  "start": "node app.js"
}
```

### 패키지 설치하기

패키지.json 파일에 정의된 종속성을 설치하기 위해서는 다음 명령어를 사용합니다.

```shell
npm install
```

위 명령어를 실행하면 패키지.json 파일에 정의된 종속성이 자동으로 다운로드되고 설치됩니다.

### 정리

이제 패키지.json 파일을 사용하여 자바스크립트 프로젝트의 리소스를 관리하는 방법을 알아보았습니다. 패키지.json 파일은 종속성 관리 뿐만 아니라 스크립트 실행 등 다양한 기능을 제공하기 때문에 프로젝트 개발에서 유용하게 활용할 수 있습니다.

### References

- [npm 공식 문서](https://docs.npmjs.com/cli/v7/configuring-npm/package-json)
- [How to Use package.json](https://www.digitalocean.com/community/tutorials/nodejs-how-to-use-package-json-for-your-projects-ko)