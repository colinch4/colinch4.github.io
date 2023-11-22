---
layout: post
title: "[js] Iteration / Generator"
description: " "
date: 2021-05-14
tags: [javascript]
comments: true
share: true
---


## Iteration / Generator

Iteration Protocol은 새롭게 추가된 `Protocol`로 문법이나 빌트인 함수가 아니고...


iteration protocol이 도입된 이유?

`for...of`, `spread` `destructuring` 과 같은 문법이 도입되면서, 데이터를 순회하는 방법이 필요하게 되었고, 이를 데이터 구조들이 각기 다른 방식으로 순회 방식을 제공하면, 위의 문법은 데이터 구조에 따라 각기 implementation을 해야하는 문제가 있다.
하지만 데이터 구조(eg. `string`, `array`, `Map/Set`이 동일한 프로토콜을 가진다면, 해당 프로토콜 (일종의 인터페이스)만을 구현하면 된다.

`for...of`, `spread`, `destructuring`은 `Symbol.iterator` 메서드 호출을 통해 이터레이터 객체를 생성하고, 이를 통해서 이터러블을 순회하게 된다.

Iteration Protocol에는 아래와 같은 두 가지의 프로토콜이 있다.

- iterable protocol
- iterator protocol




## Iterable


iterable은 `Symbol.iterator` 메서드를 `구현`하거나, 이를 `상속`한 객체를 말한다. iterate가 가능한 객체라는 뜻.

따라서, 이터러블 객체의 경우에는  `for ... in` 문을 통해서 객체를 순회할 수 있다.

> Symbol.iterator()
> iterator protocol에 해당하는 객체를 반환한다.


```javascript
const array = [1, 2, 3];

// 위 array에 iterator 메서드가 있는가?
console.log(Symbol.iterator in array);

>>> true // iterable 객체이다. 

for (const el of array) {
	console.log(el);
}

const obj = { a: 1, b: 2 };

// 일반 객체는 Symbol.iterator 메소드를 소유하지 않는다.
// 따라서 일반 객체는 이터러블 프로토콜을 준수한 이터러블이 아니다.
console.log(Symbol.iterator in obj); // false

// 이터러블이 아닌 일반 객체는 for...of 문에서 순회할 수 없다.
// TypeError: obj is not iterable
for (const p of obj) {
  console.log(p);
}
```


## Iterator

iterable 객체에  `Symbol.iterator()` 메서드 호출
-> iterator 반환
-> iterator 객체의 `next()` 메서드를 호출하며 순회

```javascript
// 배열은 iterable 객체이다. 
const array = [1, 2, 3];

// Symbol.iterator 메소드는 이터레이터를 반환한다.
const iterator = array[Symbol.iterator]();

// 이터레이터 프로토콜을 준수한 이터레이터는 next 메소드를 갖는다.
console.log('next' in iterator); // true

iterator.next();
>>> {value: 1, done: false}
iterator.next();
>>> {value: 2, done: false}
iterator.next();
>>> {value: 3, done: false}
iterator.next();
>>> {value: undefined, done: true}
```

```javascript
// 이터레이터의 next 메소드를 호출하면 value, done 프로퍼티를 갖는 이터레이터 리절트 객체를 반환한다.
// next 메소드를 호출할 때 마다 이터러블을 순회하며 이터레이터 리절트 객체를 반환한다.
console.log(iterator.next()); // {value: 1, done: false}
console.log(iterator.next()); // {value: 2, done: false}
console.log(iterator.next()); // {value: 3, done: false}
console.log(iterator.next()); // {value: undefined, done: true}
```



## 빌트인 이터러블

- Array
- String
- Map
- Set
- DOM
- Arguments


## Iteration Protocol이 사용되는 법

### for ... of

`for ... of`의 경우에는 이터러블 객체로부터  이터레이터를 얻은 후 이를 순회하게 된다.

위의 `iterator result`에서 `value`를 반환을 하고, `done` 프로퍼티를 보며, 이 프로퍼티가 true가 될때까지 순회를 하게된다.


```javascript
// 이터러블
const iterable = [1, 2, 3];

// 이터레이터
const iterator = iterable[Symbol.iterator]();

for (;;) {
  // 이터레이터의 next 메소드를 호출하여 이터러블을 순회한다.
  const res = iterator.next();

  // next 메소드가 반환하는 이터레이터 리절트 객체의 done 프로퍼티가 true가 될 때까지 반복한다.
  if (res.done) break;

  console.log(res);
}
```


## 제네레이터(Generator)
제네레이터는 generator function을 통해 반환된 객체로,  iterable 프로토콜과 iterator 프로토콜을 준수(구현)하고 있다.

```javascript
function* generator() {
	yield 1;
	yield 2;
	yield 3;
}

// generator 함수를 통해 반환된 결과값인 gen이 Generator 객체이다.
const gen1 = generator();

// Generator 객체는 iterable, iterator 프로토콜을 준수하고 있기 때문에
// next() 함수를 통해서 이를 순회할 수 있다. 

// iterable 이기 때문에 for ... of 문법 사용가능 
for (el of gen1){
    console.log(el);
}

// iterator 이기 때문에, next()를 통한 순회 가능
const gen2 = generator();
console.log(gen2.next().value); // 0
console.log(gen2.next().value); // 1
console.log(gen2.next().value); // 2

// 위와 같이 새로운 generator 객체를 만들어준 이유는, 
// gen1 객체는 이미 순회가 끝난 객체이므로, 
// next를 호출하면 아래의 값이 반환된다. 
// {value: undefined, done: true} 
```


### yield

Generator 객체의 `next`메서드를 호출하는 경우에는 Generator function 이 실행되어 yield 문을 만날때까지 expression을 진행한다. 그리고 yield 문에서 반환하는 값을 Generator가 반환하게 된다.

```javascript
[rv] = yield [expression]
```

expression : generator function으로 부터 반환되는 값.
rv : yield [expression]을 수행하게 되면 나오는 optional 값으로 generator 객체의 next() 메서드 호출에 전달된다.

즉, generator.next() 호출 -> generator function execution -> yield 값 반환의 순서가 된다.

### return

generator의 next 메서드 실행에서 만약 generator function 내에서 return keyword를 만나게 되면, generator는 멈추게된다. 즉, `done : true` 상태가 되어 버린다.

```javascript
function* foo() {
	yield 1;	
	return 'value';
	// or return;
	yield 2;
}

const boo = foo();

console.log(boo.next()) // { value: 1, done: false}
console.log(boo.next()) // { value: 'value', done: false}
// return; 일 경우 {value: undefined, done: true}
console.log(boo.next()) 
// 이 경우 이미 finish 상태이다. 
// {value: undefined, done: true}
```



A return statement in a generator, when executed, will make the generator finish (i.e. the done property of the object returned by it will be set to true). If a value is returned, it will be set as the value property of the object returned by the generator.
Much like a return statement, an error thrown inside the generator will make the generator finished -- unless caught within the generator's body.
When a generator is finished, subsequent next() calls will not execute any of that generator's code, they will just return an object of this form: {value: undefined, done: true}.


```javascript

```


### yield*

yield가 아닌 `yield*` 키워드를 사용하는 경우에는 또 다른 generator 함수에
위임 하게된다.

### passing arguments into Generators

Generator에 (generator function X) 인자를 넘겨주는 경우에도 generator function이 실행된다.

그리고 `yield` expression을 해당 인자(argument)로 대체하게 된다.



#javascript/iteration