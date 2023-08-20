---
layout: post
title: "[js] rest 파라미터와 스프레드"
description: " "
date: 2021-05-14
tags: [js]
comments: true
share: true
---

## rest 파라미터와 스프레드
rest 파라미터와 스프레드는 문법적으로 유사하다.

## rest 파라미터

Rest 파라미터는 함수의 인자를  배열로 받아들이는 방법이다.

```javascript
function foo(...args){
	console.log(args);
}
foo(1,2,3,4);
>>> [1, 2, 3, 4] 
```

과거 Rest 파라미터 문법이 없었을 때는, arguments 객체를 사용하여, 인자를 받았으나 현재는 Rest 파라미터 문법 사용이 권장된다.

rest 파라미터의 경우에는 인자의 가장 마지막에 사용해야 한다. 그렇지 않으면 Syntax Error가 발생한다.
그리고, rest에는 default 값을 줄 수 없다.

```javascript
function foo(...rest) { } // O
function foo(...rest1, ...rest2) { } //  SyntaxError
function foo(...rest, a, b) { } // SyntaxError

function foo(...rest = []){} // SyntaxError
```

> arguments 객체는 해당 함수 객체의 프로퍼티로, length 정보와 인덱스에 따른 값들을 가지고 있는 유사배열이다.  이 객체는 함수내에서 지역변수처럼 사용이 가능하나, 유사배열이기 때문에 배열이 가지는 메서드가 없어서 `call`이나 `bind` 를 통해서 사용해야했다.

```javascript
function foo(){
    console.log(arguments); // 해당 함수에서 지역변수처럼 사용가능
}

foo(1,2,3);
>>> Arguments(3) [1, 2, 3, callee: ƒ, Symbol(Symbol.iterator): ƒ] // Array를 상속받은 객체가 아니다. 
```


## (Typescript) rest 파라미터

typescript에서 rest 파라미터를 사용하는 경우 아래의 args는 `any[]` 타입이 된다.
```typescript
function foo(...args){
	console.log(args);
}
foo(1,2,3,4);
>>> [1, 2, 3, 4] 
```


만약 rest 파라미터에 타입을 주려고 할 때는 `Array<T>` 혹은 `T[]`을 사용하면된다.

```typescript
function foo(...args: (number | string)[]){
    console.log(args);
}
foo(1,2,'3','4');
```

주의해야할 점은, 배열은 기본적으로 `mutable` 특성을 가지고 있다.  아래와 같이 배열을 선언하는 경우에 arr의 type은 `number[]` 타입이 된다.

```typescript
const arr = [1, 2]; // arr: number[]
```

이러한 경우 spread 문법과 함께 사용되었을 때 문제가 될 수 있다.

```typescript
function sum (a, b) {
	console.log(a + b);
	return a + b;
}
const arr = [1, 2]; // arr: number[]
sum(...arr); // Expected 2 arguments, but got 0 or more.(2556)
```

배열의 mutable 특성 때문에 에러가 발생하게 되는 것이다.(참고1) 왜냐하면 arr는 `const`로 선언되었지만, arr는 mutable하기 때문이다.  `sum` 함수에는 인자를 2개 받도록 되어있지만,  arr는 동적으로 추가되거나 삭제될 수 있기 때문에 문제가 생기는 것이다.

그렇기 때문에 이 경우에는 arr를 type assertion을 통해 해결 해주어야 한다.

```typescript
function sum (a:number, b:number) {
	console.log(a + b);
	return a + b;
}
const arr = [1, 2] as const; 
sum(...arr);
```



> 참고1. mutable? assignment?
> const 키워드를 통해 변수를 선언할 때, mutable과 assignment를 혼용하는 경우가 있다. 만약 변수가 객체인 경우 둘 모두 `=` 연산자를 사용해 mutation과 assignment가 가능하기 때문에 (배열의 경우 push와 같은 메서드)  혼동될 수 있다. 하지만 이 둘은 다른 개념으로 const로 선언된 객체는 mutable 하지만, re-assignment는 되지 않는다.

