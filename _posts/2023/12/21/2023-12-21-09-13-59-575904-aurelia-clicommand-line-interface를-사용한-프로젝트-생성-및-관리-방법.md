---
layout: post
title: "[javascript] Aurelia CLI(Command Line Interface)를 사용한 프로젝트 생성 및 관리 방법"
description: " "
date: 2023-12-21
tags: [javascript]
comments: true
share: true
---

Aurelia는 JavaScript 프레임워크 중 하나로, 효과적인 웹 애플리케이션을 빌드할 수 있는 기능을 제공합니다. 이번 글에서는 Aurelia CLI를 사용하여 프로젝트를 생성하고 관리하는 방법에 대해 알아보겠습니다.

## Contents

1. [Aurelia CLI 설치](#aurelia-cli-설치)
2. [Aurelia 프로젝트 생성](#aurelia-프로젝트-생성)
3. [Aurelia 프로젝트 구조](#aurelia-프로젝트-구조)
4. [모듈 생성 및 관리](#모듈-생성-및-관리)
5. [Aurelia CLI을 활용한 개발 서버 실행](#aurelia-cli을-활용한-개발-서버-실행)

### 1. Aurelia CLI 설치

Aurelia CLI를 설치하려면 npm(Node Package Manager)을 사용하여 다음 명령을 실행합니다.

```sh
npm install aurelia-cli -g
```

### 2. Aurelia 프로젝트 생성

새로운 Aurelia 프로젝트를 생성하려면 터미널에서 다음 명령을 실행합니다.

```sh
au new
```

이후 프로젝트 이름 및 기타 구성 설정을 입력하여 프로젝트를 생성합니다.

### 3. Aurelia 프로젝트 구조

Aurelia CLI는 생성된 프로젝트의 구조를 지원합니다. 주요 파일 및 폴더는 다음과 같습니다.

- `src` : 소스 코드 및 리소스가 포함된 폴더
- `aurelia_project` : Aurelia CLI 프로젝트 관리 도구 설정 폴더
- `package.json` : 프로젝트의 의존성 및 스크립트 정의
- `webpack.config.js` : 웹팩(Webpack) 설정 파일

### 4. 모듈 생성 및 관리

새로운 페이지, 컴포넌트 또는 서비스를 생성하려면 다음 명령을 사용합니다.

```sh
au generate (page|component|service) <name>
```

위 명령에서 `<name>`에는 생성하려는 모듈의 이름을 지정합니다. 생성된 모듈은 `src` 폴더 내에 적절한 위치에 생성됩니다.

### 5. Aurelia CLI을 활용한 개발 서버 실행

Aurelia CLI를 사용하여 내장된 개발 서버를 실행하려면 터미널에서 아래 명령을 실행합니다.

```sh
au run --watch
```

이제 코드 변경 사항이 발생할 때마다 자동으로 빌드되어 브라우저에 즉시 반영됩니다.

이렇게 하여 Aurelia CLI를 사용하여 프로젝트를 생성하고 관리하는 방법을 알아보았습니다. Aurelia CLI를 이용하여 프로젝트를 효율적으로 관리할 수 있게 되었습니다.

#### References

- [Aurelia CLI 공식 문서](https://aurelia.io/docs/cli)
- [Aurelia GitHub 저장소](https://github.com/aurelia/cli)