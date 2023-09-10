---
layout: post
title: "자바스크립트 캡슐화와 캡처링 (Encapsulation and Capturing)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 다른 프로그래밍 언어들과 달리, **객체 지향 프로그래밍**에서의 캡슐화와 캡처링을 다른 방법으로 구현합니다. 

## 캡슐화 (Encapsulation)

캡슐화는 객체의 데이터와 기능을 하나로 묶는 것을 의미합니다. 이를 통해 정보 은닉, 데이터 보호 및 재사용성을 증가시킬 수 있습니다.

자바스크립트에서는 기본적으로 **클로저 (Closure)** 를 활용하여 캡슐화를 구현할 수 있습니다. 아래는 캡슐화된 객체 예시입니다.

```javascript
function createCounter() {
  let count = 0;

  function increment() {
    count++;
    console.log(count);
  }

  function decrement() {
    count--;
    console.log(count);
  }

  return {
    increment,
    decrement
  };
}

const counter = createCounter();
counter.increment(); // 1
counter.increment(); // 2
counter.decrement(); // 1
```

위 코드에서 `createCounter` 함수는 `count` 변수와 `increment`, `decrement` 함수를 가지고 있는 객체를 반환합니다. 이를 통해 `count` 변수는 외부에서 직접 접근할 수 없으며, `increment`와 `decrement` 함수를 통해서만 값을 변경할 수 있습니다.

## 캡처링 (Capturing)

캡처링은 클로저를 활용하여 외부 함수 범위에 있는 변수를 기억하는 것을 의미합니다. 이를 통해 함수 내에서 외부 변수의 값을 계속해서 사용할 수 있습니다.

아래는 캡처링을 활용한 예시입니다.

```javascript
function createMultiplier(x) {
  return function(y) {
    return x * y;
  };
}

const multiplyByTwo = createMultiplier(2);
const multiplyByThree = createMultiplier(3);

console.log(multiplyByTwo(5)); // 10
console.log(multiplyByThree(5)); // 15
```

위 코드에서 `createMultiplier` 함수는 주어진 숫자 `x` 값을 기억하는 클로저를 반환합니다. 이를 통해 `multiplyByTwo`와 `multiplyByThree`는 각각 주어진 숫자에 `2`와 `3`을 곱하는 함수가 됩니다.

## 결론

자바스크립트에서는 클로저를 활용하여 캡슐화와 캡처링을 구현할 수 있습니다. 이를 통해 객체의 정보를 보호하고 재사용성을 높일 수 있습니다. 캡슐화와 캡처링은 대규모 애플리케이션 개발에서 중요한 개념이므로, 그 활용법을 익혀두는 것이 좋습니다.