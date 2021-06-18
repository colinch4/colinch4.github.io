---
layout: post
title: "[javascript] This"
description: " "
date: 2021-06-18
tags: [javascript]
comments: true
share: true
---

# javscript => This

> - JS 는 OOP 언어이다? 객체 지향 언어 (O)
> - this => 무조건 '어떤' object 를 지칭
> - method => 객체안에 정의된 함수 `( .methodname()으로 실행되는 함수)`
> - function => method 가 아닌 모든 함수 ( 일단 이렇게 이해해야 편함 )
> - `function() {}` 정의 할 때,
>   - this 가 window 가 아닌 경우. **딱 2가지!!**
>     1. **method 안의 this -> 해당 method 가 정의된 객체 (object)**
>     2. **생성자 함수 안의 this**



**method 정의할 때, function() {} 로 정의 한다.**

```html
<script>
    const obj = {
      name: 'obj',

      method1: function () {
        console.log(this)
      },

      objInObj: {
        name: 'oio',
          
        // oioMethod: function () {} ==> 아래와 완전히 같음
        oioMethod () { // ES6 문법설탕: 코드를 짧고 쉽게
          console.log(this) // objInObj
        }
      },

      arr: [0, 1, 2],

      newArr: [],

      method2 () {
        this.arr.forEach(
          /*
          function(number) {
            // console.log(this)
            this.newArr.push(number * 100)
          }.bind(this)
          */
          (number) => {
            this.newArr.push(number * 100)
          }
        )
      }
    }
</script>    
```





 **:cupid:ES6 이후 addEventListener**

- `this -> event.target`

```js
  // 예전코드 (관습)
  const dogButton = document.querySelector('#dog')
  dogButton.addEventListener('click', function(event) {
    this. // dogButton, event.target, 불려진 객체, 수동적
  })

  // 최근코드 ( ES6 이후 )
  dogButton.addEventListener('click', (event) => {
    event.target
  })
```