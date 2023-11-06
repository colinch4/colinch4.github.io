---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 로깅 설정하기"
description: " "
date: 2023-11-06
tags: [default]
comments: true
share: true
---

JavaScript 프로젝트에서 로깅은 애플리케이션의 동작을 모니터링하고 디버깅하는 데에 중요한 요소입니다. Package.json 파일을 사용하여 JavaScript 프로젝트의 로깅 설정을 구성할 수 있습니다. 이 블로그 포스트에서는 Package.json 파일을 사용하여 프로젝트에서 로깅을 활성화하고 로깅 레벨을 설정하는 방법에 대해 알아보겠습니다.

## Package.json 파일 수정하기

1. 프로젝트의 루트 디렉토리에서 `package.json` 파일을 엽니다.
2. `"scripts"` 항목에 `"start"` 또는 원하는 스크립트 명령어를 찾습니다. 예를 들어, `"start"` 스크립트를 찾는다고 가정합니다.
3. `"start"` 스크립트 명령어에 `NODE_ENV` 환경 변수를 설정합니다. 예를 들어, 다음과 같이 `"start"` 명령어를 수정할 수 있습니다:

   ```json
   "scripts": {
     "start": "NODE_ENV=production node app.js"
   }
   ```

   이 예제에서는 `NODE_ENV` 환경 변수를 `"production"`으로 설정하고 `app.js` 파일을 실행하는 명령어를 사용합니다.

4. 로깅 라이브러리를 사용하는 경우, 해당 라이브러리의 설정을 추가합니다. 로깅 라이브러리마다 다른 설정 방법이 있을 수 있으므로 라이브러리의 공식 문서를 참고하세요. 일반적으로 라이브러리의 설정은 `logging` 또는 `logger` 섹션에 추가됩니다. 예를 들어, `winston` 로깅 라이브러리를 사용한다고 가정하고 다음과 같이 설정을 추가할 수 있습니다:

   ```json
   "logging": {
     "level": "debug"
   }
   ```

   위의 예제에서는 로깅 레벨을 `"debug"`로 설정합니다.

## 참고 자료

- [npm 공식 문서](https://docs.npmjs.com/cli/v7/using-npm/scripts#default-values)
- [winston 공식 문서](https://github.com/winstonjs/winston)

로깅은 애플리케이션의 에러 추적, 성능 모니터링, 사용자 활동 추적 등 다양한 목적으로 사용될 수 있습니다. JavaScript 프로젝트에서 로깅을 설정하고 활용하는 것은 개발과 유지 보수 과정에서 매우 유용합니다. Package.json 파일을 이용하여 손쉽게 로깅 설정을 구성해보세요!