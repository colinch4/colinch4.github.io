---
layout: post
title: "자바스크립트 배열 메서드(forEach, map, filter, reduce 등)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 배열을 다루는데 많은 유용한 메서드들을 제공합니다. 이러한 배열 메서드를 사용하면 배열을 반복하고 각 항목에 작업을 수행하거나, 배열을 변형하거나 필터링하여 새로운 배열을 생성할 수 있습니다. 이번 포스트에서는 일반적으로 사용되는 자바스크립트 배열 메서드들에 대해 알아보겠습니다.

## forEach()

`forEach()` 메서드는 배열의 각 항목에 대해 콜백 함수를 실행합니다. 이 메서드는 주어진 배열을 변경하지 않고, 단순히 각 항목에 대해 주어진 동작을 수행합니다.

```javascript
const numbers = [1, 2, 3, 4, 5];

numbers.forEach(num => {
  console.log(num * 2);
});
```

위의 예제에서 `forEach()` 메서드를 사용하여 numbers 배열의 각 항목에 2를 곱한 결과를 콘솔에 출력합니다.

## map()

`map()` 메서드는 배열의 모든 항목에 대해 주어진 콜백 함수를 실행하고, 각 항목에 대한 새로운 값을 반환하는 새로운 배열을 생성합니다. 원본 배열은 변경되지 않습니다.

```javascript
const numbers = [1, 2, 3, 4, 5];

const doubled = numbers.map(num => {
  return num * 2;
});

console.log(doubled); // [2, 4, 6, 8, 10]
```

위의 예제에서 `map()` 메서드를 사용하여 numbers 배열의 각 항목에 2를 곱한 결과를 새로운 배열로 생성합니다.

## filter()

`filter()` 메서드는 주어진 조건에 만족하는 배열의 항목들로만 새로운 배열을 생성합니다. 조건을 만족하지 않는 항목은 새로운 배열에 포함되지 않습니다.

```javascript
const numbers = [1, 2, 3, 4, 5];

const evenNumbers = numbers.filter(num => {
  return num % 2 === 0;
});

console.log(evenNumbers); // [2, 4]
```

위의 예제에서 `filter()` 메서드를 사용하여 numbers 배열에서 짝수만 추출하여 새로운 배열로 생성합니다.

## reduce()

`reduce()` 메서드는 배열의 항목들을 하나의 값으로 줄이는 데 사용됩니다. 콜백 함수를 통해 이전 값을 유지하면서 배열의 항목들을 처리하고 최종 결과를 반환합니다.

```javascript
const numbers = [1, 2, 3, 4, 5];

const sum = numbers.reduce((total, num) => {
  return total + num;
}, 0);

console.log(sum); // 15
```

위의 예제에서 `reduce()` 메서드를 사용하여 numbers 배열의 모든 항목을 합산하여 최종 합계를 반환합니다.

## 기타 배열 메서드들

위에서 다룬 메서드 외에도 자바스크립트는 다른 유용한 배열 메서드들을 제공합니다. 여기에는 `some()`, `every()`, `find()`, `findIndex()` 등이 있습니다. 이러한 메서드는 배열을 조작하고 새로운 값을 생성하는 데 유용합니다.

자바스크립트의 배열 메서드를 이용하면 반복문을 사용하지 않고도 배열을 다룰 수 있습니다. 이는 코드의 가독성을 향상시키고 작업을 간결하게 만들어줍니다. 이러한 배열 메서드들을 적절하게 활용하여 자바스크립트의 배열을 효율적으로 다루는 방법을 익혀보세요.