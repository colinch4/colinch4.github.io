---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 웹 페이지 개발"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

웹 개발에서 시간 지연이 필요한 경우, JavaScript에서 setTimeout과 setInterval 함수를 사용할 수 있습니다. 이 두 함수는 특정 코드 또는 함수를 일정 시간 간격으로 실행하는 용도로 사용됩니다. 이번 블로그 포스트에서는 setTimeout과 setInterval 함수의 사용법과 예제를 살펴보겠습니다.

## setTimeout

setTimeout 함수는 특정 시간이 지난 후에 코드를 실행할 때 사용됩니다. setTimeout 함수는 다음과 같은 문법으로 사용됩니다:

```javascript
setTimeout(function, delay);
```

- `function`: 실행할 코드 또는 함수를 작성합니다.
- `delay`: 코드를 실행하기 전에 기다릴 시간을 밀리초 단위로 지정합니다.

예를 들어, 아래의 코드는 3초 후에 "Hello, World!"를 출력합니다:

```javascript
setTimeout(function() {
    console.log("Hello, World!");
}, 3000);
```

## setInterval

setInterval 함수는 일정 시간 간격으로 코드를 반복적으로 실행할 때 사용됩니다. setInterval 함수는 다음과 같은 문법으로 사용됩니다:

```javascript
setInterval(function, delay);
```

- `function`: 실행할 코드 또는 함수를 작성합니다.
- `delay`: 코드를 실행하는 간격을 밀리초 단위로 지정합니다.

아래의 예제는 1초 간격으로 현재 시간을 출력합니다:

```javascript
setInterval(function() {
    var date = new Date();
    console.log("Current time: " + date.toLocaleTimeString());
}, 1000);
```

## 주의사항

setTimeout과 setInterval 함수는 무한 반복이 가능하기 때문에 코드를 작성할 때 주의해야 합니다. 지나치게 짧은 간격으로 반복되는 경우 성능 문제를 일으킬 수 있습니다. 따라서 적절한 간격을 설정하여 사용해야 합니다.

## 결론

setTimeout과 setInterval 함수를 사용하면 웹 페이지에서 시간 지연을 만들고, 코드를 일정 시간 간격으로 반복 실행할 수 있습니다. 이를 활용하여 다양한 기능을 개발할 수 있으며, 적절한 간격을 설정하여 성능을 최적화하는 것이 중요합니다.

관련 참고 문서:
- [MDN Web Docs - setTimeout](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs - setInterval](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)