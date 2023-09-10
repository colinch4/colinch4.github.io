---
layout: post
title: "자바스크립트 JSON.stringify()와 JSON.parse()의 차이점"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 `JSON.stringify()`와 `JSON.parse()`는 JSON 데이터를 문자열로 직렬화하거나, 문자열을 JSON 형식으로 역직렬화하는 데에 사용되는 함수입니다. 이 두 함수의 차이점을 알아보고 어떻게 사용되는지 살펴보겠습니다.

## `JSON.stringify()`

`JSON.stringify()` 함수는 JavaScript 객체나 값들을 JSON 문자열 형태로 변환하는데 사용됩니다. JSON 문자열은 JavaScript에서 객체를 표현한것과 동일한 구조를 갖습니다. 이 함수의 주요 목적은 JavaScript 객체를 JSON 형식에 맞추어 문자열로 변환하여 네트워크로 전송하거나 로컬 스토리지에 저장하는 것입니다.

예를 들어, 다음과 같은 JavaScript 객체를 `JSON.stringify()` 함수를 사용하여 JSON 문자열로 변환할 수 있습니다.

```javascript
const user = {
  name: "John",
  age: 30,
  isAdmin: true
};

const jsonString = JSON.stringify(user);
console.log(jsonString);
// 출력: '{"name":"John","age":30,"isAdmin":true}'
```

## `JSON.parse()`

`JSON.parse()` 함수는 JSON 문자열을 JavaScript 객체로 변환하는데 사용됩니다. 이 함수는 JSON 형식의 문자열을 받아 JavaScript 객체나 값으로 파싱합니다. 이 함수의 주요 목적은 JSON 문자열을 JavaScript 객체로 변환하여 이후에 쉽게 조작하고 사용할 수 있도록 하는 것입니다.

예를 들어, 이전에 생성한 JSON 문자열을 `JSON.parse()` 함수를 사용하여 JavaScript 객체로 변환할 수 있습니다.

```javascript
const jsonString = '{"name":"John","age":30,"isAdmin":true}';
const user = JSON.parse(jsonString);
console.log(user);
// 출력: { name: 'John', age: 30, isAdmin: true }
```

## 결론

`JSON.stringify()` 함수는 JavaScript 객체나 값들을 JSON 문자열로 직렬화하는데 사용되며, `JSON.parse()` 함수는 JSON 문자열을 JavaScript 객체로 역직렬화하는데 사용됩니다. 이 두 함수는 JSON 데이터를 JavaScript 객체와 문자열 사이를 변환하는 강력한 도구입니다. 이러한 함수들을 적절하게 활용하여 웹 애플리케이션에서 JSON 데이터를 조작하고 전송하는데 활용할 수 있습니다.