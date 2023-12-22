---
layout: post
title: "[javascript] 자바스크립트의 비동기 처리 방법: 콜백(callback), 프로미스(Promise), async/await"
description: " "
date: 2023-12-22
tags: [javascript]
comments: true
share: true
---

콜백(callback), 프로미스(Promise), async/await은 자바스크립트에서 비동기 처리를 다룰 때 사용되는 주요한 방법들이다. 

## 콜백(callback)
콜백은 가장 기본적인 비동기 처리 방법으로, 함수 A를 실행한 후에 함수 B를 실행하도록 지정하는 방식이다. 
```javascript
function fetchData(callback) {
  setTimeout(() => {
    callback('Data received');
  }, 1000);
}

function displayData(data) {
  console.log(data);
}

fetchData(displayData);
```

콜백 지옥(callback hell)이 발생할 수 있어서 여러 개의 중첩 콜백 함수를 사용할 경우 코드를 관리하기 어려울 수 있다.

## 프로미스(Promise)
프로미스는 ES6에서 도입된 콜백 지옥을 해결하기 위한 개념이다. 프로미스는 비동기 작업이 성공 또는 실패 시에 대한 결과를 나타내는 객체이다. 

```javascript
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Data received');
    }, 1000);
  });
}

fetchData()
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error(error);
  });
```

프로미스는 then(), catch() 메소드를 사용하여 성공 또는 실패 시에 각각의 처리를 할 수 있다.

## async/await
async/await는 ES8에서 도입된 문법으로, 프로미스를 더 쉽게 다룰 수 있도록 도와준다. 

```javascript
async function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Data received');
    }, 1000);
  });
}

async function displayData() {
  try {
    const data = await fetchData();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

displayData();
```

async 키워드는 함수가 항상 프로미스를 반환함을 나타내고, await는 프로미스가 처리될 때까지 기다렸다가 결과를 받는다.

## 요약
콜백(callback), 프로미스(Promise), async/await은 모두 비동기 처리를 다루는 강력하고 유연한 방법들이다. 선택하는 방법은 상황과 개발자의 선호에 따라 다를 수 있다.

참고문헌:
- [MDN web docs](https://developer.mozilla.org/ko/docs/Web/JavaScript)
- [JavaScript.Info](https://javascript.info/)