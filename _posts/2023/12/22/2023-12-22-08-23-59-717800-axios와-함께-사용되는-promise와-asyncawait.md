---
layout: post
title: "[typescript] Axios와 함께 사용되는 Promise와 async/await"
description: " "
date: 2023-12-22
tags: [typescript]
comments: true
share: true
---

Axios는 JavaScript 및 TypeScript에서 가장 인기 있는 HTTP 클라이언트 라이브러리 중 하나입니다. 이 라이브러리를 사용할 때 주로 Promise 및 async/await와 함께 사용됩니다. 이 블로그 포스트에서는 Axios를 사용하는 동안 Promise와 async/await의 동작 방식에 대해 알아보고, 이를 TypeScript에서 어떻게 활용할 수 있는지 살펴보겠습니다.

## Promise와 async/await

### Promise

Promise는 JavaScript 및 TypeScript에서 비동기 코드를 다룰 때 사용되는 빌트인 객체입니다. 이는 비동기 작업이 완료되었을 때 또는 에러가 발생했을 때 값을 반환하는 객체입니다. Promise는 `then` 및 `catch` 메서드를 사용하여 비동기 코드의 성공 또는 실패를 처리합니다.

```typescript
function fetchData() {
  return new Promise((resolve, reject) => {
    // 비동기 작업
    // 성공시 resolve 호출, 실패시 reject 호출
  });
}

fetchData()
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

### async/await

async/await는 Promise를 더욱 쉽게 다룰 수 있도록 하는 문법적인 기능입니다. `async` 키워드를 사용하여 함수를 비동기 함수로 만들고, `await` 키워드를 사용하여 Promise가 settled 될 때까지 기다립니다.

```typescript
async function fetchAndLogData() {
  try {
    const data = await fetchData();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}
```

## Axios와 Promise

Axios는 HTTP 요청에 대한 Promise를 반환합니다. 이를 통해 비동기 HTTP 요청을 보다 쉽게 처리할 수 있습니다.

```typescript
import axios from 'axios';

axios.get('https://api.example.com/data')
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
```

## Axios와 async/await

async/await을 사용하면 Axios를 보다 간단하게 사용할 수 있습니다. 다음은 async/await을 이용하여 Axios를 사용하는 예시입니다.

```typescript
import axios from 'axios';

async function fetchData() {
  try {
    const response = await axios.get('https://api.example.com/data');
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}
```

이렇게 하면 코드가 더 읽기 쉽고 유지보수가 쉬워집니다.

Axios와 Promise, 그리고 async/await을 함께 사용하면 비동기 HTTP 작업을 보다 간편하게 다룰 수 있습니다. TypeScript와 함께 사용하면 타입 안정성과 함께 효율적으로 코드를 작성할 수 있습니다.

이상으로 Promise와 async/await을 활용한 Axios의 사용 방법에 대해 알아보았습니다. 감사합니다!

## References
- [MDN Web Docs: Promise](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [MDN Web Docs: async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [Axios Documentation](https://axios-http.com/docs/intro)