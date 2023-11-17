---
layout: post
title: "자바스크립트에서 Nullish Coalescing을 사용한 JSON 데이터 파싱 방법"
description: " "
date: 2023-09-29
tags: [javascript]
comments: true
share: true
---

## 개요

JSON 데이터를 파싱하는 과정에서 null 또는 undefined 값을 처리할 수 있는 자바스크립트의 Nullish Coalescing 연산자에 대해 알아보겠습니다. 이를 통해 간단한 방법으로 JSON 데이터를 파싱하고 기본 값 지정이 가능합니다.

## Nullish Coalescing

Nullish Coalescing 연산자는 좌항의 값이 null 또는 undefined인 경우, 우항의 값을 반환하는 연산자입니다. 이를 활용하여 JSON 데이터의 값이 null인 경우 기본 값을 사용할 수 있습니다.

## 예시

```javascript
const jsonStr = `{"name": "John Doe", "age": null, "email": "johndoe@example.com"}`;

const userData = JSON.parse(jsonStr);
const name = userData.name ?? "Unnamed";
const age = userData.age ?? "Unknown";
const email = userData.email ?? "No email provided";

console.log(name);    // 출력: John Doe
console.log(age);     // 출력: Unknown
console.log(email);   // 출력: johndoe@example.com
```

위 예시에서 `JSON.parse()`를 사용하여 JSON 문자열을 파싱한 뒤, Nullish Coalescing 연산자인 `??`를 사용하여 각 필드의 값이 null인 경우에 대한 기본 값을 지정했습니다. 이를 통해 이름과 이메일 필드에서는 기본 값을 사용하지 않고, 나이 필드에서는 "Unknown"이라는 기본 값을 사용했습니다.

## 요약

Nullish Coalescing 연산자를 사용하면 JSON 데이터의 null 또는 undefined 값을 처리하는 간단하고 효율적인 방법을 제공합니다. 이를 활용하여 JSON 데이터를 파싱하고 필드의 기본 값을 설정할 수 있습니다. 자바스크립트에서 이 연산자를 사용하는 것은 코드의 가독성과 유지보수성을 높일 수 있는 좋은 방법입니다.

---

Tags: #JavaScript #NullishCoalescing