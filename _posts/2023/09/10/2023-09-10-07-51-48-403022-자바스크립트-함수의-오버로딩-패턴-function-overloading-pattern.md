---
layout: post
title: "자바스크립트 함수의 오버로딩 패턴 (Function Overloading Pattern)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 동적 타입 언어로, 함수의 인자의 개수나 타입에 제한이 없습니다. 그러나 때로는 동일한 이름의 함수를 다양한 인자 형식으로 호출하고 싶을 때가 있습니다. 이를 위해 자바스크립트에서는 **함수 오버로딩 패턴**을 사용할 수 있습니다.

함수 오버로딩 패턴은 동일한 이름의 함수를 정의하고, 이 함수가 인자의 타입에 따라 다른 동작을 수행하도록 하는 패턴입니다. 이를 통해 코드의 가독성을 향상시키고, 유지 보수성을 높일 수 있습니다. 

## 기본적인 함수 오버로딩 패턴

자바스크립트에서는 함수의 인자 개수나 타입이 다를 때, 실제로 호출되는 함수를 결정하는 시점에 오버로딩이 지원되지 않습니다. 하지만 우회적인 방법으로 기본적인 함수 오버로딩을 구현할 수 있습니다. 

```javascript
function add(a, b) {
  if (typeof a === 'number' && typeof b === 'number') {
    return a + b;
  } else if (typeof a === 'string' && typeof b === 'string') {
    return a.concat(b);
  } else {
    throw new Error('Invalid arguments');
  }
}
```

위의 예시에서는 `add` 함수가 두 개의 인자를 받으며, 각 인자의 `typeof`를 검사하여 작업을 수행합니다. 인자가 두 개의 숫자일 경우, 덧셈을 수행하고 인자가 두 개의 문자열일 경우, 문자열을 연결합니다. 그 외의 경우에는 예외를 throw합니다. 이렇게 함으로써 다양한 형식의 인자에 대한 오버로딩 효과를 낼 수 있습니다.

## 객체를 이용한 함수 오버로딩 패턴

자바스크립트에서는 객체를 이용하여 보다 유연하고 확장 가능한 함수 오버로딩 패턴을 구현할 수 있습니다. 

```javascript
function calculate(args) {
  if (typeof args === 'object') {
    if (args.a && args.b && args.operation === 'add') {
      return args.a + args.b;
    } else if (args.a && args.b && args.operation === 'subtract') {
      return args.a - args.b;
    }
  } else { 
    throw new Error('Invalid arguments');
  }
}

console.log(calculate({ a: 5, b: 3, operation: 'add' })); // 8
console.log(calculate({ a: 10, b: 7, operation: 'subtract' })); // 3
```

위의 예시에서는 `calculate` 함수가 하나의 인자를 받습니다. 만약 인자가 객체일 경우, `args` 객체의 속성을 검사하여 적절한 계산을 수행합니다. `operation` 속성이 `add` 일 경우 덧셈을 수행하고, `operation` 속성이 `subtract` 일 경우 뺄셈을 수행합니다. 그 외의 경우에는 예외를 throw합니다.

이렇게 객체를 이용한 함수 오버로딩 패턴을 사용하면, 인자의 타입이나 개수에 따라 다양한 동작을 구현할 수 있으며, 코드의 가독성과 확장성을 개선할 수 있습니다.

## 정리

자바스크립트에서는 함수의 인자의 타입이나 개수에 따라 다른 동작을 수행하기 위해 함수 오버로딩 패턴을 사용할 수 있습니다. 기본적인 함수 오버로딩 패턴은 인자 타입을 검사하여 적절한 작업을 수행하고, 객체를 이용한 오버로딩 패턴은 인자로 객체를 받아 객체의 속성을 검사하여 작업을 수행합니다. 이러한 패턴을 활용하여 코드의 가독성과 유지 보수성을 높일 수 있습니다.