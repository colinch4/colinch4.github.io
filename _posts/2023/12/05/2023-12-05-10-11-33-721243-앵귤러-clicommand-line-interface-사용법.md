---
layout: post
title: "[javascript] 앵귤러 CLI(Command Line Interface) 사용법"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

앵귤러 CLI는 앵귤러 프로젝트를 쉽게 만들고 관리하는 도구입니다. 이번 블로그 글에서는 앵귤러 CLI의 기본 사용법에 대해 알아보겠습니다.

## 1. 앵귤러 CLI 설치하기
앵귤러 CLI를 사용하기 위해서는 먼저 Node.js와 npm(Node Package Manager)이 설치되어 있어야 합니다. 설치가 완료되었다면 터미널 또는 명령 프롬프트를 열고 다음 명령어를 입력해 앵귤러 CLI를 설치합니다.

```bash
npm install -g @angular/cli
```

## 2. 새로운 앵귤러 프로젝트 생성하기
앵귤러 CLI를 사용하여 새로운 앵귤러 프로젝트를 생성하는 방법은 매우 간단합니다. 터미널 또는 명령 프롬프트에서 다음 명령어를 실행합니다.

```bash
ng new my-project
```

위 명령어를 실행하면 `my-project`라는 이름의 새로운 앵귤러 프로젝트가 생성됩니다.

## 3. 앵귤러 프로젝트 실행하기
앵귤러 프로젝트를 실행하기 위해서는 먼저 프로젝트 폴더로 이동합니다. 그리고 다음 명령어를 실행합니다.

```bash
cd my-project
ng serve
```

위 명령어를 실행하면 앵귤러 개발 서버가 실행되고 앵귤러 프로젝트가 브라우저에 표시됩니다.

## 4. 앵귤러 CLI 명령어 모음
앵귤러 CLI에는 다양한 명령어가 있습니다. 몇 가지 가장 자주 사용되는 명령어를 소개하겠습니다.

- `ng generate component my-component`: 새로운 컴포넌트를 생성합니다.
- `ng generate service my-service`: 새로운 서비스를 생성합니다.
- `ng build`: 앵귤러 프로젝트를 빌드합니다.
- `ng test`: 유닛 테스트를 실행합니다.
- `ng lint`: 코드 스타일을 검사합니다.

앵귤러 CLI 명령어에 대한 자세한 내용은 [앵귤러 공식 문서](https://angular.io/cli)를 참고하시기 바랍니다.

앵귤러 CLI는 앵귤러 개발을 더욱 편리하게 만들어주는 강력한 도구입니다. 위에서 소개한 기본 사용법을 익히고 실제 프로젝트에 적용해 보세요!