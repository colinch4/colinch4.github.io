---
layout: post
title: "[typescript] Promise.all과 Promise.race의 차이점"
description: " "
date: 2023-12-14
tags: [typescript]
comments: true
share: true
---

자바스크립트의 Promise 객체는 비동기 작업을 다루는 데 유용한데, `Promise.all`과 `Promise.race`는 둘 다 여러 개의 프로미스를 다룰 때 유용하게 사용됩니다. 하지만 둘 간에는 몇 가지 중요한 차이점이 있습니다. 이번 글에서는 `Promise.all`과 `Promise.race`의 차이점을 알아보겠습니다.

## Promise.all

`Promise.all`은 배열로 전달된 프로미스들이 모두 이행될 때까지 기다린 후 결과를 반환합니다. 만약 하나 이상의 프로미스가 거부된다면, `Promise.all`은 첫 번째 거부된 프로미스의 이유로 거부됩니다. 예시 코드는 아래와 같습니다.

```typescript
const promises = [
  new Promise((resolve) => setTimeout(resolve, 1000, 'one')),
  new Promise((resolve) => setTimeout(resolve, 2000, 'two')),
  new Promise((resolve) => setTimeout(resolve, 3000, 'three'))
];

Promise.all(promises)
  .then((results) => {
    console.log(results); // ['one', 'two', 'three']
  })
  .catch((error) => {
    console.error(error); // 만약 하나 이상의 프로미스가 거부되었을 때의 처리
  });
```

## Promise.race

`Promise.race`는 배열로 전달된 프로미스들 중 가장 먼저 이행 또는 거부된 프로미스의 결과를 반환합니다. 따라서 `Promise.race`는 가장 먼저 이행되는 프로미스의 결과를 반환하거나, 가장 먼저 거부되는 프로미스의 이유로 거부됩니다. 예시 코드는 아래와 같습니다.

```typescript
const promises = [
  new Promise((resolve) => setTimeout(resolve, 1000, 'one')),
  new Promise((resolve, reject) => setTimeout(reject, 500, 'error')),
  new Promise((resolve) => setTimeout(resolve, 3000, 'three'))
];

Promise.race(promises)
  .then((result) => {
    console.log(result); // 'one'
  })
  .catch((error) => {
    console.error(error); // 만약 가장 먼저 거부된 프로미스가 있을 때의 처리
  });
```

## 결론

`Promise.all`은 모든 프로미스가 완료될 때까지 기다렸다가 모든 결과를 반환하고, `Promise.race`는 가장 먼저 완료된 프로미스의 결과를 반환합니다. 각각의 사용 용도에 맞게 적절히 활용하면 비동기 작업을 효과적으로 처리할 수 있습니다.

이상으로 `Promise.all`과 `Promise.race`의 차이점에 대해 알아보았습니다. 부족한 부분이 있다면 추가로 알려주시면 감사하겠습니다.