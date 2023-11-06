---
layout: post
title: "Package.json 파일을 사용하여 JavaScript 프로젝트 설정하기"
description: " "
date: 2023-11-06
tags: []
comments: true
share: true
---

자바스크립트 프로젝트를 시작하면 해당 프로젝트의 설정과 의존성 관리를 위해 Package.json 파일을 사용하는 것이 일반적입니다. Package.json 파일은 프로젝트의 메타데이터와 의존성 패키지의 버전 정보를 포함하고 있어 프로젝트를 관리하기 용이합니다.

## Package.json 파일 생성하기

1. 프로젝트 루트 디렉토리에서 터미널을 열고 다음 명령을 실행하여 Package.json 파일을 생성합니다:

   ```shell
   npm init
   ```

   이 명령을 실행하면 프로젝트에 대한 몇 가지 정보를 입력하라는 프롬프트가 나타납니다.

2. 프롬프트에 따라 프로젝트의 이름, 버전, 설명 등의 정보를 입력합니다.

3. 응답한 정보로 Package.json 파일이 생성됩니다.

## 의존성 관리하기

프로젝트에 필요한 외부 라이브러리나 모듈의 의존성을 관리하기 위해 Package.json 파일을 사용할 수 있습니다. 프로젝트에서 사용하는 각각의 의존성 패키지는 Package.json 파일에 추가되어야 합니다.

1. 프로젝트에 사용할 외부 패키지를 설치합니다. 예를 들어, lodash 패키지를 설치하려면 다음 명령을 실행합니다:

   ```shell
   npm install lodash
   ```

2. 의존성 패키지가 설치되면, `--save` 플래그를 사용하여 해당 패키지를 Package.json 파일에 추가합니다:

   ```shell
   npm install lodash --save
   ```

   이렇게 하면 Package.json 파일의 `dependencies` 필드에 lodash 패키지와 해당 버전 정보가 추가됩니다.

3. 만약 개발환경에서만 필요한 패키지라면, `--save-dev` 플래그를 사용하여 해당 패키지를 개발 의존성으로 추가할 수 있습니다:

   ```shell
   npm install eslint --save-dev
   ```

   이렇게 하면 Package.json 파일의 `devDependencies` 필드에 eslint 패키지와 해당 버전 정보가 추가됩니다.

## 스크립트 실행하기

Package.json 파일을 사용하여 프로젝트의 스크립트를 실행할 수도 있습니다. 스크립트는 프로젝트의 특정 작업이나 명령을 실행하기 위해 사용됩니다. 예를 들어, 프로젝트를 시작하는 스크립트를 작성해보겠습니다.

1. Package.json 파일에서 `scripts` 필드를 찾습니다.

2. `scripts` 필드에 `"start"`라는 이름의 스크립트를 추가합니다:

   ```json
   "scripts": {
     "start": "node index.js"
   }
   ```

   이 예제에서는 `start` 스크립트를 실행하면 `index.js` 파일이 실행됩니다.

3. 이제 터미널에서 다음 명령을 실행하여 `start` 스크립트를 실행할 수 있습니다:

   ```shell
   npm start
   ```

## 결론

Package.json 파일은 JavaScript 프로젝트의 설정과 의존성 관리를 위해 중요한 역할을 합니다. 이 파일을 사용하여 프로젝트의 메타데이터, 의존성 패키지 정보, 스크립트 등을 관리할 수 있습니다. 이를 통해 프로젝트의 효율성을 개선하고 필요한 작업을 자동화할 수 있습니다.

참고:
- [npm 공식 문서](https://docs.npmjs.com/cli/v7/configuring-npm/package-json)