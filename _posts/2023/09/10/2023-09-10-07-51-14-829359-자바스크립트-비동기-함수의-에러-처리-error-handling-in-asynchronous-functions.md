---
layout: post
title: "자바스크립트 비동기 함수의 에러 처리 (Error Handling in Asynchronous Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 비동기 함수를 통해 네트워크 요청, 파일 처리, 데이터베이스 쿼리와 같은 작업을 수행합니다. 하지만 비동기 함수는 예측이 힘들고 에러를 처리하기 어렵게 만들 수 있습니다. 이러한 에러 처리는 중요한 부분이며, 개발자가 미리 예측하고 처리하는 것이 좋습니다.

## Callback 방식의 에러 처리

콜백(callback)을 사용하는 전통적인 방식에서는 에러 처리를 하기 위해 주로 첫 번째 인자로 에러 객체를 전달합니다. 예를 들어, 아래의 코드는 콜백 함수에서 에러를 처리하는 예시입니다.

```javascript
function fetchData(callback) {
  // 비동기 작업 수행
  getDataFromServer((error, data) => {
    if (error) {
      callback(error);
    } else {
      callback(null, data);
    }
  });
}

fetchData((error, data) => {
  if (error) {
    console.error("에러 발생:", error);
  } else {
    console.log("데이터 가져옴:", data);
  }
});
```

하지만 이러한 방식은 콜백 함수를 중첩하면서 코드가 복잡해지고 가독성이 떨어진다는 단점이 있습니다. 또한, 에러가 발생한 후에도 콜백 체인이 계속 진행되는 문제도 있을 수 있습니다.

## Promise와 에러 처리

ES6부터 도입된 Promise는 비동기 함수의 에러 처리를 훨씬 간편하게 할 수 있는 방법을 제공합니다. Promise는 성공(resolve)과 실패(reject) 두 가지 상태를 가지며, 에러가 발생하면 reject 상태로 전환됩니다.

아래는 Promise를 사용한 에러 처리의 예시입니다.

```javascript
function fetchData() {
  return new Promise((resolve, reject) => {
    // 비동기 작업 수행
    getDataFromServer((error, data) => {
      if (error) {
        reject(error);
      } else {
        resolve(data);
      }
    });
  });
}

fetchData()
  .then((data) => {
    console.log("데이터 가져옴:", data);
  })
  .catch((error) => {
    console.error("에러 발생:", error);
  });
```

Promise를 사용하면 then 메소드를 사용하여 성공한 경우의 로직을 처리하고, catch 메소드를 사용하여 에러를 처리할 수 있습니다. 또한, Promise 체인을 사용하여 여러 개의 비동기 함수를 순차적으로 처리할 수도 있습니다.

## async/await와 에러 처리

ES8에서 도입된 async와 await는 비동기 코드를 동기식으로 작성할 수 있는 편리한 방법을 제공합니다. async 함수 내에서 await 키워드를 사용하여 비동기 작업이 완료될 때까지 대기할 수 있습니다. 이때 에러 처리는 try-catch 블록을 사용하여 처리할 수 있습니다.

아래는 async/await를 사용한 에러 처리의 예시입니다.

```javascript
async function fetchData() {
  try {
    const data = await getDataFromServer();
    console.log("데이터 가져옴:", data);
  } catch (error) {
    console.error("에러 발생:", error);
  }
}

fetchData();
```

async 함수 내에서는 일반적인 동기 코드와 같이 예외 처리를 할 수 있으며, 에러가 발생하면 catch 블록으로 이동합니다.

## 결론

자바스크립트 비동기 함수의 에러 처리는 중요한 부분이며, 콜백, Promise, async/await를 통해 각각 다른 방식으로 처리할 수 있습니다. 콜백 함수를 사용하면서 코드가 복잡해지는 것을 피하기 위해 Promise나 async/await를 사용하는 것이 좋습니다. 따라서 프로젝트의 요구사항과 개발 환경에 따라 적합한 방식을 선택하여 에러 처리를 잘 처리하는 것이 중요합니다.