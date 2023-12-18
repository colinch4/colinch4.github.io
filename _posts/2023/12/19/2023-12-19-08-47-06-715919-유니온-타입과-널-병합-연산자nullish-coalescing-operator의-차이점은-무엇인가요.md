---
layout: post
title: "[typescript] 유니온 타입과 널 병합 연산자(Nullish Coalescing Operator)의 차이점은 무엇인가요?"
description: " "
date: 2023-12-19
tags: [typescript]
comments: true
share: true
---

### 유니온 타입
유니온 타입(Union Types)은 여러 타입 중 하나가 될 수 있는 값을 선언할 때 사용됩니다. 예를 들어, `number | string`은 숫자 혹은 문자열이 될 수 있는 값을 나타냅니다.

예시:
```typescript
function displayData(value: number | string) {
    console.log(value);
}

displayData(10); // 유효
displayData("Hello"); // 유효
displayData(true); // 무효 - 유니온 타입에 포함되지 않는 값
```

### 널 병합 연산자 (Nullish Coalescing Operator)
널 병합 연산자(`??`)는 피연산자가 `null` 또는 `undefined`인 경우 대체값으로 사용됩니다. 이를테면, `a ?? b`는 `a`가 `null` 또는 `undefined`이면 `b`를 반환하고, 그렇지 않으면 `a`를 반환합니다.

예시:
```typescript
const result = userInput ?? "기본값";
console.log(result);
```

따라서, 유니온 타입과 널 병합 연산자는 서로 다른 용도에 사용되며, 각각 다른 상황에서 유용합니다.

자세한 정보는 TypeScript 공식 문서를 참고하시기 바랍니다.
- [유니온 타입 공식 문서](https://www.typescriptlang.org/docs/handbook/unions-and-intersections.html)
- [널 병합 연산자 공식 문서](https://www.typescriptlang.org/docs/handbook/releases/overview.html#nullish-coalescing)