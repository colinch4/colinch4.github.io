---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 알림 기능 제어"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 setTimeout과 setInterval은 알림 기능을 제어하는데 사용되는 함수입니다. 이들 함수를 사용하여 일정 시간이 지난 후에 특정한 동작을 수행하거나 주기적인 작업을 반복할 수 있습니다.

## setTimeout 함수

setTimeout 함수는 지정된 시간이 지난 후에 한 번만 동작을 수행할 수 있습니다. 아래는 setTimeout 함수의 기본적인 사용 방법입니다.

```javascript
setTimeout(function() {
  // 지정된 시간이 지나면 실행할 동작
}, 지연시간);
```
예를 들어, 3초 후에 "안녕하세요!"라는 알림을 표시하고자 한다면 다음과 같이 코드를 작성할 수 있습니다.

```javascript
setTimeout(function() {
  alert("안녕하세요!");
}, 3000);
```

## setInterval 함수

setInterval 함수는 지정된 시간마다 주기적으로 동작을 수행할 수 있습니다. 아래는 setInterval 함수의 기본적인 사용 방법입니다.

```javascript
setInterval(function() {
  // 주기적으로 실행할 동작
}, 간격시간);
```

예를 들어, 1초마다 현재 시간을 콘솔에 출력하고자 한다면 다음과 같이 코드를 작성할 수 있습니다.

```javascript
setInterval(function() {
  var currentTime = new Date();
  console.log(currentTime);
}, 1000);
```

## 알림 기능 제어하기

setTimeout과 setInterval 함수를 사용하여 알림 기능을 제어할 수 있습니다. 예를 들어, 5초 후에 알림을 표시한 후 1초마다 알림을 업데이트하고자 한다면 다음과 같이 코드를 작성할 수 있습니다.

```javascript
// 알림 표시
setTimeout(function() {
  showNotification();
  
  // 1초마다 알림 업데이트
  setInterval(function() {
    updateNotification();
  }, 1000);
}, 5000);

function showNotification() {
  // 알림을 표시하는 동작
}

function updateNotification() {
  // 알림을 업데이트하는 동작
}
```

위의 코드에서 `showNotification` 함수는 알림을 표시하는 동작을 정의하고, `updateNotification` 함수는 알림을 업데이트하는 동작을 정의합니다. setTimeout 함수를 사용하여 5초 후에 `showNotification` 함수를 실행하고, setInterval 함수를 사용하여 1초마다 `updateNotification` 함수를 주기적으로 실행하도록 설정합니다.

이처럼 자바스크립트의 setTimeout과 setInterval 함수를 사용하여 알림 기능을 제어할 수 있습니다.

## 참고 자료

- [MDN web docs: WindowTimers.setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN web docs: WindowTimers.setInterval()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)