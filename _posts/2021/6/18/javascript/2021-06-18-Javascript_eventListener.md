---
layout: post
title: "[javascript] eventListener"
description: " "
date: 2021-06-18
tags: [javascript]
comments: true
share: true
---

## Javascript

## :one: eventListener

> - 콜백함수 개념이 들어간다.
>   - `a함수가 b함수를 인자로 받아서 a함수 내에서 b함수를 실행하면 콜백, 실행 안하면 X `
>
> - JS 에서의 함수는 1급 객체로서 함수안의 인자가 함수로 들어갈 수 있다.

```js
class Node {
    addEventListener(eventName, callback) {
        if (evenName) {
            callback()
        }
    }
}

class Gang {
    passedFunctionButNotCallback(notCallback) {
        // notCallback()
    }
}

// 전달되는 함수 === callback 이다? (XXXXX 아니다.)
// a함수가 b함수를 인자로 받아서 a함수 내에서 b함수를 실행하면 콜백, 실행 안하면 X 
```





**eventListener("___", 함수)**

- ___ 는 크롬 개발자 도구 `F12 - Elements - Event Listener` 에 있다.
  - 공식문서에는 엄청나게 많아서 외울수가 없음
  - 쓰다보면 자주 쓰는 것 위주로 외우게 됨 





```html
<button id="myButton">얍</button>  

<script>
    // 변수 정의
    const myButton = document.querySelector('#myButton')
	
    // 방법 1
    function confirmMessage(event) {
        confirm('얍?')
    }
    // 요소.addEventListener('이벤트', '이벤트 발생시 실행할 함수')
    myButton.addEventListener('click', confirmMessage)

    
    // 방법 2
    // '이벤트' 가 발생 => 함수를 실행한다.
    // path('article/', views.index) 랑 똑같음. 콜백함수 이미 장고에서 쓰고있었음
    // article 경로로 들어오면 views.py 에 index() 함수 실행 시킨다.
    myButton.addEventListener('click', function(event) {
        confirm('얍!!')
    })
</script>
```



**복사 금지 코드**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nono Copy</title>
</head>
<body>
  <h1>복사 이제 안된다.</h1>
  <script>
    document.addEventListener('copy', function(event) {
      console.log(event)
      event.preventDefault()
      alert('복사하지마셈')
    })
  </script>
</body>
</html>
```

