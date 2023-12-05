---
layout: post
title: "[javascript] setTimeout과 setInterval의 인자로 전달할 수 있는 값"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

`setTimeout`과 `setInterval`은 자바스크립트에서 비동기적인 작업을 실행하기 위해 사용되는 함수입니다. 이 두 함수는 실행할 콜백 함수와 지연 시간을 인자로 받습니다. 하지만 이 외에도 다양한 값들을 인자로 전달할 수 있습니다.

### 1. 콜백 함수

`setTimeout`과 `setInterval`의 첫 번째 인자로 실행할 콜백 함수를 전달할 수 있습니다. 이 콜백 함수는 지정된 시간이 경과한 후에 실행됩니다.

```javascript
setTimeout(() => {
  console.log("Hello, world!");
}, 1000);
```

### 2. 문자열로 표현된 코드

또한, `setTimeout`과 `setInterval`의 첫 번째 인자로 문자열로 표현된 코드를 전달할 수도 있습니다. 이는 동적으로 실행하고자 하는 코드를 문자열로 작성할 수 있는 간편한 방법입니다.

```javascript
setTimeout("console.log('Hello, world!')", 1000);
```

### 3. 함수 참조

`setTimeout`과 `setInterval`은 함수의 참조를 전달할 수도 있습니다. 이는 특정 함수를 지연 시간 후에 실행하고자 할 때 유용합니다.

```javascript
function sayHello() {
  console.log("Hello, world!");
}

setTimeout(sayHello, 1000);
```

### 4. 함수 호출 시 인자 전달

콜백 함수를 실행할 때 인자를 전달하고 싶다면, `setTimeout`과 `setInterval`의 인자로 익명 함수를 전달하여 인자를 포함한 콜백을 실행할 수 있습니다.

```javascript
setTimeout(() => {
  console.log("Hello, " + name + "!");
}, 1000);
```

위 예제에서 `name`은 인자로 전달되는 변수입니다.

### 5. 인자로 전달할 값이 있는 함수 참조

만약 특정 함수에 인자를 전달하고 싶다면, 함수의 참조를 전달하고 인자를 포함한 익명 함수를 만들어 `setTimeout`과 `setInterval`의 인자로 전달할 수 있습니다.

```javascript
function sayHello(name) {
  console.log("Hello, " + name + "!");
}

setTimeout(sayHello.bind(null, "John"), 1000);
```

위 예제에서 `sayHello` 함수에 `John`이라는 인자를 전달하려고 `bind` 메소드를 사용하여 새로운 함수를 생성한 후에 전달하고 있습니다.

`setTimeout`과 `setInterval`의 인자로 전달 가능한 값들은 다양하며 위의 예시만 일부이므로 다른 값들도 가능함에 유의해야 합니다. 자바스크립트의 유연성을 이용하여 다양한 비동기 작업을 실행할 수 있습니다.

---

참고 문서:
- [setTimeout - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [setInterval - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)