---
layout: post
title: "자바스크립트 비동기 함수의 에러 처리 (Error Handling in Asynchronous Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 비동기 함수를 사용할 때, 에러 처리는 매우 중요합니다. 비동기 함수는 다양한 작업을 수행하기 위해 백그라운드에서 실행되는데, 이때 발생하는 에러를 적절히 처리하지 않으면 예기치 않은 동작이 발생할 수 있습니다. 이번 블로그 포스트에서는 자바스크립트에서 비동기 함수의 에러 처리에 대해 알아보도록 하겠습니다.

## try-catch 구문을 사용한 에러 처리

일반적으로 동기 함수에서는 `try-catch` 구문을 사용하여 예외를 처리할 수 있습니다. 하지만 비동기 함수에서는 `try-catch` 구문만으로는 에러를 제대로 처리할 수 없습니다. 이는 비동기 함수가 즉시 실행되는 것이 아니라 이벤트 루프에서 대기하다 실행되기 때문입니다.

```javascript
try {
  setTimeout(function() {
    throw new Error('에러 발생!');
  }, 1000);
} catch (error) {
  console.log('에러 처리:', error.message);
}
```

위의 코드에서 `setTimeout` 함수 내부에서 에러를 발생시키고 있습니다. 하지만 이 코드에서는 `try-catch` 구문으로 에러를 캐치할 수 없습니다. 에러는 `setTimeout` 콜백 함수 내부에서 발생하지만, `setTimeout` 함수는 비동기적으로 실행되므로 `try-catch`구문이 완료된 이후에 발생합니다.

## 콜백 함수를 통한 에러 처리 

비동기 함수 내부에서 발생하는 에러를 다루기 위해선 콜백 함수를 사용할 수 있습니다. 콜백 함수를 통해 에러를 전달하면, 호출자가 콜백 함수를 적절히 처리할 수 있습니다.

```javascript
function asyncFunction(callback) {
  setTimeout(function() {
    try {
      throw new Error('에러 발생!');
    } catch (error) {
      callback(error);
    }
  }, 1000);
}

asyncFunction(function(error) {
  console.log('에러 처리:', error.message);
});
```

위의 코드에서는 `asyncFunction`이라는 비동기 함수를 정의하고, 내부에서 `setTimeout` 콜백 함수에서 에러를 발생시키고, 에러를 콜백 함수로 전달하고 있습니다. 이후 호출하는 코드에서는 콜백 함수를 정의하고, 에러를 처리하는 로직을 구현합니다.

## 프라미스를 사용한 에러 처리

ES6부터 추가된 프라미스(Promise)는 비동기 코드를 더욱 간결하고 효율적으로 다룰 수 있게 해줍니다. 프라미스를 사용하면 비동기 함수에서 발생하는 에러를 `catch` 메서드를 이용하여 쉽게 처리할 수 있습니다.

```javascript
function asyncFunction() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      reject(new Error('에러 발생!'));
    }, 1000);
  });
}

asyncFunction()
  .catch((error) => {
    console.log('에러 처리:', error.message);
  });
```

위의 코드에서는 `asyncFunction`이라는 비동기 함수를 정의하고, 내부에서 `setTimeout`과 함께 `Promise`를 반환하고 있습니다. 에러 발생 시에는 `reject` 메서드를 호출하여 에러를 전달합니다. 이후 호출하는 코드에서는 `catch` 메서드를 이용하여 에러 처리 로직을 구현합니다.

## async/await를 사용한 에러 처리

ES8부터 추가된 async/await는 프라미스를 더욱 쉽게 사용할 수 있는 구문입니다. async 함수 내부에서 await 키워드를 사용하여 프라미스가 완료될 때까지 기다린 후 결과를 반환합니다. async/await를 사용하면 비동기 함수에서 발생하는 에러를 `try-catch` 구문으로 캐치할 수 있습니다.

```javascript
function asyncFunction() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      reject(new Error('에러 발생!'));
    }, 1000);
  });
}

async function main() {
  try {
    await asyncFunction();
  } catch (error) {
    console.log('에러 처리:', error.message);
  }
}

main();
```

위의 코드에서는 `asyncFunction`이라는 비동기 함수를 정의하고, 내부에서 `setTimeout`과 함께 `Promise`를 반환하고 있습니다. 에러 발생 시에는 `reject` 메서드를 호출하여 에러를 전달합니다. 이후 `main` 함수에서는 `async` 키워드로 선언하여 async 함수로 만들고, `try-catch` 구문을 이용하여 에러 처리 로직을 구현합니다.

## 결론

자바스크립트에서 비동기 함수의 에러 처리는 애플리케이션의 신뢰성과 안정성을 보장하는 중요한 요소입니다. 앞서 설명한 콜백 함수, 프라미스, async/await를 이용하여 비동기 함수에서 발생하는 에러를 적절히 처리할 수 있습니다. 각각의 방식은 장단점이 있으므로, 상황에 맞게 적절한 방법을 선택하여 사용하시면 됩니다. 반드시 에러 처리를 고려하여 비동기 함수를 설계하고 사용하시기 바랍니다.