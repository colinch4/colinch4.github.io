---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 이메일 발송 처리"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

자바스크립트는 비동기적인 처리를 위해 `setTimeout`과 `setInterval`과 같은 함수를 제공합니다. 이를 활용하여 이메일 발송과 같은 작업을 처리할 수 있습니다. 이 글에서는 `setTimeout`과 `setInterval`의 사용법과 이메일 발송을 예시로 설명하겠습니다.

## setTimeout 함수

`setTimeout` 함수는 일정 시간이 지난 후에 특정한 작업을 실행하고자 할 때 사용됩니다. 함수의 구조는 다음과 같습니다. 

```javascript
setTimeout(callback, delay);
```

- `callback`: 지정한 시간이 지난 후 실행될 함수를 지정합니다.
- `delay`: 함수 실행 전까지의 시간을 밀리초로 지정합니다.

이메일 발송을 예로 들어보겠습니다. 다음은 5초 후에 이메일을 발송하는 코드입니다.

```javascript
function sendEmail() {
  console.log("이메일을 발송합니다.");
}

setTimeout(sendEmail, 5000);
```

위 코드에서는 `sendEmail` 함수를 5초 후에 실행하도록 `setTimeout` 함수를 호출하였습니다. 이렇게 하면 5초 후에 "이메일을 발송합니다."라는 메시지가 콘솔에 출력됩니다.

## setInterval 함수

`setInterval` 함수는 일정한 간격으로 반복적으로 작업을 실행하고자 할 때 사용됩니다. 함수의 구조는 다음과 같습니다.

```javascript
setInterval(callback, interval);
```

- `callback`: 일정한 간격으로 실행될 함수를 지정합니다.
- `interval`: 함수 실행 간격을 밀리초로 지정합니다.

이메일 발송을 예로 들어보겠습니다. 다음은 10초마다 이메일을 발송하는 코드입니다.

```javascript
function sendEmail() {
  console.log("이메일을 발송합니다.");
}

setInterval(sendEmail, 10000);
```

위 코드에서는 `sendEmail` 함수를 10초 간격으로 실행하도록 `setInterval` 함수를 호출하였습니다. 이렇게 하면 매 10초마다 "이메일을 발송합니다."라는 메시지가 콘솔에 출력됩니다.

## 주의사항

`setTimeout`과 `setInterval` 함수를 사용할 때 주의해야 할 사항이 있습니다.

1. 반복적으로 실행되는 작업을 멈추려면 `clearTimeout` 또는 `clearInterval` 함수를 사용해야 합니다.
2. `setTimeout`과 `setInterval` 함수에서 반환되는 값을 변수에 저장하면 나중에 작업을 취소할 수 있습니다.

```javascript
const timer = setTimeout(callback, delay);

// 나중에 작업 취소
clearTimeout(timer);
```

```javascript
const timer = setInterval(callback, interval);

// 나중에 작업 취소
clearInterval(timer);
```

이제 `setTimeout`과 `setInterval` 함수를 사용하여 이메일 발송과 같은 비동기 작업을 처리하는 방법을 알게 되었습니다. 이를 적절히 응용하여 다양한 작업을 처리할 수 있습니다.

## 참고 자료

- [MDN Web Docs: WindowOrWorkerGlobalScope.setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs: WindowOrWorkerGlobalScope.setInterval()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)