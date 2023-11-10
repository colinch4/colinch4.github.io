---
layout: post
title: "npm 의 기능과 사용법 (npm features and usage)"
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

npm은 Node Package Manager의 약어로, JavaScript 개발자들이 패키지를 관리하고 공유할 수 있는 강력한 도구입니다. 이 글에서는 npm의 주요 기능과 사용법을 살펴보겠습니다.

## 1. 패키지 관리

npm을 사용하면 다른 개발자들이 만든 JavaScript 패키지를 쉽게 설치하고 관리할 수 있습니다. 패키지의 종속성 관리와 버전 관리를 편리하게 수행할 수 있으며, `npm install` 명령어를 사용하여 패키지를 설치할 수 있습니다.

예를 들어, `npm install express` 명령어를 실행하면 Express 패키지가 프로젝트에 설치됩니다. 이렇게 설치된 패키지는 `node_modules` 폴더에 저장됩니다.

## 2. 패키지 배포

npm을 사용하여 자신이 개발한 패키지를 공유할 수 있습니다. 패키지를 배포하기 위해서는 [npm 공식 웹사이트](https://www.npmjs.com/)에 회원가입하고, `npm publish` 명령어를 사용합니다.

패키지를 배포하면 다른 개발자들이 `npm install`을 통해 손쉽게 패키지를 설치하여 사용할 수 있습니다.

## 3. 스크립트 실행

npm은 `package.json` 파일 내부의 `scripts` 섹션을 통해 다양한 스크립트를 실행할 수 있는 기능을 제공합니다. 이를 통해 프로젝트를 빌드하거나 실행하는 등의 작업을 자동화할 수 있습니다.

예를 들어, `package.json` 파일에서 `"scripts"` 섹션에 `"start": "node index.js"`를 추가하면 `npm start` 명령어를 통해 `index.js` 파일을 실행할 수 있습니다.

## 4. 버전 관리

npm은 패키지의 버전을 효율적으로 관리할 수 있는 기능을 제공합니다. 패키지의 버전은 [Semantic Versioning](https://semver.org/)을 따르며, `major.minor.patch` 형식으로 표현됩니다.

버전을 효율적으로 관리하면서 패키지의 업데이트를 수행할 수 있으며, `npm update` 명령어를 통해 일괄적으로 패키지를 업데이트할 수 있습니다.

---

이글은 npm의 기능과 사용법에 대해 알아보았습니다. npm은 JavaScript 개발에 필수적인 도구로, 개발 생산성을 높이고 코드 재사용성을 향상시키는데 큰 도움을 줍니다.

긴 주소의 경우: (source: [npm 공식 웹사이트](https://www.npmjs.com/))

#npm #NodePackageManager