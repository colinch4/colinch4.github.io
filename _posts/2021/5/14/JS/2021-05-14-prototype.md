---
layout: post
title: "[js] 프로토타입"
description: " "
date: 2021-05-14
tags: [js]
comments: true
share: true
---

## 프로토타입

## 프로토타입

```
Contructor   prototype 
    | new    / 
    |       /
    |      /
instance  __proto__
```

prototype property는 아래와 같은 특성을 가진다.
- writable : false
- Enumerable : false
- configurable : false

따라서, Object.key

모든 `함수`는 prototype이라는 특수한 프로퍼티를 가진다.


##  프로토타입 가져오기.
- `getPrototypeOf`  : 스펙상 공식적인 방법.
- `__proto__` : 비표준으로, 웹 브라우저가 지원. 현재 deprecated.

```javascript
// example1
const person = {
	name: 'mike',
}
const prototype = Object.getPrototypeOf(person);
console.log(typeof prototype);
console.log(person.___proto__ === prototype);

// example2
const Person = function () {
    
};
const pius = new Person();
Object.getPrototypeOf(pius);
// >>> Pius
Object.getPrototypeOf(pius) === pius.__proto__
// >>> true
```

## 프로토타입 설정하기
new Operation을 사용하면, 생성자 함수의 `prototype property`를 인스턴스의 `__proto__` 가 가리킨다.


```javascript
// new operation
const Person = function () {
    
};
const pius = new Person();
pius.__proto__ === Person.prototype
>>> true

// manually 
const Person = function () {
    
};
const pius = {
    name: 'pius'
};
Object.setPrototypeOf(pius, Person);
pius.__proto__
>>> Person
```

## prototype chain

```javascript
const person = { 
	name: 'pius',
}
const programmer = {
	language: 'js'
} 
const frontendDev = {
	framework: 'react'
}

Object.setPrototypeOf(programmer, person);
Object.setPrototypeOf(frontendDev, programmer);

// 자신에게 해당 속성이 없으면 프로토타입을 따라서 올라가게 된다.
console.log(frontendDev.name, frontendDev.language);
>> pius js

console.log(
	frontendDev.__proto__.__proto__.name,
	frontendDev.__proto__.language
);
>>> pius js
```


```javascript
const person = { 
	name: 'pius',
}
const programmer = {
	language: 'js'
}
Object.setPrototypeOf(programmer, person);
programmer.name = 'pius712'
console.log(programmer.name);
>>> pius712
console.log(person.name);
>>> pius
// 덮어 쓰는 것이 아니라, 자기 자신의 포로퍼티에 할당을 하고, 프로토타입의 속성은 shadowing 된다. 
```

## prototype 상속

```javascript
const person = { 
	name: 'pius',
}
const programmer = {
	language: 'js'
}
Object.setPrototypeOf(programmer, person);

for (const prop in programmer) {
	console.log(prop);
}
>>> language
>>> name

for (let prop in programmer) {
	if(programmer.hasOwnProperty(prop) {
		console.log(prop);
	}
}
>>> language
for (let prop of Object.keys(programmer)){
	console.log(prop);
}
>>> langugage
```

## 생성자 함수

	- 모든 함수는 프로토타입 프로퍼티를 가진다. 
	- 모든 함수의 프로토타입은 `Function.prototype` 이다. 
```javascript
function Person(name) {
	// this = {};
	this.name = name;
	// return this;
}
const person = new Person('pius');
console.log(person.name);
>>> pius
console.log(person);
>>> { name : 'pius' };
```

```javascript
function Person(name) {
	this.name = name;
}
const person = new Person('pius');

console.log(Person.prototype);
// Person.prototype
// 이거는 프로토타입 속성
console.log(Object.getPrototypeOf(person); 
// person.__proto__
// 이것은 프로토타입

person.__proto__ === Person.prototype
>>> true
```

```javascript
function Person(name) {
	this.name = name;
}
const citizen = new Person('pius');

console.log(Object.getPrototypeOf(Person) !== Person.prototype);

console.log(Object.getPrototypeOf(citizen) === Person.prototype);

console.log(Object.getPrototypeOf(Person) === Object.prototype);

console.log(Object.getPrototypeOf(Person) === Function.prototype);

console.log(Object.getPrototypeOf(Object) === Function.prototype);

console.log(Object.getPrototypeOf(Function.prototype) === Object.prototype);

console.log(Object.getPrototypeOf(Object.prototype) === null); 
```

##  기본 타입 (리터럴 생성)
```javascript
const obj = {};
const arr = [];
const num = 123.456;
const str = 'abc';

console.log(Object.getPrototypeOf(obj) === Object.prototype); 

console.log(Object.getPrototypeOf(arr) === 
Array.prototype);

console.log(Object.getPrototypeOf(num) === Number.prototype);

console.log(Object.getPrototypeOf(str) === String.prototype);

console.log(num.toFixed === Number.prototype.toFixed);
```

## 프로토타입 프로퍼티 수정

```javascript
function Person(name) {
	this.name = name;
}

const person1 = new Person('mike');

const newPrototype = {
	arr : [],
	push(value) {
		this.arr.push(value);
	},
	getArr(){ 
		return this.arr
	}
}

Person.prototype = newPrototype;
const person2 = new Person('pius');
console.log(Object.getPrototypeOf(person1) 
					!== newPrototype);
>>> true
console.log(Object.getPrototypeOf(person2) 
					=== newPrototype);
>>> true
person2.push(1);
person2.push(2);
console.log(person2.getArr());
```

## 상속 최적화
```javascript
function Person() {
	this.fn1 = function () {},
	this.fn2 = function () {},
}
const person1 = new Person();
const person2 = new Person();
>> 인스턴스 생성마다 fn1, fn2 함수가 생성된다.

function Person() { }
Person.prototype = {
	fn1 = function () {},
	fn2 = function () {}
}
const person1 = new Person();
const person2 = new Person();
>> 프로토타입에 있는 함수의 경우, 객체마다 복사하지 않고 참조하기 때문에 함수를 복사하지 않아서 메모리 효율적이다. 
```

## Constructor

```javascript
function Person(name) {
	this.name = name;
}
console.log(Person.prototype.constructor === Person);
>>> true
console.log(Person.constructor === ?);
// Person에는 constructor라는 프로퍼티가 없다. 
// 따라서 Person.__proto__.constructor를 찾아간다.
// Person.__proto__.constructor === Person.constructor
// Person.__proto__ 는 Function 객체의 prototype 프로퍼티이다. 
// Function 객체의 prototype 프로퍼티에 해당하는 객체는
// Function 객체를 가리키는 constructor 프로퍼티가 있는데,
// Person.constructor는 이를 가리키는 것.
```


### 프로토타입 상속

```javascript
function Person(name, age) {
	this.name = n;
	this.age = a;
}

Person.prototype.setOlder = function() {
	this.age += 1;
}
Person.prototype.getAge = function() {
	return this.age;
}

var person1 = new Person('pius1', 29);
var person2 = new Person('pius2', 30);

person1.setOlder();
person1.getAge();
person2.setOlder();
person2.getAge();
```



#javascript/객체#