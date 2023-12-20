---
layout: post
title: "[typescript] 기본 데이터 타입 (number, string, boolean, null, undefined)"
description: " "
date: 2023-12-20
tags: [typescript]
comments: true
share: true
---

이번에는 TypeScript의 기본 데이터 타입에 대해 알아보겠습니다.

1. [number](#number)
2. [string](#string)
3. [boolean](#boolean)
4. [null과 undefined](#null-undefined)

---

## number
number 타입은 모든 숫자를 다룰 수 있으며, 정수나 부동 소수점 숫자를 포함합니다.

예시:
```typescript
let num: number = 10;
let decimal: number = 10.5;
```

## string
string 타입은 텍스트 데이터를 나타냅니다.

예시:
```typescript
let name: string = "John Doe";
let message: string = `Hello, ${name}!`;
```

## boolean
boolean 타입은 논리적인 값인 `true`나 `false`를 표현합니다.

예시:
```typescript
let isDone: boolean = false;
```

## null과 undefined
`null`과 `undefined`는 각각 null과 undefined 값을 가지는 타입입니다.

예시:
```typescript
let n: null = null;
let u: undefined = undefined;
```

이상으로 TypeScript의 기본 데이터 타입에 대한 간단한 소개를 마치겠습니다. 참고 문헌은 다음과 같습니다.

- TypeScript 공식 문서: https://www.typescriptlang.org/docs/handbook/basic-types.html

감사합니다!