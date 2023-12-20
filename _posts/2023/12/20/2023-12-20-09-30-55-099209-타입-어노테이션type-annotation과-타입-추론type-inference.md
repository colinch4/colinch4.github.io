---
layout: post
title: "[typescript] 타입 어노테이션(type annotation)과 타입 추론(type inference)"
description: " "
date: 2023-12-20
tags: [typescript]
comments: true
share: true
---

타입스크립트는 **타입 어노테이션(type annotation)** 과 **타입 추론(type inference)**을 통해 변수의 타입을 명시하거나 추론할 수 있습니다. 이 두 가지 기능은 코드를 작성할 때 변수의 타입을 명확하게 지정하거나 생략할 수 있는 유용한 도구입니다.

### 타입 어노테이션

타입 어노테이션은 변수의 타입을 명시적으로 지정하는 것을 말합니다. 이를 통해 개발자는 해당 변수가 어떤 타입의 값일 것으로 예상되는지를 명확하게 나타낼 수 있습니다.

예를 들어, 다음과 같이 `number` 타입을 가진 변수를 선언하고 해당 타입을 명시적으로 지정할 수 있습니다.

```typescript
let age: number;
age = 26;
```

### 타입 추론

타입 추론은 변수의 타입을 초기화의 값을 기반으로 추측하는 기능을 말합니다. 타입스크립트는 변수를 선언할 때 초기값을 할당하는 경우, 해당 값을 기반으로 변수의 타입을 추론합니다.

예를 들어, 다음과 같이 `name` 변수를 선언하면, 해당 변수의 타입은 문자열로 추론됩니다.

```typescript
let name = "Alice";
```

타입 어노테이션과 타입 추론은 개발자가 코드를 더 명확하고 유연하게 작성할 수 있도록 도와줍니다.

### 결론

타입 어노테이션과 타입 추론은 타입스크립트의 강력한 기능 중 하나입니다. 이를 활용하여 코드를 더 간결하게 작성하고 타입 안정성을 유지할 수 있습니다.

참조: [TypeScript Handbook - Type Annotations](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-annotations)

[TypeScript Handbook - Type Inference](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-inference)