---
layout: post
title: "자바스크립트 프로미스 기반 비동기 함수 (Promise-based Asynchronous Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

**자바스크립트**는 단일 스레드 기반 언어로, 동기적으로 작동하는 특성이 있습니다. 이는 비동기 작업을 처리할 때 문제가 될 수 있습니다. 하지만 **프로미스 (Promise)** 를 활용하여 비동기 함수를 작성하면, 비동기 작업을 좀 더 간편하게 다룰 수 있습니다. 이번 글에서는 자바스크립트 프로미스 기반 비동기 함수에 대해 알아보겠습니다.

## 프로미스란 무엇인가요?

**프로미스**는 **비동기적 작업의 완료 또는 실패**를 나타내는 객체입니다. 비동기 작업의 결과를 예측하기 위해 유용하게 사용됩니다. 프로미스는 세 가지 상태를 가지며, **대기 (pending), 이행 (fulfilled), 거부 (rejected)**로 구분됩니다.

## 비동기 함수 작성하기

자바스크립트에서 비동기 작업을 처리할 때, 주로 **콜백 (callback)** 함수를 사용합니다. 그러나 콜백 함수는 중첩될 수도 있고, 구조가 복잡해질 수 있습니다. 이를 해결하기 위해 프로미스를 사용하는 것이 좋습니다.

아래는 프로미스를 사용하여 비동기 함수를 작성하는 예시입니다.

```javascript
function getData() {
  return new Promise((resolve, reject) => {
    // 비동기 작업 수행
    const data = fetchData();
    
    if (data) {
      // 비동기 작업 성공 시
      resolve(data);
    } else {
      // 비동기 작업 실패 시
      reject("Error fetching data");
    }
  });
}

// 비동기 함수 호출
getData()
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error(error);
  });
```

위의 예시에서 `getData` 함수는 프로미스를 반환합니다. `fetchData` 함수는 비동기 작업을 수행하고, 작업이 완료되면 `resolve` 메서드를 호출하여 성공 상태로 변경합니다. 작업이 실패한 경우 `reject` 메서드를 호출하여 실패 상태로 변경합니다.

비동기 함수를 호출할 때에는 `then` 메서드로 성공 상태를 처리하고, `catch` 메서드로 실패 상태를 처리합니다.

## 프로미스 체이닝 (Promise Chaining)

프로미스는 체이닝을 통해 여러 비동기 작업을 연결해서 처리할 수 있습니다. 예를 들어, 데이터를 가져온 후에 데이터를 가공하거나, 다른 비동기 작업을 수행할 수 있습니다.

아래는 프로미스 체이닝을 활용한 예시입니다.

```javascript
getData()
  .then((data) => {
    // 데이터 가공
    return process(data);
  })
  .then((processedData) => {
    // 가공된 데이터를 다른 비동기 작업에 활용
    return anotherAsyncTask(processedData);
  })
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(error);
  });
```

위의 예시에서 `getData` 함수에서 가져온 데이터를 `process` 함수로 가공한 뒤, `anotherAsyncTask` 함수로 전달하여 다른 비동기 작업을 수행합니다. 마지막으로 처리된 결과를 출력합니다.

프로미스 체이닝을 통해 작업 단계를 쉽게 조합하고, 가독성 있고 재사용 가능한 비동기 함수를 만들 수 있습니다.

## 요약

프로미스를 사용하여 자바스크립트에서 비동기 작업을 처리하면, 콜백 함수에 비해 코드 구조를 간결하게 유지할 수 있습니다. 프로미스는 비동기 작업의 완료 또는 실패를 다룰 때 유용하게 사용됩니다. 프로미스 체이닝을 통해 여러 비동기 작업을 연결하여 처리할 수 있습니다.

**참고 자료**
- [Mozilla Developer Network - JavaScript Promise](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise)