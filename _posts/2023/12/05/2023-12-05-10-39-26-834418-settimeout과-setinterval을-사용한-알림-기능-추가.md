---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 알림 기능 추가"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

알림 기능은 웹 애플리케이션에서 중요한 부분입니다. 사용자에게 메시지, 경고 또는 알림을 표시하여 상호작용을 유도하거나 정보를 전달할 수 있습니다. 이러한 알림 기능을 구현하기 위해 자바스크립트의 setTimeout과 setInterval을 사용할 수 있습니다.

## setTimeout

setTimeout 함수는 일정 시간이 지난 후에 특정 코드를 실행합니다. 형식은 다음과 같습니다:

```javascript
setTimeout(callback, delay);
```

- callback: 지정한 지연 시간(delay) 후에 실행할 함수
- delay: 지연 시간 (밀리초 단위)

예를 들어, 5초 후에 알림을 표시하고 싶다면 다음과 같은 코드를 작성할 수 있습니다:

```javascript
setTimeout(function() {
  alert("알림 메시지");
}, 5000);
```

위 코드는 5초 후에 "알림 메시지"를 경고창으로 표시합니다.

## setInterval

setInterval 함수는 일정한 간격으로 특정 코드를 반복적으로 실행합니다. 형식은 다음과 같습니다:

```javascript
setInterval(callback, interval);
```

- callback: 주기적으로 실행할 함수
- interval: 실행 간격 (밀리초 단위)

예를 들어, 1초마다 현재 시간을 표시하는 알림 기능을 구현하고 싶다면 다음과 같은 코드를 작성할 수 있습니다:

```javascript
setInterval(function() {
  var currentTime = new Date().toLocaleTimeString();
  console.log(currentTime);
}, 1000);
```

위 코드는 1초마다 현재 시간을 콘솔에 출력합니다.

## 주의사항

setTimeout과 setInterval 함수는 사용할 때 주의해야 합니다. 계속해서 코드를 실행하므로, 메모리 누수와 성능 문제를 일으킬 수 있습니다. 따라서, 알림 기능을 구현할 때에는 적절한 시간 간격을 설정하고, 필요한 경우 코드를 중지하는 로직을 추가하는 것이 중요합니다.

## 결론

자바스크립트에서 setTimeout과 setInterval을 사용하여 알림 기능을 구현할 수 있습니다. setTimeout은 일정 시간이 지난 후에 코드를 실행하고, setInterval은 주기적으로 코드를 반복 실행합니다. 이러한 함수를 적절하게 활용하여 사용자에게 알림을 표시할 수 있습니다.