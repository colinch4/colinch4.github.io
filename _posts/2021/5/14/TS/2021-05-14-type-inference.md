---
layout: post
title: "[ts] 타입 추론"
description: " "
date: 2021-05-14
tags: [ts]
comments: true
share: true
---

##  타입 추론
아래의 경우에는 아래와 같이 타입을 명시하지 않아도, 타입추론이 일어난다.

- 변수, 객체의 멤버 변수 초기화
- 파라미터의 default value 설정시
- 함수의 return type

```typescript
let v1 = 123; // number
let v2 = 'abc';  // string

const v1 = 123; // type이 123
const v2 = 'abc'; // type이 'abc'
let v3: typeof v1 = 234; // error
// let v3: typeof v1 = 123; // error 아님

const obj1 = { name: 'pius', age: 20, adult: true }
// obj: { id: string, age: number, adult: boolean }
```


## Best common type

대부분의 경우에는 자동으로 타입추론이 일어나는데, 타입을 추론하는 방식은 `best common type`이다.

주어진 candidate들 중에서 공통의 것을 찾아서 타입을 정하는 것이다.

```typescript
const arr1 = [10, 20, 30]; 
// arr: number[]

const arr2 = [1, 2, null, undefined];
// arr2: (number | null | undefined)[];

```

만약에 각 type이 공통의 super type을 가지고 있다고 하더라도, candidate에 super type이 없으면 이를 추론하지 못한다.

```typescript
interface Person {
	name: string;
	age: number;
}

interface Korean extendns Person {
	liveInSeoul: boolean;
}

interface Japanese extends Person {
	liveInTokyo: boolean;
}

const p1:Person = { name: 'pius', age: 23 };
const p2:Korean = { name: 'mike', age: 25, liveInSeoul: true};
const p3:Japanese = { name: 'mike', age: 25, liveInTokyo: true};

const arr1 = [p1, p2, p3]; // arr1:Person[]
const arr2 = [p2, p3]; // 
```

위의 경우, arr2 변수의 타입이  arr2:(Korean | Japanese)[] 인 이유는 p2, p3 중에서 super type이 존재하지 않기 때문이다.

## Contextual Typing



#타입스크립트/타입추론
