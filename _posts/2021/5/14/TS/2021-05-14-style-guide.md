---
layout: post
title: "[ts] Style Guide"
description: " "
date: 2021-05-14
tags: [ts]
comments: true
share: true
---

# Style Guide

## Type annotation

type inference가 동작하는 기본적인 타입, 초기화 등에는 굳이 사용하지 않아도 되고, 그렇지 않은 경우에는 annotation을 붇여줘야한다.

예를들어,  아래의 경우에는 붙이지 않아도 된다.

```typescript
// bad cases
const x: boolean = true;
const x: Set<string> = new Set<>;
```


## Nullable/undefined type aliases


Type aliases *must not* include |null or |undefined in a union type. Nullable aliases typically indicate that null values are being passed around through too many layers of an application, and this clouds the source of the original issue that resulted in null. They also make it unclear when specific values on a class or interface might be absent.
Instead, code *must* only add |null or |undefined when the alias is actually used. Code *should* deal with null values close to where they arise, using the above techniques.


## Interface vs Type aliases

객체를 선언하는 경우에는 type aliases가 아니라 인터페이스를 사용.


## Array<T> vs T[]

단일 타입에 대해서는 types에 대해서는 `T[]`를 사용하고,
그 보다 복잡한 상황에서는 `Array<T>`를 사용한다.

```typescript
const a: string[];
const b: Array<string|number>;

```

#타입스크립트