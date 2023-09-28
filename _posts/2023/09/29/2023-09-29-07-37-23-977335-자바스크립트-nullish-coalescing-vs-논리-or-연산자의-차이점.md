---
layout: post
title: "자바스크립트 Nullish Coalescing vs. 논리 OR 연산자의 차이점"
description: " "
date: 2023-09-29
tags: [javascript, programming]
comments: true
share: true
---

자바스크립트에서 Nullish Coalescing과 논리 OR 연산자는 비슷해 보이지만, 실제로는 다른 동작을 수행합니다. 이번 블로그 포스트에서는 이 두 가지 연산자의 차이점과 어떤 상황에서 어떤 연산자를 사용해야 하는지 알아보겠습니다.

## Nullish Coalescing 연산자 (??)

Nullish Coalescing 연산자는 좌항의 값이 null 또는 undefined 인 경우에만 우항의 값을 반환합니다. 그 외의 경우에는 좌항의 값을 그대로 반환합니다. Nullish Coalescing 연산자는 좌항이 falsy 값 (false, 0, '', NaN)인 경우에도 우항의 값을 반환하지 않습니다.

다음은 Nullish Coalescing 연산자의 예시 코드입니다:

```javascript
const name = null ?? 'Unknown';
console.log(name); // Output: Unknown

const age = undefined ?? 30;
console.log(age); // Output: 30

const isActive = false ?? true;
console.log(isActive); // Output: false
```

## 논리 OR 연산자 (||)

논리 OR 연산자는 좌항의 값이 falsy 값이면 우항의 값을 반환합니다. Nullish Coalescing 연산자와는 달리, 좌항의 값이 null이나 undefined가 아니라면 무조건 우항의 값을 반환합니다.

다음은 논리 OR 연산자의 예시 코드입니다:

```javascript
const name = null || 'Unknown';
console.log(name); // Output: Unknown

const age = undefined || 30;
console.log(age); // Output: 30

const isActive = false || true;
console.log(isActive); // Output: true
```

## 언제 어떤 연산자를 사용해야 할까요?

Nullish Coalescing 연산자를 사용하는 것이 좋은 경우는 변수가 null 또는 undefined 인 경우에만 다른 값을 할당하고자 할 때입니다. 예를 들어, 사용자의 이름이 null인 경우에만 "Unknown"으로 값을 설정하고 싶다면 Nullish Coalescing 연산자를 사용할 수 있습니다.

논리 OR 연산자는 좌항이 falsy 값이면 다른 값을 할당하고자 할 때 사용될 수 있습니다. 예를 들어, 사용자의 나이가 0인 경우에만 기본값인 30을 할당하고 싶다면 논리 OR 연산자를 사용할 수 있습니다.

## 결론

자바스크립트에서 Nullish Coalescing 연산자와 논리 OR 연산자는 좌항의 값과 우항의 값이 다를 수 있는 상황에서 다른 동작을 수행합니다. Nullish Coalescing 연산자는 좌항이 null 또는 undefined 인 경우에만 우항의 값을 반환하고, 논리 OR 연산자는 좌항이 falsy 값일 경우 우항의 값을 반환합니다. 앞으로 코딩하면서 이 두 가지 연산자의 차이점을 알고 적절하게 사용하는 것이 중요합니다.

#javascript #programming