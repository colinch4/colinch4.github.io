---
layout: post
title: "[typescript] Jest에서의 어설션(Assertion)과 Matchers의 개념 및 활용법"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

Jest는 JavaScript 및 TypeScript용으로 설계된 강력한 테스트 프레임워크입니다. Jest를 사용하면 코드의 동작을 검증하고 테스트할 수 있습니다. 이를 위해 Jest는 어설션(Assertion)과 Matchers를 제공하는데, 이를 통해 코드의 정확성을 확인할 수 있습니다.

이 포스트에서는 Jest에서의 어설션과 Matchers의 개념과 활용법에 대해 알아보겠습니다.

## 어설션(Assertion) 개념

어설션이란 특정 조건이 참인지 검사하는 것을 말합니다. Jest에서의 어설션은 코드의 특정 부분이 예상대로 동작하는지 확인하는 데 사용됩니다. 예를 들어, 어떤 함수가 특정 입력에 대해 올바른 결과를 반환하는지 확인하려면 어설션을 사용합니다.

```typescript
test('두 값이 같은지 확인', () => {
  expect(2 + 2).toBe(4);
});
```

위 코드에서 `expect(2 + 2).toBe(4)`는 2 + 2가 4와 같은지 확인하는 어설션입니다.

## Matchers 개념

Matchers는 어설션을 보다 유용하게 만들어주는 Jest의 기능입니다. Matchers를 사용하면 다양한 종류의 어설션을 작성할 수 있습니다. Jest는 다양한 Matchers를 제공하고, 사용자가 직접 Matchers를 확장할 수도 있습니다.

```typescript
test('배열에 특정 값이 포함되는지 확인', () => {
  expect([1, 2, 3]).toContain(2);
});
```

위 코드에서 `expect([1, 2, 3]).toContain(2)`는 배열에 2가 포함되어 있는지 확인하는 어설션으로, `toContain`이라는 Matcher를 사용하고 있습니다.

## Matchers 활용법

Matchers를 활용하면 다양한 형태의 어설션을 작성할 수 있습니다. 몇 가지 일반적인 Matchers를 살펴보겠습니다.

- `toBe(value)`: 값이 정확히 `value`와 같은지 확인
- `toEqual(value)`: 값이 `value`와 동등한지 확인
- `not`: 어설션이 반대로 동작하도록 설정

```typescript
test('두 값이 같은지 확인', () => {
  expect(2 + 2).toBe(4);
});

test('두 객체가 동일한 내용을 갖는지 확인', () => {
  expect({ a: 1, b: 2 }).toEqual({ a: 1, b: 2 });
});

test('두 값이 같지 않은지 확인', () => {
  expect(2 + 2).not.toBe(5);
});
```

위 코드는 각각 `toBe`, `toEqual`, 그리고 `not` Matcher를 활용한 어설션 예제입니다.

## 마무리

Jest의 어설션과 Matchers를 활용하면 코드의 정확성을 보다 쉽게 검증할 수 있습니다. 이를 통해 안정적인 소프트웨어를 개발하는 데 도움이 됩니다.

이상으로 Jest에서의 어설션과 Matchers에 대한 개념과 활용법에 대해 알아보았습니다.

참고문헌:
[Jest 공식 문서](https://jestjs.io/docs/en/expect)