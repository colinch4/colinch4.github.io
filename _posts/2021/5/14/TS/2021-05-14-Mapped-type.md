---
layout: post
title: "[ts] Mapped type"
description: " "
date: 2021-05-14
tags: [typescript]
comments: true
share: true
---

## Mapped type
## Basic
Mapped type 예제.

```typescript
type T1 = {[K in 'prop1' | 'prop2'] : boolean };

interface Person {
    name: string;
    age: number;
}

type MakeBoolean<T> = { [P in keyof T]? : boolean };
const pMap: MakeBoolean<Person> = {};
pMap.name = true;
pMap.age = false;
```


## Modifier

readonly, optional과 같은 제어자를 추가 혹은 제거할 수 있다.

### 접근제어 추가

```typescript
type User = {
	name: string;
	age: number;
}

// readonly property로 변환
type Readonly<Type> = {
	readonly [Property in keyof Type ] : Type[Property];
}

// optional property로 변환
type Partial<Type> = {
	 [ Key in keyof Type ]? : Type[Key];
}
```

### 접근제어 제거

`-readonly` , `-?` 를 통해서 각 속성을 제거할 수 있음.

```typescript
// readonly 속성 제거
type CreateMutable<Type> = {
	-readonly [Property in keyof Type]: Type[Property]
};

// optional 속성 제거
type Concrete<Type> {
	[Property in keyof Type]-? : Type[Property]; 
}

```


## 활용 및 내장 타입
### Readonly & Partial

```typescript
type T2 = Person['name']; 

type Readonly<T> = { readonly [P in keyof T]: T[P]};
// 모든 속성을 readonly
// 원래 내장 타입
type Partial<T> = {[P in keyof T]?: T[P]};
// 모든 속성을 optional
// 원래 내장 타입

type T3 = Readonly<Person>;
type T4 = Partial<Person>;


```

### Pick

```typescript
type Pick<T, K extends keyof T> = { [P in K]: T[P]};
// K에 입력한 key만을 속성으로 가지는 타입
// 내장 타입
interface Human {
    name: string;
    age: number;
    language: string;
}

type HumanKey = keyof Human;
// type HumanKey = "name" | "language" | "age"
type T5 = Pick<Human, 'name' | 'language'>;



```

### Record
```typescript
type Record<K extends string, T> = { [P in K]: T};
// 내장 타입

type t6 = Record<'p1' | 'p2', Person>;
//  === type t6 = {
//     p1: Person;
//     p2: Person;
// }
type t7 = Record<'p1' | 'p2', number>;
// === type t7 = {
//     p1: number;
//     p2: number;
// }

enum Fruit {
    Apple,
    Banana,
    Orange, // 해당 필드 추가
}
// 아래의 경우는 enum을 추가해도 에러가 나지 않기 때문에
// 누락하는 실수를 할 수 있다.
const FRUIT_PRICE1 = {
    [Fruit.Apple]: 1000,
    [Fruit.Banana]: 1500,
} 

// 아래의 경우에는 enum을 추가하면 에러가 나서 
// 컴파일 타임에 에러를 잡을 수 있다.
const FRUIT_PRICE: { [key in Fruit]: number} = {
    [Fruit.Apple]: 1000,
    [Fruit.Banana]: 1500,
}
```



#타입스크립트/mapped-type