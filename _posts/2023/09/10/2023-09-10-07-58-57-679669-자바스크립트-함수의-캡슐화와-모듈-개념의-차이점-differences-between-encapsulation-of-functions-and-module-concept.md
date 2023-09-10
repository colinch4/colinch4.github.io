---
layout: post
title: "자바스크립트 함수의 캡슐화와 모듈 개념의 차이점 (Differences between Encapsulation of Functions and Module Concept)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 다양한 프로그래밍 패러다임을 지원하는 동적인 언어입니다. 그 중에서도 함수의 캡슐화와 모듈 개념은 코드의 가독성과 유지보수성을 향상시키기 위해 사용되는 중요한 개념입니다. 이번 포스트에서는 함수의 캡슐화와 모듈 개념의 차이점을 살펴보겠습니다.

## 함수의 캡슐화

함수의 캡슐화란, 관련된 코드를 하나의 함수로 묶어서 외부에 노출되지 않도록 하는 것을 말합니다. 이렇게 하면 코드의 작성과 관리가 용이해지며, 함수 내부에 작성된 변수와 함수는 외부에서 접근할 수 없습니다. 

자바스크립트에서 함수의 캡슐화는 주로 **클로저(Closure)**를 활용하여 구현됩니다. 함수 내부에 선언된 변수들은 함수 외부에서 접근할 수 없으며, 함수 내에서 정의한 내부 함수는 외부에서 호출할 수 없습니다. 이러한 구조를 통해 데이터의 보호와 함수의 독립성을 확보할 수 있습니다.

아래는 함수의 캡슐화를 구현한 예제 코드입니다.

```javascript
function counter() {
  let count = 0;

  function increment() {
    count++;
    console.log(count);
  }

  return increment;
}

const incrementCount = counter();
incrementCount(); // 1
incrementCount(); // 2
```

위 예제에서 `counter` 함수는 `count` 변수를 내부에 선언하고, `increment` 함수를 반환합니다. 이렇게 반환된 `incrementCount` 함수는 `count` 변수에 접근하여 값을 증가시킬 수 있습니다. 하지만 외부에서는 `count` 변수에 접근할 수 없으므로 데이터의 보호가 가능해집니다.

## 모듈 개념

모듈 개념은 함수의 캡슐화보다 한 단계 더 나아가, 한 개 이상의 연관된 함수와 변수를 하나의 단위로 묶어서 외부에 노출시키는 것을 의미합니다. 모듈은 일종의 독립적인 단위로, 필요한 함수와 변수만 외부에 공개함으로써 코드의 격리와 재사용성을 높입니다.

ES6부터 자바스크립트는 모듈 개념을 공식적으로 지원하기 시작했습니다. 모듈은 다른 모듈에서 사용할 수 있는 **export**와 다른 모듈의 기능을 가져올 수 있는 **import** 구문으로 정의할 수 있습니다.

아래는 모듈 개념을 활용한 예제 코드입니다.

```javascript
// 모듈 A
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

// 모듈 B
import { add, subtract } from './moduleA';

console.log(add(2, 3)); // 5
console.log(subtract(5, 2)); // 3
```

위 예제에서 `export` 키워드를 사용하여 모듈 A에서 `add`와 `subtract` 함수를 외부에 공개합니다. 이후 모듈 B에서는 `import` 구문을 사용하여 모듈 A의 기능을 가져와 사용할 수 있습니다.

## 결론

함수의 캡슐화와 모듈 개념은 자바스크립트에서 코드의 구조화와 유지보수를 위해 사용되는 중요한 개념입니다. 함수의 캡슐화는 관련된 코드를 하나의 함수로 묶어서 외부에 노출되지 않도록 하는 것을 의미하며, 모듈 개념은 함수와 변수들을 하나의 단위로 묶어서 외부에 공개하여 코드의 격리와 재사용성을 향상시킵니다. 

이러한 개념을 적절하게 활용하면 자바스크립트 코드의 가독성과 유지보수성을 크게 향상시킬 수 있습니다.