---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 동기 처리"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript에서 비동기 작업을 처리할 때에는 일반적으로 `setTimeout`과 `setInterval` 함수를 사용합니다. 그러나 이 함수들은 비동기적으로 실행되므로, 동기적인 처리가 필요한 상황에서는 어떻게 해야 할까요?

이번 글에서는 `setTimeout`과 `setInterval`을 사용하여 동기적으로 작업을 처리하는 방법에 대해 알아보겠습니다.

## setTimeout을 사용한 동기 처리

`setTimeout` 함수는 일정 시간이 지난 후에 콜백 함수를 실행하는 함수입니다. 일반적으로 이를 사용하여 비동기 작업을 처리합니다. 그러나, `setTimeout`을 활용하여 동기적으로 처리하는 방법도 있습니다.

```javascript
function syncTimeout(callback, delay) {
    var start = new Date().getTime();
    while (new Date().getTime() < start + delay) {
        // 동기적으로 대기
    }
    callback();
}

// 동기적으로 실행되는 함수
function synchronousFunction() {
    console.log("This is a synchronous function");
}

// setTimeout을 동기적으로 사용
syncTimeout(synchronousFunction, 3000);
```

위의 예제 코드에서는 `syncTimeout` 함수를 정의하여 `setTimeout`을 동기적으로 사용하였습니다. `syncTimeout` 함수는 `setTimeout`을 호출하고 일정 시간 동안 대기한 후에 콜백 함수를 실행합니다. 이렇게 하면 비동기적으로 동작하는 `setTimeout`을 동기적으로 처리할 수 있습니다.

## setInterval을 사용한 동기 처리

`setInterval` 함수는 주어진 시간 간격마다 콜백 함수를 반복적으로 실행하는 함수입니다. 비동기적으로 작업을 처리하는 경우에 많이 사용됩니다. 그러나 `setInterval`을 활용하여 동기적으로 작업을 처리하는 방법도 있습니다.

```javascript
var syncInterval = function(callback, delay, repetitions) {
    var count = 0;
    var interval = setInterval(function() {
        callback();
        count++;
        if (count === repetitions) {
            clearInterval(interval);
        }
    }, delay);
};

// 동기적으로 실행되는 함수
function synchronousFunction() {
    console.log("This is a synchronous function");
}

// setInterval을 동기적으로 사용
syncInterval(synchronousFunction, 1000, 5);
```

위의 예제 코드에서는 `syncInterval` 함수를 정의하여 `setInterval`을 동기적으로 사용하였습니다. `syncInterval` 함수는 `setInterval`을 호출하고 일정 시간 간격으로 콜백 함수를 반복 실행합니다. `repetitions` 매개변수를 통해 실행 횟수를 제한하여 동기 처리를 구현할 수 있습니다.

이렇게하면 `setInterval` 함수를 사용하면서도 필요에 따라 동기적으로 작업을 처리할 수 있습니다.

## 정리

JavaScript에서 `setTimeout`과 `setInterval`을 사용하여 비동기 작업을 처리하는 것은 일반적인 방법입니다. 그러나 때로는 동기적으로 작업을 처리해야하는 상황이 발생할 수 있습니다.

이 글에서는 `setTimeout`과 `setInterval`을 사용하여 동기적으로 작업을 처리하는 방법을 다루었습니다. `setTimeout`을 활용하여 동기 처리를 수행하는 예제 코드와 `setInterval`을 활용하여 동기 처리를 수행하는 예제 코드를 소개했습니다.

이러한 방법들을 적절하게 활용하여 애플리케이션의 성능과 사용자 경험을 향상시킬 수 있습니다.

## 참고 자료

- [MDN Web Docs: setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs: setInterval](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)