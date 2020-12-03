---
layout: post
title: "[Typescript] 2. 인터페이스"
description: " "
date: 2020-12-03
tags: [Typescript]
comments: true
share: true
---


# 타입스크립트 인터페이스

-   [타입스크립트 핸드북 - 기본타입](https://www.typescriptlang.org/docs/handbook/basic-types.html)
-

### 우리의 첫번째 인터페이스

-   예제를 보면 이해하기 좋다.

```ts
function printLabel(labeledObj: { label: string }) {
    console.log(labeledObj.label)
}

let myObj = { size: 10, label: 'Size 10 Object' }
printLabel(myObj)
```

위의 예제는 아래와 같이 인터페이스로 정의할 수 있다.

```ts
interface LabeledValue {
    label: string
}

function printLabel(labeledObj: LabeledValue) {
    console.log(labeledObj.label)
}

let myObj = { size: 10, label: 'Size 10 Object' }
printLabel(myObj)
```

### Optional Properties

인터페이스의 모든 프로퍼티가 필요하지 않을 수 있다.
옵셔널 프로퍼티는 `?`를 붙인다.

```ts
interface SquareConfig {
    color?: string
    width?: number
}

function createSquare(config: SquareConfig): { color: string; area: number } {
    let newSquare = { color: 'white', area: 100 }
    if (config.color) {
        newSquare.color = config.color
    }
    if (config.width) {
        newSquare.area = config.width * config.width
    }
    return newSquare
}

let mySquare = createSquare({ color: 'black' })
```

### 읽기전용 프로퍼티

-   어떤 프로퍼티는 객체가 생성되는 시점에만 값이 설정되도록 하고 싶다. 프로퍼티 앞에 readonly 명시한다.

```ts
interface Point {
    readonly x: number
    readonly y: number
}
```

-   객체 리터럴 대입으로 Point를 생성할 수 있다. 할당된 후에는 x와 y는 변경될 수 없다.

```ts
let p1: Point = { x: 10, y: 20 }
p1.x = 5 // error! Cannot assign to 'x' because it is a read-only property.
```

#### 읽기전용 배열 `ReadonlyArray<T>`

-   타입스크립트는 `ReadonlyArray<T>`를 제공한다. `ReadonlyArray<T>`는 `Array<T>`에서 변경 메소드들을 제거한 것이다. 따라서 `ReadonlyArray<T>`는 생성된 후에는 배열을 변경할 수 없다.

```ts
let a: number[] = [1, 2, 3, 4]
let ro: ReadonlyArray<number> = a

ro[0] = 12 // error!
ro.push(5) // error!
ro.length = 100 // error!
a = ro // error!
```

-   위의 마지막줄 에러는 타입 Assertion으로 해결할 수 있다.

```ts
let a: number[] = [1, 2, 3, 4]
let ro: ReadonlyArray<number> = a

a = ro as number[]
```

##### readonly 와 const

readonly는 프로퍼티를 변경할 수 없는 개념이고
const는 변수를 변경할 수 없다.

### Excess Property Checks(과도한 속성 검사)

-   아래의 결과는 width 속성이 전달되었고, colour 속성은 변수명이 달라서 무시될 것으로 생각할 수 있다. 그러나 타입스크립트는 이 코드에 버그가 있을 수 있다는 입장을 취한다. 객체 리터럴은 다른 변수에 할당하거나 인수로 전달할 때 특수처리 되고, 과도한 속성 검사를 한다.

```ts
interface SquareConfig {
    color?: string
    width?: number
}

function createSquare(config: SquareConfig): { color: string; area: number } {
    return { color: config.color || 'red', area: config.width ? config.width * config.width : 20 }
}

let mySquare = createSquare({ colour: 'red', width: 100 })
```

-   에러 메시지

```
Argument of type '{ colour: string; width: number; }' is not assignable to parameter of type 'SquareConfig'.
  Object literal may only specify known properties, but 'colour' does not exist in type 'SquareConfig'. Did you mean to write 'color'?
```

-   이러한 체크를 통과하는 것은 매우 간단하다. 가장 간단한 방법은 타입 단정을 사용하는 것이다.

```ts
let mySquare = createSquare({ width: 100, opacity: 0.5 } as SquareConfig)
```

-   그러나 객체에 몇 가지 추가 속성이 있을 수 있다고 확신하는 더 나은 방법은 아래와 같이 문자열 인덱스 시그니처를 추가하는 것이다.

```ts
interface SquareConfig {
    color?: string
    width?: number
    [propName: string]: any
}
```

-   또 다른 방법은 약간 의외일 수 있다. 객체 리터럴일때 과도한 속성 검사를 하므로, 객체 리터럴을 다른 변수에 할당한 후, 변수를 파라미터로 전달하는 것이다.

```ts
let squareOptions = { colour: 'red', width: 100 }
let mySquare = createSquare(squareOptions)
```

### 함수 타입

-   인터페이스는 자바스크립트 객체가 취할 수 있는 다양한 형태를 설명할 수 있다. 인터페이스는 프로퍼티외에도 함수 타입을 설명할 수도 있다.
-   아래는 인터페이스에 함수를 정의하는 예이다.

```ts
interface SearchFunc {
    (source: string, subString: string): boolean
}
```

-   일단 정의되면 다른 인터페이스처럼 함수 유형 인터페이스를 사용할 수 있다. 여기서는 함수 유형의 변수를 생성하고, 동일한 유형의 함수 값을 할당하는 방법을 보여준다.

```ts
let mySearch: SearchFunc

mySearch = function (source: string, subString: string) {
    let result = source.search(subString)
    return result > -1
}
```

-   인터페이스의 함수 타입은 파라미터 타입과 리턴타입만을 체크한다. 함수의 파라미터명은 일치하지 않아도 된다.

```ts
let mySearch: SearchFunc

mySearch = function (src: string, sub: string): boolean {
    let result = src.search(sub)
    return result > -1
}
```

-   타입스크립트는 함수의 파라미터 타입을 추론할 수 있다. 아래는 파라미터에 타입을 명시하지 않았지만, SearchFunc 인터페이스에 의해 타입을 추론하여 에러가 아니다.

```ts
let mySearch: SearchFunc

mySearch = function (src, sub) {
    let result = src.search(sub)
    return result > -1
}
```

### Indexable 타입

-   `a[10], ageMap['daniel']` 같은 인덱싱이 가능한 타입을 위해 인덱스 시그니처가 있다.

```ts
interface StringArray {
    [index: number]: string
}

let myArray: StringArray
myArray = ['Bob', 'Fred']

let myStr: string = myArray[0]
```

-   위에서 `StringArray`에는 인덱스 시그니처가 있다. 지원되는 인덱스 시그니처는 문자열과 숫자 두가지 유형이 있다. 두 유형의 인덱서를 모두 지원할 수 있지만, 숫자 인덱서에서 반환된 유형은 문자열 인덱서에서 반환된 유형의 하위유형이어야 한다. 이것은 자바스크립트가 숫자를 인덱싱할 때 실제로는 문자열로 인덱싱하기 때문이다. 예를 들어, 숫자 100으로 인덱싱하는 것은 문자열 '100'으로 인덱싱하는 것과 동일한다. 따라서 아래와 같은 형태는 에러가 발생한다.

```ts
interface Animal {
    name: string
}

interface Dog extends Animal {
    breed: string
}

// Error: indexing with a numeric string might get you a completely separate type of Animal!
interface NotOkay {
    [x: number]: Animal
    [x: string]: Dog
}
// Error msg: Numeric index type 'Animal' is not assignable to string index type 'Dog'.
```

-   문자열 인덱스 서명은 딕셔너리 패턴을 설명하는 강력한 방법이지만, 모든 속성이 반환 유형과 일치하도록 강제한다.
-   왜냐하면 문자열 인덱스는 `obj.property` 를 obj['property']로도 이용가능하기 때문이다. 아래의 예에서 'name' 프로퍼티의 타입이 문자열이라서 `[index:string]:number`와 충돌하므로 에러가 발생한다.

```ts
interface NumberDictionary {
  [index: string]: number;
  length: number; // ok, length is a number
  name: string; // error, the type of 'name' is not a subtype of the indexer
Property 'name' of type 'string' is not assignable to string index type 'number'.
}
```

-   하지만 인덱스 시그니처를 union 타입으로 정의하면 서로 다른 타입을 허용할 수 있다.

```ts
interface NumberOrStringDictionary {
    [index: string]: number | string
    length: number // ok, length is a number
    name: string // ok, name is a string
}
```

-   인덱스 시그니처에 readonly 를 붙여서 수정할 수 없도록 만들 수 있다.

```ts
interface ReadonlyStringArray {
    readonly [index: number]: string
}

let myArray: ReadonlyStringArray = ['Alice', 'Bob']
myArray[2] = 'Mallory' // error! Index signature in type 'ReadonlyStringArray' only permits reading.
```
