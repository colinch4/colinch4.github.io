---
layout: post
title: "자바스크립트 함수의 동적 바인딩 (Dynamic Binding of JavaScript Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

JavaScript는 동적 프로그래밍 언어로서, 함수의 동적 바인딩(dynamic binding) 기능을 제공합니다. 이는 함수의 실행 시간에 함수를 다른 객체에 바인딩할 수 있는 능력을 의미합니다. 

일반적으로, 함수는 선언 시점에서 함수의 범위(scope)와 연결됩니다. 하지만 동적 바인딩을 사용하면, 함수를 새로운 객체에 바인딩하여 객체의 메서드로 사용하거나, 다른 객체의 메서드를 오버라이드(override)하는 등 다양한 활용이 가능합니다.

## 동적 바인딩의 예시

아래 예시를 통해 동적 바인딩이 어떻게 작동하는지 살펴보겠습니다.

```javascript
const myObj1 = {
  value: 1,
};

const myObj2 = {
  value: 2,
};

function getValue() {
  return this.value;
}

console.log(getValue()); // 출력: undefined

const boundFunc1 = getValue.bind(myObj1);
console.log(boundFunc1()); // 출력: 1

const boundFunc2 = getValue.bind(myObj2);
console.log(boundFunc2()); // 출력: 2
```

위의 예시에서, `getValue` 함수는 `this.value`를 반환하는 함수입니다. 하지만 `getValue`를 직접 호출하면 `undefined`를 반환합니다. 이는 함수가 독립적으로 호출되었기 때문입니다.

하지만 `bind` 메서드를 사용하여 함수를 객체에 동적으로 바인딩하면, 해당 객체에 속한 메서드로써 함수를 호출할 수 있습니다. `bind` 메서드는 새로운 함수를 반환하며, 이 반환된 함수는 `this`가 인수로 전달한 객체로 설정됩니다. 

위 예시에서, `boundFunc1`은 `getValue` 함수가 `myObj1` 객체에 바인딩된 결과입니다. 마찬가지로, `boundFunc2`는 `getValue` 함수가 `myObj2` 객체에 바인딩된 결과입니다. 따라서 `boundFunc1`을 호출하면 `1`, `boundFunc2`를 호출하면 `2`를 반환합니다.

이와 같이 동적 바인딩을 이용하면 같은 함수를 다양한 객체에 바인딩하여 재사용이 가능하고, 객체에 속한 메서드로 사용될 수 있습니다.

## 동적 바인딩의 활용

동적 바인딩은 다양한 상황에서 유용하게 활용될 수 있습니다. 아래 예시를 통해 동적 바인딩의 활용성을 살펴보겠습니다.

### 객체의 메서드 할당

```javascript
function printName() {
  console.log(this.name);
}

const person1 = {
  name: "John",
  print: printName,
};

const person2 = {
  name: "Jane",
  print: printName,
};

person1.print(); // 출력: John
person2.print(); // 출력: Jane
```

위의 예시에서, `printName` 함수는 `this.name` 값을 출력하는 함수입니다. `person1`과 `person2` 객체는 동일한 메서드인 `printName`을 갖고 있지만, 각 객체에 동적으로 바인딩되어 `this`가 올바른 객체를 참조할 수 있습니다. 따라서 `person1.print()`를 호출하면 `John`이 출력되고, `person2.print()`를 호출하면 `Jane`이 출력됩니다.

### 다른 객체의 메서드 오버라이드

```javascript
const calculator = {
  value: 0,
  add: function (num) {
    this.value += num;
  },
  subtract: function (num) {
    this.value -= num;
  },
};

const calculator2 = {
  value: 100,
};

calculator.add(10);
console.log(calculator.value); // 출력: 10

const subtractFunc = calculator.subtract.bind(calculator2);
subtractFunc(20);
console.log(calculator2.value); // 출력: 80
```

위의 예시에서, `calculator` 객체의 `add`와 `subtract` 메서드는 `value` 값을 조작하는 역할을 합니다. `calculator2` 객체는 `value` 값을 `100`으로 가지고 있습니다.

`subtractFunc`은 `calculator.subtract` 함수를 `calculator2` 객체에 동적으로 바인딩한 결과입니다. 이를 호출하면 `calculator2` 객체의 `value`가 `20`만큼 감소됩니다. 따라서 `calculator2.value`를 출력하면 `80`이 됩니다.

이와 같이 동적 바인딩을 이용하여 다른 객체의 메서드를 오버라이드하거나 다른 객체의 메서드를 추가하여 유연한 프로그래밍이 가능합니다.

## 결론

JavaScript의 동적 바인딩은 함수를 실행 시간에 다른 객체에 바인딩하는 기능을 제공하여 유연하고 재사용 가능한 코드를 작성할 수 있게 합니다. 동적 바인딩은 객체의 메서드로 함수를 할당하고, 다른 객체의 메서드를 오버라이드하는 등 다양한 상황에서 활용될 수 있습니다. 프로그래밍의 유연성과 확장성을 높이기 위해 동적 바인딩을 적절히 활용해 보세요.