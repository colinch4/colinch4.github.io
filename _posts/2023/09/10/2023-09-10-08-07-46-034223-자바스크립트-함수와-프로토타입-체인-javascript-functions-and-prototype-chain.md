---
layout: post
title: "자바스크립트 함수와 프로토타입 체인 (JavaScript Functions and Prototype Chain)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 함수 중심의 프로그래밍 언어입니다. **함수**는 자바스크립트에서 가장 중요한 개념 중 하나이며, 프로토타입 체인은 자바스크립트 객체 지향 프로그래밍에서 핵심 개념 중 하나입니다. 이 블로그에서는 자바스크립트 함수와 프로토타입 체인에 대해 알아보겠습니다.

## 함수

자바스크립트에서 함수는 변수와 마찬가지로 값으로 취급됩니다. 따라서 변수에 함수를 할당하거나, 함수를 매개변수로 전달하고 리턴값으로 사용할 수 있습니다. 이러한 특징은 함수를 First-Class Citizen으로 만들어줍니다.

함수는 `function` 키워드를 사용하여 정의합니다. 예를 들어, 다음은 간단한 덧셈 함수의 예입니다.

```javascript
function add(a, b) {
  return a + b;
}

let result = add(5, 10);
console.log(result); // 15
```

또한, 자바스크립트에서는 익명 함수(anonymous function)를 사용할 수도 있습니다. 익명 함수는 변수에 직접 할당하여 사용하거나, 즉시 실행할 수 있습니다.

```javascript
let multiply = function(a, b) {
  return a * b;
}

let result = multiply(3, 4);
console.log(result); // 12

(function() {
  console.log("I am an immediately invoked function expression");
})();
```

## 프로토타입 체인

자바스크립트는 프로토타입 기반의 객체 지향 프로그래밍을 지원합니다. 자바스크립트의 모든 객체는 **프로토타입(prototype)**이라고 불리는 다른 객체를 가리키는 숨겨진 링크인 `__proto__` 속성을 가지고 있습니다.

프로토타입 체인은 자바스크립트에서 객체가 어떤 메서드나 속성에 접근할 때, 해당 메서드나 속성이 객체 자체에 존재하지 않으면, 프로토타입 체인을 따라 상위 객체의 프로토타입에서 찾게 되는 메커니즘입니다.

예를 들어, 다음은 `Person` 생성자 함수를 사용하여 `name` 속성을 가진 객체를 생성하는 예제입니다. 이때, `Person.prototype` 객체에 `greet` 메서드를 정의하고 `Person` 객체를 생성하면, `greet` 메서드를 사용할 수 있습니다.

```javascript
function Person(name) {
  this.name = name;
}

Person.prototype.greet = function() {
  console.log(`Hello, my name is ${this.name}`);
};

let person = new Person("John");
person.greet(); // Hello, my name is John
```

프로토타입 체인을 통해 객체는 자신의 프로토타입, 그리고 상위 프로토타입의 메서드와 속성에 접근할 수 있게 됩니다.

## 마치며

이 블로그에서는 자바스크립트에서 함수와 프로토타입 체인에 대해 알아보았습니다. 함수는 자바스크립트에서 가장 중요한 개념 중 하나이며, 프로토타입 체인은 객체 지향 프로그래밍에서 핵심 개념입니다. 이러한 개념을 이해하면 자바스크립트로 더욱 유연하고 강력한 코드를 작성할 수 있습니다.