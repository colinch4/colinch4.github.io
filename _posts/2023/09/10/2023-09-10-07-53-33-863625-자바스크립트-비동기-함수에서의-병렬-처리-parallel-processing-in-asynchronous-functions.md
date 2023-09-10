---
layout: post
title: "자바스크립트 비동기 함수에서의 병렬 처리 (Parallel Processing in Asynchronous Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 싱글 스레드 언어이기 때문에 성능 향상을 위해 **비동기 프로그래밍**을 사용합니다. 이를 통해 긴 작업이 필요한 동안 다른 작업을 처리하고, 작업이 완료되었을 때 결과를 처리할 수 있습니다. 이 때, **병렬 처리**는 여러 개의 비동기 작업을 동시에 실행하여 처리 속도를 향상시키는 방법입니다.

비동기 함수에서는 일반적으로 **콜백 함수**를 사용하여 작업이 완료되었을 때 처리를 진행합니다. 그러나 이러한 방식은 작업의 수가 많아질수록 코드가 복잡해지고 유지보수가 어려워집니다. 따라서 병렬 처리를 통해 비동기 함수를 효율적으로 사용하는 방법을 알아보겠습니다.

## Promise와 병렬 처리

ECMAScript 6부터 도입된 `Promise`는 비동기 작업을 더욱 간편하게 다룰 수 있는 객체입니다. `Promise`는 성공 또는 실패를 나타내는 상태를 갖고 있으며, 이를 활용하여 비동기 작업을 병렬로 처리할 수 있습니다.

```javascript
const fetchData = () => {
  return new Promise((resolve, reject) => {
    // 비동기 작업 코드
    resolve(data); // 작업이 성공적으로 완료된 경우
    reject(error); // 작업이 실패한 경우
  });
};

const fetchDataParallel = async () => {
  const promises = [];
  
  for (let i = 0; i < 5; i++) {
    promises.push(fetchData());
  }

  const results = await Promise.all(promises);
  console.log(results);
}

fetchDataParallel();
```

위의 예제에서는 `fetchData`라는 비동기 함수를 호출하고, `Promise` 객체를 반환합니다. 이후 `fetchDataParallel` 함수에서 `Promise.all` 메소드를 사용하여 병렬로 여러 개의 비동기 작업을 처리합니다. 이렇게 하면 해당 작업이 모두 완료될 때까지 기다리고, 모든 작업의 결과를 배열로 반환합니다.

## Worker와 병렬 처리

`Worker`는 별도의 스레드에서 JavaScript 코드를 실행할 수 있는 웹 브라우저의 API입니다. 이를 활용하여 비동기 작업을 병렬로 처리할 수 있습니다.

```javascript
// worker.js
self.onmessage = event => {
  const data = event.data;

  // 비동기 작업 코드
  self.postMessage(result); // 작업이 완료되면 결과를 메인 스레드로 전송
};

// main.js
const workers = [];
for (let i = 0; i < 5; i++) {
  const worker = new Worker('worker.js');
  workers.push(worker);
}

workers.forEach(worker => {
  worker.postMessage(data); // 작업 데이터를 워커에게 전송
});

workers.forEach(worker => {
  worker.onmessage = event => {
    const result = event.data;
    console.log(result);
  }
});
```

위의 예제에서는 `worker.js` 파일에서 `self.onmessage` 이벤트 핸들러를 사용하여 메인 스레드로부터 데이터를 전달받고, 비동기 작업을 처리한 후 결과를 메인 스레드로 전송합니다. `main.js` 파일에서는 여러 개의 워커를 생성하고, 각각에게 작업 데이터를 전송합니다. 이후 각 워커는 작업을 수행한 후 결과를 메인 스레드로 보내고, 메인 스레드에서 결과를 처리합니다.

## RxJS와 병렬 처리

RxJS는 Reactive Extensions의 자바스크립트 구현으로, 비동기 데이터 스트림을 다루기 위한 라이브러리입니다. 이를 활용하여 데이터 스트림을 병렬로 처리할 수 있습니다.

```javascript
import { from } from 'rxjs';
import { mergeMap } from 'rxjs/operators';

const fetchData = () => {
  return new Promise(resolve => {
    // 비동기 작업 코드
    resolve(data);
  });
};

const fetchDataParallel = () => {
  const observables = from(Array(5).fill(fetchData()));

  observables.pipe(
    mergeMap(data => data)
  ).subscribe(result => console.log(result));
}

fetchDataParallel();
```

위의 예제에서는 `rxjs` 라이브러리에서 제공하는 `from` 함수를 사용하여 데이터 스트림을 생성하고, `mergeMap` 연산자를 이용하여 각 데이터를 병렬로 처리합니다. 이후 결과를 구독(subscribe)하여 처리합니다.

## 결론

자바스크립트 비동기 함수에서의 병렬 처리를 위해 `Promise`, `Worker`, 그리고 `RxJS`를 활용할 수 있습니다. 이를 통해 여러 개의 비동기 작업을 동시에 처리하고, 성능을 향상시킬 수 있습니다. 비동기 함수를 효율적으로 사용하여 웹 애플리케이션의 성능을 개선해보세요.