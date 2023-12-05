---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 반복 작업 처리"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript에서는 setTimeout과 setInterval 함수를 사용하여 반복 작업을 처리할 수 있습니다. 이러한 함수들은 웹 애플리케이션에서 비동기적인 작업을 처리하기 위해 많이 사용됩니다.

## setTimeout

setTimeout 함수는 일정 시간이 지난 후에 한 번만 작업을 실행하는 함수입니다. 

```javascript
setTimeout(function(){
  // 작업 내용
}, 1000);
```

위의 예제에서는 1초(1000ms) 후에 작업 내용을 실행합니다. setTimeout 함수의 첫 번째 매개변수로는 실행할 작업의 코드를 전달하고, 두 번째 매개변수로는 지연 시간을 밀리초(milliseconds) 단위로 전달합니다. 

## setInterval

setInterval 함수는 일정한 시간 간격으로 작업을 반복하여 실행하는 함수입니다.

```javascript
setInterval(function(){
  // 작업 내용
}, 2000);
```

위의 예제에서는 2초(2000ms) 간격으로 작업 내용을 반복해서 실행합니다. setInterval 함수의 사용 방법은 setTimeout과 유사하지만, 작업을 한 번만 실행하는 것이 아니라 반복 실행됩니다. 마찬가지로 첫 번째 매개변수로는 실행할 작업의 코드를 전달하고, 두 번째 매개변수로는 간격 시간을 밀리초 단위로 전달합니다.

## 작업 중지하기

반복 작업을 중지하기 위해서는 clearInterval 함수를 사용합니다. 

```javascript
var intervalId = setInterval(function(){
  // 작업 내용
}, 2000);

// 5초 후에 작업 중지
setTimeout(function(){
  clearInterval(intervalId);
}, 5000);
```

위의 예제에서는 setInterval로 시작한 작업을 5초 후에 clearInterval로 중지하도록 설정하였습니다. setInterval 함수 호출시 반환되는 값을 변수에 저장하여, 이를 활용하여 작업을 중지할 수 있습니다.

## 결론

JavaScript에서는 setTimeout과 setInterval 함수를 사용하여 일정 시간이 지나고나 일정 시간 간격으로 작업을 반복하여 실행할 수 있습니다. 이를 활용하면 웹 애플리케이션에서 비동기 작업을 처리하는데 유용하게 사용할 수 있습니다.

---

참고

- [setTimeout - MDN Web Docs](https://developer.mozilla.org/ko/docs/Web/API/WindowTimers/setTimeout)
- [setInterval - MDN Web Docs](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)