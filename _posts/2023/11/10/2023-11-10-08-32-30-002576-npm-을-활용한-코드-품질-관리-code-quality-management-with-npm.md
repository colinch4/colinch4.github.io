---
layout: post
title: "npm 을 활용한 코드 품질 관리 (Code quality management with npm)"
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

코드 품질은 소프트웨어 개발에서 매우 중요한 요소입니다. 품질이 낮은 코드는 유지보수가 어렵고 버그를 발생시키기 쉽습니다. 이러한 이유로 많은 개발자들은 코드 품질 관리에 신경을 쓰고 있습니다. 

이번 글에서는 npm을 사용하여 코드 품질을 관리하는 방법에 대해 알아보겠습니다.

## 1. ESLint를 사용한 코드 스타일 검사
ESLint는 자바스크립트 코드의 스타일과 품질을 검사할 수 있는 도구입니다. 프로젝트의 루트 디렉토리에서 `npm install eslint --save-dev` 명령어를 사용하여 ESLint를 설치할 수 있습니다. 설치가 완료된 후 `.eslintrc.json` 파일을 생성하여 ESLint의 설정을 추가할 수 있습니다. ESLint를 실행하면 코드 스타일 관련 문제를 식별할 수 있으며, 이를 해결하여 코드 품질을 높일 수 있습니다.

## 2. Prettier를 사용한 코드 포맷팅
Prettier는 코드의 포맷팅을 자동으로 처리해주는 도구입니다. Prettier를 사용하면 개발자는 코드 포맷팅에 신경쓰지 않고 개발에 집중할 수 있습니다. 프로젝트의 루트 디렉토리에서 `npm install prettier --save-dev` 명령어를 사용하여 Prettier를 설치할 수 있습니다. 또한 `.prettierrc.json` 파일을 생성하여 Prettier의 설정을 추가할 수 있습니다.

## 3. Husky와 lint-staged를 사용한 pre-commit 훅 설정
Husky와 lint-staged는 Git 커밋 이전에 코드 검사 작업을 수행하는 도구입니다. Husky와 lint-staged를 사용하면 커밋을 수행하기 전에 자동으로 코드 스타일 검사와 포맷팅을 진행할 수 있습니다.

먼저, `npm install husky lint-staged --save-dev` 명령어를 사용하여 Husky와 lint-staged를 설치합니다. 그런 다음 `package.json` 파일에 아래와 같은 스크립트를 추가합니다.

```json
"husky": {
  "hooks": {
    "pre-commit": "lint-staged"
  }
},
"lint-staged": {
  "src/**/*.{js,jsx}": [
    "eslint --fix",
    "prettier --write"
  ]
}
```

이제 코드를 수정하고 커밋을 하면 Husky와 lint-staged가 자동으로 코드 스타일 검사와 포맷팅을 수행합니다.

## 결론
npm을 활용하여 코드 품질을 관리하는 방법에 대해 알아보았습니다. ESLint와 Prettier를 사용하여 코드 스타일을 유지하고, Husky와 lint-staged를 사용하여 pre-commit 훅을 설정하여 코드 품질을 높일 수 있습니다. 이러한 도구들을 적절하게 활용하면 더 나은 코드를 작성할 수 있고, 유지보수가 용이해질 것입니다.

[#npm](https://www.npmjs.com/) [#코드품질관리](https://ko.wikipedia.org/wiki/%EC%BD%94%EB%93%9C_%ED%92%88%EC%A7%88_%EA%B4%80%EB%A6%AC)