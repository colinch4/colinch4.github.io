---
layout: post
title: "자바스크립트 apply, call, bind 메서드 (apply, call, bind Methods)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 자주 사용되는 메서드 중 apply, call, bind는 함수를 호출하고 실행할 때 유용한 기능을 제공합니다. 이러한 메서드는 함수에 특정 context를 지정하거나 인자를 전달하는 데 사용됩니다. 이번 블로그 포스트에서는 apply, call, bind 메서드에 대해 자세히 알아보겠습니다.

## apply 메서드

apply 메서드는 함수를 호출할 때 특정 context와 인자들을 배열 형태로 전달합니다. 이렇게 하면 함수 내부에서 사용 가능한 this 값과 인자 값을 지정할 수 있습니다.

```javascript
function sayHello(name) {
  console.log("Hello, " + name);
}

sayHello.apply(null, ["John"]);
```

위의 예시에서는 sayHello 함수를 호출하면서 컨텍스트로 null을 전달하고, 인자로는 "John"을 포함한 배열을 전달합니다. 이렇게 하면 sayHello 함수 내부에서 this는 null이 되고, 인자로 "John"이라는 값을 사용할 수 있게 됩니다.

## call 메서드

call 메서드도 apply 메서드와 비슷한 역할을 수행하지만, 인자들을 개별적으로 전달하는 다른 방식을 사용합니다.

```javascript
function sayHello(name) {
  console.log("Hello, " + name);
}

sayHello.call(null, "John");
```

위의 예시에서는 sayHello 함수를 호출하면서 컨텍스트로 null을 전달하고, 인자로 "John"을 개별적으로 전달합니다. 이렇게 하면 apply 메서드와 같은 결과를 얻을 수 있습니다.

## bind 메서드

bind 메서드는 함수를 호출할 때 특정 context를 설정해주고, 인자들을 미리 지정하는 방법입니다. bind 메서드는 새로운 함수를 반환하며, 필요한 시점에서 호출할 수 있습니다.

```javascript
function sayHello(greeting) {
  console.log(greeting + ", " + this.name);
}

var person = {
  name: "John"
};

var sayHelloToPerson = sayHello.bind(person, "Hello");
sayHelloToPerson();
```

위의 예시에서는 sayHello 함수를 호출하면서 context로 person 객체를 지정하고, "Hello"라는 인자를 미리 지정합니다. bind 메서드는 person 객체에 sayHello 함수의 컨텍스트를 바인딩한 새로운 함수인 sayHelloToPerson을 반환합니다. 이렇게 새로운 함수를 호출하면 설정된 context와 인자를 사용하여 원하는 동작을 수행할 수 있습니다.

## 결론

apply, call, bind 메서드는 자바스크립트에서 함수 호출과 관련된 기능을 다양하게 제공합니다. 개발자는 이러한 메서드를 활용하여 함수의 컨텍스트와 인자를 유연하게 제어할 수 있습니다. 이러한 메서드들은 특히 객체 지향 프로그래밍에서 유용하게 사용될 수 있으며, 자바스크립트의 강력한 기능 중 하나입니다.