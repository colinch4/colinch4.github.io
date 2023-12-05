---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 종료 시간 설정"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

자바스크립트에서는 `setTimeout`과 `setInterval` 함수를 사용하여 특정 작업을 지정된 시간 이후에 혹은 일정한 간격으로 반복 수행할 수 있습니다. 이 기능을 활용하여 특정 작업을 종료할 시간을 설정할 수 있습니다.

## setTimeout 함수

`setTimeout` 함수는 일정 시간 이후에 한 번만 특정 작업을 수행하도록 예약할 수 있습니다. 아래는 `setTimeout` 함수의 기본 사용법입니다.

```javascript
setTimeout(function() {
  // 실행할 작업
}, 지연시간);
```

위 코드에서 `지연시간`에는 밀리초 단위로 지연할 시간을 입력합니다. 예를 들어, `5000`을 입력하면 5초 후에 작업이 실행됩니다. 작업은 익명 함수 형태로 전달되며, 해당 함수의 내용에는 원하는 작업을 구현하면 됩니다.

## setInterval 함수

`setInterval` 함수는 지정된 시간 간격으로 특정 작업을 반복 수행할 수 있습니다. 아래는 `setInterval` 함수의 기본 사용법입니다.

```javascript
setInterval(function() {
  // 실행할 작업
}, 간격시간);
```

위 코드에서 `간격시간`에는 밀리초 단위로 반복할 시간 간격을 입력합니다. 예를 들어, `1000`을 입력하면 1초마다 작업이 반복됩니다. 마찬가지로 작업은 익명 함수 형태로 전달되며, 해당 함수의 내용에는 원하는 작업을 구현하면 됩니다.

## 종료 시간 설정

`setTimeout`과 `setInterval` 함수는 기본적으로 무한히 작업을 수행하기 때문에 종료 시간을 설정하지 않으면 계속해서 작업이 반복될 수 있습니다. 따라서 특정 조건을 만족했을 때 작업을 종료하도록 설정해야 합니다.

아래는 `setTimeout` 함수를 사용하여 종료 시간을 설정하는 예시입니다.

```javascript
function doSomething() {
  // 작업 수행
  setTimeout(doSomething, 5000); // 5초 후에 다시 작업을 예약
}

// 작업 시작
setTimeout(doSomething, 5000); // 5초 후에 작업 예약
```

위 코드에서 `doSomething` 함수는 작업을 수행하고, `setTimeout` 함수를 사용하여 5초 후에 다시 작업을 예약하도록 설정합니다. 이렇게 설정하면 5초마다 `doSomething` 함수가 반복 실행되며, 필요한 작업을 수행한 뒤에는 특정 조건에 따라 작업을 중지시킬 수 있습니다.

`setInterval` 함수를 사용하여 종료 시간을 설정하려면 조건문을 활용하여 작업을 중지시켜야 합니다.

```javascript
var intervalId = setInterval(function() {
  // 작업 수행
  if (조건) {
    clearInterval(intervalId); // 작업 중지
  }
}, 1000); // 1초마다 작업 실행
```

위 코드에서 `intervalId` 변수는 `setInterval` 함수에 의해 반환되는 작업 식별자입니다. 조건을 만족하면 `clearInterval` 함수를 사용하여 작업을 중지시킵니다.