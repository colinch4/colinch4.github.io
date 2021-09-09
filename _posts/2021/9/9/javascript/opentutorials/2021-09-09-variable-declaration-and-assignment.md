---
layout: post
title: "[JavaScript] 변수 선언 / 값 할당"
description: " "
date: 2021-09-09
tags: [JavaScript]
comments: true
share: true
---


# 변수 선언 / 값 할당

## 선언

JavaScript의 선언에는 3가지 방법이 있다.

- [`var`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/var)

  변수를 선언. 추가로 동시에 값을 초기화

- [`let`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let)

  블록 범위(scope) 지역 변수를 선언. 추가로 동시에 값을 초기화

- [`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const)

  블록 범위 읽기 전용 상수를 선언

기억하고 싶은 데이터 유형을 변수(variable)에 참조(reference)/할당(assignment)한다. 

### 변수 선언

```js
var current year; // 공백으로 인한 error
var current-year; // 하이픈으로 인한 error

var currentYear; // camelCase success
var current_year; // snake_case success
```

`=`  할당 연산자(operator) 를 통해 값(literal) 할당(assignment) 할 수 있다.

## 참고

- [문법과 타입](