---
layout: post
title: "[JavaScript] 데이터 유형과 리터럴"
description: " "
date: 2021-09-09
tags: [JavaScript]
comments: true
share: true
---

# 데이터 유형과 리터럴

데이터 유형(Data Types): JavaScript 변수에 할당/참조 가능한 값

리터럴(Literal): 컴퓨터 과학 분야에서 리터럴은 소스코드의 고정된 값을 대표하는 용어이다. 거의 모든 프로그래밍 언어는 정수, 부동 소수점 숫자, 문자열, 불리언(Boolean) 데이터 타입과 같은 용어를 가진다. 리터럴과 대조적으로 고정된 값을 가질 수 있는 변수나 변경되지 않는 상수가 있다. 다음과 같이 리터럴은 변수 초기화 과정에서 사용된다.

```js
// 변수 til에 문자 리터럴 'today i learned' 데이터 값이 할당됨
var til='today i learned'
```

## 데이터 유형(Types)

최신 ECMAScript 표준은 7가지 데이터 유형을 정의한다

6가지 원시 데이터(Primitive Data) 유형

- null
- undefined
- number
- string
- boolean
- symbol (ES6+)

그리고 객체(Object) 데이터 유형 (일반 객체, 배열 객체, 함수 객체)

- function object
- array object
- object

객체는 아래와 같이 생성할 수 있다

```js
new 생성자 함수()

// 1. 함수
new Function()
// 2. 배열
new Array()
// 3. 오브젝트
new Object()
```

숫자, 문자, 불리언은 객체라고 볼 수 있다.

```js
90; // 원시 데이터 값
var n = new Number(90); // 숫자 객체 생성

n.valueOf() // n의 값을 도출
```

위는 숫자 90이라는 값을 도출 하기위해 객체를 생성하고 호출 하는 과정이다. 이 과정이 불합리하기 때문에 **원시 데이터는** 객체를 생성하는것 보다는 **그 자체를 그대로 사용하는것이 유용**하다.

## 리터럴(Literal)

JavaScript에서 값을 나타내기 위해 리터럴을 사용한다. 스크립트에 부여한 고정값으로, 변수가 아니다.

- number 리터럴
- string 리터럴
- boolean 리터럴
- array 리터럴
- function 리터럴
- object 리터럴

아래와 같이 각각을 객체로 생성한 후 호출해 사용할 수 있다.

```js
fn = new Function(); // 함수 선언
fn // 함수 호출

var arr = new Array(); // 배열 선언
arr // 배열 호출

var obj = new Object(); // 오브젝트 선언
obj // 오브젝트 호출
```

하지만, 자바스크립트에서 부여한 고정값으로 더 편리하게 사용이 가능하다.

```js
// 함수: function(){};
// 배열: []
// 오브젝트: {}
```

## 작성 패턴

한줄에 모든 객체를 선언하는 패턴 :

```js
var num=9, str='nine', boo=true, fun=fucntion(){}, arr=[], obj={};
```

Single var pattern :

```js
var num=9, 
    str='nine', 
    boo=true,
    fun=fucntion(){},
    arr=[],
    obj={};
```

가장 일반적인 패턴 :

```js
var num=9, 
var str='nine', 
var boo=true,
var fun=fucntion(){},
var arr=[],
var obj={};
```

## 참고

- [문법과 타입](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Values,_variables,_and_literals)

