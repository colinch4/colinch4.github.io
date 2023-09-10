---
layout: post
title: "자바스크립트 apply, call, bind 메서드 (apply, call, bind Methods)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 함수를 다루는 방법 중 중요한 개념은 `apply`, `call`, `bind` 메서드입니다. 이러한 메서드는 함수를 호출하고, 함수 내에서 `this` 값을 설정하거나, 함수의 인수(arguments)를 전달하는 데 사용됩니다. 이 글에서는 `apply`, `call`, `bind` 메서드의 개념과 각각의 차이를 알아보겠습니다.

## `apply` 메서드

`apply` 메서드는 함수를 호출할 때 사용되며, 함수를 호출할 때 `this` 값과 인수(arguments)를 설정할 수 있습니다. `apply` 메서드는 함수를 호출하는 대상에 함수와 함께 배열로 묶인 인자(arguments)를 넘깁니다.

다음은 `apply` 메서드의 구문입니다.

```javascript
function.apply(thisArg, [argsArray])
```

- `thisArg`: 함수를 호출할 때 사용할 `this` 값을 지정합니다. 만약 `null` 또는 `undefined`가 제공된 경우, 전역 객체가 `this` 값으로 사용됩니다.
- `argsArray`: 배열로 묶인 실제 인수(arguments)를 지정합니다.

다음은 `apply` 메서드를 사용하는 예제입니다.

```javascript
function greet(name) {
  console.log(`Hello, ${name}! I am ${this.job}.`);
}

const person = {
  job: 'developer'
};

greet.apply(person, ['John']);
```

위의 예제에서 `apply` 메서드는 `greet` 함수를 호출하면서, `person` 객체를 `this` 값으로 설정하고, `['John']` 배열을 인수(arguments)로 전달합니다. 이렇게 `apply` 메서드를 사용하여 함수를 호출하면, `Hello, John! I am developer.`가 출력됩니다.

## `call` 메서드

`call` 메서드는 `apply` 메서드와 비슷하게 함수를 호출할 때 사용됩니다. 다만, `call` 메서드는 인수(arguments)를 배열이 아닌 개별 인자로 전달합니다.

다음은 `call` 메서드의 구문입니다.

```javascript
function.call(thisArg, arg1, arg2, ...)
```

- `thisArg`: 함수를 호출할 때 사용할 `this` 값을 지정합니다. 만약 `null` 또는 `undefined`가 제공된 경우, 전역 객체가 `this` 값으로 사용됩니다.
- `arg1, arg2, ...`: 실제 인수(arguments)를 개별 인자로 지정합니다.

다음은 `call` 메서드를 사용하는 예제입니다.

```javascript
function greet(name) {
  console.log(`Hello, ${name}! I am ${this.job}.`);
}

const person = {
  job: 'developer'
};

greet.call(person, 'John');
```

위의 예제에서 `call` 메서드는 `greet` 함수를 호출하면서, `person` 객체를 `this` 값으로 설정하고, `'John'` 인자를 개별 인자로 전달합니다. 마찬가지로, `Hello, John! I am developer.`가 출력됩니다.

## `bind` 메서드

`bind` 메서드는 함수를 호출하지 않고, 함수를 새로운 함수로 래핑하는 역할을 합니다. `bind` 메서드는 주로 함수의 `this` 값을 영구적으로 설정하려는 경우에 사용됩니다.

다음은 `bind` 메서드의 구문입니다.

```javascript
function.bind(thisArg, arg1, arg2, ...)
```

- `thisArg`: 생성된 새로운 함수에서 사용할 `this` 값을 지정합니다. 만약 `null` 또는 `undefined`가 제공된 경우, 전역 객체가 `this` 값으로 사용됩니다.
- `arg1, arg2, ...`: 새로운 함수에게 전달할 인수(arguments)를 지정합니다.

다음은 `bind` 메서드를 사용하는 예제입니다.

```javascript
function greet(name) {
  console.log(`Hello, ${name}! I am ${this.job}.`);
}

const person = {
  job: 'developer'
};

const greetPerson = greet.bind(person);

greetPerson('John');
```

위의 예제에서 `bind` 메서드는 `greet` 함수를 `person` 객체에 묶어서 새로운 함수 `greetPerson`을 생성합니다. 그 후, `greetPerson` 함수를 호출하면서 `'John'`을 인자로 전달합니다. 결과로 `Hello, John! I am developer.`가 출력됩니다.

## 결론

`apply`, `call`, `bind` 메서드는 자바스크립트에서 함수를 호출하고, `this` 값을 설정하며, 인수(arguments)를 전달하는 데 사용됩니다. `apply` 메서드는 함수를 호출할 때 배열로 묶인 인수를 전달하고, `call` 메서드는 개별 인자로 전달합니다. `bind` 메서드는 호출하지 않고 함수를 새로운 함수로 래핑합니다. 이러한 메서드들은 자바스크립트에서 유용하게 사용되며, 함수의 `this` 값을 명확하게 지정하거나, 특정 인수를 고정하여 새로운 함수를 생성하는 데 도움을 줍니다.