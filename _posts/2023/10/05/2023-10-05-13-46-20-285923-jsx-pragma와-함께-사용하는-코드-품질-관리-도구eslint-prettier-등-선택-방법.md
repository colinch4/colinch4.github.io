---
layout: post
title: "JSX pragma와 함께 사용하는 코드 품질 관리 도구(ESLint, Prettier 등) 선택 방법"
description: " "
date: 2023-10-05
tags: []
comments: true
share: true
---

코드 품질 관리 도구는 모던 웹 개발에서 매우 중요합니다. 특히 JSX(JavaScript XML)와 같은 비동기 UI 라이브러리를 사용하는 프로젝트에서는 코드의 일관성과 가독성을 유지하기 위해 이러한 도구들이 필수적입니다. JSX pragma와 함께 사용할 수 있는 두 가지 인기있는 코드 품질 관리 도구인 ESLint와 Prettier에 대해 알아보겠습니다.

### 1. ESLint

ESLint는 JavaScript 코드에서 잠재적인 문제를 식별하고 관리할 수 있는 지능형 정적 분석 도구입니다. JSX pragma와 함께 사용하기 위해 다음 단계를 따를 수 있습니다.

1. 프로젝트 루트 디렉토리에서 `eslint`를 설치합니다.
   ```sh
   npm install eslint --save-dev
   ```

2. `.eslintrc` 파일을 생성하고 다음과 같은 최소한의 구성을 추가합니다.
   ```json
   {
     "parser": "@babel/eslint-parser",
     "extends": [
       "eslint:recommended",
       "plugin:react/recommended"
     ]
   }
   ```

3. `@babel/eslint-parser`를 설치하여 JSX를 지원하도록 설정합니다.
   ```sh
   npm install @babel/eslint-parser --save-dev
   ```

4. 필요한 경우 추가적인 규칙이나 구성을 `.eslintrc` 파일에 추가합니다.

5. 개발 환경에 맞는 플러그인을 설치하여 코드 스타일을 지정할 수 있습니다. 예를 들어, Airbnb 스타일 가이드를 사용하기 위해 다음과 같이 설치합니다.
   ```sh
   npm install eslint-config-airbnb --save-dev
   ```

6. 개발 환경에 맞게 ESLint를 구성합니다. 예를 들어, 프로젝트의 빌드 스크립트에 다음을 추가하여 빌드 시 ESLint를 실행할 수 있습니다.
   ```sh
   eslint src
   ```

### 2. Prettier

Prettier는 코드 포맷팅 도구로, 코드를 일관된 스타일로 자동으로 정렬해줍니다. JSX pragma와 함께 사용하기 위해 다음 단계를 따를 수 있습니다.

1. 프로젝트 루트 디렉토리에서 `prettier`를 설치합니다.
   ```sh
   npm install prettier --save-dev
   ```

2. `.prettierrc` 파일을 생성하고 Prettier의 선호하는 스타일 옵션을 추가합니다.
   ```json
   {
     "semi": true,
     "singleQuote": true,
     "jsxSingleQuote": true,
     "trailingComma": "all"
   }
   ```

3. 개발 환경에 맞게 Prettier를 구성합니다. 예를 들어, 프로젝트의 빌드 스크립트에 다음을 추가하여 코드를 자동으로 정렬할 수 있습니다.
   ```sh
   prettier --write "src/**/*.js"
   ```

### 종합적인 선택

ESLint와 Prettier는 각각 다른 목적을 가지고 있습니다. ESLint는 코드 품질을 유지하고 잠재적인 문제를 발견하는 데에 초점을 맞추고, Prettier는 일관된 코드 스타일을 유지하는 데에 중점을 둡니다. JSX pragma를 사용하는 프로젝트에서는 두 도구를 함께 사용하여 최상의 결과를 얻을 수 있습니다.

```sh
#JSX #ESLint #Prettier
```

이렇게 쓸 경우, JSX, ESLint, Prettier와 관련된 내용이 검색 시에 노출될 가능성이 높아집니다.