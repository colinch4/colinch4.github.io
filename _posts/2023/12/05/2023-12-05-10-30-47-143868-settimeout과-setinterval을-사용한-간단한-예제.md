---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 간단한 예제"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

이번 포스트에서는 JavaScript의 `setTimeout`과 `setInterval` 함수를 사용하여 간단한 예제를 작성해보겠습니다. 이러한 함수들은 특정 시간 후에 코드를 실행하거나 반복적으로 코드를 실행하는 데 유용하게 사용됩니다.

## setTimeout 예제

`setTimeout` 함수는 일정 시간 후에 코드를 한 번 실행하는 함수입니다. 아래의 예제는 3초 후에 "Hello, world!"라는 메시지를 출력하는 예제입니다.

```javascript
setTimeout(() => {
  console.log("Hello, world!");
}, 3000);
```

위의 코드에서 `setTimeout` 함수는 첫 번째 인자로 콜백 함수를 받습니다. 콜백 함수는 지연된 시간 이후에 실행될 코드를 포함하고 있습니다. 두 번째 인자로는 시간을 밀리초 단위로 전달합니다. 위의 예제에서는 3000밀리초로 설정되어 있으므로 3초 후에 콜백 함수가 실행됩니다.

## setInterval 예제

`setInterval` 함수는 일정한 간격으로 코드를 반복적으로 실행하는 함수입니다. 아래의 예제는 1초마다 "Hello, world!"라는 메시지를 출력하는 예제입니다.

```javascript
setInterval(() => {
  console.log("Hello, world!");
}, 1000);
```

위의 코드에서 `setInterval` 함수도 첫 번째 인자로 콜백 함수를 받습니다. 이 콜백 함수는 설정한 간격마다 실행될 것입니다. 두 번째 인자로는 반복 간격을 밀리초 단위로 전달합니다. 위의 예제에서는 1000밀리초로 설정되어 있으므로 1초마다 콜백 함수가 실행됩니다.

## 정리

이 포스트에서는 JavaScript의 `setTimeout`과 `setInterval` 함수를 사용하여 간단한 예제를 작성하였습니다. `setTimeout` 함수는 일정 시간 후에 코드를 실행하는데 사용되고, `setInterval` 함수는 일정한 간격으로 코드를 반복적으로 실행하는데 사용됩니다. 이러한 함수들은 웹 애플리케이션 개발 등 다양한 상황에서 유용하게 사용될 수 있습니다.

### 참고 자료

- [MDN Web Docs - WindowOrWorkerGlobalScope.setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs - WindowOrWorkerGlobalScope.setInterval()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)