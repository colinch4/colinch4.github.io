---
layout: post
title: "자바스크립트 함수와 프로토타입 체인 (JavaScript Functions and Prototype Chain)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 함수 중심의 프로그래밍 언어로서, 함수가 중요한 역할을 수행합니다. 이번 블로그 포스트에서는 자바스크립트 함수와 그들이 어떻게 프로토타입 체인과 관련되는지 살펴보겠습니다.

## 함수와 객체

자바스크립트에서 함수는 일급 객체입니다. 이는 함수를 변수에 할당하거나, 다른 함수의 인자로 전달하고, 반환값으로 사용할 수 있다는 의미입니다. 함수는 객체처럼 프로퍼티를 가질 수 있고, 메서드를 정의할 수도 있습니다.

예를 들어, 다음과 같이 `greeting`이라는 함수를 정의하고 호출할 수 있습니다:

```javascript
function greeting(name) {
  console.log("Hello, " + name + "!");
}

greeting("John"); // 출력: Hello, John!
```

## 프로토타입 체인

자바스크립트에서 모든 객체는 **프로토타입**이라는 다른 객체를 가지고 있습니다. 이 프로토타입은 해당 객체의 **부모 역할**을 수행하며, 프로퍼티 및 메서드를 상속받을 수 있습니다. 프로토타입 체인은 객체들이 서로 연결되어 있는 체인 구조를 말합니다.

예를 들어, `Person`이라는 생성자 함수를 정의하고, `name` 속성을 가진 객체를 생성할 수 있습니다:

```javascript
function Person(name) {
  this.name = name;
}

var person1 = new Person("John");
var person2 = new Person("Emily");

console.log(person1.name); // 출력: John
console.log(person2.name); // 출력: Emily
```

위의 예제에서 `person1`과 `person2` 객체는 `Person` 함수의 인스턴스입니다. 이들은 `name` 속성을 직접 가지고 있지 않지만, 프로토타입 체인을 통해 `Person` 함수의 프로토타입 객체로부터 상속받아 사용할 수 있습니다.

## 프로토타입 메서드

프로토타입을 통해 객체가 상속받은 메서드를 호출할 수 있습니다. 프로토타입 메서드는 해당 객체의 모든 인스턴스가 공유합니다.

예를 들어, `Person` 생성자 함수의 프로토타입에 `greet` 메서드를 추가해봅시다:

```javascript
Person.prototype.greet = function() {
  console.log("Hi, my name is " + this.name);
};

person1.greet(); // 출력: Hi, my name is John
person2.greet(); // 출력: Hi, my name is Emily
```

위의 예제에서 `greet` 메서드는 `Person` 생성자 함수의 프로토타입에 추가되었습니다. 이로 인해 `person1`과 `person2` 객체 모두에서 `greet` 메서드를 호출할 수 있게 되었습니다.

## 객체 상속과 프로토타입 체인

프로토타입 체인은 객체 상속을 구현하는 데 중요한 역할을 합니다. 객체는 상속을 통해 다른 객체의 프로퍼티와 메서드를 상속받을 수 있습니다.

예를 들어, `Employee` 생성자 함수를 정의하고 `Person` 생성자 함수의 인스턴스를 상속받아 `Employee` 객체를 만들어봅시다:

```javascript
function Employee(name, position) {
  Person.call(this, name); // Person 생성자 함수를 호출하여 name 속성을 상속받음
  this.position = position;
}

Employee.prototype = Object.create(Person.prototype); // Person 생성자 함수의 프로토타입을 상속

var emp = new Employee("Jane", "Manager");
emp.greet(); // 출력: Hi, my name is Jane
console.log(emp.position); // 출력: Manager
```

위의 예제에서 `Employee` 생성자 함수는 `Person` 생성자 함수를 호출하여 `name` 속성을 상속받습니다. 또한, `Employee`의 프로토타입을 `Person`의 프로토타입으로 설정하여 `greet` 메서드를 상속받습니다.

## 결론

자바스크립트에서 함수와 프로토타입 체인은 객체 지향 프로그래밍과 상속을 구현하는 데 매우 유용한 개념입니다. 함수를 이용하여 객체를 생성하고, 그들이 프로토타입 체인을 통해 상속을 받을 수 있습니다. 프로토타입 메서드를 추가하고, 객체들 사이에 상속 관계를 만들어 프로그래밍의 효율성을 높일 수 있습니다.

더 자세한 정보를 원하신다면, 자바스크립트의 함수와 프로토타입 체인에 대해 더 깊이 공부해보시기 바랍니다.