---
layout: post
title: "[typescript] 타입 오류(type error)와 타입 검사(type checking)"
description: " "
date: 2023-12-20
tags: [typescript]
comments: true
share: true
---

TypeScript는 JavaScript의 확장으로, 정적 타입 시스템을 제공하여 코드의 안정성과 신뢰성을 높입니다. 그러나 때때로 TypeScript 코드에서도 **타입 오류**가 발생할 수 있습니다. 이러한 오류를 해결하고 더욱 견고한 코드를 작성하기 위해서는 **타입 검사**의 개념을 잘 이해해야 합니다.

## 타입 오류 (Type Errors)

TypeScript에서 **타입 오류**는 코드에서 올바르지 않은 타입을 사용하거나, 타입 관련 오작동이 발생했을 때 발생합니다. 예를 들어, 숫자 타입을 사용해야 하는 곳에 문자열을 전달하거나, 존재하지 않는 프로퍼티에 접근하려고 할 때 타입 오류가 발생할 수 있습니다.

```typescript
// 숫자 타입을 기대하지만, 문자열을 전달하므로 타입 오류가 발생합니다
function greet(name: number) {
  console.log(`Hello, ${name}`);
}
greet('John'); // 타입 오류: 'John'은 숫자 타입이 아닙니다
```

## 타입 검사 (Type Checking)

TypeScript는 컴파일 시점에서 코드의 **타입 검사**를 수행하여 잠재적인 타입 오류를 발견합니다. 다양한 타입 검사 기능을 통해 코드의 타입 안정성을 높일 수 있습니다. 

**타입 가드(Type Guards)**는 런타임에서의 타입 검사를 통해 타입 안정성을 확보하는 기능을 제공합니다. 

```typescript
// 타입 가드를 사용하여 문자열일 때에만 함수를 실행
function processInput(input: string | number) {
  if (typeof input === 'string') {
    // input이 문자열일 때 동작하는 로직
    console.log(input.toUpperCase());
  }
}
```

TypeScript의 **타입스크립트 스크립트**와 **대명선언(type alias)** 등을 활용하여 타입을 정의하고 관리할 수 있습니다.

## 결론

TypeScript를 사용하면 코드의 안정성을 높이고 개발 과정에서의 실수를 줄일 수 있지만, 타입 오류가 발생할 수 있습니다. 이때 타입 검사를 통해 코드의 안정성을 유지하고 개선할 수 있습니다.

더 많은 정보를 원하신다면, [TypeScript 공식 문서](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)를 참고해보세요.