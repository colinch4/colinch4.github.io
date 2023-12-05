---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 데이터 갱신"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript에서 데이터를 주기적으로 갱신할 때 `setTimeout`과 `setInterval` 함수를 사용할 수 있습니다. 이들 함수를 사용하면 일정한 간격으로 함수를 실행하거나 일정한 시간이 지난 후에 함수를 실행할 수 있습니다. 이를 활용하여 웹 애플리케이션이나 웹사이트에서 실시간으로 데이터를 업데이트할 수 있습니다.

### setTimeout 함수

`setTimeout` 함수는 지정된 시간이 경과된 후에 한 번만 함수를 실행합니다. 아래는 `setTimeout` 함수를 사용하여 1초 후에 `updateData` 함수를 실행하는 예제입니다.

```javascript
setTimeout(updateData, 1000);

function updateData() {
  // 데이터 갱신 로직
}
```

위의 코드에서 `setTimeout` 함수의 첫 번째 인자로 실행할 함수인 `updateData` 함수를 전달하고, 두 번째 인자로 갱신 간격인 1000밀리초(1초)를 전달합니다. 따라서 1초 후에 `updateData` 함수가 실행됩니다.

### setInterval 함수

`setInterval` 함수는 지정된 간격마다 함수를 반복적으로 실행합니다. 아래는 `setInterval` 함수를 사용하여 5초마다 `updateData` 함수를 실행하는 예제입니다.

```javascript
setInterval(updateData, 5000);

function updateData() {
  // 데이터 갱신 로직
}
```

위의 코드에서 `setInterval` 함수의 첫 번째 인자로 실행할 함수인 `updateData` 함수를 전달하고, 두 번째 인자로 갱신 간격인 5000밀리초(5초)를 전달합니다. 따라서 5초마다 `updateData` 함수가 반복해서 실행됩니다.

### clearInterval 함수

`setInterval` 함수로 실행한 반복 작업을 중지하려면 `clearInterval` 함수를 사용할 수 있습니다. `clearInterval` 함수는 `setInterval` 함수가 반환한 값을 인자로 전달하여 호출하면 됩니다. 아래는 `setInterval` 함수로 실행한 작업을 중지하는 예제입니다.

```javascript
var intervalId = setInterval(updateData, 5000);

// 일정 시간 후에 작업 중지
setTimeout(stopUpdate, 30000);

function updateData() {
  // 데이터 갱신 로직
}

function stopUpdate() {
  clearInterval(intervalId);
}
```

위의 코드에서 `setInterval` 함수가 반환한 값을 변수 `intervalId`에 저장하여 `clearInterval` 함수로 사용합니다. `setTimeout` 함수를 사용하여 30초 후에 `stopUpdate` 함수를 호출하도록 설정하였습니다. 따라서 30초 후에 작업이 중지됩니다.

### 요약

`setTimeout`과 `setInterval` 함수는 JavaScript에서 데이터 갱신을 위해 유용하게 사용될 수 있는 함수입니다. `setTimeout` 함수는 한 번만 함수를 실행하고, `setInterval` 함수는 일정한 간격으로 반복적으로 함수를 실행합니다. `clearInterval` 함수로 `setInterval` 함수로 실행한 작업을 중지할 수 있습니다.

더 자세한 내용은 [MDN setTimeout 문서](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)와 [MDN setInterval 문서](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)를 참고하세요.