---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 검색 기능 개선"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

때로는 웹 애플리케이션에서 사용자가 검색을 할 때 실시간으로 결과를 표시해 주는 기능이 필요합니다. 이러한 기능을 구현하는데 있어서 setTimeout과 setInterval 함수를 활용할 수 있습니다. 이번 글에서는 이 두 함수를 사용하여 검색 기능을 개선하는 방법에 대해 알아보겠습니다.

## setTimeout 함수
`setTimeout` 함수는 주어진 시간이 지난 후에 한 번만 특정 코드를 실행합니다. 이 함수는 첫 번째 매개변수로 실행할 코드를 받고, 두 번째 매개변수로 지연 시간(밀리초)을 받습니다.

예를 들어, 사용자가 키보드로 검색어를 입력할 때마다 새로운 검색 요청을 보내지 않고, 사용자가 검색어를 입력하는 동안 일정 시간 동안 동작하지 않은 후에 검색 요청을 보내고 싶다고 해봅시다. 이런 경우에 setTimeout 함수를 사용할 수 있습니다.

```javascript
let timeoutId;

function handleSearchInput(event) {
  clearTimeout(timeoutId);
  
  timeoutId = setTimeout(() => {
    // 검색 요청 코드 작성
  }, 500); // 500ms 동안 입력이 멈춰야만 검색 요청을 보냄
}
```

위 코드에서는 `handleSearchInput` 함수가 호출될 때마다 이전에 등록한 `setTimeout`을 취소하고, 500ms 동안 입력이 멈춰야만 새로운 검색 요청을 보냅니다.

## setInterval 함수
`setInterval` 함수는 주어진 시간 간격마다 반복해서 특정 코드를 실행합니다. 이 함수는 첫 번째 매개변수로 실행할 코드를 받고, 두 번째 매개변수로 시간 간격(밀리초)을 받습니다.

검색 결과를 실시간으로 업데이트하기 위해 사용자가 검색어를 입력할 때마다 주기적으로 검색 요청을 보내고 싶다면, setInterval 함수를 활용할 수 있습니다.

```javascript
let intervalId;

function startRealtimeSearch() {
  intervalId = setInterval(() => {
    // 검색 요청 코드 작성
  }, 1000); // 1초마다 검색 요청을 보냄
}

function stopRealtimeSearch() {
  clearInterval(intervalId);
}
```

위 코드에서는 `startRealtimeSearch` 함수가 호출되면 1초마다 검색 요청을 보내고, `stopRealtimeSearch` 함수가 호출되면 검색 요청을 멈춥니다.

## 결론
setTimeout과 setInterval 함수를 사용하면 검색 기능을 개선할 수 있습니다. setTimeout을 사용하면 사용자가 일정 시간 동안 입력을 멈추었을 때에만 검색 요청을 보내고, setInterval을 사용하면 일정 시간 간격으로 검색 요청을 반복적으로 보낼 수 있습니다. 이를 활용하여 웹 애플리케이션의 검색 기능을 더욱 효율적으로 개선할 수 있습니다.

---

참고 자료:
- [MDN Web Docs - setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs - setInterval](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)