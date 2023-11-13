---
layout: post
title: "npm 을 활용한 테스트 자동화 (Test automation with npm)"
description: " "
date: 2023-11-10
tags: [npm]
comments: true
share: true
---

테스트 자동화는 개발 프로세스에서 필수적인 단계입니다. 이를 통해 개발자는 코드 변경에 따른 영향을 빠르게 확인하고, 소프트웨어의 품질을 유지할 수 있습니다. 이번 포스트에서는 npm을 활용하여 테스트 자동화를 어떻게 수행할 수 있는지 알아보겠습니다.

## 1. npm 스크립트 (npm scripts)

npm은 패키지 관리 도구로 잘 알려져 있지만, 실제로는 테스트 자동화에도 큰 도움을 줍니다. npm은 `package.json` 파일에서 scripts 섹션을 통해 사용자 정의 스크립트를 실행할 수 있습니다.

```json
{
  "scripts": {
    "test": "mocha tests/*.js",
    "start": "node server.js"
  }
}
```

위의 예시에서 `npm run test` 명령어를 실행하면 `mocha`를 사용하여 `tests` 폴더에 있는 모든 테스트 파일을 실행할 수 있습니다.  이렇게 하면 명령어 한 줄로 테스트를 실행할 수 있으며, 테스트 스크립트를 작성하여 커맨드 라인에서 실행할 수 있습니다.

## 2. 테스트 러너 (Test runners)

테스트 러너는 테스트 스크립트를 실행하여 테스트를 자동화하는 도구입니다. npm을 사용하여 다양한 테스트 러너를 설치하고 사용할 수 있습니다. 여기에서는 가장 인기있는 테스트 러너 중 하나인 `Mocha`를 사용해보겠습니다.

```bash
npm install mocha --save-dev
```

위 명령어를 사용하여 `Mocha`를 설치한 후, `package.json`에서 `test` 스크립트를 수정해봅시다.

```json
{
  "scripts": {
    "test": "mocha"
  }
}
```

이제 `npm run test` 명령어를 실행하면 `Mocha`가 현재 폴더에서 `test`라는 이름의 폴더를 찾아 테스트 파일을 실행합니다.

## 3. 어설션 라이브러리 (Assertion libraries)

테스트 결과를 확인하기 위해 어설션(assertion) 라이브러리를 사용할 수 있습니다. 이 라이브러리를 사용하여 예상된 결과와 실제 결과를 비교하고, 테스트가 성공했는지 여부를 판단할 수 있습니다. `chai`라는 어설션 라이브러리를 설치하여 사용해보겠습니다.

```bash
npm install chai --save-dev
```

설치가 완료되면 테스트 파일에서 `chai`를 사용하여 어설션을 작성할 수 있습니다.

```javascript
const chai = require('chai');
const expect = chai.expect;

describe('Example Test', () => {
  it('should return true', () => {
    expect(true).to.be.true;
  });
});
```

위의 예시에서는 `chai`를 사용하여 예상 결과와 실제 결과를 비교하는 `expect`문을 작성하였습니다.

## 마무리

이렇게하여 `npm`을 활용한 테스트 자동화를 쉽게 수행할 수 있습니다. `npm scripts`를 사용하여 테스트 스크립트를 실행하고, `테스트 러너`와 `어설션 라이브러리`를 조합하여 테스트를 자동화할 수 있습니다.

[#npm](https://www.npmjs.com/) [#TestAutomation](https://en.wikipedia.org/wiki/Test_automation)