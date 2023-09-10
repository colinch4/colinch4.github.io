---
layout: post
title: "자바스크립트 표준 내장 함수 (Standard Built-in Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 많은 유용한 내장 함수를 제공하여 개발자들이 간편하게 작업할 수 있도록 도와줍니다. 이러한 내장 함수는 표준으로 정의되어 있으며, 모든 자바스크립트 환경에서 사용할 수 있습니다. 이번 블로그 포스트에서는 자바스크립트의 몇 가지 표준 내장 함수를 살펴보겠습니다.

## `parseInt()`

`parseInt()` 함수는 문자열을 정수로 변환합니다. 이 함수는 문자열에서 시작하는 숫자를 파싱하며, 반환값으로 해당 정수를 리턴합니다. 예를 들어:

```javascript
let num1 = parseInt("123");
console.log(num1); // Output: 123

let num2 = parseInt("456hello");
console.log(num2); // Output: 456
```

## `parseFloat()`

`parseFloat()` 함수는 문자열을 부동소수점 숫자로 변환합니다. 이 함수는 문자열에서 시작하는 부동소수점 숫자를 파싱하며, 반환값으로 해당 숫자를 리턴합니다. 예를 들어:

```javascript
let num1 = parseFloat("3.14");
console.log(num1); // Output: 3.14

let num2 = parseFloat("10.5hello");
console.log(num2); // Output: 10.5
```

## `String()`

`String()` 함수는 다른 데이터 타입을 문자열로 변환합니다. 이 함수는 주어진 값의 문자열 표현을 반환합니다. 예를 들어:

```javascript
let num = 123;
let str = String(num);
console.log(str); // Output: "123"
```

## `Math.random()`

`Math.random()` 함수는 0과 1 사이의 난수를 생성합니다. 반환값은 항상 0 이상 1 미만의 수입니다. 예를 들어:

```javascript
let randomNum = Math.random();
console.log(randomNum); // Output: 0.5738714691241824
```

## `Array.isArray()`

`Array.isArray()` 함수는 주어진 값이 배열인지 여부를 확인합니다. 만약 주어진 값이 배열이면 `true`를, 그렇지 않으면 `false`를 반환합니다. 예를 들어:

```javascript
let arr = [1, 2, 3];
let isArr = Array.isArray(arr);
console.log(isArr); // Output: true

let str = "Hello";
let isArr = Array.isArray(str);
console.log(isArr); // Output: false
```

이상으로 자바스크립트의 몇 가지 표준 내장 함수를 살펴보았습니다. 이 함수들은 개발자들이 자주 사용하는 유용한 기능을 제공합니다. 코드를 작성할 때 이러한 내장 함수를 활용하여 작업을 간단하고 효율적으로 할 수 있습니다.