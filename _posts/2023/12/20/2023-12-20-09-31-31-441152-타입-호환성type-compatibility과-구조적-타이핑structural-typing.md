---
layout: post
title: "[typescript] 타입 호환성(type compatibility)과 구조적 타이핑(structural typing)"
description: " "
date: 2023-12-20
tags: [typescript]
comments: true
share: true
---

타입스크립트(TypeScript)에서 **타입 호환성**과 **구조적 타이핑**은 매우 중요한 개념입니다. 이 두 가지 개념은 코드를 작성하고 유지보수하는 과정에서 매우 유용하며, 자바스크립트와 비교하여 타입스크립트의 장점 중 하나입니다.

## 타입 호환성

타입 호환성은 **타입 A가 타입 B로 할당될 수 있는지 여부**를 결정하는 규칙을 의미합니다. 기본적으로, **타입 A가 타입 B로 할당 가능하려면 B에 있는 모든 멤버가 A에도 존재하여야 합니다**. 이를 말로하면 "source 타입(S)이 target 타입(T)에 할당 가능하려면 S의 모든 멤버가 T에 있는 멤버에 대응해야 한다"라고 할 수 있습니다.

아래는 간단한 예제입니다.

```typescript
interface Animal {
  name: string;
}

interface Dog {
  name: string;
  breed: string;
}

let animal: Animal;
let dog: Dog;

animal = dog; // OK
dog = animal; // Error: property 'breed' is missing in type 'Animal' but required in type 'Dog'
```

위 예제에서 `Animal`과 `Dog`는 둘 다 `name`이라는 속성을 가지고 있지만, `Dog`에만 `breed`라는 속성이 추가로 존재합니다. 그래서 `animal = dog;`는 문제가 없지만, `dog = animal;`은 **에러**가 발생합니다.

## 구조적 타이핑

타입스크립트는 또한 **구조적 타이핑**을 지원합니다. 구조적 타이핑은 **명시적으로 인터페이스를 구현하지 않아도, 구조적으로 동일한 멤버를 가지고 있다면 호환성을 가진다**는 뜻입니다.

예를 들어,

```typescript
interface Point {
  x: number;
  y: number;
}

function printPoint(p: Point) {
  console.log(`${p.x}, ${p.y}`);
}

// 다음과 같이 작성해도 문제가 없습니다.
let point = { x: 10, y: 20, z: 30 };
printPoint(point); // 출력 결과: 10, 20
```

위 예제에서 `point`는 `Point` 인터페이스를 명시적으로 구현하지 않았지만, 구조적으로 동일한 멤버(`x`, `y`)를 가지고 있기 때문에 호환성이 있습니다.

## 결론

타입 호환성과 구조적 타이핑은 타입스크립트에서 코드를 작성하고 유지보수하는 데 매우 중요한 역할을 합니다. 코드를 작성할 때 이러한 개념을 이해하고 활용하여 타입 안정성을 높이는 것이 중요합니다.