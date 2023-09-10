---
layout: post
title: "자바스크립트 표준 내장 함수 (Standard Built-in Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 많은 내장 함수들을 제공하여 개발자들이 다양한 작업을 수행할 수 있도록 도와줍니다. 이러한 내장 함수들은 자바스크립트 언어 자체에 내장되어 있으므로 별도의 설치나 임포트가 필요하지 않습니다.

자바스크립트의 표준 내장 함수 중 일부를 소개하겠습니다.

## 1. parseInt()

`parseInt()` 함수는 문자열을 정수로 변환하는 함수입니다. 이 함수는 문자열을 분석하고 첫 번째로 나오는 숫자를 반환합니다.

```javascript
let num = parseInt("123");
console.log(num); // Output: 123
```

## 2. parseFloat()

`parseFloat()` 함수는 문자열을 부동 소수점 숫자로 변환하는 함수입니다. 이 함수는 문자열을 분석하고 첫 번째로 나오는 부동 소수점 숫자를 반환합니다.

```javascript
let num = parseFloat("3.14");
console.log(num); // Output: 3.14
```

## 3. isNaN()

`isNaN()` 함수는 주어진 값이 NaN(Not-a-Number)인지 여부를 확인하는 함수입니다. NaN은 숫자가 아닌 값을 나타내는 특수한 값입니다.

```javascript
let result = isNaN("Hello");
console.log(result); // Output: true

result = isNaN(123);
console.log(result); // Output: false
```

## 4. typeof()

`typeof()` 함수는 주어진 값의 타입을 반환하는 함수입니다. 이 함수를 사용하여 변수의 타입을 확인할 수 있습니다.

```javascript
let num = 123;
let str = "Hello World";

console.log(typeof num); // Output: number
console.log(typeof str); // Output: string
```

## 5. Math.random()

`Math.random()` 함수는 0과 1 사이의 임의의 난수를 생성하는 함수입니다. 이 함수를 사용하여 랜덤한 값을 생성할 수 있습니다.

```javascript
let randomNum = Math.random();
console.log(randomNum); // Output: 0.12345 (임의의 값)
```

## 6. Array.isArray()

`Array.isArray()` 함수는 주어진 값이 배열인지 여부를 확인하는 함수입니다. 이 함수를 사용하여 변수가 배열인지 아닌지를 확인할 수 있습니다.

```javascript
let arr = [1, 2, 3];
console.log(Array.isArray(arr)); // Output: true

let str = "Hello World";
console.log(Array.isArray(str)); // Output: false
```

위에서 소개한 함수들은 자바스크립트에서 가장 많이 사용되는 표준 내장 함수 중 일부입니다. 이 외에도 다양한 내장 함수들이 있으며, 자바스크립트 공식 문서에서 더 많은 함수들을 찾아볼 수 있습니다. 이러한 내장 함수들은 개발자들이 자바스크립트를 보다 효율적으로 사용할 수 있도록 도와줍니다.

이 글에서는 몇 가지 예시만을 다루었지만, 자바스크립트의 내장 함수들은 다양한 작업을 수행하는데 도움을 주는 강력한 기능들이 있습니다. 자바스크립트를 사용하여 개발할 때 내장 함수들을 잘 활용하면 더욱 효율적이고 간결한 코드를 작성할 수 있습니다.