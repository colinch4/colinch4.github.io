---
layout: post
title: "[JavaScript] 동적 형 지정 / 자동 형 변환"
description: " "
date: 2021-09-09
tags: [javascript]
comments: true
share: true
---

## 동적 형 지정 / 자동 형 변환

## JavaScript 데이터 유형 변환

JavaScript는 동적 형지정 언어이다. (대표적인 동적 형 지정 언어: JavaScript, Python)

* 변수를 선언할 때 데이터 형을 지정할 필요가 없다
* 데이터 형이 스크립트 실행 도중 필요에 의해 자동으로 변환된다

```js
var total = 1456;
var current = 10;
var message = '동적 형 지정언어 JavaScript';
var show = false;
```

위 변수에는 어떤 데이터 형도 올 수 있으며, 필요에 따라 자동으로 형이 변경된다. (장점이자 단점)

대표적인 정적 형 지정 언어: C, Java

Typescript는 정적 형 지정 언어처럼 사용이 가능하며, 지정 후 JavaScript로 변환된다. 정적 형 지정언어의 장점은 디버깅이 유용한 것이다.

## JavaScript의 형 변환

```js
var n = 9;
var m = 'hi good job';
n + m
> "9hi good job"
```

9라는 숫자 데이터 형이 자동으로 스트링 형으로 변경되는 상황을 확인할 수 있다.

### 숫자 값이 문자로 변경되는 경우

```Js
String(숫자)
숫자 + ''
```

### 숫자형 문자 값이 숫자로 변경되는 경우

```js
var k = '12345' // k 의 값 선언

Number(k)
+k
k - 0
k * 1
k / 1
```

명시적으로 `Number(숫자 데이터)` 와 같이 작성하는것이 바람직하다.

```js
k + 'px' // '12345px'이 되며, k에 이 값을 다시 대입하고 싶은 경우 아래와 같이 작성한다
k = k + 'px' // 이 경우 k의 값에 '12345px' 이 대입 된다
```

이후 k는 숫자 형 데이터가 아닌 문자 형 데이터가 된다

```js
Number(k);
> NaN
```

NaN = Not a Number

### 문자 값을 숫자로 변경해야 하는 경우

```js
window.parseInt(문자,10)
window.parseFloat(문자,10)
```

Integer: 정수

Float: 실수(소수를 포함)

### 불리언 값으로 변경하는 경우

```js
Boolean(데이터유형)
!!데이터유형
Boolean(1)
> true
Boolean(-1)
> true
Boolean(0)
> false
0 == false
> true
```

0은 자동으로 불리언의 `false` 로 형변환이 이루어진다.

`0`,`''` (빈 문자열), `null`, `undefined` 는 부정을 의미하며 불리언값의 false로 변환되게 된다.

함수`function(){}`, 배열 `[0, 1, 2]`, 객체 `{object}` 는 존재한다고 인식하며 true로 변환된다.

## 참고

- [window.parseInt()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/parseInt)