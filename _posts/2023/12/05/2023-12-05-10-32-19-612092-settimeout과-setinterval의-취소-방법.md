---
layout: post
title: "[javascript] setTimeout과 setInterval의 취소 방법"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

자바스크립트에서는 `setTimeout`과 `setInterval` 함수를 사용하여 일정 시간 후에 코드를 실행하거나 주기적으로 반복 실행할 수 있습니다. 그러나 때로는 실행을 중지하고자 할 수도 있습니다. 이를 취소하는 방법에 대해 알아보겠습니다.

### setTimeout 취소하기

`setTimeout` 함수를 사용하여 실행 예약된 함수를 취소하려면 `clearTimeout` 함수를 사용하면 됩니다. 이 함수는 `setTimeout` 함수가 반환한 타이머 식별자를 매개변수로 받습니다. 아래는 예제 코드입니다.

```javascript
// 타이머 ID를 저장할 변수
let timerId;

// 3초 후에 실행되는 함수
function myFunction() {
  console.log('3초 후에 실행되었습니다.');
}

// setTimeout 함수로 함수 실행 예약
timerId = setTimeout(myFunction, 3000);

// 실행 취소
clearTimeout(timerId);
```

위 코드에서는 `setTimeout` 함수를 사용하여 `myFunction` 함수를 3초 후에 실행하도록 예약합니다. 그 후 `clearTimeout` 함수를 사용하여 실행을 취소합니다. 실행이 취소되었기 때문에 함수는 실행되지 않습니다.

### setInterval 취소하기

`setInterval` 함수를 사용하여 주기적으로 실행되는 함수를 취소하려면 마찬가지로 `clearInterval` 함수를 사용하면 됩니다. 이 함수도 `setInterval` 함수가 반환한 타이머 식별자를 매개변수로 받습니다. 아래는 예제 코드입니다.

```javascript
// 타이머 ID를 저장할 변수
let timerId;

// 1초마다 실행되는 함수
function myFunction() {
  console.log('1초마다 실행됩니다.');
}

// setInterval 함수로 함수 실행 예약
timerId = setInterval(myFunction, 1000);

// 실행 취소
clearInterval(timerId);
```

위 코드에서는 `setInterval` 함수를 사용하여 `myFunction` 함수가 1초마다 실행되도록 예약합니다. `clearInterval` 함수를 사용하여 실행을 취소합니다. 실행이 취소되었기 때문에 함수는 더 이상 주기적으로 실행되지 않습니다.

### 정리

`setTimeout`과 `setInterval` 함수로 예약된 실행을 취소하기 위해 `clearTimeout`과 `clearInterval` 함수를 사용할 수 있습니다. 이러한 함수를 사용하여 자바스크립트에서 실행 예약을 취소할 수 있습니다.

**참고 자료:**

- [MDN Web Docs - WindowOrWorkerGlobalScope.setTimeout()](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs - WindowOrWorkerGlobalScope.setInterval()](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)
- [MDN Web Docs - WindowOrWorkerGlobalScope.clearTimeout()](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/clearTimeout)
- [MDN Web Docs - WindowOrWorkerGlobalScope.clearInterval()](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/clearInterval)