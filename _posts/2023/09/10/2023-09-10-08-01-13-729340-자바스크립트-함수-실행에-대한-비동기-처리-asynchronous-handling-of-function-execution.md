---
layout: post
title: "자바스크립트 함수 실행에 대한 비동기 처리 (Asynchronous Handling of Function Execution)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 단일 스레드로 동작하는 언어입니다. 이는 한 번에 한 가지 작업만 수행할 수 있다는 것을 의미합니다. 하지만 비동기 처리를 통해 함수 실행에 유연성을 더할 수 있습니다.

비동기 처리는 실행 시간이 오래 걸리는 작업을 블로킹하지 않고 백그라운드에서 실행할 수 있는 메커니즘입니다. 이를 통해 웹 애플리케이션에서 사용자 인터랙션에 반응하거나 네트워크 요청을 보내는 등의 작업을 효율적으로 처리할 수 있습니다.

## 콜백 함수 (Callback Functions)

비동기 처리를 위해 가장 일반적으로 사용되는 방법은 콜백 함수(callback function)입니다. 콜백 함수는 비동기 작업이 완료되면 호출되는 함수로, 다음과 같은 형태를 가집니다.

```javascript
function longRunningOperation(callback) {
  // 오랜 시간이 걸리는 작업
  // 완료 후 콜백 함수 호출
  callback();
}

function callback() {
  // 비동기 작업 완료 후 실행할 로직
}

// 비동기 작업 시작
longRunningOperation(callback);
```

위의 예제에서 `longRunningOperation` 함수는 오랜 시간이 걸리는 작업을 수행한 뒤 `callback` 함수를 호출합니다. 이를 통해 비동기 작업의 완료를 감지하고 콜백 함수를 실행할 수 있습니다.

## 프로미스 (Promises)

콜백 함수를 사용하는 방식은 코드가 복잡해지고 가독성이 떨어지는 문제가 있습니다. 이를 해결하기 위해 ES6에서는 프로미스(Promises)를 도입했습니다. 프로미스는 비동기 작업의 성공 또는 실패를 나타내는 객체입니다.

프로미스는 다음과 같은 형태를 가집니다.

```javascript
function longRunningOperation() {
  return new Promise((resolve, reject) => {
    // 오랜 시간이 걸리는 작업
    if (completed) {
      resolve(result);
    } else {
      reject(error);
    }
  });
}

longRunningOperation()
  .then((result) => {
    // 성공 시 실행할 로직
  })
  .catch((error) => {
    // 실패 시 실행할 로직
  });
```

위의 예제에서 `longRunningOperation` 함수는 프로미스 객체를 반환합니다. 프로미스 객체는 `resolve`와 `reject` 함수를 인자로 받는 생성자 함수를 통해 생성됩니다. 비동기 작업이 성공하면 `resolve` 함수를 호출하고, 실패하면 `reject` 함수를 호출합니다.

프로미스 객체는 `then` 메서드를 통해 성공 시 실행할 로직을 등록할 수 있고, `catch` 메서드를 통해 실패 시 실행할 로직을 등록할 수 있습니다. 이를 통해 콜백 함수보다 더 직관적이고 가독성 높은 비동기 코드를 작성할 수 있습니다.

## 비동기/대기 (async/await)

ES8에서는 다른 비동기 처리 방법인 `async`와 `await` 키워드를 도입했습니다. `async` 함수는 항상 프로미스를 반환하고, `await` 키워드는 프로미스가 처리될 때까지 코드의 실행을 일시 중단합니다.

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    // 데이터 처리
  } catch (error) {
    // 에러 처리
  }
}

fetchData();
```

위의 예제에서 `fetchData` 함수는 `async` 키워드로 정의되어 있으며, `fetch` 함수와 `response.json()` 메서드 앞에 `await` 키워드가 사용되었습니다. 이를 통해 비동기 작업이 완료될 때까지 기다리고 결과를 처리할 수 있습니다.

`async/await`는 프로미스와 달리 에러 처리를 `try/catch` 문으로 직관적으로 작성할 수 있어 가독성이 크게 향상됩니다. 또한, 기존의 동기 코드와 유사한 구조를 가지기 때문에 코드를 작성하고 이해하는 것이 훨씬 쉬워집니다.

## 결론

자바스크립트에서 비동기 작업을 다루는 방법은 콜백 함수, 프로미스, `async/await` 등 다양합니다. 이를 통해 복잡한 비동기 코드를 더 직관적이고 유지보수하기 쉬운 형태로 작성할 수 있습니다.

각 방법은 서로 다른 장단점을 가지고 있으므로 상황에 맞게 선택하는 것이 중요합니다. 프로젝트의 요구사항과 개발자의 스킬에 맞는 비동기 처리 방법을 선택하여 자바스크립트 애플리케이션의 성능과 가독성을 향상시킬 수 있습니다.