---
layout: post
title: "[javascript] Ramda의 고차 함수(Higher-Order Functions) 활용"
description: " "
date: 2023-11-30
tags: [javascript]
comments: true
share: true
---

고차 함수는 함수를 인자로 받거나 함수를 리턴하는 함수를 말합니다. 이러한 고차 함수를 사용하면 코드의 재사용성과 가독성을 높일 수 있습니다. 이번 포스트에서는 자바스크립트 라이브러리인 Ramda를 사용하여 고차 함수를 활용하는 방법에 대해 알아보겠습니다.

## 1. `map` 함수

먼저, `map` 함수는 배열 요소에 함수를 적용하여 새로운 배열을 생성하는 고차 함수입니다. Ramda의 `map` 함수는 기존의 `Array.prototype.map` 함수와 비슷하지만 몇 가지 차이점이 있습니다.

```javascript
const numbers = [1, 2, 3, 4, 5];

const square = x => x * x;

const squaredNumbers = R.map(square, numbers);

console.log(squaredNumbers); // [1, 4, 9, 16, 25]
```

위의 예시에서 `R.map(square, numbers)`는 `numbers` 배열의 모든 요소에 `square` 함수를 적용하여 새로운 배열을 생성합니다. 

## 2. `filter` 함수

다음으로, `filter` 함수는 배열에서 특정 조건을 만족하는 요소만을 필터링하여 새로운 배열을 생성하는 고차 함수입니다.

```javascript
const numbers = [1, 2, 3, 4, 5];

const isEven = x => x % 2 === 0;

const evenNumbers = R.filter(isEven, numbers);

console.log(evenNumbers); // [2, 4]
```

위의 예시에서 `R.filter(isEven, numbers)`는 `numbers` 배열에서 짝수인 요소만을 필터링하여 새로운 배열을 생성합니다.

## 3. `compose` 함수

마지막으로, `compose` 함수는 여러 개의 함수를 조합하여 하나의 함수로 만드는 고차 함수입니다. 이를 통해 함수들을 연결하여 코드의 가독성을 높이고 중첩된 함수를 피할 수 있습니다.

```javascript
const add1 = x => x + 1;
const multiply2 = x => x * 2;
const subtract3 = x => x - 3;

const compute = R.compose(subtract3, multiply2, add1);

console.log(compute(5)); // (5 + 1) * 2 - 3 = 9
```

위의 예시에서 `R.compose(subtract3, multiply2, add1)`은 `add1`, `multiply2`, `subtract3` 함수들을 차례로 적용하는 함수를 생성합니다. `compute` 함수를 호출하면 `5`를 인자로 받고, `add1`, `multiply2`, `subtract3` 함수들이 차례대로 적용되어 결과값 `9`를 반환합니다.

## 결론

Ramda의 고차 함수를 활용하면 코드의 재사용성과 가독성을 높일 수 있습니다. `map`, `filter`, `compose` 함수 등 다양한 고차 함수를 활용하면 더욱 효율적인 코드를 작성할 수 있습니다. 좀 더 자세한 사용법은 Ramda 공식 문서를 참고하시기 바랍니다.

## 참고 자료

- [Ramda 공식 문서](https://ramdajs.com/docs/)
- [JavaScript Higher-Order Functions Explained with Examples](https://www.freecodecamp.org/news/higher-order-functions-in-javascript/)