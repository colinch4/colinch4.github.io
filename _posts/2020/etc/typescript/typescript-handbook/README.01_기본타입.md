---
layout: post
title: "[Typescript] 1. 기본 타입"
description: " "
date: 2020-12-03
tags: [Typescript]
comments: true
share: true
---

# Typescript basic

-   [타입스크립트 핸드북 - 기본타입](https://www.typescriptlang.org/docs/handbook/basic-types.html)

### 기본 타입들

-   boolean, number, string

```ts
let isDone: boolean = false
let decimal: number = 6
let hex: number = 0xf00d
let binary: number = 0b1010
let octal: number = 0o744

let color: string = 'blue'
```

### Array

```ts
let list: number[] = [1, 2, 3]
let list: Array<number> = [1, 2, 3]
```

### Tuple

```ts
let x: [string, number]
x = ['hello', 10] // OK
// x = [10, "hello"]; // Error

console.log(x[0].substring(1)) // OK
```

### Enum

```ts
enum Color {
    Red,
    Green,
    Blue,
}
let c: Color = Color.Green
```

```ts
enum Color {
    Red = 1,
    Green = 2,
    Blue = 4,
}
let c: Color = Color.Green
```

```ts
enum Color {
    Red = 1,
    Green,
    Blue,
}
let colorName: string = Color[2]
console.log(colorName) // 'Green'
```

### Any

```ts
let notSure: any = 4
notSure = 'maybe a string instead'
notSure = false // okay, definitely a boolean
```

```ts
let notSure: any = 4
notSure.ifItExists() // okay, ifItExists might exist at runtime
notSure.toFixed() // okay, toFixed exists (but the compiler doesn't check)

let prettySure: Object = 4
prettySure.toFixed() // Error: Property 'toFixed' doesn't exist on type 'Object'.
```

-   Object 타입은 다른 프로그래밍 언어들처럼 어떤 타입이라도 대입할 수는 있다. 숫자도 대입할 수 있고, 문자도 대입할 수 있다. 예를 들어 숫자를 대입할 수 있는데, 특이하게도 number 객체의 메소드를 호출할 수는 없다. 예를 들어 toFixed()는 number의 메소드이지만, Object 타입으로 대입한 경우 호출할 수 없다.
    -   이것의 용도가 뭐지?

```ts
let notSure: any = 4
notSure.ifItExists() // okay, ifItExists might exist at runtime
notSure.toFixed() // okay, toFixed exists (but the compiler doesn't check)

let prettySure: Object = 4
prettySure.toFixed() // Error: Property 'toFixed' doesn't exist on type 'Object'.
```

### void

void는 값이 없음을 의미한다. 보통 함수의 리턴 타입으로 void를 적는다.

```ts
function warnUser(): void {
    console.log('This is my warning message')
}
```

-   변수를 void로 선언하면 null이나 undefined만 대입이 가능하다. 만약 컴파일 옵션에 `--strictNullChecks`를 지정하면 undefined만 대입이 가능하다.

```ts
let unusable: void = undefined
unusable = null // OK if `--strictNullChecks` is not given
```

### null과 undefined

타입 스크립트에서 undefined와 null은 실제로는 타입의 이름이다.

```ts
let u: undefined = undefined
let n: null = null
```

-   기본으로 null과 undefined는 모든 타입들의 서브타입이다. 이것은 number 타입에 null이나 undefined를 대입할 수 있음을 의미한다.
-   그러나 `--strictNullChecks` 플래그를 사용하면 null과 undefined는 any타입에만 대입이 가능하다. 예외적으로 undefined는 void 타입에도 대입이 가능하다. 유니온 타입, string|null|undefined를 사용할 수도 있다.
-   union 타입은 나중에 다룬다.
-   가능하면 `--strictNullChecks`를 사용해라.

### Never

-   never는 절대로 발생하지 않는 타입을 의미한다. 예를 들어 never를 함수의 리턴타입으로 사용한다는 것은 이 함수는 항상 예외를 던지거나 절대로 리턴하지 않는 함수임을 의미한다.
-   never 타입은 모든 타입의 하위 타입이며, 모든 타입에 대입할 수는 있다. 그러나 never의 하위 타입은 없고, never 타입에 대입할 수도 없다.

```ts
// Function returning never must have unreachable end point
function error(message: string): never {
    throw new Error(message)
}

// Inferred return type is never
function fail() {
    return error('Something failed')
}

// Function returning never must have unreachable end point
function infiniteLoop(): never {
    while (true) {}
}
```

### Object

-   object는 Non-Primitive 타입을 의미한다. 예를 들면, number, string, boolean, bigint, symbol, null, undefined가 아니다.
-   object 타입은, Object.create 같은 API를 더 잘 표현한다. 예를 들면

```ts
declare function create(o: object | null): void

create({ prop: 0 }) // OK
create(null) // OK

create(42) // Error
create('string') // Error
create(false) // Error
create(undefined) // Error
```

### Type assertions, 타입 캐스팅

타입 단언, Type assertions은 타입 캐스팅을 의미한다.

```ts
let someValue: any = 'this is a string'

let strLength: number = (<string>someValue).length
```

또는 as 문법으로도 가능하다.

```ts
let someValue: any = 'this is a string'

let strLength: number = (someValue as string).length
```
