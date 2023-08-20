---
layout: post
title: "[javascript] Array Helper Methods"
description: " "
date: 2021-06-18
tags: [javascript]
comments: true
share: true
---

## Array Helper Methods

> - map(), forEach(), filter()
>   - 인자로 함수 자체가 와야함.
> - 콜백함수 개념



## :one: Map()

```js
    /* 1. map */
    ['1', '2', '3'].map(Number) // map(int, ['1','2','3']) 파이썬문법

    const numbers = [0, 9, 99]

    function addOne(number) {
      return number + 1
    }

    const newNumbers1 = numbers.map(addOne)
    console.log(newNumbers1)

    const newNumbers2 = [0, 9, 99].map(function(number) {
      // [0, 9, 99] 를 순회하며, 각 요소를 (number) 자리에 넣는다.
      // 그리고 리턴된 값을 새로운 배열에 넣고 마지막에 리턴한다.
      // [] => [1] => [1, 10] => [1, 10, 100] ... 리턴 순서
      return number + 1
    })
    console.log(newNumbers2)
```



## :two: forEach()

```js
/* 2. forEach */
    // let sum = 0; 세미콜론!! 없으면 에러 날수도있음 0[1,2,3] 으로 인식해버림
    // [1,2,3].forEach() 에러발생 

    let sum = 0
    const newNumbers = [1,2,3]

    newNumbers.forEach(function(number) {
      // newNumbers 의 각 요소를 number 자리에 넣고,
      // 나머지는 알아서 하세요. 리턴 없습니다.
      sum += number
    })
    console.log(sum)
```



## :three: filter()

```js
    /* 3. filter */
    const adds = [1, 2, 3].filter(function(number) {
      // 각 요소를 number 자리에 넣고,
      // 리턴이 true 인 요소들만 모아서 새로운 배열로 리턴.
      return number %  2 === 1
    })
    console.log(adds)
```

