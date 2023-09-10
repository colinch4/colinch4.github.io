---
layout: post
title: "자바스크립트 배열 메서드(forEach, map, filter, reduce 등)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 강력한 배열 메서드를 제공하여 배열을 효과적으로 다룰 수 있도록 도와줍니다. 이러한 배열 메서드는 데이터 처리 및 변형에 유용하며, 개발자들이 더욱 쉽고 간결한 코드를 작성할 수 있게 해줍니다. 다음은 몇 가지 중요한 자바스크립트 배열 메서드에 대한 소개입니다.

## forEach 메서드

`forEach` 메서드는 배열의 각 요소에 대해 주어진 함수를 실행합니다. 이 메서드는 일반적으로 배열의 각 요소를 순회하거나 각 요소에 대한 특정 동작을 수행할 때 사용됩니다.

```javascript
const numbers = [1, 2, 3, 4, 5];

numbers.forEach(num => {
  console.log(num);
});
```

## map 메서드

`map` 메서드는 배열의 각 요소에 대해 주어진 함수를 실행하고, 새로운 배열을 반환합니다. 반환된 배열은 원본 배열과 같은 길이를 가지며, 각 요소는 주어진 함수의 반환값으로 채워집니다.

```javascript
const numbers = [1, 2, 3, 4, 5];

const doubledNumbers = numbers.map(num => {
  return num * 2;
});

console.log(doubledNumbers); // [2, 4, 6, 8, 10]
```

## filter 메서드

`filter` 메서드는 주어진 함수의 반환값이 `true`인 배열의 요소만 추출하여 새로운 배열로 반환합니다. 이 메서드는 조건을 만족하는 요소들로 새로운 배열을 만들 때 사용됩니다.

```javascript
const numbers = [1, 2, 3, 4, 5];

const evenNumbers = numbers.filter(num => {
  return num % 2 === 0;
});

console.log(evenNumbers); // [2, 4]
```

## reduce 메서드

`reduce` 메서드는 배열의 각 요소를 순회하며 주어진 함수를 적용하여, 하나의 결과값을 반환합니다. 이 메서드는 배열의 모든 요소를 결합하거나, 배열의 요소들을 연산하거나, 배열의 값을 축적하는 데 사용됩니다.

```javascript
const numbers = [1, 2, 3, 4, 5];

const sum = numbers.reduce((acc, curr) => {
  return acc + curr;
}, 0);

console.log(sum); // 15
```

위에서 설명한 메서드 외에도 자바스크립트는 다양한 배열 메서드를 제공합니다. 이러한 배열 메서드들은 매우 유용하며, 개발자들은 이를 적절하게 활용하여 보다 효과적인 코드를 작성할 수 있습니다.