---
layout: post
title: "Package.json 설정을 활용한 JavaScript 프로젝트의 리팩토링 지침 설정하기"
description: " "
date: 2023-11-06
tags: [javascript]
comments: true
share: true
---

리팩토링은 코드의 가독성, 유지보수성, 확장성을 향상시키기 위해 코드를 개선하는 작업입니다. JavaScript 프로젝트에서 리팩토링을 진행할 때는 Package.json 파일을 활용하여 리팩토링 지침을 설정할 수 있습니다. 이 글에서는 Package.json 설정을 통해 JavaScript 프로젝트의 리팩토링을 지원하는 방법에 대해 알아보겠습니다.

## 1. ESLint 설정 추가하기

ESLint는 JavaScript 코드의 문제점을 찾아주고, 일관된 코딩 스타일을 유지할 수 있도록 도와주는 도구입니다. Package.json 파일에서 `"eslintConfig"` 속성을 추가하여 ESLint 설정을 지정할 수 있습니다.

```json
{
  "eslintConfig": {
    "extends": "eslint:recommended",
    "rules": {
      "no-unused-vars": "error",
      "no-console": "off"
    }
  }
}
```

위 예시에서는 ESLint의 기본 설정을 활용하고, `"no-unused-vars"`와 `"no-console"` rule을 추가하여 사용하지 않는 변수와 콘솔 사용을 감지하도록 설정하였습니다.

## 2. Prettier 설정 추가하기

Prettier는 코드의 포맷팅을 자동으로 처리해주는 도구입니다. Package.json 파일에서 `"prettier"` 속성을 추가하여 Prettier 설정을 지정할 수 있습니다.

```json
{
  "prettier": {
    "singleQuote": true,
    "trailingComma": "es5"
  }
}
```

위 예시에서는 작은따옴표를 사용하는 `"singleQuote"` 옵션과 ES5에서도 마지막 쉼표를 허용하는 `"trailingComma"` 옵션을 설정하였습니다.

## 3. Husky와 lint-staged 설정 추가하기

Husky와 lint-staged를 함께 사용하면, Git 커밋 전에 코드에 대한 검사를 자동으로 수행할 수 있습니다. Package.json 파일에서 `"husky"`와 `"lint-staged"` 속성을 추가하여 Husky와 lint-staged 설정을 지정할 수 있습니다.

```json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "*.js": [
      "eslint --fix",
      "prettier --write"
    ]
  }
}
```

위 예시에서는 `"pre-commit"` hook을 설정하여 커밋 전에 lint-staged를 실행하도록 하였고, lint-staged에는 JavaScript 파일에 대해 ESLint와 Prettier를 순서대로 실행하도록 설정하였습니다. 이를 통해 Git 커밋 시 코드의 일관성과 품질을 관리할 수 있습니다.

## 4. 참고 자료

- [ESLint 공식 문서](https://eslint.org/docs/user-guide/getting-started)
- [Prettier 공식 문서](https://prettier.io/docs/en/index.html)
- [Husky 공식 문서](https://typicode.github.io/husky/#/)
- [lint-staged 공식 문서](https://github.com/okonet/lint-staged)

위의 설정을 참고하여 JavaScript 프로젝트에서 Package.json을 활용한 리팩토링 지침을 설정해보세요! 

#JavaScript #리팩토링