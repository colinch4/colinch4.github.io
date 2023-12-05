---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 게임 개발"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript를 사용하여 게임을 개발할 때, 시간에 따라 반복되는 작업을 처리해야 할 때가 많습니다. 이런 경우 setTimeout과 setInterval 함수를 사용하여 원하는 동작을 수행할 수 있습니다. 이번 블로그에서는 setTimeout과 setInterval을 사용하여 간단한 게임을 만드는 방법에 대해 알아보도록 하겠습니다.

## 1. setTimeout 함수

setTimeout 함수는 일정 시간이 지난 후에 한 번만 특정 동작을 수행합니다. 다음은 setTimeout 함수의 기본적인 사용 방법입니다.

```javascript
setTimeout(function() {
  // 원하는 동작 수행
}, 1000); // 1초 후에 동작 수행
```

위의 예제에서는 1초 후에 주어진 함수를 실행합니다. 이렇게 setTimeout 함수를 사용하면 게임에서 일정 지연 시간 후에 특정 이벤트가 발생하도록 할 수 있습니다.

## 2. setInterval 함수

setInterval 함수는 일정 시간마다 반복적으로 특정 동작을 수행합니다. 다음은 setInterval 함수의 기본적인 사용 방법입니다.

```javascript
setInterval(function() {
  // 원하는 동작 수행
}, 1000); // 1초마다 동작 수행
```

위의 예제에서는 1초마다 주어진 함수를 실행합니다. 이를 이용하면 게임에서 주기적으로 발생하는 동작이나 업데이트를 처리할 수 있습니다.

## 3. setTimeout과 setInterval을 활용한 게임 예제

이제 setTimeout과 setInterval을 사용하여 간단한 게임을 만들어보겠습니다.

```javascript
let score = 0;

// 게임 시작
function startGame() {
  // 1초마다 점수를 1씩 증가
  setInterval(function() {
    score += 1;
    console.log("Score:", score);
  }, 1000);

  // 10초 후에 게임 종료
  setTimeout(function() {
    console.log("Game Over");
    clearInterval(interval);
  }, 10000);
}

// 게임 시작
startGame();
```

위의 예제는 1초마다 점수를 1씩 증가시키고, 10초 후에 게임을 종료하는 간단한 게임입니다. setTimeout 함수를 사용하여 게임이 종료되면 setInterval을 멈추도록 구현하였습니다.

## 결론

JavaScript에서 setTimeout과 setInterval 함수를 사용하여 게임을 개발할 때, 시간에 따라 반복되는 작업을 처리할 수 있습니다. setTimeout을 사용하여 일정 시간 후에 동작을 수행하거나, setInterval을 사용하여 주기적으로 동작을 수행하는 등 다양한 방식으로 게임을 제어할 수 있습니다.