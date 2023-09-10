---
layout: post
title: "자바스크립트의 내장 함수를 이용한 문자열 처리 (String Processing using Built-in Functions in JavaScript)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

## 1. 문자열 길이 확인하기

```javascript
let str = "Hello, World!";
console.log(str.length); // 13
```

자바스크립트의 문자열은 `length` 프로퍼티를 통해 길이를 확인할 수 있습니다. 위 예시에서는 "Hello, World!"라는 문자열의 길이가 13임을 확인할 수 있습니다.

## 2. 대소문자 변환하기

```javascript
let str = "Hello, World!";
console.log(str.toUpperCase()); // "HELLO, WORLD!"
console.log(str.toLowerCase()); // "hello, world!"
```

문자열의 대소문자를 변환하고 싶을 때는 `toUpperCase()`와 `toLowerCase()` 함수를 사용할 수 있습니다. 위 예시에서는 각각 대문자로 변환된 "HELLO, WORLD!"와 소문자로 변환된 "hello, world!"를 확인할 수 있습니다.

## 3. 문자열 일부 추출하기

```javascript
let str = "Hello, World!";
console.log(str.slice(7, 12)); // "World"
console.log(str.substring(7, 12)); // "World"
console.log(str.substr(7, 5)); // "World"
```

문자열의 일부를 추출하기 위해 `slice()`, `substring()`, `substr()` 함수를 사용할 수 있습니다. 각 함수의 동작 방식은 약간씩 다르지만, 위 예시에서는 모두 문자열의 인덱스 7부터 12 이전까지의 부분 문자열 "World"를 추출한 결과를 확인할 수 있습니다.

## 4. 특정 문자열 찾기

```javascript
let str = "Hello, World!";
console.log(str.indexOf("World")); // 7
console.log(str.lastIndexOf("o")); // 8
console.log(str.includes("Hello")); // true
```

문자열 내에서 특정 문자열을 찾기 위해 `indexOf()`, `lastIndexOf()`, `includes()` 함수를 사용할 수 있습니다. 위 예시에서는 각각 "World" 문자열의 시작 위치, 마지막으로 등장하는 "o" 문자의 위치, 그리고 "Hello" 문자열이 포함되어 있는지 여부를 확인하는 결과를 확인할 수 있습니다.

## 5. 문자열 분리 및 결합하기

```javascript
let str = "Hello, World!";
console.log(str.split(", ")); // ["Hello", "World!"]
console.log(str.concat(" Welcome")); // "Hello, World! Welcome"
console.log(str.replace("Hello", "Hi")); // "Hi, World!"
```

문자열을 분리하거나 결합하기 위해 `split()`, `concat()`, `replace()` 함수를 사용할 수 있습니다. 위 예시에서는 각각 ", "를 기준으로 문자열을 분리하여 배열로 반환한 결과, "Welcome" 문자열을 추가한 결과, 그리고 "Hello"를 "Hi"로 변경한 결과를 확인할 수 있습니다.

자바스크립트의 내장 함수를 활용하면 문자열 처리를 더욱 편리하게 할 수 있습니다. 이 외에도 다양한 함수들이 존재하니 필요에 따라 문서를 참고하여 사용해보세요!