> 참고2. typescript에서 타입이란?
>  types are used to determine both *reading* and *writing* behavior.
> typescript에서 타입은 해당 타입을 읽고, 쓰는 행위에 제약을 하는 것이다.
>  여기서 const 변수는 string, number 타입과 객체 사이에는 차이가 생기는데 이는 태생적으로 자바스크립트에 영향을 받은 경우이다.
>  const 변수가 string, number와 같은 타입이 들어오는 경우 자바스크립트에서 이 값은 재할당이나 mutation이 불가능하다.  그렇기 때문에, `const a = 'foo'` 와 같은 경우에는 type literal이 되어, a  변수 자체가 'foo' 타입이 되는 것이다.
>
>  하지만 자바스크립트의 객체는 각 프로퍼티의 값을 객체 자체가 소유하지 않고, 레퍼런스를 가지게 된다. 이 레퍼런스 자체(가리키고 있는것)는 immutable 하지만,  레퍼런스가 가지는 값은 immutable하다.
>  따라서 객체를 const로 선언하는 경우에는  각각의 프로퍼티는 이후에 수정될 수 있기 때문에, 타입이 추론되기는 하지만, type literal이 되지 않고,  string, number 와 같은 일반적인(general) 형식으로 추론되는 것이다.


## 스프레드 문법

스프레드 문법은 이터러블을 개별 값들로 전개(펼쳐줌)해주는 문법이다.  스프레드는 연산자가 아니기 때문에(값, value가 아니다), 이를 통해서 변수에 할당할 수는 없다.


```javascript
console.log(...[1, 2, 3]); // 1 2 3 
// console.log(1, 2, 3) // 1 2 3
console.log(...'foo'); // f o o
// console.log('f', 'o', 'o'); // f o o 

const a = ...[1, 2, 3] // Syntax Error
```


> 참고3. 이터러블은 Array, String, Map, Set 과 같은 객체이다.


> 참고4. 스프레드 문법은 Rest 파라미터 문법과 `...` 키워드를 사용한다는 점에서 형태가 동일하다. 하지만 Rest 파라미터는 함수를 선언, 정의할 때 가변인자를 받기 위해서 즉, 여러 개의 값을 배열 묶음으로 받는 문법이고, 스프레드는 오  이터러블의 형태로 묶여있는 데이터를 전개한다는 점에서 완전히 반대되는 역할을 한다.

## 스프레드 문법 UseCase

스프레드 문법은 이터러블을 `전개` 해준다는 점에서 이러한 문맥에서 사용될 수 있다.

- 함수 `호출`시 인자
- 객체 리터럴
- 배열 리터럴
- 불변성

### 객체 리터럴

