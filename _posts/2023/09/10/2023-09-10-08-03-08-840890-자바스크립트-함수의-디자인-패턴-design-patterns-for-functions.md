---
layout: post
title: "자바스크립트 함수의 디자인 패턴 (Design Patterns for Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 함수가 일급 객체로서 강력한 기능을 갖추고 있습니다. 함수를 작성할 때, 잘 구조화된 디자인 패턴을 사용하면 코드의 가독성과 유지 보수성을 향상시킬 수 있습니다. 이번 블로그에서는 자바스크립트 함수의 디자인 패턴을 살펴보겠습니다.

## IIFE (Immediately Invoked Function Expression)

IIFE는 즉시 실행되는 함수 표현식을 의미합니다. 함수를 정의하고 즉시 실행하기 때문에 전역 스코프를 오염시키지 않고 변수의 충돌을 막을 수 있습니다.

```javascript
(function() {
  // 코드 작성
})();
```

## 콜백 (Callback)

콜백 패턴은 비동기 작업을 처리할 때 매우 유용한 패턴입니다. 함수의 인수로 다른 함수를 전달하여 비동기 작업의 결과를 처리할 수 있습니다.

```javascript
function fetchData(callback) {
  // 비동기 작업 수행
  // 결과를 콜백 함수로 전달
  callback(result);
}
```

## 프로미스 (Promises)

프로미스는 ES6 이후부터 추가된 기능으로, 콜백 패턴의 단점을 보완하는 패턴입니다. 비동기 작업의 결과를 나중에 처리하기 위해 프로미스 객체를 반환합니다.

```javascript
function fetchData() {
  return new Promise((resolve, reject) => {
    // 비동기 작업 수행
    // 성공시 resolve로 결과 전달
    // 실패시 reject로 오류 전달
  });
}

fetchData()
  .then(result => {
    // 비동기 작업 성공 시 처리 로직
  })
  .catch(error => {
    // 비동기 작업 실패 시 처리 로직
  });
```

## 제너레이터 (Generators)

제너레이터는 함수의 실행을 일시 중단한 후 나중에 다시 시작할 수 있는 기능을 제공합니다. `yield` 키워드를 사용하여 제너레이터 함수의 실행을 멈출 수 있습니다.

```javascript
function* generatorFunction() {
  yield 1;
  yield 2;
  yield 3;
}

const generator = generatorFunction();
console.log(generator.next().value); // 1
console.log(generator.next().value); // 2
console.log(generator.next().value); // 3
```

## 커링 (Currying)

커링은 다중 인수를 받는 함수를 단일 인수를 받는 함수의 체인으로 변환하는 패턴입니다. 이를 통해 함수의 재사용성과 일관성을 높일 수 있습니다.

```javascript
function add(x) {
  return function(y) {
    return x + y;
  };
}

const addFive = add(5);
console.log(addFive(3)); // 8
console.log(addFive(7)); // 12
```

위에서 소개한 디자인 패턴들은 자바스크립트 함수를 구조화하고 재사용성을 높이는 데에 매우 유용합니다. 익숙해지고 적절하게 활용하여 코드를 더욱 효율적이고 견고하게 개발할 수 있도록 노력해보세요.

**Happy coding!**