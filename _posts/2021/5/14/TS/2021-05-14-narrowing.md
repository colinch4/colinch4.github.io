---
layout: post
title: "[ts] Narrowing / 타입 가드"
description: " "
date: 2021-05-14
tags: [ts]
comments: true
share: true
---

# Narrowing / 타입 가드

type을 check 하는 것은 type guard

type을 더 상세한 type으로 정제하는 과정은 Narrowing

```typescript
function padLeft(padding: number | string, input: string) {
  // if로 타입 체크하는 것 자체는 type guard
	// 타입 체크 후 메서드를 호출하고 오퍼레이션을 하는 과정들은 narrowing
	if (typeof padding === "number") {
    return new Array(padding + 1).join(" ") + input;
  }
  return padding + input;
}

```

## `typeof`

```typescript
function padLeft(padding: number | string, input: string) {
	if (typeof padding === "number") {
    return new Array(padding + 1).join(" ") + input;
  }
  return padding + input;
}

```

## `instanceof`
```typescript
class Person {
    name: string;
    age: number;
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

}

class Product {
    name: string;
    price: number;
    constructor(name: string, price: number) {
        this.name = name;
        this.price = price;
    }
}

function print1(value: Person | Product){
    if(value instanceof Person){
        console.log(value.age);
    }else {
        console.log(value.price);
    }
}


interface IPerson {
    name: string;
    age: number;
}

interface IProduct {
    name: string;
    price: number;
}


// 아래의 경우 에러가 나는데, 
// 컴파일 타임에 JS로 변환이 일어나면서, 인터페이스 선언부는 모두 제거가 된다.
// 그로 인해서 instanceof keyword 우측에는 클래스나, 생성자 함수가 와야한다.

function print2(value: IPerson | IProduct){
    if(value instanceof IPerson){
        console.log(value.age);
    }else {
        console.log(value.price);
    }
}


// 방법 1: 식별 가능한 유니온 타입
interface IPerson2 {
    type: 'a',
    name: string;
    age: number;
}

interface IProduct2 {
    type: 'b';
    name: string;
    price: number;
}
// 이 경우에도 타입 가드가 동작한다. 

function print3(value: IPerson2 | IProduct2){
    if(value.type === 'a'){
        console.log(value.age);
    }else {
        console.log(value.price);
    }
}

// 방법2: 타입을 구분 하는 함수 작성
function isPerson(x: Person| Product): x is Person {
    return (x as Person).age !== undefined;
}

function print4(value: IPerson2 | IProduct2){
    if(isPerson(value)){
        console.log(value.age);
    }else {
        console.log(value.price)
    }
}
```

## The `in` operator narrowing
```typescript
// 방법3:  js 'in' keyword 사용
function print5(value: IPerson2 | IProduct2){
    if('age' in value){
        console.log(value.age);
    }else {
        console.log(value.price)
    }
}

// optional이 있는 경우
type Fish = { swim: () => void };
type Bird = { fly: () => void };
type Human = {  swim?: () => void, fly?: () => void };
function move(animal: Fish | Bird | Human) {
  if ("swim" in animal) { 
    animal
		// (parameter) animal: Fish | Human
  } else {
    animal
      // (parameter) animal: Bird | Human
  }
}

```


## Type Predicate
return type에 Type Predicate를 사용할 수 있다.
`parameterName is Type` 와 같은 방식으로 사용이 가능하고, parameterName은 실제 함수의 파라미터 이름과 같은 것을 사용해야한다.


```typescript
function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}
```

```typescript
const zoo: (Fish | Bird)[] = [getSmallPet(), getSmallPet(), getSmallPet()];
const underWater1: Fish[] = zoo.filter(isFish);
// or, equivalently
const underWater2: Fish[] = zoo.filter(isFish) as Fish[];
// The predicate may need repeating for more complex examples
const underWater3: Fish[] = zoo.filter((pet): pet is Fish => {
  if (pet.name === "sharkey") return false;
  return isFish(pet);
});

```
#타입스크립트/타입가드