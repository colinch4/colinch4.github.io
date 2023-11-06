---
layout: post
title: "Package.json을 활용하여 JavaScript 프로젝트의 API 문서화하기"
description: " "
date: 2023-11-06
tags: [javascript]
comments: true
share: true
---

JavaScript 프로젝트에서는 API 문서화가 매우 중요합니다. 이를 통해 개발자들은 프로젝트의 기능 및 사용법을 이해하고, 해당 API를 활용할 수 있습니다. 이번 포스트에서는 Package.json 파일을 활용하여 JavaScript 프로젝트의 API를 문서화하는 방법을 알아보겠습니다.

## 1. JSDoc 주석 사용하기

JSDoc은 JavaScript의 주석을 활용하여 API 문서를 작성하는 도구입니다. JSDoc 주석을 사용하면 코드에 포함된 함수, 클래스, 변수 등의 설명과 예시를 제공할 수 있습니다. JSDoc 주석을 활용하여 API 문서를 작성하고, 이를 Package.json 파일에 등록하는 방법을 소개하겠습니다.

```javascript
/**
 * @function greet
 * @description 인사말을 출력하는 함수입니다.
 * 
 * @param {string} name - 인사할 대상의 이름
 * @returns {string} - 인사말을 반환합니다.
 */
function greet(name) {
  return "Hello, " + name + "!";
}
```

위의 예시에서 볼 수 있듯이, 주석의 첫 줄에는 `@function` 태그를 사용하여 함수를 선언하고, `@description` 태그를 사용하여 함수의 설명을 작성합니다. `@param` 태그를 사용하여 함수의 매개변수를 설명하고, `@returns` 태그를 사용하여 반환 값의 설명을 작성합니다.

## 2. Package.json에 API 문서 등록하기

Package.json 파일은 JavaScript 프로젝트의 메타데이터를 저장하는 파일입니다. API 문서를 등록하기 위해서는 이 파일에 적절한 필드를 추가해야 합니다. 보통 `"scripts"` 필드에 문서화 관련 스크립트를 추가하는 것이 일반적입니다.

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "scripts": {
    "docs": "jsdoc -c jsdoc-config.json"
  },
  "devDependencies": {
    "jsdoc": "^3.6.7"
  }
}
```

위의 예시에서 `"scripts"` 필드에 `"docs"` 스크립트를 추가하였습니다. 이 스크립트는 `jsdoc` 명령어를 실행하여 `jsdoc-config.json` 파일을 참조하여 API 문서를 생성합니다. 따라서, 해당 프로젝트의 루트 디렉토리에 `jsdoc-config.json` 파일을 작성해야 합니다.

```json
{
  "source": {
    "include": ["src"],
    "exclude": ["node_modules"]
  },
  "opts": {
    "destination": "docs"
  }
}
```

위의 예시에서 `"source"` 필드를 통해 문서화할 소스 코드의 경로를 설정하고, `"opts"` 필드를 통해 문서가 생성될 경로를 설정합니다. `"destination"` 필드의 값인 `"docs"`는 문서가 `docs` 디렉토리에 생성되도록 설정한 것입니다.

## 3. API 문서 생성하기

Package.json 파일에 `"docs"` 스크립트를 등록하고, jsdoc-config.json 파일을 작성한 후 다음과 같은 명령어를 실행하여 API 문서를 생성할 수 있습니다.

```bash
npm run docs
```

위의 명령어를 실행하면 스크립트에 등록한 `jsdoc` 명령어가 실행되어 API 문서가 생성됩니다. 생성된 문서는 `"opts"` 필드에 설정한 경로에 저장되며, 해당 경로의 `index.html` 파일을 열어 API 문서를 확인할 수 있습니다.

## 마무리

이번 포스트에서는 Package.json 파일을 활용하여 JavaScript 프로젝트의 API를 문서화하는 방법을 알아보았습니다. JSDoc 주석을 사용하여 API 문서를 작성하고, Package.json 파일에 문서화 관련 스크립트를 추가하여 문서를 생성하는 방법을 소개했습니다. API 문서화는 개발 팀 내에서의 협업과 코드의 가독성을 높이는 데 매우 중요한 역할을 합니다. 따라서, 프로젝트를 시작할 때부터 API를 문서화하는 습관을 가지는 것이 좋습니다.

더 자세한 정보는 [JSDoc 공식 문서](https://jsdoc.app/)를 참고하시기 바랍니다.

\#javascript #api-docs