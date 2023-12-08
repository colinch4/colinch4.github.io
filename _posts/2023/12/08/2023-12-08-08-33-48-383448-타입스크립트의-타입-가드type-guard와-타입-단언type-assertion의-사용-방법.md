---
layout: post
title: "[typescript] 타입스크립트의 타입 가드(Type Guard)와 타입 단언(Type Assertion)의 사용 방법"
description: " "
date: 2023-12-08
tags: [typescript]
comments: true
share: true
---

타입스크립트는 정적 타입 언어이며, 변수나 파라미터의 타입을 명확히 지정하여 코드 안정성을 높일 수 있습니다. 타입 가드(Type Guard)와 타입 단언(Type Assertion)은 이를 위한 중요한 도구로, 다양한 상황에서 유용하게 활용됩니다.

## 타입 가드(Type Guard)란?

타입 가드(Type Guard)는 런타임에서 동작하여 특정 타입으로의 값 변환을 보장하는 조건을 나타내는 타입스크립트의 구문이며, 주로 `typeof`, `instanceof`, `in`, `is` 등의 연산자를 사용합니다. 이를 통해 런타임 시점에서 변수의 타입을 체크하고 해당 타입으로 변환할 수 있습니다.

다음은 `typeof`를 이용한 예시입니다.

```typescript
function printLength(value: string | string[]) {
    if (typeof value === 'string') {
        console.log(value.length);  // value의 타입이 string인 경우에만 length 속성에 접근 가능
    } else {
        value.forEach(str => console.log(str.length));  // value의 타입이 string[]인 경우에만 forEach 메서드 사용 가능
    }
}
```

## 타입 단언(Type Assertion)이란?

타입 단언(Type Assertion)은 컴파일러에게 "내가 정확히 알고 있으니 이 타입으로 취급해달라"고 알려주는 것으로, 값이 실제로 해당 타입과 일치하지 않더라도 컴파일 시점에 타입 체크를 통과하도록 합니다. 주로 `<Type>` 구문이나 `as Type` 구문을 사용합니다.

다음은 `as`를 이용한 예시입니다.

```typescript
let userInput: unknown;
let userName: string;

userInput = "hello";
userName = userInput as string;   // userInput이 실제로 string임을 개발자가 확신할 때 사용
```

타입 가드와 타입 단언은 코드의 가독성과 안정성을 높이는 데 중요한 역할을 하며, 올바르게 활용함으로써 타입스크립트의 강력한 타입 시스템을 활용할 수 있습니다.