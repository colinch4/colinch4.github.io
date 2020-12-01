---
layout: post
title: "[Javascript기초] Arrow function"
description: " "
date: 2020-01-05
tags: [Javascript]
comments: true
share: true
---


## Arrow Function

> ```javascript
> // 매개변수 지정 방법
> () => { ... } // 매개변수가 없을 경우 
> x => { ... } // 매개변수가 한 개인 경우, 소괄호를 생략할 수 있다. 
> (x, y) => { ... } // 매개변수가 여러 개인 경우, 소괄호를 생략할 수 없다. 
> 
> // 함수 몸체 지정 방법 
> x => { return x * x } // single line block
> x => x * x // 함수 몸체가 한줄의 구문이라면 중괄호를 생략할 수 있으며 암묵적으로 return된다. 위 표현과 동일하다. 
> 
> () => { return { a: 1 }; } 
> () => ({ a: 1 }) // 위 표현과 동일하다. 객체 반환시 소괄호를 사용한다. 
> 
> () => { // multi line block. const x = 10; return x * x; };
> ```



