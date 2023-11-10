---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 코드 난독화 설정하기"
description: " "
date: 2023-11-06
tags: [Package]
comments: true
share: true
---

JavaScript 프로젝트를 개발하다 보면, 코드를 난독화하여 보안을 강화하고 소스코드를 보호하는 것이 중요해집니다. 코드 난독화는 해커들이 소스코드를 이해하거나 수정하기 어렵게 만들어줍니다. 이번에는 package.json 파일을 사용하여 JavaScript 프로젝트의 코드 난독화를 설정하는 방법에 대해 알아보겠습니다.

## package.json 설정

1. 프로젝트의 루트 디렉토리에서 package.json 파일을 엽니다.

2. "scripts" 항목을 찾습니다. 이 항목은 프로젝트의 커맨드를 정의하는 부분입니다.

3. "scripts" 항목 아래에 "build"가라는 새로운 스크립트를 추가합니다. 이 스크립트는 코드 난독화를 진행할 때 사용됩니다.

   ```json
   "scripts": {
     "build": "uglifyjs src/*.js -o dist/bundle.min.js"
   }
   ```

   위의 예시는 `uglifyjs` 라이브러리를 사용하여 `src` 디렉토리에 있는 모든 JavaScript 파일을 난독화한 후 `dist/bundle.min.js` 파일로 저장하는 스크립트입니다. 

4. 추가한 스크립트를 실행하기 위해 터미널에서 아래의 커맨드를 입력합니다.

   ```
   npm run build
   ```

   위의 커맨드를 실행하면 코드 난독화가 진행되어 최종 결과물이 `dist/bundle.min.js` 파일로 생성됩니다.

## 참고 자료

- [UglifyJS 공식 문서](https://github.com/mishoo/UglifyJS)
- [JavaScript 코드 난독화에 대한 더 많은 정보](https://codeburst.io/javascript-obfuscation-explained-518409cb1608)

#javascript #코드난독화