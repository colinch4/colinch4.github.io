---
layout: post
title: "[javascript] 타이머 함수(setTimeout, setInterval)"
description: " "
date: 2023-12-07
tags: [javascript]
comments: true
share: true
---

자바스크립트에서는 타이머 함수를 사용하여 특정 코드를 일정 시간 후에 실행하거나, 주기적으로 실행할 수 있습니다. 타이머 함수에는 setTimeout과 setInterval이 있으며, 각각 한 번만 실행하고 종료되거나 반복적으로 실행되는 기능을 제공합니다.

## setTimeout

setTimeout 함수는 일정 시간 후에 특정 코드를 실행하고자 할 때 사용합니다. 다음은 setTimeout 함수의 기본 형식입니다.

```javascript
setTimeout(callback, delay);
```

- `callback`은 지연된 후에 실행하고자 하는 함수를 의미합니다.
- `delay`는 실행을 지연시킬 시간을 밀리초 단위로 표현한 값입니다.

아래 예제는 3초 후에 "Hello, World!"를 출력하는 예제입니다.

```javascript
setTimeout(function() {
  console.log("Hello, World!");
}, 3000);
```

## setInterval

setInterval 함수는 일정 시간 간격으로 특정 코드를 반복해서 실행하고자 할 때 사용합니다. 다음은 setInterval 함수의 기본 형식입니다.

```javascript
setInterval(callback, delay);
```

- `callback`은 주기적으로 실행하고자 하는 함수를 의미합니다.
- `delay`는 각 실행 사이의 시간 간격을 밀리초 단위로 표현한 값입니다.

아래 예제는 1초 간격으로 "Hello, World!"를 출력하는 예제입니다. 5번 출력된 후에 clearInterval 함수를 사용하여 반복을 중지합니다.

```javascript
let count = 0;

let intervalId = setInterval(function() {
  console.log("Hello, World!");

  count++;

  if (count === 5) {
    clearInterval(intervalId);
  }
}, 1000);
```

## 정리

자바스크립트의 타이머 함수를 사용하면 일정 시간 후에 코드를 실행하거나 주기적으로 실행할 수 있습니다. setTimeout 함수는 한 번만 실행하고 종료되는 반면, setInterval 함수는 주기적으로 반복되는 특징이 있습니다. 이를 적절히 활용하여 원하는 기능을 구현할 수 있습니다.

## 참고 자료

- [MDN Web Docs - WindowOrWorkerGlobalScope.setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs - WindowOrWorkerGlobalScope.setInterval()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)