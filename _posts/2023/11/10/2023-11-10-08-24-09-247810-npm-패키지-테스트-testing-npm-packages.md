---
layout: post
title: "npm 패키지 테스트 (Testing npm packages)"
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

npm은 JavaScript 개발자들이 패키지를 공유하고 재사용할 수 있는 생태계를 제공하는 역할을 합니다. npm을 사용하면 다른 사용자들이 만든 패키지를 손쉽게 사용할 수 있을 뿐만 아니라, 자신의 패키지를 배포하여 다른 사람들과 공유할 수도 있습니다.

하지만 npm 패키지를 사용하기 전에 테스트를 진행하여 예기치 않은 오류나 문제가 없는지 확인하는 것이 중요합니다. 이번 포스트에서는 npm 패키지를 테스트하는 방법에 대해 알아보겠습니다.

## 테스트 프레임워크 선택

npm 패키지를 테스트하기 위해 다양한 테스트 프레임워크를 사용할 수 있습니다. 대표적인 테스트 프레임워크로는 [Jest](https://jestjs.io/), [Mocha](https://mochajs.org/), [Jasmine](https://jasmine.github.io/) 등이 있습니다. 이 중에서는 Jest를 예시로 사용하여 테스트를 진행하겠습니다.

## Jest 설치

Jest를 사용하기 위해서는 먼저 Jest를 설치해야 합니다. npm을 통해 Jest를 설치하는 방법은 아래와 같습니다.

```shell
npm install --save-dev jest
```

위 명령어를 실행하면 `package.json` 파일에 Jest가 devDependencies로 추가됩니다.

## 테스트 작성

Jest를 설치하였으면 이제 테스트 파일을 작성해야 합니다. 일반적으로 테스트 파일은 `.test.js` 확장자를 가지며, 테스트 대상 모듈의 파일과 같은 디렉토리에 위치시킵니다.

테스트 파일은 테스트할 함수 또는 모듈의 기대 동작을 정의합니다. Jest에서 기대 동작은 `expect` 함수와 `toMatch` 메소드 등을 사용하여 정의할 수 있습니다. 예를 들어 아래 코드는 `add` 함수가 제대로 동작하는지 테스트하는 예시입니다.

```javascript
// add.js
function add(a, b) {
  return a + b;
}

module.exports = add;
```

```javascript
// add.test.js
const add = require('./add');

test('add 함수의 결과가 정확한지 확인', () => {
  expect(add(1, 2)).toBe(3);
});
```

위 코드에서 `test` 함수는 Jest에서 제공하는 테스트 함수입니다. 첫 번째 인자로는 테스트에 대한 설명 문자열을 전달하고, 두 번째 인자로는 테스트 함수를 전달합니다. `expect` 함수의 인자로는 테스트할 값을 전달하고, 기대 동작을 `toBe` 메소드를 사용하여 정의합니다.

## 테스트 실행

테스트 파일을 작성하였으면 이제 Jest를 실행하여 테스트를 진행할 수 있습니다. `package.json` 파일의 `scripts` 부분을 수정하여 Jest를 실행하도록 설정할 수 있습니다.

```json
"scripts": {
  "test": "jest"
}
```

위 설정을 추가한 후 아래 명령어를 실행하면 Jest가 테스트를 실행합니다.

```shell
npm test
```

Jest는 테스트 파일을 검색하고 실행한 후, 테스트 결과를 콘솔에 출력합니다. 이를 통해 테스트 도중 발생한 오류나 실패한 테스트 케이스를 쉽게 확인할 수 있습니다.

## 결론

npm 패키지를 테스트하는 것은 코드의 신뢰성과 안정성을 확보하는 데 매우 중요합니다. Jest와 같은 테스트 프레임워크를 사용하여 효율적이고 체계적인 테스트를 진행할 수 있으며, 이를 통해 패키지의 품질을 높일 수 있습니다. 테스트를 통해 안정적이고 신뢰할 수 있는 패키지를 만들 수 있도록 노력해보세요.

#npm #testing