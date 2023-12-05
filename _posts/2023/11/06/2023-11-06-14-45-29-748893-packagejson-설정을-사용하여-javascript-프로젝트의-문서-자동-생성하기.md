---
layout: post
title: "Package.json 설정을 사용하여 JavaScript 프로젝트의 문서 자동 생성하기"
description: " "
date: 2023-11-06
tags: [package]
comments: true
share: true
---

많은 JavaScript 프로젝트에서 문서 작성은 매우 중요한 작업입니다. 문서는 프로젝트의 기능, API 및 사용법을 명확하게 설명하고 개발자들 사이의 협업을 용이하게 합니다. 이번 포스트에서는 Package.json 설정을 사용하여 JavaScript 프로젝트의 문서를 자동으로 생성하는 방법을 다루겠습니다.

## 1. JSDoc을 사용하여 주석 작성하기

JSDoc은 JavaScript 코드에 주석을 작성하여 문서를 생성하는 도구입니다. 주석은 특정 부분이나 함수, 클래스, 메소드 등의 기능에 대한 설명을 포함합니다. JSDoc 주석을 작성할 때는 `/** */`와 같은 형태로 작성하고 문서화할 대상 코드 윗줄에 위치시켜야 합니다.

예를 들어, 다음은 JSDoc 주석을 사용하여 함수의 설명을 작성한 예시입니다.

```javascript
/**
 * 두 수를 더하는 함수
 * @param {number} a 첫 번째 숫자
 * @param {number} b 두 번째 숫자
 * @returns {number} a와 b의 합
 */
function add(a, b) {
  return a + b;
}
```

## 2. Prettier와 ESLint를 설정하기

Prettier와 ESLint는 코드 스타일을 통일시키고 오류를 찾아주는 도구입니다. 이 두 도구를 사용하면 일관된 코드 스타일을 적용하고 잠재적인 오류를 사전에 방지할 수 있습니다. Prettier와 ESLint의 설정 파일인 `.prettierrc`와 `.eslintrc`를 프로젝트 디렉토리에 추가하고 원하는 규칙을 설정합니다.

## 3. Documentation.js 설정하기

Documentation.js는 JSDoc 주석을 기반으로 문서를 생성하는 도구입니다. 먼저 `documentation` 패키지를 프로젝트에 설치합니다.

```bash
npm install --save-dev documentation
```

그런 다음, `package.json` 파일에 다음과 같은 스크립트를 추가합니다.

```json
"scripts": {
  "docs": "documentation build --format md --output docs ./src"
}
```

위 스크립트를 실행하면 `src` 디렉토리의 코드를 기반으로 Markdown 형식의 문서가 `docs` 디렉토리에 생성됩니다.

## 4. 문서 빌드하기

마지막으로, 다음과 같은 명령어를 사용하여 문서를 빌드합니다.

```bash
npm run docs
```

위 명령어를 실행하면 `docs` 디렉토리에 Markdown 형식의 문서가 생성됩니다. 이제 생성된 문서를 읽고 수정하고 필요한 경우에 프로젝트와 함께 배포할 수 있습니다.

## 결론

Package.json 설정과 JSDoc 주석, Prettier 및 ESLint를 활용하여 JavaScript 프로젝트의 문서를 자동으로 생성하는 방법에 대해 알아보았습니다. 이를 통해 프로젝트의 문서화 작업을 효율적으로 수행할 수 있고, 개발자들 간의 협업과 코드 품질을 향상시킬 수 있습니다.

## 참고 자료
- [JSDoc 공식 문서](https://jsdoc.app/)
- [Prettier 공식 문서](https://prettier.io/docs/en/index.html)
- [ESLint 공식 문서](https://eslint.org/docs/user-guide/getting-started)
- [Documentation.js GitHub 페이지](https://github.com/documentationjs/documentation)