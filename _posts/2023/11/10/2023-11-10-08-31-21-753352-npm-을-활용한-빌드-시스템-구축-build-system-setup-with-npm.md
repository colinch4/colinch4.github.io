---
layout: post
title: "npm 을 활용한 빌드 시스템 구축 (Build system setup with npm)"
description: " "
date: 2023-11-10
tags: [npm]
comments: true
share: true
---

빌드 시스템은 애플리케이션의 개발, 배포 및 유지 관리를 위해 필수적인 요소입니다. npm을 이용하여 간편하게 빌드 시스템을 구축할 수 있습니다. npm은 JavaScript 패키지 관리자로 널리 사용되며, 편리한 명령어와 도구를 제공하여 프로젝트의 빌드 프로세스를 자동화할 수 있습니다.

## 1. package.json 파일 생성

먼저 프로젝트 루트 디렉토리에 package.json 파일을 생성해야 합니다. 이는 프로젝트의 의존성 패키지를 관리하기 위한 설정 파일입니다. 아래 명령어를 실행하여 package.json 파일을 생성합니다.

```shell
npm init -y
```

## 2. 빌드 스크립트 등록

빌드 작업을 수행하기 위해 package.json 파일에서 "scripts" 속성을 설정해야 합니다. 이 속성에 빌드에 필요한 명령어 및 스크립트를 등록할 수 있습니다.

```json
{
  "scripts": {
    "build": "your-build-command"
  }
}
```

위 예시에서 "build"는 사용자 정의한 빌드 스크립트를 실행하는 명령어입니다. "your-build-command"에는 실제 빌드 작업을 수행하는 명령이나 스크립트를 입력합니다.

## 3. 빌드 실행

빌드 스크립트가 등록되었다면, 아래 명령어를 통해 빌드를 실행할 수 있습니다.

```shell
npm run build
```

npm은 "run" 명령을 통해 package.json 파일 내 등록된 스크립트를 실행할 수 있습니다. 위 명령은 "build" 스크립트를 실행하는 것입니다.

## 4. 추가 설정 및 사용 예제

빌드 시스템을 구축하는 데 있어 추가적인 설정과 사용 예제는 프로젝트의 요구사항과 개발환경에 따라 다를 수 있습니다. 다양한 npm 패키지를 활용하여 개발 툴, 태스크 러너, 번들러 등을 지원받을 수 있습니다.

예를 들어, SCSS를 CSS로 변환하는 작업을 빌드에 포함하고 싶다면, `node-sass` 패키지와 함께 `sass` 명령어를 사용하여 빌드 스크립트를 작성할 수 있습니다.

```json
{
  "scripts": {
    "build": "node-sass styles.scss -o dist/css"
  }
}
```

위 예시는 `styles.scss` 파일을 `dist/css` 디렉토리에 CSS 파일로 변환하는 빌드 스크립트입니다.

## 마무리

npm을 이용하여 빌드 시스템을 구축하면 효율적인 개발 및 배포 프로세스를 구현할 수 있습니다. package.json 파일과 스크립트 설정을 통해 필요한 빌드 작업을 간편하게 실행할 수 있으며, 다양한 npm 패키지를 활용하여 개발 환경에 적합한 빌드 시스템을 구성할 수 있습니다.

**참고자료:**
- [npm 문서](https://docs.npmjs.com/)
- [node-sass 패키지](https://www.npmjs.com/package/node-sass)

#빌드시스템 #npm