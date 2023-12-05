---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 데이터 저장 방식"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript에서 데이터를 저장하고 처리하는 방법은 다양합니다. 이번 글에서는 `setTimeout`과 `setInterval` 함수를 사용하여 데이터를 저장하는 방식을 알아보겠습니다.

## 1. setTimeout 함수

`setTimeout` 함수는 일정 시간이 지난 후에 특정한 동작을 수행할 수 있도록 지연을 설정해주는 함수입니다. 이 함수를 사용하여 데이터를 저장하려면 다음과 같은 방법을 사용할 수 있습니다.

```javascript
// 데이터 저장을 위한 변수
let data = null;

// 5초 후에 데이터 저장하기
setTimeout(() => {
  data = '저장된 데이터';
}, 5000);
```

위의 코드에서 `setTimeout` 함수에 전달된 콜백 함수 내에서 데이터를 저장하도록 설정하였습니다. 5초 후에 `data` 변수에 '저장된 데이터' 값을 할당합니다.

## 2. setInterval 함수

`setInterval` 함수는 일정한 시간 간격으로 특정한 동작을 반복적으로 수행할 수 있도록 도와주는 함수입니다. 이 함수를 사용하여 데이터를 저장하려면 다음과 같은 방법을 사용할 수 있습니다.

```javascript
// 데이터 저장을 위한 변수
let data = [];

// 1초마다 데이터 저장하기
const interval = setInterval(() => {
  const newData = '새로운 데이터';
  data.push(newData);
}, 1000);
```

위의 코드에서 `setInterval` 함수에 전달된 콜백 함수 내에서 데이터를 저장하도록 설정하였습니다. 1초마다 '새로운 데이터'를 생성하여 `data` 변수에 추가합니다.

## 3. 데이터 사용하기

위의 방식으로 데이터를 저장한 뒤에는 해당 데이터를 활용할 수 있습니다. 예를 들어, 저장된 데이터를 출력하거나 다른 연산을 수행할 수 있습니다.

```javascript
// 저장된 데이터 출력하기
console.log(data);

// 데이터 연산하기
const dataLength = data.length;
console.log(`저장된 데이터 개수: ${dataLength}`);
```

위의 코드에서는 저장된 데이터를 출력한 후, 데이터의 개수를 계산하여 출력하는 예제입니다.

## 4. 참고자료

- [MDN Web Docs - setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs - setInterval](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)

`setTimeout`과 `setInterval` 함수를 사용하여 데이터를 저장하고 활용하는 방법에 대해 알아보았습니다. 이러한 방법을 사용하면 다양한 작업에 유용하게 활용할 수 있습니다.