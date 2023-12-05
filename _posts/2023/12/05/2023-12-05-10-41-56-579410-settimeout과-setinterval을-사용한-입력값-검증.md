---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 입력값 검증"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

웹 개발을 하다보면 사용자의 입력값을 검증해야 하는 상황이 자주 발생합니다. 이때, setTimeout과 setInterval 함수를 사용하면 효과적인 입력값 검증을 구현할 수 있습니다. 이번 블로그 포스트에서는 이러한 사용 예시를 알아보도록 하겠습니다.

## setTimeout 함수를 사용한 입력값 검증

setTimeout 함수는 일정 시간이 지난 후에 특정 작업을 실행할 수 있게 해줍니다. 이를 활용하여 사용자의 입력값을 검증하는 예시를 살펴보겠습니다.

```javascript
function validateInput(input) {
   if (input === '') {
      setTimeout(function() {
         alert('입력값이 비어있습니다!');
      }, 1000);
   } else {
      alert('올바른 입력값입니다!');
   }
}
```

위 예시에서는 사용자의 입력값이 빈 문자열인 경우, 1초 후에 알림창으로 "입력값이 비어있습니다!"라는 메시지가 뜨도록 설정하였습니다. 입력값이 비어있지 않을 경우에는 "올바른 입력값입니다!"라는 메시지가 바로 뜨게 됩니다.

## setInterval 함수를 사용한 입력값 검증

setInterval 함수는 일정 시간 간격으로 특정 작업을 반복해서 실행할 수 있게 해줍니다. 이를 활용하여 주기적으로 사용자의 입력값을 검증하는 예시를 살펴보겠습니다.

```javascript
var intervalID = setInterval(function() {
   var input = document.getElementById('input-text').value;
   
   if (input.length > 10) {
      clearInterval(intervalID);
      alert('입력값은 10자 이하여야 합니다!');
   }
}, 1000);
```

위 예시에서는 매 1초마다 사용자가 입력한 텍스트의 길이를 검사하여, 10자를 초과하는 경우에는 반복 작업을 멈추고 알림창으로 "입력값은 10자 이하여야 합니다!"라는 메시지가 뜨게 됩니다.

## 마무리

setTimeout과 setInterval을 사용하면 사용자의 입력값을 효과적으로 검증할 수 있습니다. setTimeout은 일정 시간 후에 한 번 작업을 실행하고, setInterval은 일정 시간 간격으로 반복 작업을 실행하는 함수입니다. 이를 적절히 활용하여 웹 애플리케이션에서 입력값을 검증하면 사용자 경험을 향상시킬 수 있습니다.

참고 자료:
- [MDN Web Docs - setTimeout](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs - setInterval](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)