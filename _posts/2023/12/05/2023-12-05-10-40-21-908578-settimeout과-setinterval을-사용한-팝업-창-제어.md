---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 팝업 창 제어"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

자바스크립트에서는 `setTimeout`과 `setInterval` 함수를 사용하여 팝업 창을 제어할 수 있습니다. 이 두 가지 함수는 특정 시간이 지난 후에 특정한 동작을 수행하거나, 일정한 간격으로 반복적인 동작을 수행할 수 있도록 해줍니다.

### setTimeout 함수

`setTimeout` 함수는 일정한 시간이 지난 후에 한 번만 동작하는 기능을 제공합니다. 함수의 첫 번째 인자로는 실행할 함수나 실행할 코드 블록을 전달하고, 두 번째 인자로는 실행을 지연할 시간(밀리초 단위)을 전달합니다. 예를 들어, 2초 후에 팝업 창을 띄우는 코드를 작성해보겠습니다.

```javascript
setTimeout(function() {
  // 팝업 창을 띄우는 코드
  alert('팝업 창이 나타납니다.');
}, 2000);
```

### setInterval 함수

`setInterval` 함수는 일정한 간격으로 동작을 반복하는 기능을 제공합니다. `setTimeout`과 마찬가지로 함수의 첫 번째 인자로는 실행할 함수나 실행할 코드 블록을 전달하고, 두 번째 인자로는 반복 간격(밀리초 단위)을 전달합니다. 예를 들어, 3초마다 팝업 창을 띄우는 코드를 작성해보겠습니다.

```javascript
setInterval(function() {
  // 팝업 창을 띄우는 코드
  alert('팝업 창이 나타납니다.');
}, 3000);
```

### 팝업 창을 제어하는 활용 예시

`setTimeout`과 `setInterval` 함수를 활용하여 팝업 창을 제어하는 다양한 상황들을 구현할 수 있습니다. 예를 들어, 특정 조건이 충족되었을 때 팝업 창을 띄우거나, 사용자의 동작에 따라 팝업 창을 업데이트하는 등의 기능을 구현할 수 있습니다.

```javascript
var timeoutId = setTimeout(function() {
  // 조건이 충족되었을 때 팝업 창을 띄우는 코드
  alert('팝업 창이 나타납니다.');
}, 2000);

// 사용자가 버튼을 클릭하면 팝업 창을 취소하는 예시
var cancelButton = document.getElementById('cancel-button');
cancelButton.addEventListener('click', function() {
  clearTimeout(timeoutId);
});
```

### 결론

`setTimeout`과 `setInterval` 함수를 사용하면 자바스크립트에서 간편하게 팝업 창을 제어할 수 있습니다. 이를 활용하여 다양한 시나리오에서 팝업 창을 사용하고, 필요에 따라 적절하게 제어해보세요.

---

### 참고 자료

- [MDN Web Docs: setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs: setInterval](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)