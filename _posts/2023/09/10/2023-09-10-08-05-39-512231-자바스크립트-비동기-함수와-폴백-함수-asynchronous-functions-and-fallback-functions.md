---
layout: post
title: "자바스크립트 비동기 함수와 폴백 함수 (Asynchronous Functions and Fallback Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 단일 스레드로 동작하는 언어이기 때문에 **비동기 함수**는 중요한 개념입니다. 비동기 함수는 특정 작업이 완료될 때까지 코드 실행을 차단하지 않고 계속 실행되도록 하는 함수입니다. 이를 통해 사용자 경험을 향상시키고, 브라우저에서 끊김 없는 사용자 인터랙션을 제공할 수 있습니다.

비동기 함수를 사용하는 일반적인 예는 HTTP 요청, 파일 로딩, 데이터베이스 작업 등입니다. 이러한 작업은 실행에 시간이 걸리므로, 비동기 함수를 사용하여 작업이 완료될 때까지 다른 작업을 계속할 수 있습니다.

## 비동기 함수의 문제점

비동기 함수를 사용하면 코드가 더 유연하고 반응적이게 됩니다. 그러나 이러한 함수는 작업이 완료될 때까지 어떤 결과를 반환하지 않기 때문에 결과를 기다리는 동안 다른 작업을 수행하기가 어렵습니다.

또한 비동기 함수는 작업이 완료된 후에 호출되는 **콜백 함수**를 통해 결과를 처리합니다. 이는 JavaScript에서 **폴백 함수**로 알려져 있습니다. 콜백 함수의 재사용성과 유지보수 가능성을 낮추는 문제가 있을 수 있습니다.

## Promise를 통한 비동기 함수 처리

ES6에서는 Promise라는 개념이 도입되었습니다. Promise는 비동기 작업의 결과를 나타내는 객체입니다. 비동기 함수는 Promise를 반환하여 작업의 성공 또는 실패 여부를 나타낼 수 있습니다. 이는 코드의 가독성과 유지보수성을 향상시킵니다.

Promise를 사용하는 비동기 함수의 일반적인 예는 다음과 같습니다.

```javascript
function fetchData(url) {
  return new Promise((resolve, reject) => {
    fetch(url)
      .then(response => response.json())
      .then(data => resolve(data))
      .catch(error => reject(error));
  });
}
```

위의 예제에서는 `fetchData` 함수가 비동기 함수이며, URL을 매개변수로 받아 해당 URL에서 데이터를 가져옵니다. `fetch` 함수는 HTTP 요청을 보내고 응답을 받아옵니다. 응답을 JSON으로 변환하고, 성공적으로 변환된 데이터를 `resolve` 함수를 통해 반환합니다. 실패한 경우는 `catch` 함수를 통해 `reject` 함수를 호출하여 실패를 처리합니다.

## Async/Await를 통한 비동기 함수 처리

ES8에서는 async/await라는 새로운 문법이 도입되었습니다. 이를 통해 Promise를 더 직관적으로 사용할 수 있고, 코드를 더 읽기 쉽게 만들 수 있습니다.

위에서 작성한 예제를 async/await를 사용하여 다시 작성하면 다음과 같습니다.

```javascript
async function fetchData(url) {
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  } catch (error) {
    throw error;
  }
}
```

`fetchData` 함수의 매개변수는 URL이며, 데이터를 가져와서 JSON으로 변환합니다. 데이터를 성공적으로 반환할 경우 `return` 키워드를 사용하여 결과를 반환하고, 실패한 경우는 `throw` 키워드를 사용하여 예외를 발생시킵니다.

## 폴백 함수를 사용한 오류 처리

응답을 처리하는 것 외에도 다양한 종류의 오류 처리가 필요할 수 있습니다. 이때 폴백 함수를 사용하면 오류에 대한 처리가 더욱 유연해집니다.

```javascript
fetchData(url)
  .then(data => handleData(data))
  .catch(error => handleError(error));
```

위의 예제에서는 `fetchData` 함수를 호출하여 데이터를 가져온 후, `handleData` 함수로 데이터를 전달합니다. 만약 에러가 발생한 경우에는 `handleError` 함수가 호출되어 오류를 처리합니다.

## 결론

비동기 함수와 폴백 함수는 JavaScript에서 중요한 개념입니다. Promise와 async/await를 사용하여 비동기 작업을 처리하면 코드의 가독성과 유지보수성이 개선되며, 오류 처리에는 폴백 함수를 사용할 수 있습니다. 이러한 개념을 잘 이해하고 올바르게 사용하면 JavaScript에서 효율적인 비동기 프로그래밍을 할 수 있습니다.