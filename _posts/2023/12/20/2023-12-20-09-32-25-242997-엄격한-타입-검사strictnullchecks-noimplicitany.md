---
layout: post
title: "[typescript] 엄격한 타입 검사(strictNullChecks, noImplicitAny)"
description: " "
date: 2023-12-20
tags: [typescript]
comments: true
share: true
---

TypeScript는 JavaScript의 확장된 버전으로, 정적 유형 검사와 강력한 타입 지원을 제공합니다. 이를 통해 코드의 안정성을 향상하고 오류를 사전에 방지할 수 있습니다. TypeScript의 엄격한 타입 검사 옵션은 코드의 안정성을 높이며, 유지보수성을 향상시킵니다.

## strictNullChecks

`strictNullChecks` 옵션은 null이나 undefined를 명시적으로 포함하는 것을 강제합니다. 이 옵션을 활성화하면 변수에 null 또는 undefined 값을 할당할 수 없습니다. 이는 런타임 에러를 사전에 방지하여 안정성을 증가시킵니다.

예를 들어, 다음과 같이 옵션을 설정할 수 있습니다.

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "strictNullChecks": true
  }
}
```

## noImplicitAny

`noImplicitAny` 옵션은 타입이 명시되지 않은 경우, 암시적으로 'any' 타입을 사용하는 것을 금지합니다. 이는 모호한 타입을 사용함으로써 발생할 수 있는 오류를 사전에 방지하여 코드 안정성을 향상시킵니다.

예를 들어, 다음과 같이 옵션을 활성화할 수 있습니다.

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "noImplicitAny": true
  }
}
```

## 결론

TypeScript의 엄격한 타입 검사 옵션을 활용하여 코드의 안정성과 유지보수성을 향상시킬 수 있습니다. 이러한 옵션들을 활성화하여 안정적이고 견고한 코드를 작성하는 데 도움이 될 것입니다.

더 많은 정보는 [TypeScript 공식 문서](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)를 참고하시기 바랍니다.