---
layout: post
title: "npm 을 활용한 프로젝트 관리 (Project management with npm)"
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

## 개요

npm은 Node.js 패키지 매니저로, JavaScript 프로젝트에서 종속성을 관리하고 실행 환경을 구축하는 데 필요한 도구입니다. 이 글에서는 npm을 활용한 프로젝트 관리에 대해 알아보겠습니다.

## npm 설치하기

npm을 사용하기 위해서는 우선 Node.js를 설치해야 합니다. Node.js 설치가 완료되면 npm도 함께 설치됩니다. 설치가 완료되었다면, 터미널 또는 명령 프롬프트에서 `npm --version` 명령어를 실행하여 npm 버전을 확인할 수 있습니다.

## 프로젝트 생성

npm을 이용하여 프로젝트를 생성하는 방법은 매우 간단합니다. 프로젝트를 생성할 디렉토리로 이동한 후 다음 명령어를 실행하면 됩니다.

```shell
npm init
```

이 명령어를 실행하면 프로젝트 설정을 위한 몇 가지 질문이 표시됩니다. 질문에 답하고 나면 `package.json` 파일이 생성되며, 이 파일은 프로젝트의 구성과 종속성 정보를 담고 있습니다.

## 종속성 관리

npm을 사용하면 매우 편리하게 프로젝트의 종속성을 관리할 수 있습니다. 종속성을 추가하기 위해서는 `npm install` 명령어를 사용합니다. 예를 들어, `lodash`라는 라이브러리를 프로젝트에 추가하려면 다음과 같이 실행합니다.

```shell
npm install lodash
```

이렇게 하면 `package.json` 파일의 `dependencies` 항목에 `lodash`가 추가되며, 설치된 라이브러리는 `node_modules` 폴더에 저장됩니다.

## 스크립트 실행

`package.json` 파일의 `scripts` 항목을 활용하면 편리하게 스크립트를 실행할 수 있습니다. `scripts` 항목에는 자주 사용하는 스크립트들을 등록할 수 있습니다.

```json
{
  "scripts": {
    "start": "node app.js",
    "test": "jest"
  }
}
```

위의 예시에서는 `npm run start` 명령어로 `app.js` 파일을 실행하고, `npm run test` 명령어로 `jest`를 실행할 수 있습니다.

## 개발 의존성 관리

개발 환경에서만 필요한 종속성은 `--save-dev` 옵션을 사용하여 `devDependencies`에 추가할 수 있습니다.

```shell
npm install jest --save-dev
```

이렇게 하면 `jest`가 `devDependencies`에 추가되며, 배포 과정에서는 해당 종속성이 설치되지 않습니다.

## 프로젝트 배포

프로젝트를 배포할 때는 종속성을 함께 포함하여 설치할 필요가 있습니다. 이를 위해 `package.json` 파일과 함께 `package-lock.json` 파일을 사용할 수 있습니다. `package-lock.json` 파일은 정확한 종속성 버전을 관리하여, 다른 환경에서 프로젝트를 실행할 때 일관된 결과를 얻을 수 있습니다.

```shell
npm install --production
```

위의 명령어를 실행하면 프로덕션 환경에서 필요한 종속성만 설치됩니다.

## 결론

npm을 이용하여 프로젝트를 관리하는 방법에 대해 알아보았습니다. npm을 통해 프로젝트의 종속성을 손쉽게 관리하고, 스크립트를 실행하며, 개발 및 배포 환경을 설정할 수 있습니다. 이러한 기능들을 통해 프로젝트의 개발 및 유지보수를 효율적으로 진행할 수 있습니다.

---

#npm #프로젝트관리