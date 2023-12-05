---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 로그인 기능 구현"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

로그인 기능은 대부분 웹 애플리케이션에서 필수적으로 사용되는 기능 중 하나입니다. 이 기능을 JavaScript와 setTimeout, setInterval 함수를 사용하여 구현해보겠습니다.

## 1. setTimeout을 사용한 로그인 기능 구현

먼저, setTimeout 함수를 사용하여 로그인이 성공적으로 이루어지는 시나리오를 구현해보겠습니다. 

```javascript
function loginUser(username, password) {
  // 서버로 로그인 요청을 보냄
  setTimeout(function() {
    if (username === 'admin' && password === 'admin123') {
      console.log('로그인 성공!');
    } else {
      console.log('로그인 실패!');
    }
  }, 2000); // 2초 뒤에 실행되도록 설정
}

// 예시
loginUser('admin', 'admin123');
```

위의 코드에서 setTimeout 함수는 2초 뒤에 콜백 함수를 실행하도록 설정되어 있습니다. 콜백 함수 내에서는 입력된 username과 password가 admin/admin123와 일치하는지 확인하여 로그인 성공 여부를 출력합니다.

## 2. setInterval을 사용한 로그인 기능 구현

이번에는 setInterval 함수를 사용하여 일정 시간 간격으로 로그인을 시도하는 시나리오를 구현해보겠습니다.

```javascript
let loginAttempts = 0;
let maxAttempts = 5;
let loginInterval;

function loginUser(username, password) {
  // 일정 시간 간격으로 로그인을 시도하는 함수
  loginInterval = setInterval(function() {
    if (loginAttempts >= maxAttempts) {
      clearInterval(loginInterval);
      console.log('로그인 시도 횟수 초과!');
      return;
    }

    loginAttempts++;
    if (username === 'admin' && password === 'admin123') {
      clearInterval(loginInterval);
      console.log('로그인 성공!');
    } else {
      console.log('로그인 실패!');
    }
  }, 1000); // 1초에 한 번씩 실행되도록 설정
}

// 예시
loginUser('admin', 'admin123');
```

위의 코드에서 setInterval 함수는 1초마다 콜백 함수를 실행하도록 설정되어 있습니다. 콜백 함수 내에서는 일정 횟수(maxAttempts)만큼 로그인을 시도하고, 로그인이 성공하면 clearInterval 함수를 사용하여 로그인 시도를 중지합니다.

## 참고 자료

- [setTimeout - JavaScript | MDN](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [setInterval - JavaScript | MDN](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)