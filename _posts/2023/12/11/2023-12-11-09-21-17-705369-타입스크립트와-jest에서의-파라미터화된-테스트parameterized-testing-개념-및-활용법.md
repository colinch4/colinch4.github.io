---
layout: post
title: "[typescript] 타입스크립트와 Jest에서의 파라미터화된 테스트(Parameterized Testing) 개념 및 활용법"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

테스트 케이스를 작성할 때, 비슷한 테스트 코드를 반복 작성하는 것은 비효율적일 수 있습니다. 파라미터화된 테스트를 사용하면 이러한 문제를 해결할 수 있습니다. 이번 글에서는 타입스크립트와 Jest 환경에서 파라미터화된 테스트를 어떻게 작성하고 활용하는지 알아보겠습니다.

## 1. 파라미터화된 테스트란?

파라미터화된 테스트(Parameterized Testing)는 동일한 테스트를 다양한 입력값을 사용하여 여러번 실행하는 것을 말합니다. 이를 통해 테스트 코드의 중복을 줄이고 효율적으로 테스트 케이스를 관리할 수 있습니다.

## 2. Jest에서의 파라미터화된 테스트

Jest에서는 `test.each`나 `test.each.each`를 사용하여 파라미터화된 테스트를 작성할 수 있습니다. 

다음은 간단한 덧셈 함수를 테스트하는 예제입니다.
```typescript
test.each([
  [1, 1, 2],
  [1, 2, 3],
  [2, 2, 4],
])('덧셈 함수는 두 숫자를 더하여 올바른 결과를 반환해야 합니다', (a, b, expected) => {
  expect(sum(a, b)).toBe(expected);
});
```

위 예제에서 `test.each`는 배열의 각 요소를 이용하여 테스트를 반복 수행합니다. 

## 3. 타입스크립트와의 통합

타입스크립트와 함께 Jest를 사용할 때, 파라미터화된 테스트를 작성할 때 반복적인 타입 선언을 줄일 수 있습니다. 

다음은 타입스크립트와 Jest를 함께 사용하여 파라미터화된 테스트를 작성하는 예제입니다.
```typescript
type TestData = [number, number, number];

const testCases: TestData[] = [
  [1, 1, 2],
  [1, 2, 3],
  [2, 2, 4],
];

test.each(testCases)('덧셈 함수는 두 숫자를 더하여 올바른 결과를 반환해야 합니다', (a, b, expected) => {
  expect(sum(a, b)).toBe(expected);
});
```

위 예제에서 `TestData` 타입을 정의하고, `testCases` 배열에 테스트 데이터를 저장하여 코드의 재사용성과 가독성을 높였습니다.

## 4. 결론

파라미터화된 테스트는 중복된 테스트 코드를 줄일 뿐만 아니라, 테스트 케이스를 보다 효율적으로 관리하는데 도움을 줍니다. 타입스크립트와 Jest를 함께 사용할 때 효율적으로 파라미터화된 테스트를 작성하고 활용하여 코드의 품질을 향상시킬 수 있습니다.