---
layout: post
title: "[typescript] XMLHttpRequest 객체를 사용한 REST API 호출"
description: " "
date: 2023-12-12
tags: [typescript]
comments: true
share: true
---

웹 애플리케이션에서 서버 측 리소스에 데이터를 요청하거나 변경하기 위해 [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) (XHR) 객체를 사용할 수 있습니다. 이 기술은 RESTful API와 함께 사용되어 서버와 통신하는 데 자주 활용됩니다. 

이 포스트에서는 TypeScript를 사용하여 XMLHttpRequest 객체를 통해 RESTful API를 호출하는 방법을 살펴보겠습니다.

## XMLHttpRequest로 GET 요청 보내기

XMLHttpRequest 객체를 사용하여 서버로 GET 요청을 보내는 방법을 먼저 알아보겠습니다. 아래는 TypeScript 코드 예시입니다.

```typescript
function fetchData(url: string, callback: (data: any) => void) {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.onload = function () {
    if (xhr.status >= 200 && xhr.status < 300) {
      callback(JSON.parse(xhr.responseText));
    } else {
      // 오류 처리
    }
  };
  xhr.send();
}
```

위의 코드에서는 `fetchData`라는 함수를 정의하여 서버로 GET 요청을 보내고, 서버로부터 받은 데이터를 콜백 함수를 통해 처리하고 있습니다. 

## XMLHttpRequest로 POST 요청 보내기

이제 POST 요청을 보내는 방법을 살펴보겠습니다.

```typescript
function postData(url: string, data: any, callback: (response: any) => void) {
  const xhr = new XMLHttpRequest();
  xhr.open('POST', url, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function () {
    if (xhr.status >= 200 && xhr.status < 300) {
      callback(JSON.parse(xhr.responseText));
    } else {
      // 오류 처리
    }
  };
  xhr.send(JSON.stringify(data));
}
```

위의 코드에서는 `postData` 함수를 통해 서버로 POST 요청을 보내고 있으며, 데이터를 JSON 문자열로 변환하여 전송하고 있습니다.

## 요약

이상으로 XMLHttpRequest 객체를 사용하여 TypeScript에서 RESTful API를 호출하는 방법을 알아봤습니다. 이를 통해 웹 애플리케이션에서 서버와 데이터를 주고받는 기술을 익힐 수 있습니다.

더 많은 정보를 찾으려면 [MDN web docs](https://developer.mozilla.org/ko/docs/Web/API/XMLHttpRequest)를 참조하세요.