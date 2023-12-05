---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 시간 간격 조절"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---
자바스크립트에서 setTimeout과 setInterval 함수는 웹 애플리케이션에서 비동기적으로 코드를 실행하거나 일정한 시간 간격으로 작업을 반복할 때 유용한 기능입니다. 이번 블로그 포스트에서는 setTimeout과 setInterval을 사용하여 시간 간격을 조절하는 방법에 대해 알아보겠습니다.

## setTimeout
setTimeout 함수는 일정한 시간이 지난 후에 한 번만 실행되는 함수입니다. 아래의 예제 코드를 통해 setTimeout을 사용하는 방법을 확인해봅시다.

```javascript
setTimeout(function() {
  console.log("Hello, world!");
}, 1000); // 1초(1000ms) 후에 실행됩니다.
```

위 코드는 "Hello, world!"라는 문자열을 1초 후에 콘솔에 출력합니다. setTimeout 함수는 첫 번째 인자로 콜백 함수를 받으며, 두 번째 인자로 지연 시간을 milliseconds 단위로 받습니다.

## setInterval
setInterval 함수는 일정한 시간 간격으로 반복해서 실행되는 함수입니다. 아래의 예제 코드를 통해 setInterval을 사용하는 방법을 확인해봅시다.

```javascript
setInterval(function() {
  console.log("Hello, world!");
}, 2000); // 2초(2000ms) 간격으로 실행됩니다.
```

위 코드는 "Hello, world!"라는 문자열을 2초 간격으로 콘솔에 출력합니다. setInterval 함수도 setTimeout과 마찬가지로 첫 번째 인자로 콜백 함수를 받으며, 두 번째 인자로 반복 간격을 milliseconds 단위로 받습니다.

## clearTimeout과 clearInterval
setTimeout나 setInterval 함수를 사용하여 작업을 예약했다면, 필요에 따라 작업을 취소할 수도 있습니다. clearTimeout 함수는 setTimeout 함수로 예약된 작업을 취소하고, clearInterval 함수는 setInterval 함수로 예약된 작업을 취소합니다.

아래의 예제 코드를 통해 clearTimeout과 clearInterval 함수를 사용하는 방법을 확인해봅시다.

```javascript
let timeoutId = setTimeout(function() {
  console.log("This message will not be printed!");
}, 1000);

clearTimeout(timeoutId); // setTimeout 작업을 취소합니다.

let intervalId = setInterval(function() {
  console.log("This message will be printed every 2 seconds!");
}, 2000);

clearInterval(intervalId); // setInterval 작업을 취소합니다.
```

위 코드에서는 setTimeout 함수로 예약된 작업은 clearTimeout 함수를 사용하여 취소하고, setInterval 함수로 예약된 작업은 clearInterval 함수를 사용하여 취소합니다.

## 결론
setTimeout과 setInterval은 자바스크립트에서 시간 간격을 조절하는 데에 유용한 함수입니다. setTimeout은 일정 시간 이후에 작업을 실행하고, setInterval은 일정 시간 간격으로 작업을 반복합니다. clearTimeout과 clearInterval 함수를 사용하여 예약된 작업을 취소하는 것도 가능합니다. 이러한 기능들을 활용하여 웹 애플리케이션에서 비동기적으로 코드를 실행하거나 반복 작업을 수행할 수 있습니다.