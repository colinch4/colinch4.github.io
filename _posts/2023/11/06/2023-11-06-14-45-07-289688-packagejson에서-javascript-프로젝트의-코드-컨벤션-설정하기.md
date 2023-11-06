---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 코드 컨벤션 설정하기"
description: " "
date: 2023-11-06
tags: [markdown, javascript]
comments: true
share: true
---

JavaScript 프로젝트에서 코드 컨벤션은 코드의 가독성, 일관성, 유지 보수성을 향상시키기 위해 매우 중요합니다. 코드 컨벤션을 설정하는 가장 일반적인 방법은 `package.json` 파일에 관련 설정을 추가하는 것입니다. 이를 통해 프로젝트의 모든 개발자가 일관된 컨벤션을 따르고 코드 품질을 유지할 수 있습니다. 

## 코드 컨벤션 설정을 위한 패키지 설치

코드 컨벤션을 설정하기 위해 `eslint` 패키지를 사용할 것입니다. `eslint`는 JavaScript 코드의 문제를 식별하고 보고하는 데 도움을 주는 도구입니다.

먼저, 프로젝트의 루트 디렉토리에서 아래 명령을 실행하여 `eslint` 패키지를 설치합니다.

```bash
npm install eslint --save-dev
```

## .eslintrc.json 파일 생성

다음으로, 프로젝트의 루트 디렉토리에 `.eslintrc.json` 파일을 생성합니다. 이 파일은 `eslint`에서 사용할 설정을 정의하는 역할을 합니다.

```json
{
  "extends": "eslint:recommended",
  "rules": {
    // 코드 컨벤션 규칙을 설정합니다
  }
}
```

위의 예시는 `eslint`에서 기본적으로 제공하는 권장 설정을 사용한다는 의미입니다.

## 코드 컨벤션 규칙 설정

`rules` 객체를 사용하여 코드 컨벤션 규칙을 설정할 수 있습니다. 아래는 몇 가지 일반적인 예시입니다:

- `"indent"`: 코드의 들여쓰기 수준을 지정합니다. 예를 들어, `"indent": ["error", 2]`는 2칸의 들여쓰기를 지정합니다.
- `"semi"`: 세미콜론 사용 여부를 지정합니다. 예를 들어, `"semi": ["error", "always"]`는 세미콜론을 항상 사용해야 함을 의미합니다.
- `"quotes"`: 따옴표 사용 여부를 지정합니다. 예를 들어, `"quotes": ["error", "single"]`는 작은 따옴표를 사용해야 함을 의미합니다.

여러분은 프로젝트에 맞게 필요한 규칙을 설정할 수 있습니다. 자세한 규칙은 [ESLint 공식 문서](https://eslint.org/docs/rules/)를 참조하십시오.

## npm 스크립트에서 코드 검사 실행

마지막으로, `package.json`의 `scripts` 섹션에 코드 검사를 실행하는 npm 스크립트를 추가해야 합니다.

```json
{
  "scripts": {
    "lint": "eslint ."
  }
}
```

위의 예시는 `npm run lint` 명령을 실행하면 현재 디렉토리에서 코드 검사가 수행된다는 의미입니다.

## 코드 컨벤션 검사하기

이제 프로젝트의 루트 디렉토리에서 다음 명령을 실행하면 코드 컨벤션 검사가 수행됩니다.

```bash
npm run lint
```

`eslint`는 설정한 규칙에 어긋나는 코드를 식별하고 해당 파일과 줄 번호를 보고합니다. 이를 통해 개발자는 코드 컨벤션을 준수하도록 개선할 수 있습니다.

## 결론

해당 프로젝트의 코드 컨벤션을 설정하고 유지하는 것은 코드의 가독성과 유지 보수성을 향상시키는 데 중요합니다. `package.json` 파일을 사용하여 `eslint`를 설정하고 npm 스크립트로 코드 검사를 자동화할 수 있으며, 이를 통해 일관된 코드 컨벤션을 유지할 수 있습니다.

[#markdown](https://en.wikipedia.org/wiki/Markdown) [#javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)