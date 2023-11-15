---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 커버리지 보고서 설정하기"
description: " "
date: 2023-11-06
tags: [javascript]
comments: true
share: true
---

커버리지 보고서는 JavaScript 프로젝트에서 코드의 테스트 커버리지를 확인하는 데 도움이 되는 유용한 도구입니다. 이 문서에서는 `package.json` 파일을 사용하여 JavaScript 프로젝트에서 커버리지 보고서를 설정하는 방법을 알아보겠습니다.

## package.json 파일에 커버리지 보고서 설정하기

1. `package.json` 파일을 엽니다.
2. `"scripts"` 항목을 찾습니다.
3. `"scripts"` 항목 내에 `"test"` 스크립트가 있는 경우, 해당 스크립트를 `"npm test -- --coverage"`로 변경합니다. 이렇게 설정하면 테스트 시 자동으로 커버리지 보고서가 생성됩니다. 예를 들면 다음과 같이 변경될 수 있습니다:

   ```json
   "scripts": {
     "test": "npm test -- --coverage"
   }
   ```

4. 만약 `"scripts"` 항목 내에 `"test"` 스크립트가 존재하지 않는다면, `"scripts"` 항목 하단에 `"test": "npm test -- --coverage"`를 추가합니다. 예를 들면 다음과 같이 추가할 수 있습니다:

   ```json
   "scripts": {
     // 기존 스크립트들 ...

     "test": "npm test -- --coverage"
   }
   ```

5. `package.json` 파일을 저장합니다.

## 커버리지 보고서 사용하기

이제 커버리지 보고서를 생성하려면 다음 명령어를 터미널에서 실행하면 됩니다:

```bash
npm test
```

위 명령어를 실행하면 테스트 스크립트가 실행되며, 테스트 결과와 함께 커버리지 보고서가 생성됩니다. 일반적으로 커버리지 보고서는 `coverage`라는 디렉토리(프로젝트 루트 경로에 자동 생성됨)에 생성됩니다. 해당 디렉토리 안에는 HTML 형식의 커버리지 보고서 파일들이 포함되어 있습니다.

커버리지 보고서 파일을 웹 브라우저로 열어서 테스트 커버리지 정보를 확인할 수 있습니다.

## 결론

`package.json` 파일을 사용하여 JavaScript 프로젝트에서 커버리지 보고서를 설정하는 방법을 알아보았습니다. 이제 테스트 수행 시 자동으로 커버리지 보고서를 생성하여 테스트 커버리지를 확인할 수 있습니다.

**참고 자료:** 
- [Jest - Generating Coverage Reports](https://jestjs.io/docs/configuration#collectcoverage-boolean)
- [Istanbul - Code Coverage](https://istanbul.js.org/)