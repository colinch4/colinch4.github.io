---
layout: post
title: "자바스크립트 캡슐화와 캡처링 (Encapsulation and Capturing)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 동적인 특성을 가지고 있어 개발자에게 많은 자유를 제공합니다. 그러나 이는 코드의 유지보수성과 가독성을 낮출 수 있는 위험도 내포하고 있습니다. 이러한 문제를 해결하기 위해 자바스크립트에서는 **캡슐화**와 **캡처링**이라는 개념을 사용할 수 있습니다.

## 캡슐화 (Encapsulation)

캡슐화란 데이터와 해당 데이터를 조작하는 메소드를 하나의 단위로 묶어서 외부에 노출시키지 않는 것을 의미합니다. 이를 통해 코드의 유지보수성과 가독성을 향상시킬 수 있습니다.

```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    getName() {
        return this.name;
    }

    getAge() {
        return this.age;
    }

    sayHello() {
        console.log(`안녕하세요, ${this.name}입니다.`);
    }
}

const person = new Person('John', 25);
console.log(person.getName()); // John
console.log(person.getAge()); // 25
person.sayHello(); // 안녕하세요, John입니다.
```

위의 예제에서 `Person` 클래스는 `name`과 `age`라는 데이터를 캡슐화하고, `getName()`, `getAge()`, `sayHello()`와 같은 메소드를 제공합니다. 외부에서는 `name`과 `age`에 직접 접근할 수 없으며, 메소드를 통해서만 데이터에 접근할 수 있습니다.

## 캡처링 (Capturing)

캡처링은 클로저(Closure)를 통해 함수 내부에 정의한 변수를 외부에서도 사용할 수 있도록 하는 개념입니다. 이를 통해 변수의 스코프를 제한하고, 변수에 대한 접근을 보호할 수 있습니다.

```javascript
function createCounter() {
    let count = 0;

    return function() {
        count++;
        console.log(`현재 count 값: ${count}`);
    };
}

const counter = createCounter();
counter(); // 현재 count 값: 1
counter(); // 현재 count 값: 2
```

위의 예제에서 `createCounter` 함수는 내부에 `count` 변수를 정의하고, 해당 변수를 조작하는 클로저를 반환합니다. 이렇게 반환된 클로저는 외부에서 호출될 때마다 `count` 변수를 증가시키고 그 값을 출력합니다. 

이렇게 클로저를 통해 `count` 변수는 외부에서 접근할 수 없지만, 클로저 내부에서는 계속해서 해당 변수에 접근하여 조작할 수 있습니다.

## 결론

자바스크립트는 캡슐화와 캡처링을 통해 코드의 유지보수성과 가독성을 향상시킬 수 있습니다. 적절하게 이러한 개념들을 활용하여 코드를 작성하면, 더 안정적이고 효율적인 JavaScript 애플리케이션을 개발할 수 있습니다.