---
layout: post
title: "[javascript] 자바스크립트에서 함수형 프로그래밍(Functional Programming) 개념과 적용 방법"
description: " "
date: 2023-12-26
tags: [javascript]
comments: true
share: true
---

함수형 프로그래밍은 **함수를 일급 객체로 취급**하고, **불변성(Immutability)**과 **순수 함수(Pure Function)**를 강조하는 프로그래밍 패러다임입니다. 이번 포스트에서는 자바스크립트에서의 함수형 프로그래밍 개념과 적용 방법에 대해 살펴보도록 하겠습니다.

## 1. 함수형 프로그래밍의 기본 개념

함수형 프로그래밍은 **부작용이 없는 순수 함수**를 중심에 두고, **데이터 불변성**을 강조합니다. 여기서 **순수 함수**는 동일한 입력마다 항상 동일한 출력을 반환하며, 외부 상태에 의존하지 않는 함수를 말합니다. 이러한 특성으로 함수형 프로그래밍은 예측 가능하고 테스트하기 쉬운 코드를 작성할 수 있습니다.

## 2. 자바스크립트에서의 함수형 프로그래밍 적용 방법

### 2.1. 순수 함수 활용

순수 함수를 활용하여 외부 상태의 변경을 최소화하고, 코드의 예측 가능성을 높일 수 있습니다. 순수 함수에 대한 예시로는 다음과 같습니다.
```javascript
// 순수 함수 예시
function add(a, b) {
  return a + b;
}
```
위의 `add` 함수는 외부 상태에 의존하지 않고, 동일한 입력에 대해 항상 동일한 결과를 반환합니다.

### 2.2. 불변성 유지

자바스크립트에서는 객체나 배열의 불변성을 유지하기 위해 `Object.freeze`나 불변성 라이브러리인 `Immutable.js`를 활용할 수 있습니다.

```javascript
// Object.freeze를 사용한 불변성 유지 예시
const person = Object.freeze({ name: 'Alice', age: 30 });
person.age = 31; // TypeError: Cannot assign to read only property 'age' of object
```

### 2.3. 고차 함수 활용

고차 함수는 다른 함수를 인자로 받거나 함수를 반환하는 함수를 말합니다. 고차 함수를 활용하여 함수형 프로그래밍의 개념을 적용할 수 있습니다.

```javascript
// 고차 함수 예시
function multiplyBy(factor) {
  return function (number) {
    return number * factor;
  };
}

const multiplyByTwo = multiplyBy(2);
console.log(multiplyByTwo(5)); // 10
```

함수형 프로그래밍은 코드의 유지보수성과 가독성을 높이고, **동시성 처리**와 **병렬 처리**에도 유용합니다. 자바스크립트에서 함수형 프로그래밍을 적용하여 **객체 간 상태 변이를 최소화**하고, **테스트 가능한 코드**를 작성할 수 있습니다.

함수형 프로그래밍은 모든 프로그래밍 언어에서 적용 가능하며, **람다 계산법**이나 **카테고리 이론** 등과 함께 공부하면 더 깊이있게 이해할 수 있습니다.

함수형 프로그래밍을 자바스크립트에서 적용하여 **유연하고 안정적인 애플리케이션**을 만들 수 있습니다.

## 참고 링크
- [MDN Web Docs - 함수형 프로그래밍](https://developer.mozilla.org/ko/docs/Web/JavaScript/Functional_programming)
- [이일우의 함수형 자바스크립트 프로그래밍](https://yjmanito.tistory.com/32)