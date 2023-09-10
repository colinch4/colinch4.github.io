---
layout: post
title: "자바스크립트 함수를 인자로 받고 함수를 반환하는 고차 함수 (Higher Order Functions that Take Functions as Arguments and Return Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

고차 함수는 다른 함수를 인자로 받거나 함수를 반환하는 함수를 말합니다. 자바스크립트에서 고차 함수를 사용하는 경우가 많이 있습니다. 그 중에서도 자바스크립트 함수를 인자로 받고 함수를 반환하는 고차 함수는 매우 유용합니다. 이러한 함수를 사용하면 코드의 재사용성을 높이고 복잡한 로직을 간단하고 모듈화된 방식으로 작성할 수 있습니다.

## 고차 함수의 기본 구조

고차 함수는 다음과 같은 기본 구조를 갖습니다.

```javascript
function higherOrderFunction(callback) {
  // 고차 함수 내부 로직
  // 인자로 받은 함수(callback) 실행
  callback();
  
  // 필요에 따라 추가 로직 작성 가능
}
```

위의 코드에서 `higherOrderFunction`은 함수를 인자로 받는 고차 함수입니다. 인자로 받은 함수인 `callback`을 실행하는 내부 로직이 포함되어 있습니다. 필요에 따라 추가적인 로직을 작성할 수도 있습니다.

## 함수를 인자로 받는 고차 함수의 예제

이제 함수를 인자로 받고 함수를 반환하는 고차 함수의 예제를 살펴보겠습니다.

```javascript
function multiplyBy(n) {
  return function(x) {
    return x * n;
  }
}

const multiplyByTwo = multiplyBy(2);
const multiplyByThree = multiplyBy(3);

console.log(multiplyByTwo(4)); // Output: 8
console.log(multiplyByThree(4)); // Output: 12
```

위의 코드는 `multiplyBy`라는 고차 함수입니다. 이 함수는 인자로 받은 숫자 `n`을 곱하는 함수를 반환합니다. 반환된 함수를 `multiplyByTwo`와 `multiplyByThree` 변수에 할당하여 사용할 수 있습니다. 이후 해당 변수를 호출하여 숫자를 곱하는 동작을 수행할 수 있습니다. 위의 예제에서 `multiplyByTwo(4)`는 4에 2를 곱한 결과인 8을 반환하며, `multiplyByThree(4)`는 4에 3을 곱한 결과인 12를 반환합니다.

이 예제는 함수를 인자로 받아서 필요한 로직을 처리하고 그 결과로 함수를 반환하는 고차 함수의 간단한 예시입니다. 이러한 고차 함수를 사용하면 코드의 재사용성과 가독성을 높일 수 있습니다.

## 정리

자바스크립트에서 함수를 인자로 받고 함수를 반환하는 고차 함수는 유용한 개념입니다. 이를 활용하여 코드를 모듈화하고 재사용성을 높일 수 있습니다. 함수를 다루는 이러한 기술은 자바스크립트에서 함수형 프로그래밍 개념을 활용하는 데 중요한 역할을 합니다. 반복적인 코드를 방지하고 유연성을 갖춘 소프트웨어 개발을 위해 고차 함수를 학습하고 활용하는 것을 권장합니다.