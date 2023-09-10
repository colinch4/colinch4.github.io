---
layout: post
title: "자바스크립트 함수의 오버로딩 패턴 (Function Overloading Pattern)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 동적 타입 언어로서, 함수를 정의할 때 매개변수의 개수나 타입에 제한이 없습니다. 이는 자바스크립트에서 함수 오버로딩을 구현하는데 매우 유연한 방법을 제공합니다. 

함수 오버로딩이란, 같은 이름의 함수를 다양한 매개변수나 타입으로 정의하고 호출할 수 있는 기능을 의미합니다. 이는 코드의 가독성과 재사용성을 높이는데 도움을 줄 수 있습니다. 

## 기본적인 함수 오버로딩 패턴

기본적인 함수 오버로딩 패턴은 조건문을 사용하여 인자의 타입이나 개수에 따라 다른 동작을 수행하는 것입니다. 아래는 기본적인 함수 오버로딩 패턴의 예시입니다.

```javascript
function greet(name) {
  if (typeof name === 'string') {
    console.log("Hello, " + name + "!");
  } else if (Array.isArray(name)) {
    console.log("Hello, " + name.join(" and ") + "!");
  } else {
    console.log("Hello, stranger!");
  }
}

greet("John"); // 출력: Hello, John!
greet(["John", "Jane"]); // 출력: Hello, John and Jane!
greet(123); // 출력: Hello, stranger!
```

위 예시에서는 매개변수 `name`의 타입과 개수에 따라 다른 동작을 수행하도록 하였습니다. 문자열이면 해당 이름으로 인사를 하고, 배열이면 배열의 요소들로 인사를 하며, 그 외의 경우에는 "stranger"로 인사합니다.

## 객체를 활용한 함수 오버로딩 패턴

객체를 활용한 함수 오버로딩 패턴은 함수 내부에서 인자들을 객체의 속성으로 처리하여 다양한 형태의 인자를 받을 수 있도록 합니다. 아래는 객체를 활용한 함수 오버로딩 패턴의 예시입니다.

```javascript
function calculate(options) {
  if (typeof options === 'number') {
    console.log("Square: " + options ** 2);
  } else if (typeof options === 'object') {
    let result = options.a + options.b;
    console.log("Sum: " + result);
  } else {
    console.log("Invalid input!");
  }
}

calculate(5); // 출력: Square: 25
calculate({ a: 2, b: 3 }); // 출력: Sum: 5
calculate("test"); // 출력: Invalid input!
```

위 예시에서는 매개변수 `options`를 객체로 받아, 숫자면 제곱을 계산하고, 객체면 속성의 값을 더하여 합을 계산합니다. 그 외의 경우에는 "Invalid input!"을 출력합니다.

## 정규식을 활용한 함수 오버로딩 패턴

정규식을 활용한 함수 오버로딩 패턴은 매개변수의 타입이 아닌 매개변수의 패턴에 따라 다른 동작을 수행하도록 합니다. 아래는 정규식을 활용한 함수 오버로딩 패턴의 예시입니다.

```javascript
function validate(value) {
  if (/^\d+$/.test(value)) {
    console.log("Number: " + value);
  } else if (/^[a-zA-Z]+$/.test(value)) {
    console.log("String: " + value);
  } else {
    console.log("Invalid value!");
  }
}

validate("123"); // 출력: Number: 123
validate("abc"); // 출력: String: abc
validate("1a2b"); // 출력: Invalid value!
```

위 예시에서는 매개변수 `value` 값이 정규식 패턴에 일치하면 해당하는 타입으로 처리하고, 그 외의 경우에는 "Invalid value!"를 출력합니다.

자바스크립트 함수의 오버로딩 패턴은 코드의 유연성과 가독성을 높일 수 있는 강력한 기능입니다. 함수를 정의할 때 다양한 인자의 형태를 고려하여 오버로딩 패턴을 적용해보세요.