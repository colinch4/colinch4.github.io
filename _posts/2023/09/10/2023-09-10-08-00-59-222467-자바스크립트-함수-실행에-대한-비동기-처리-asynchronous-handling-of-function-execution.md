---
layout: post
title: "자바스크립트 함수 실행에 대한 비동기 처리 (Asynchronous Handling of Function Execution)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 단일 스레드 언어로, 함수들이 순차적으로 실행되는 특징이 있습니다. 그러나 때로는 함수 실행 중에 다른 작업을 동시에 처리하고 싶을 때도 있습니다. 이러한 요구사항을 충족시키기 위해 자바스크립트는 **비동기 처리**를 지원합니다.

비동기 처리는 함수의 실행이 완료되지 않아도 다음 코드가 실행되는 것을 의미합니다. 이는 네트워크 요청, 파일 읽기/쓰기, 데이터베이스 쿼리 등과 같이 시간이 오래 걸리는 작업에 유용합니다. 비동기 처리를 구현하기 위해 자바스크립트에서는 **콜백 함수**, **프로미스**, **async/await** 세 가지 주요 패턴을 사용할 수 있습니다.

## 콜백 함수 (Callback Functions)

콜백 함수는 비동기 작업의 완료 시점에 호출되는 함수입니다. 콜백 함수는 비동기 작업의 결과를 처리하거나 다음 단계로의 제어 흐름을 전달하는 데 사용됩니다.

```javascript
function fetchData(callback) {
  setTimeout(function() {
    const data = 'Some data from an API';
    callback(data);
  }, 2000);
}

function process(data) {
  console.log(data); // 출력: 'Some data from an API'
}

fetchData(process);
```

위 예제에서 `fetchData` 함수는 2초 후에 콜백 함수 `process`를 호출하여 데이터를 전달합니다. 이러한 방식으로 비동기 작업을 처리할 수 있지만, 콜백 함수를 중첩해서 사용하는 경우 코드의 가독성과 유지보수성이 저하될 수 있습니다.

## 프로미스 (Promises)

프로미스는 콜백 함수를 사용하지 않고 비동기 작업을 처리하는 패턴입니다. 프로미스는 비동기 작업의 성공 또는 실패를 나타내는 객체로, 상태와 결과를 처리하는 메서드를 제공합니다.

```javascript
function fetchData() {
  return new Promise(function(resolve, reject) {
    setTimeout(function() {
      const data = 'Some data from an API';
      resolve(data);
    }, 2000);
  });
}

fetchData()
  .then(function(data) {
    console.log(data); // 출력: 'Some data from an API'
  })
  .catch(function(error) {
    console.error(error);
  });
```

위 예제에서 `fetchData` 함수는 프로미스 객체를 반환하며, 2초 후에 데이터를 성공적으로 처리하면 `resolve` 메서드를 호출하여 데이터를 전달합니다. 성공적인 처리 외에도, 오류가 발생하면 `reject` 메서드를 호출하여 오류 객체를 전달할 수 있습니다. `then` 메서드를 통해 성공적으로 처리된 데이터를, `catch` 메서드를 통해 오류를 처리할 수 있습니다.

## async/await

`async`와 `await`는 자바스크립트의 최신 비동기 처리 패턴입니다. 이 패턴을 사용하면 비동기 코드를 동기식처럼 작성할 수 있으며, 가독성이 좋아지고 오류 처리가 간편해집니다.

```javascript
async function fetchData() {
  return new Promise(function(resolve, reject) {
    setTimeout(function() {
      const data = 'Some data from an API';
      resolve(data);
    }, 2000);
  });
}

(async function() {
  try {
    const data = await fetchData();
    console.log(data); // 출력: 'Some data from an API'
  } catch (error) {
    console.error(error);
  }
})();
```

위 예제에서 `fetchData` 함수는 프로미스 객체를 반환합니다. `async` 키워드로 정의된 함수 내에서 `await`를 사용하여 비동기 작업을 대기하고, 작업이 완료된 후 데이터를 변수에 할당할 수 있습니다. 오류 처리는 `try-catch` 블록으로 간단하게 처리할 수 있습니다.

## 결론

자바스크립트에서는 비동기 처리를 위해 콜백 함수, 프로미스, async/await 세 가지 패턴을 사용할 수 있습니다. 각 패턴은 특정 상황에 따라 적합한 선택일 수 있으며, 코드의 가독성과 유지보수성을 고려하여 적절한 패턴을 선택하는 것이 중요합니다.

비동기 처리를 효율적으로 다루면서 신속한 데이터 로딩과 사용자 경험 개선에 도움이 될 수 있습니다. 자바스크립트에서의 비동기 처리에 대한 이해를 바탕으로, 더 나은 프론트엔드 개발을 위한 노력을 이어가길 바랍니다.