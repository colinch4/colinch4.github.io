---
layout: post
title: "자바스크립트 비동기 함수와 폴백 함수 (Asynchronous Functions and Fallback Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 싱글 스레드 기반의 비동기 프로그래밍 언어로 알려져 있습니다. 이는 한 번에 하나의 작업만 처리할 수 있기 때문에, 동기적으로 코드를 실행하면 작업이 느려질 수 있다는 단점이 있습니다. 이러한 문제를 해결하기 위해 자바스크립트에서는 비동기 함수와 폴백 함수를 사용합니다.

## 비동기 함수 (Asynchronous Functions)
비동기 함수는 작업이 완료될 때까지 기다리지 않고 다음 코드 블록을 실행하는 함수입니다. 자바스크립트에서는 일반적으로 비동기 함수를 사용하여 Ajax 요청, 파일 다운로드, 타이머 설정 등의 작업을 처리합니다. 

```javascript
function fetchData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = { id: 1, name: 'John Doe' };
      resolve(data);
    }, 2000);
  });
}

console.log("Start");
fetchData("https://api.example.com/users").then(data => {
  console.log(data);
});
console.log("End");
```

위 예제에서 `fetchData` 함수는 2초 후에 주어진 URL에서 데이터를 가져오는 비동기 작업을 수행합니다. `fetchData` 함수는 **Promise** 객체를 반환하고, 데이터가 준비되면 `resolve` 콜백을 호출하여 데이터를 반환합니다. 

`fetchData` 함수를 호출한 후에는 `then` 메소드를 사용하여 데이터를 처리할 수 있습니다. 이 때, `then` 메소드에 전달된 함수는 비동기 작업이 완료된 후 실행됩니다.

출력 결과는 다음과 같을 것입니다:
```
Start
End
{ id: 1, name: 'John Doe' }
```

위 예제에서 볼 수 있듯이, "Start"와 "End"는 즉시 출력되지만, 데이터는 2초 후에 비동기적으로 출력됩니다.

## 폴백 함수 (Fallback Functions)
폴백 함수는 비동기 함수에서 발생할 수 있는 오류를 처리하는 함수입니다. 비동기 함수에서 발생한 오류는 예외로 처리되지 않고 리턴값으로 전달되기 때문에, 별도의 폴백 함수를 사용하여 이를 처리해야 합니다.

```javascript
function fetchData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const error = new Error("Failed to fetch data");
      reject(error);
    }, 2000);
  });
}

function handleFallback(error) {
  console.log("Error:", error.message);
}

console.log("Start");
fetchData("https://api.example.com/users")
  .then(data => {
    console.log(data);
  })
  .catch(handleFallback);
console.log("End");
```

위 예제에서 `fetchData` 함수는 명시적으로 오류를 발생시켜 `reject`를 호출합니다. 이렇게 되면 `catch` 블록이 실행되며, `handleFallback` 함수가 호출되어 에러 메시지를 출력합니다.

출력 결과는 다음과 같을 것입니다:
```
Start
End
Error: Failed to fetch data
```

이렇게 폴백 함수를 사용하면 비동기 함수에서 발생한 오류를 안전하게 처리할 수 있습니다. 

자바스크립트에서는 이 외에도 더욱 다양한 방식으로 비동기 함수와 폴백 함수를 사용할 수 있습니다. 이를 통해 자바스크립트의 비동기 프로그래밍 모델을 이해하고, 효율적으로 코드를 작성할 수 있습니다.