---
layout: post
title: "자바스크립트에서 Nullish Coalescing을 활용한 HTTP 요청 처리 방법"
description: " "
date: 2023-09-29
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 HTTP 요청을 처리하기 위해서는 종종 null 또는 undefined인 경우에 대한 처리가 필요합니다. 이러한 경우에 Nullish Coalescing 연산자를 활용하면 효과적으로 처리할 수 있습니다. Nullish Coalescing 연산자는 좌항의 값이 null 또는 undefined인 경우에 우항의 값으로 대체하는 연산자입니다.

아래는 Nullish Coalescing 연산자를 활용한 HTTP 요청 처리의 예시 코드입니다. 이 코드는 브라우저 환경에서 Fetch API를 사용하여 GET 요청을 보내는 예시입니다.

```javascript
const fetchUserData = async () => {
  const response = await fetch('https://api.example.com/user');

  // HTTP 상태 코드가 200인 경우에만 데이터를 처리합니다.
  if (response.status === 200) {
    const userData = await response.json();
    // userData가 null 또는 undefined인 경우에 'Unknown User'를 사용합니다.
    const userName = userData.name ?? 'Unknown User';
    console.log(`User name: ${userName}`);
  } else {
    console.error('Failed to fetch user data');
  }
};

fetchUserData();
```

위의 코드에서는 fetch를 사용하여 'https://api.example.com/user' 엔드포인트로 GET 요청을 보내고, 응답으로 받은 데이터를 처리합니다. userData 객체의 name 속성이 null 또는 undefined인 경우에는 'Unknown User' 문자열을 사용합니다.

위의 예시 코드에서는 Nullish Coalescing 연산자를 사용하여 간단하게 null 또는 undefined인 경우의 처리를 처리합니다. 이를 통해 코드의 가독성을 높이고, 조건문을 사용한 추가적인 처리를 줄일 수 있습니다.

#javascript #nullishcoalescing