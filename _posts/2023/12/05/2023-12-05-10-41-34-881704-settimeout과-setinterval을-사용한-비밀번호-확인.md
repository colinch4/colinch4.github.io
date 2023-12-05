---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 비밀번호 확인"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

비밀번호 확인은 웹 개발에서 매우 중요한 부분입니다. 이번에는 자바스크립트의 `setTimeout`과 `setInterval`을 사용하여 비밀번호 확인을 구현하는 방법에 대해 알아보겠습니다.

## 1. setTimeout을 사용한 비밀번호 확인

```javascript
function checkPassword(password) {
  setTimeout(function() {
    // 비밀번호 확인 로직 작성
    if (password === "1234") {
      console.log("비밀번호가 일치합니다.");
    } else {
      console.log("비밀번호가 일치하지 않습니다.");
    }
  }, 2000); // 비밀번호 확인까지 2초 후 실행
}

checkPassword("1234");
console.log("비밀번호 확인 중...");
```

위의 예시 코드에서는 `checkPassword` 함수 내에 `setTimeout`을 사용하여 2초 후에 비밀번호 확인 로직을 실행하고 있습니다. 이를 통해 비밀번호가 맞는지 확인할 수 있습니다. `setTimeout`은 일정 시간이 지난 후에 콜백 함수를 실행하도록 설정하는 역할을 합니다.

## 2. setInterval을 사용한 비밀번호 확인

```javascript
let intervalID;

function startCheckingPassword(password) {
  intervalID = setInterval(function() {
    // 비밀번호 확인 로직 작성
    if (password === "1234") {
      console.log("비밀번호가 일치합니다.");
      clearInterval(intervalID); // 비밀번호가 일치하면 setInterval 종료
    } else {
      console.log("비밀번호가 일치하지 않습니다.");
    }
  }, 1000); // 1초마다 비밀번호 확인
}

startCheckingPassword("1234");
console.log("비밀번호 확인 중...");
```

위의 예시 코드에서는 `startCheckingPassword` 함수 내에 `setInterval`을 사용하여 1초마다 비밀번호 확인 로직을 실행하고 있습니다. `setInterval`은 일정 시간 간격으로 콜백 함수를 반복적으로 실행하도록 설정하는 역할을 합니다. 비밀번호가 맞을 경우 `clearInterval`을 사용하여 `setInterval`을 종료합니다.

## 마무리

위의 예시 코드들을 사용하여 비밀번호 확인을 구현할 수 있습니다. `setTimeout`과 `setInterval`은 다양한 상황에서 유용하게 사용될 수 있는 자바스크립트의 함수입니다. 비밀번호 확인 외에도 일정 시간 후에 실행해야 하는 다양한 작업에 적용할 수 있습니다.

- 참고 링크: [setTimeout - JavaScript | MDN](https://developer.mozilla.org/ko/docs/Web/API/Window/setTimeout), [setInterval - JavaScript | MDN](https://developer.mozilla.org/ko/docs/Web/API/Window/setInterval)