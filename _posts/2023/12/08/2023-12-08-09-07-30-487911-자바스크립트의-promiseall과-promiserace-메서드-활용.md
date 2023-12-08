---
layout: post
title: "[javascript] 자바스크립트의 Promise.all()과 Promise.race() 메서드 활용"
description: " "
date: 2023-12-08
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 Promise 객체를 사용하면 비동기적인 작업을 처리할 수 있습니다. Promise 객체를 다룰 때 유용하게 활용되는 두 가지 메서드인 `Promise.all()`과 `Promise.race()`에 대해 알아보겠습니다.

## Promise.all()

`Promise.all()` 메서드는 여러 개의 Promise 객체를 인자로 받고, 모든 Promise 객체들이 완료될 때까지 기다린 후에 하나의 Promise 객체를 반환합니다. 이 반환된 Promise 객체는 모든 입력된 Promise 객체들이 성공적으로 종료되었을 때에만 성공 상태가 됩니다. 만약 입력된 Promise 객체 중 하나라도 실패하면, 반환된 Promise 객체는 실패 상태가 됩니다.

예를 들어, 여러 개의 비동기 작업을 동시에 실행하고 그 결과를 기다려야 하는 경우에 `Promise.all()`을 사용할 수 있습니다.

다음은 `Promise.all()`을 사용한 예제 코드입니다.

```javascript
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Promise 1 완료');
  }, 1000);
});

const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Promise 2 완료');
  }, 2000);
});

Promise.all([promise1, promise2])
  .then((values) => {
    console.log(values);
  })
  .catch((error) => {
    console.error(error);
  });
```

위의 코드는 `promise1`과 `promise2`를 모두 완료한 후에 `then()` 메서드가 호출되어 두 Promise 객체의 반환값을 출력합니다.

## Promise.race()

`Promise.race()` 메서드는 여러 개의 Promise 객체를 인자로 받고, 가장 먼저 완료된 Promise 객체의 반환값을 갖는 하나의 Promise 객체를 반환합니다. 따라서 입력된 Promise 객체들 중 가장 먼저 완료되는 Promise 객체의 결과만을 사용하고 싶을 때에 `Promise.race()`를 사용할 수 있습니다.

예를 들어, 여러 개의 비동기 작업 중 가장 빨리 완료된 작업의 결과를 사용하고자 할 때에 `Promise.race()`가 유용합니다.

다음은 `Promise.race()`를 사용한 예제 코드입니다.

```javascript
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Promise 1 완료');
  }, 1000);
});

const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Promise 2 완료');
  }, 2000);
});

Promise.race([promise1, promise2])
  .then((value) => {
    console.log(value);
  })
  .catch((error) => {
    console.error(error);
  });
```

위의 코드는 `promise1`과 `promise2` 중에서 더 빨리 완료된 `promise1`의 반환값만 출력합니다.

`Promise.all()`과 `Promise.race()` 메서드를 적절히 활용하면 여러 개의 비동기 작업을 효율적으로 처리할 수 있습니다.

## 결론

Promise 객체를 사용하여 비동기 작업을 처리할 때, `Promise.all()`과 `Promise.race()` 메서드는 여러 개의 비동기 작업을 관리하고 그 결과를 효율적으로 처리하는 데에 유용하게 활용될 수 있습니다. 적절한 상황에 각 메서드를 적절히 활용하여 코드를 보다 간결하고 효율적으로 작성할 수 있습니다.

참고 자료:
- [MDN web docs: Promise.all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)
- [MDN web docs: Promise.race](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race)