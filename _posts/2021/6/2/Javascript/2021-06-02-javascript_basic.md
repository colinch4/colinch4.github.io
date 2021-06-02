---
layout: post
title: "[javascript] Javascript Theory"
description: " "
date: 2021-06-02
tags: [javascript]
comments: true
share: true
---

# Javascript Theory

> Nomad Coders 바닐라JS강의를 들으면서 학습한 내용입니다.

<br>

## 기본 개념
* Javascript는 동적인 웹페이지를 구현하기 위해 개발된 언어이다. 즉, 사용자와 상호작용하는 언어.
HTML은 한번 출력되면 그 정보가 바뀌지 않지만 Javascript는 바꿀 수 있다. 
~~~html
 CSS: lovely (꾸며줌)
 html: Dog (정보)
 Javascript: barks (동작)
~~~

<br>

## JS ES6, Vanilla Javascript란?
* Javascript의 정확한 코드네임은 ECMA Script이고 넘버가 올라갈수록 새로운 스펙으로 업데이트가 된다.
* Javascript는 꽤나 중앙 집중화 되어 있어서 누가 스펙을 업데이트를 하면 모든 브라우저에서 작동을 하게 된다. (여기서 자바스크립트 스펙이라하면 어떻게 사용하는지를 알려주는 메뉴얼 책자 같은거다.) 그래서 ES6라함은 가장 최신 스펙의 Javascript를 말하는것. (2020.2 기준)
* 파이어폭스나 크롬 같은 브라우저가 하는 일은 이런 자바스트립트 스펙을 받아서 자기들 방식으로 실행한다. 즉, 같은 결과를 이루려고 노력하는데 자기들만의 방식을 사용한다는 것. __하지만 처음 배우는 단계에서는 이런걸 고려할필요가 없음. 그냥 자바스크립트를 배우면 됨!__
* 바닐라자바스크립트는 라이브러리가 없는 자바스크립트 자체를 말한다. 메이크업 없는 자바스크립트. 날 것의 자바스크립트라고 보면 된다. 바닐라자바스크립트를 잘 다룰 줄 알아야 진정한 실력자다.

<br>

## Javascript를 이해하기 위한 간단한 간단한 규칙들
1) 모든 expressions은 각각 다른 라인에 위치해야한다.

2) 하나의 expression이 끝남을 선언하는 방법은 ; 세미콜론

3) 변수를 사용하는 기본방법
> 1 create(변수 생성) 2 initialize(초기화) 3 use(사용)
```
let a = 221;
```
* 이라 하면 a 라는변수를 생성하고 221로 초기화한것이다.
(이 두개는 한번에 가능)
* let은 처음 변수를 생성했음을 선언하는 표현.
* 내 변수가 바뀌어도 괜찮다면 let을 사용해야하지만, 바뀌어선 안되는것이라면 const를 사용해야한다. (상수)
변수를 선언하는 var라는 것도 동일하게 적용되지만 자바스크립트에서 var로 인해 생기는 문제들이 종종 발생함.
* 변수를 사용할때, 기본으로 const를 사용하는 연습하기. 내가 필요해질때까지 let은 쓰는거 아님!

<br>

## 변수 타입

### 원시 타입
* Number : 숫자
* String : 문자
  * "" 사이에 있는것을 자바스크립트는 텍스트로 받아들인다.
* Boolean: True or False
* Null: 빈 값
* Undefined: 빈 값
* Symbol : ES6에서 새로 등장한 개념. 지금은 신경쓸 필요 없음

### 객체 타입
* Object
~~~
// Number
var num1 = 1001;
var num2 = 10.50;

// String
var string1 = 'Hello';
var string2 = "World";

// Boolean
var bool = true;

// null
var foo = null;

// undefined
var bar;

// Object
var obj = { name: 'Lee', gender: 'male' };

// Array
var array = [ 1, 2, 3 ];

// function
var foo = function() {};
~~~

<br>

## Reference
* https://velog.io/@rimu/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-classList.add-remove-contains-toggle
* https://poiemaweb.com/js-syntax-basics