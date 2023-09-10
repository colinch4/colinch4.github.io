---
layout: post
title: "자바스크립트 함수를 인자로 받고 함수를 반환하는 고차 함수 (Higher Order Functions that Take Functions as Arguments and Return Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 일급 함수(first-class functions)를 지원하여 함수를 값으로 다룰 수 있는 언어입니다. 이러한 특성을 활용하여 **고차 함수 (higher order functions)** 라는 개념을 사용할 수 있습니다. 고차 함수는 다른 함수를 인자로 받거나, 함수를 반환하는 함수를 뜻합니다.

이번 글에서는 자바스크립트에서 고차 함수를 어떻게 활용할 수 있는지 살펴보겠습니다. 특히, 함수를 인자로 받고 함수를 반환하는 고차 함수에 초점을 맞출 것입니다.

## 함수를 인자로 받는 고차 함수

```javascript
function calculator(operation, num1, num2) {
    return operation(num1, num2);
}

function add(a, b) {
    return a + b;
}

function multiply(a, b) {
    return a * b;
}

const result1 = calculator(add, 2, 3);
console.log(result1); // 5

const result2 = calculator(multiply, 4, 5);
console.log(result2); // 20
```

위의 예제에서 `calculator` 함수는 `operation` 함수를 인자로 받습니다. 그리고 `operation` 함수에 `num1`과 `num2` 인자를 전달하여 결과를 반환합니다. `calculator` 함수를 호출할 때 다른 함수들을 `operation` 인자로 전달하여 다양한 연산을 수행할 수 있습니다.

위의 예제에서는 `add` 함수와 `multiply` 함수를 `calculator` 함수의 `operation` 인자로 전달하여 덧셈과 곱셈 연산을 수행하고 있습니다.

## 함수를 반환하는 고차 함수

```javascript
function greeter(name) {
    return function() {
        console.log("Hello, " + name + "!");
    }
}

const greetAnna = greeter("Anna");
greetAnna(); // Hello, Anna!

const greetJohn = greeter("John");
greetJohn(); // Hello, John!
```

위의 예제에서 `greeter` 함수는 `name` 인자를 받고 함수를 반환합니다. 반환된 함수는 `name` 인자를 사용하여 "Hello, {name}!"을 출력하는 역할을 합니다.

위의 예제에서는 `greeter` 함수를 호출하여 `greetAnna`과 `greetJohn`이라는 변수에 반환된 함수를 저장하였습니다. 이후에 `greetAnna`과 `greetJohn` 변수를 호출하여 함수를 실행시킬 수 있습니다.

## 결론

고차 함수는 자바스크립트의 강력한 기능 중 하나입니다. 함수를 인자로 받거나 함수를 반환하는 고차 함수를 사용하면 코드의 재사용성과 유연성을 크게 향상시킬 수 있습니다. 이로써 함수형 프로그래밍의 개념을 더욱 쉽게 이해하고 적용할 수 있게 됩니다.

고차 함수를 사용하여 복잡한 작업을 수행하는 코드를 단순화하고 가독성을 개선할 수 있습니다. 또한, 함수를 값으로 다룰 수 있는 자바스크립트의 특성을 최대한 활용하여 프로그래밍을 할 수 있습니다.

다음번에는 고차 함수를 사용하여 더 복잡한 예제들을 살펴보도록 하겠습니다.