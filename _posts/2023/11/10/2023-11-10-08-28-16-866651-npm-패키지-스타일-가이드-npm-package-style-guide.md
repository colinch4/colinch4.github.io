---
layout: post
title: "npm 패키지 스타일 가이드 (npm package style guide)"
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

npm은 JavaScript 패키지 관리 도구로서, 패키지를 만들고 공유할 수 있는 플랫폼입니다. 이번 블로그 포스트에서는 npm 패키지를 작성할 때 지켜야 할 스타일 가이드에 대해 알아보겠습니다.

## 1. 패키지 이름

- 패키지 이름은 소문자로 작성하며, 중간에 하이픈(-)을 사용하여 단어를 구분합니다.
- 유니크한 이름을 선택하고, 다른 패키지와 충돌하지 않도록 주의해야 합니다.

```json
{
  "name": "my-first-package"
}
```

## 2. 버전 관리

- 패키지 버전은 [Semantic Versioning](https://semver.org/lang/ko/) 기준에 따라 작성하며, `major.minor.patch` 형식으로 표기합니다.
- 패키지의 변경사항에 따라 버전을 업데이트하고, 공개 버전의 버전 히스토리를 잘 관리해야 합니다.

```json
{
  "version": "1.0.0"
}
```

## 3. 의존성 관리

- `dependencies`와 `devDependencies` 필드를 사용하여 패키지의 종속성 관리를 합니다.
- `dependencies`는 프로덕션 버전에서 필요한 패키지를, `devDependencies`는 개발 시에 필요한 패키지를 설치합니다.

```json
{
  "dependencies": {
    "react": "^17.0.2"
  },
  "devDependencies": {
    "babel": "^7.13.16"
  }
}
```

## 4. 코드 스타일

- 코드 스타일은 일관성 있는 형태로 작성되어야 합니다. 대부분의 패키지는 프로젝트가 사용하는 코드 스타일과 일치하도록 구성됩니다.
- 코드 포맷터 도구를 사용하여 코드를 자동으로 포맷팅하고, linter를 통해 코드 스타일 가이드를 준수하는지 확인합니다.

```bash
npm install prettier eslint --save-dev
```

```json
{
  "scripts": {
    "format": "prettier --write .",
    "lint": "eslint ."
  }
}
```

## 5. 배포

- 패키지를 배포하기 전에, 패키지의 파일만 포함된 NPM 패키지를 빌드해야 합니다.
- `main` 필드에는 패키지 진입점 파일을 지정하고, `files` 필드에는 포함되어야 할 파일을 명시합니다.

```json
{
  "main": "dist/index.js",
  "files": ["dist"]
}
```

## 6. 문서화

- 패키지를 사용하는 다른 개발자들에게 패키지의 사용 방법을 설명하는 문서를 작성해야 합니다.
- README 파일에는 패키지의 설치, 사용법 및 간단한 예제 코드를 포함시키는 것이 좋습니다.

## 7. 테스트

- 패키지의 안정성과 품질을 검증하기 위해 테스트 코드를 작성하는 것이 중요합니다.
- Jest, Mocha, Jasmine 등의 테스트 프레임워크를 사용하여 단위 테스트와 통합 테스트를 수행할 수 있습니다.

```bash
npm install jest --save-dev
```

```json
{
  "scripts": {
    "test": "jest"
  }
}
```

위의 스타일 가이드를 따르면, npm 패키지를 개발하고 관리하는 일이 더욱 효율적이고 견고해질 것입니다. 새로운 패키지를 만들 때, 이러한 스타일 가이드를 기반으로 시작해 보세요!

#npm #패키지 #스타일가이드