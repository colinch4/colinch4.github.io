---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 화면 갱신"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript에서 화면을 일정 시간마다 갱신하고 싶을 때, setTimeout과 setInterval 함수를 사용할 수 있습니다. 이 두 가지 함수는 자바스크립트 코드를 일정 시간 간격으로 실행하는 데 사용됩니다.

### setTimeout 함수

setTimeout 함수는 일정 시간이 지난 후에 한 번만 코드를 실행합니다. 다음은 setTimeout 함수의 사용 방법입니다.

```javascript
setTimeout(function() {
    // 실행할 코드 작성
}, 대기 시간);
```

위의 예제에서 `대기 시간`은 밀리초 단위로 지정합니다. 예를 들어, 1000 밀리초는 1초를 의미합니다. 따라서 `대기 시간`으로 1000을 전달하면, 1초 후에 코드가 실행됩니다.

### setInterval 함수

setInterval 함수는 일정 시간 간격으로 주기적으로 코드를 실행합니다. 다음은 setInterval 함수의 사용 방법입니다.

```javascript
setInterval(function() {
    // 실행할 코드 작성
}, 간격 시간);
```

위의 예제에서 `간격 시간`은 밀리초 단위로 지정합니다. 예를 들어, 1000 밀리초는 1초를 의미합니다. 따라서 `간격 시간`으로 1000을 전달하면, 1초마다 코드가 실행됩니다.

### 주의 사항

화면을 갱신하는 데 자주 사용되는 setTimeout과 setInterval 함수이지만, 너무 자주 사용하면 성능 문제가 발생할 수 있습니다. 화면 갱신이 필요한 경우에만 사용하고, 주기적으로 실행되는 코드가 필요하지 않을 때는 반드시 clearInterval 함수를 사용하여 간격을 정지시켜야 합니다.

```javascript
var intervalId = setInterval(function() {
    // 실행할 코드 작성
}, 간격 시간);

// 일정 시간 후에 setInterval 정지
setTimeout(function() {
    clearInterval(intervalId);
}, 대기 시간);
```

위의 예제에서 `intervalId`는 setInterval 함수가 반환하는 식별자로, clearInterval 함수를 호출하여 주기적으로 실행되는 코드를 정지시킬 수 있습니다.

### 결론

JavaScript에서 화면을 갱신할 때 setTimeout과 setInterval 함수를 사용하면 편리하게 코드를 작성할 수 있습니다. 하지만, 성능 측면을 고려하여 적절한 주기와 실행 횟수를 설정하여야 합니다.

---

**참고 자료**
- [MDN setTimeout](https://developer.mozilla.org/ko/docs/Web/API/WindowTimers/setTimeout)
- [MDN setInterval](https://developer.mozilla.org/ko/docs/Web/API/WindowTimers/setInterval)