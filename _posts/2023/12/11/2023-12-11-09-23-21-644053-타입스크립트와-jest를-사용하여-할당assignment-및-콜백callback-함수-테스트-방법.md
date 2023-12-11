---
layout: post
title: "[typescript] 타입스크립트와 Jest를 사용하여 할당(Assignment) 및 콜백(Callback) 함수 테스트 방법"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

타입스크립트는 자바스크립트의 확장된 버전으로, 정적 타입을 지원하여 코드의 안정성을 높이고 개발 생산성을 향상시킵니다. Jest는 페이스북에서 만든 테스트 프레임워크로, JavaScript 및 타입스크립트 프로젝트에서 간단하고 효율적으로 테스트를 작성할 수 있도록 도와줍니다.

이번 글에서는 타입스크립트와 Jest를 사용하여 할당 및 콜백 함수를 테스트하는 방법을 알아보겠습니다.

## 1. 할당(Assignment) 함수 테스트 방법

할당 함수는 변수에 할당되는 함수를 의미합니다. 예를 들어, 다음과 같이 할당 함수를 작성해보겠습니다.

```typescript
// 할당 함수
function add(a: number, b: number): number {
  return a + b;
}
```

이제 Jest를 사용하여 이 할당 함수를 테스트해보겠습니다.

```typescript
// 할당 함수 테스트
test('add 함수 테스트', () => {
  expect(add(1, 2)).toBe(3);
  expect(add(5, 5)).toBe(10);
});
```

위 코드에서 `test` 함수는 테스트 케이스를 정의하고, `expect` 함수는 특정 값에 대한 기대 값을 설정합니다. Jest는 이러한 설정에 따라 테스트를 수행하고 결과를 반환합니다. 

## 2. 콜백(Callback) 함수 테스트 방법

콜백 함수는 다른 함수의 인자로 전달되는 함수를 의미합니다. 예를 들어, 다음과 같이 콜백 함수를 작성해보겠습니다.

```typescript
// 콜백 함수
function multiply(a: number, b: number, callback: (result: number) => void) {
  const result = a * b;
  callback(result);
}
```

Jest를 사용하여 이 콜백 함수를 테스트할 때에는 `mock` 함수를 사용하여 콜백 함수가 올바르게 호출되는지 테스트할 수 있습니다.

```typescript
// 콜백 함수 테스트
test('multiply 함수 테스트', () => {
  const mockCallback = jest.fn();
  multiply(2, 3, mockCallback);
  expect(mockCallback).toHaveBeenCalledWith(6);
});
```

위 코드에서 `mockCallback`은 가짜 콜백 함수로, `jest.fn()`을 사용하여 생성합니다. 이 가짜 콜백 함수를 통해 `multiply` 함수가 올바르게 동작하는지를 테스트합니다.

이처럼 타입스크립트와 Jest를 사용하여 할당 및 콜백 함수를 간단하게 테스트할 수 있습니다.

참고 문헌:
- Jest 공식 문서: https://jestjs.io/
- 타입스크립트 공식 문서: https://www.typescriptlang.org/docs/