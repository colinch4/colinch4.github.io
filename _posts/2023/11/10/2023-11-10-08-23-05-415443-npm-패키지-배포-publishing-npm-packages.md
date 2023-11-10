---
layout: post
title: "npm 패키지 배포 (Publishing npm packages)"
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

![npm](https://cdn.pixabay.com/photo/2015/04/23/17/41/node-js-736399_960_720.png)

npm은 자바스크립트 패키지 관리자로, 개발자들이 패키지를 생성하고 공유하고 재사용할 수 있게 해줍니다. 이번 포스트에서는 npm 패키지를 배포하는 방법에 대해 알아보겠습니다.

## 1. 패키지 생성

가장 먼저, npm 패키지를 배포하기 위해서는 해당 패키지를 생성해야 합니다. 이를 위해 다음의 단계를 따라가세요:

1. 프로젝트 디렉토리에서 `npm init` 명령어를 실행합니다.
2. 패키지에 대한 정보(이름, 버전, description 등)를 제공합니다.
3. `package.json` 파일이 생성되며, 해당 파일에는 패키지 정보가 포함됩니다.

## 2. 패키지 빌드

npm 패키지를 배포하기 전에, 필요한 빌드 작업을 수행해야 합니다. 예를 들어, TypeScript 코드를 JavaScript로 변환하거나, Sass 파일을 CSS로 컴파일하는 작업 등이 있을 수 있습니다.

일반적으로 빌드 작업은 `package.json` 파일의 `scripts` 섹션에 정의됩니다. 예를 들어, `build` 스크립트를 정의하고 다음과 같이 실행하면 됩니다:

```shell
npm run build
```

## 3. npm 계정 생성

npm 패키지를 배포하려면 npm 계정이 필요합니다. npmjs.com 웹사이트에서 계정을 생성할 수 있습니다. 계정을 생성한 후, npm CLI를 사용하여 로그인해야 합니다:

```shell
npm login
```

## 4. 패키지 배포

npm 패키지를 배포하는 가장 간단한 방법은 `npm publish` 명령어를 사용하는 것입니다. 다음 명령어를 실행하면, 현재 디렉토리의 패키지가 배포됩니다:

```shell
npm publish
```

## 5. 패키지 업데이트

npm 패키지를 업데이트하려면, 새로운 버전을 `package.json` 파일의 `version` 필드에 지정하고, 빌드 작업을 다시 수행한 다음, `npm publish` 명령어를 실행합니다.

이렇게 함으로써, 개발자들은 업데이트한 버전의 패키지를 사용할 수 있게 됩니다.

## 6. 패키지 삭제

만약 패키지를 더 이상 유지하고 싶지 않다면, 해당 패키지를 npm 레지스트리에서 삭제할 수 있습니다. 이를 위해 `npm unpublish` 명령어를 사용하며, 다음과 같이 실행합니다:

```shell
npm unpublish <package-name> --force
```

참고로, 24시간 이내에 배포한 패키지만 삭제할 수 있습니다.

## 요약

이 포스트에서는 npm 패키지를 배포하는 단계들에 대해 간단히 알아보았습니다. 패키지 생성, 빌드, 배포, 업데이트, 삭제 등의 작업을 통해, 개발자들은 자신의 패키지를 손쉽게 공유하고 유지할 수 있습니다.

[#npm](https://www.npmjs.com/) [#패키지배포](https://www.npmjs.com/package/npm-publish)