객체는 이터러블이 아니기 때문에, 스프레드 문법을 사용할 수 없었으나 ES2018에 Rest/Spread 프로퍼티라는 스펙으로 제안되었다.  [Rest/Spread Properties for ECMAScript](https://github.com/tc39/proposal-object-rest-spread)

그렇기 때문에 객체의 경우에도 스프레드 문법을 사용할 수 있게 되었다.

```javascript
const obj1 = { a: 'foo', b: 'boo'};
const obj2 = { ...obj };

console.log(obj2);
>>> { a: 'foo', b: 'boo'}
console.log(ob1 === obj2);
>>> false
```

스프레드 문법을 통해서 객체를 병합하는 것이 쉬워졌다.  과거에는 객체를 병합하기 위해서는 `Object.assign()` 함수를 통해 객체를 병합하여, 새로운 객체를 만들 수 있었으나, 스프레드 문법을 사용하면 쉽게 병합할 수 있게 되었다.

```javascript
// before es2018
const obj1 = { a: 'foo', b: 'boo'};
const obj2 = { b: 'baz', c: 'bar' };
const mergedObj = Object.assign({}, obj1, obj2);

>>> {a: "foo", b: "baz", c: "bar"}

// spread operator
const obj1 = { a: 'foo', b: 'boo'};
const obj2 = { b: 'baz', c: 'bar' };
const mergedObj = { ...obj1, ...obj2};

>>> {a: "foo", b: "baz", c: "bar"}
```

위와 같이 병합시에는 앞선 프로퍼티와 뒤에 오는 프로퍼티가 겹치는 경우, 뒤에 오는 프로퍼티로 값이 덮어씌어진다.  그렇기 때문에 `b` 프로퍼티는 'boo'가 아니라 'baz'가 되는 것이다.



### 불변성

리액트와 같은 프론트엔드 프레임워크를 다루다보면, 불변성이라는 개념이 나오게 된다. 데이터의 불변성을 유지하는 것은 왜 중요할까?

```javascript
const Component = () => {
	const [value, setValue] = useState({a: 'foo', b: 'boo'});
	
	const handleClick = () => {
		value.a = 'baz';
	}
	return (
		<>
			<div>{value.a}</div>
			<div>{value.b}</div>
			<button onClick={handleClick}>클릭</button>
		</>
	)
}
```

위와 같은 코드를 작성하게 되면  `value.a` 영역의 텍스트가 변화하지 않는다. 그 이유는 리액트는 얕은 비교를 통해서 props, state의 변경을 감지하고 다시 렌더링을 하기 때문이다.

위의 경우 value는 내부의 프로퍼티의 값이 바뀌었지만, value 자체에 대한 레퍼런스는 변경되지 않았기 때문에, 리액트는 이 값이 변경되었다는 것을 감지하지 못한다.

아래의 경우도 실제로는 렌더링되지 않는데, `useState`로 반환된 value는 immutable 이기 때문이다.

```javascript
const handleClick = () => {
		value = { ...value, a: 'baz'};
}
```

아래의 코드의 경우는 만약 버튼을 클릭하게 되면, 2번째 <div> 태그안에 값이 사라지게 된다.  Class Component와 달리 `useState`의 `setState`는 state를 병합하지 않는다. 따라서 `setValue` 함수의 인자로 들어간 값 그 자체가 `state`가 된다.

```javascript
const Component = () => {
	const [value, setValue] = useState({a: 'foo', b: 'boo'});
	
	const handleClick = () => {
		setValue({
    		a: 'baz'
		})
	}
	return (
		<>
			<div>{value.a}</div>
			<div>{value.b}</div>
			<button onClick={handleClick}>클릭</button>
		</>	
	);
}
```

```javascript
// 1
setValue({
	a: 'baz',
	b: 'boo',
})
// 2
setValue({
	...value,
	a: 'baz',
})
```

1번과 같은 방법으로 해결할 수 있지만, state 객체가 커지는 경우에 실수하는 경우가 생길 수도 있고, 매번 적어주는 것은 번거로운 작업이 될 것이다. 따라서, 2번과 같이 스프레드 문법을 사용한다면, 실수도 줄이고, 코드도 줄일 수 있다.

추가적으로, 스프레드 문법을 이용한다면, 성능상에서도 이점을 볼 수 있다.

> 참고. 아래의 예제 Foo는 `React.memo()`가 적용되어 있다고 가정.


위의 예에서 `b`프로퍼티가 객체라고 가정을 했을때, 스프레드 문법을 이용한다면 해당 객체의 레퍼런스는 변하지 않았다.

아래와 같은 코드가 있을때, 1번 방식으로 작성을 한다면 `<Foo>` 컴포넌트는 `React.memo`를 해주어도,  리렌더링이 될 것이다. 왜냐하면, setState 내부에 새로운 객체를 만들면서 `b` 프로퍼티를 새로 만들었기 때문에 메모리에 새로운 주소가 생겼고, 리액트는 따라서 이를 다른 값이라고 판단하기 때문이다.

하지만  2번 방식을 사용하는 경우에는 b 객체의 레퍼런스를 그대로 받기 때문에,  
Foo가 리렌더가 일어나지 않게 된다.


```jsx
return (
		<>
			<div>{value.a}</div>
			<Foo data = {value.b}/>
			<button onClick={handleClick}>클릭</button>
		</>	
	);
```




#javascript/rest와스프레드 