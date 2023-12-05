---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 타이머 구현"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript는 웹 개발에서 많이 활용되는 프로그래밍 언어입니다. 이 언어를 사용하여 타이머를 구현하는 방법에는 `setTimeout`과 `setInterval` 함수를 사용하는 것이 있습니다. 이 두 가지 함수를 사용하면 일정 시간 후에 코드를 실행하거나 주기적으로 코드를 반복 실행할 수 있습니다.

## setTimeout 함수

`setTimeout` 함수를 사용하면 특정 시간이 지난 후에 코드를 한 번 실행할 수 있습니다. 아래는 `setTimeout` 함수의 기본 문법입니다.

```javascript
setTimeout(function, delay, arg1, arg2, ...)
```

- `function`: 실행할 함수를 지정합니다.
- `delay`: 지연 시간을 밀리초(ms) 단위로 지정합니다.
- `arg1, arg2, ...`: 실행할 함수에 전달할 인자들을 지정합니다. (선택 사항)

아래는 3초 후에 "타이머가 실행되었습니다!"라는 메시지를 출력하는 예제입니다.

```javascript
setTimeout(function() {
    console.log("타이머가 실행되었습니다!");
}, 3000);
```

## setInterval 함수

`setInterval` 함수를 사용하면 특정 주기로 코드를 반복해서 실행할 수 있습니다. 아래는 `setInterval` 함수의 기본 문법입니다.

```javascript
setInterval(function, delay, arg1, arg2, ...)
```

- `function`: 실행할 함수를 지정합니다.
- `delay`: 반복 주기를 밀리초(ms) 단위로 지정합니다.
- `arg1, arg2, ...`: 실행할 함수에 전달할 인자들을 지정합니다. (선택 사항)

아래는 1초마다 "타이머가 실행되었습니다!"라는 메시지를 출력하는 예제입니다. 5번 반복 후에 타이머가 멈추도록 설정되어 있습니다.

```javascript
var count = 0;
var timer = setInterval(function() {
    console.log("타이머가 실행되었습니다!");

    count++;
    if(count >= 5) {
        clearInterval(timer);
        console.log("타이머가 종료되었습니다!");
    }
}, 1000);
```

## 요약

JavaScript를 사용하여 타이머를 구현할 수 있는 `setTimeout`과 `setInterval` 함수에 대해 알아보았습니다. `setTimeout`은 일정 시간 후에 코드를 한 번 실행하고, `setInterval`은 특정 주기로 코드를 반복해서 실행합니다. 이를 활용하여 웹 애플리케이션에서 다양한 타이머 기능을 구현할 수 있습니다.

---

#### 참고 자료
- [Mozilla Developer Network - setTimeout](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [Mozilla Developer Network - setInterval](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)