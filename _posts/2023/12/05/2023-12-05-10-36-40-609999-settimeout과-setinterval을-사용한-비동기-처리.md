---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 비동기 처리"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript에서 비동기 처리를 할 때 setTimeout과 setInterval 함수를 사용할 수 있습니다. 이들 함수는 일정 시간이 지난 후에 주어진 콜백 함수를 실행하거나, 일정 시간 간격으로 반복적인 작업을 수행할 수 있도록 도와줍니다.

## setTimeout

setTimeout 함수는 일정 시간이 지난 후에 한 번만 콜백 함수를 실행합니다. 아래는 setTimeout을 사용한 간단한 예제입니다.

```javascript
setTimeout(function() {
   console.log('3초가 지났습니다.');
}, 3000);
```

위 예제에서는 3초 후에 콜백 함수가 실행되어 '3초가 지났습니다'라는 메시지를 출력합니다.

## setInterval

setInterval 함수는 주어진 시간 간격으로 콜백 함수를 반복 실행합니다. 아래는 setInterval을 사용한 예제입니다.

```javascript
var count = 0;

var intervalId = setInterval(function() {
   count++;
   console.log(count + '초가 지났습니다.');

   if (count === 5) {
       clearInterval(intervalId); // 5초가 지나면 clearInterval을 사용하여 반복을 중지합니다.
   }
}, 1000);
```

위 예제에서는 1초마다 count 변수를 증가시키고 해당 값을 출력합니다. count 변수가 5가 되면 setInterval을 중지하기 위해 clearInterval 함수를 호출합니다.

## 주의사항

setTimeout과 setInterval 함수는 비동기 처리를 위해 사용되지만, 콜백 함수의 실행 시점은 보장되지 않습니다. 따라서 정확한 시간 간격이 필요한 경우에는 더 정확한 타이머 함수를 고려해보는 것이 좋습니다.

## 참고자료

- [MDN Web Docs - WindowOrWorkerGlobalScope.setTimeout()](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs - WindowOrWorkerGlobalScope.setInterval()](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)