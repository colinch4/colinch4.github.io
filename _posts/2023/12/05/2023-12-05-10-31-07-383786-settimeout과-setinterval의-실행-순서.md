---
layout: post
title: "[javascript] setTimeout과 setInterval의 실행 순서"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript에서 비동기적인 작업을 처리하기 위해 주로 사용되는 함수로 setTimeout과 setInterval이 있습니다. 이 두 가지 함수는 특정 작업을 지연시키거나 반복적으로 실행시킬 수 있습니다. 그러나 이 두 함수의 실행 순서를 이해하는 것은 중요합니다. 

## setTimeout

setTimeout 함수는 일정 시간이 지난 후에 한 번만 작업을 실행합니다. 예를 들어, 다음과 같이 setTimeout을 사용하여 3초 후에 "Hello, World!"를 출력하는 작업을 처리할 수 있습니다.

```javascript
setTimeout(function() {
    console.log("Hello, World!");
}, 3000);
```

위의 코드는 3초 후에 "Hello, World!"를 출력하게 됩니다. setTimeout은 단 한 번 작업을 실행하고 종료됩니다.

## setInterval

setInterval 함수는 일정 시간 간격으로 작업을 반복적으로 실행합니다. 예를 들어, 다음과 같이 setInterval을 사용하여 1초마다 현재 시간을 출력하는 작업을 처리할 수 있습니다.

```javascript
setInterval(function() {
    console.log(new Date());
}, 1000);
```

위의 코드는 1초마다 현재 시간을 출력하게 됩니다. setInterval은 지정된 시간 간격으로 작업을 반복적으로 실행합니다.

## 실행 순서

setTimeout과 setInterval은 비동기적으로 동작하기 때문에 다른 작업과 동시에 실행될 수 있습니다. 그러므로 setTimeout과 setInterval이 실행되는 동안에도 다른 코드가 실행될 수 있습니다.

만약 setTimeout이나 setInterval 작업이 실행 중인데 다른 코드를 실행하고 싶지 않다면, 콜백 함수에서 추가적인 조건을 확인하여 중지할 수 있습니다. clearTimeout와 clearInterval 함수를 사용하여 작업을 중지할 수 있습니다.

아래는 setTimeout과 setInterval의 실행 순서를 이해하기 위한 예제 코드입니다.

```javascript
console.log("Start");
setTimeout(function() {
    console.log("Timeout");
}, 0);
setInterval(function() {
    console.log("Interval");
}, 1000);
console.log("End");
```

위의 코드를 실행하면 "Start"와 "End"가 먼저 출력되고, 그 후 "Timeout"이 출력될 것입니다. 그리고 1초마다 "Interval"이 반복적으로 출력될 것입니다. 

결론적으로, setTimeout은 일정 시간이 지난 후에 한 번만 작업을 실행하고 종료되지만, setInterval은 일정 시간 간격으로 반복적으로 작업을 실행합니다. 이 두 함수는 비동기적으로 동작하므로, 다른 코드와 동시에 실행될 수 있다는 점을 명심해야 합니다.