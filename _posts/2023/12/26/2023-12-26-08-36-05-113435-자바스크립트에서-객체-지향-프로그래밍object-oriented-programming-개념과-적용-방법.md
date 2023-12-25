---
layout: post
title: "[javascript] 자바스크립트에서 객체 지향 프로그래밍(Object-Oriented Programming) 개념과 적용 방법"
description: " "
date: 2023-12-26
tags: [javascript]
comments: true
share: true
---

자바스크립트는 객체 지향 프로그래밍(Object-Oriented Programming, OOP)을 지원하는 언어로, 클래스 기반의 언어와는 조금 다른 방식으로 객체를 다룹니다. 이번 글에서는 자바스크립트에서의 객체 지향 프로그래밍 개념과 적용 방법에 대해 알아보겠습니다.

## 객체 지향 프로그래밍이란?

객체 지향 프로그래밍은 현실 세계의 사물을 모방하여 소프트웨어를 설계하는 방법론으로, **객체**라는 개념을 기반으로 합니다. 객체는 **속성**과 **기능**을 갖고 있으며, 이러한 객체들 간의 상호작용을 통해 프로그램이 동작합니다.

## 자바스크립트에서의 객체

자바스크립트에서는 모든 것이 객체입니다. **함수**, **배열**, **문자열** 등 모든 것이 내장 객체로 구현되어 있으며, 개발자가 직접 객체를 생성하여 사용할 수도 있습니다.

예를 들어, 다음과 같이 객체를 생성할 수 있습니다.

```javascript
// 객체 리터럴 방식
let person = {
  name: 'John',
  age: 30,
  greet: function() {
    console.log('Hello!');
  }
};
```

## 프로토타입 기반 상속

자바스크립트는 **프로토타입 기반 상속**을 지원합니다. 이는 클래스가 아닌 **프로토타입**을 통해 상속 관계를 구현하는 방식입니다. 모든 객체는 다른 객체를 참조하는 **프로토타입**을 가지고 있으며, 이를 통해 상속과 메서드 공유를 구현합니다.

```javascript
// 프로토타입을 통한 상속
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.greet = function() {
  console.log('Hello!');
};

let john = new Person('John', 30);
john.greet(); // 'Hello!'
```

## ES6 클래스 문법

ES6부터는 클래스(class) 문법을 도입하여 객체 지향 프로그래밍을 더욱 쉽게 할 수 있게 되었습니다.

```javascript
// ES6 클래스 문법을 이용한 객체 정의
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log('Hello!');
  }
}

let john = new Person('John', 30);
john.greet(); // 'Hello!'
```

## 결론

자바스크립트는 객체 지향 프로그래밍을 지원하는 다양한 기능을 제공하며, 프로토타입 기반 상속과 ES6 클래스 문법을 통해 객체를 보다 강력하게 다룰 수 있습니다.

더 많은 자바스크립트 객체 지향 프로그래밍에 대한 내용은 [MDN web docs](https://developer.mozilla.org/ko/docs/Web/JavaScript) 등의 자료를 참고하시기 바랍니다.