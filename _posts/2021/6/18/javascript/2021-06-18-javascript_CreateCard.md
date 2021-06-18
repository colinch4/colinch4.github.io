---
layout: post
title: "[javascript] CreateCard"
description: " "
date: 2021-06-18
tags: [javascript]
comments: true
share: true
---

# JS ( Browswer)

## :one: ES ( JS 코어 문법 )

> - 바닐라JS
> - Callback Function ( 이벤트를 다루기 위해 필수로 알게 됨 )
>   - function() {}
>   - () => { }  # 에로우 펑션
>   - this
> - `function`



**Javascript 여러가지 Fuction**

```js
  <script>
    // 1. default args (기본 인자)
    function defaultArgs(a=1, b=2) {
      console.log(a + b)
      // return a + b
    }
    defaultArgs()
    defaultArgs(20, 40)

    // 2. JS 함수의 인자 개수
    function wrongArgCount(a, b) {
      console.log(a, b)
    }
    wrongArgCount() // 에러가 안난다.
    wrongArgCount(1)
    wrongArgCount(1, 2, 3)

    function noArgs() {
      console.log('no args...')
    }
    noArgs(1, 2, 3, 4, 5, 6) // 인자를 안받기로 정의해도 실행은 된다.

    // 3. JS rest operator
    function restOperator1(...numbers) {
      console.log(numbers)
    }
    restOperator1(1, 2, 3, 4, 5) // [1,2,3,4,5] 배열 나온다. *args 비슷

    function restOperator2(a, b, ...numbers) {
      console.log(a, b, numbers)
    }
    restOperator2(1, 2, 3, 4, 5) // 1, 2, [3,4,5]

    // 4. JS spread operator
    function spreadOperator(a, b, c) {
      console.log(a, b, c)
    }
    let numbers = [1, 2, 3]
    spreadOperator(numbers[0], numbers[1], numbers[2]) // 아래와 같은 결과
    spreadOperator(...numbers) // spread
    numbers = [1,2,3,4]
    spreadOperator(...numbers) // 3개 까지만 받고 4는 모름

    // 배열 합치기
    let newNumbers =  [0, ...numbers, 5]
    console.log(newNumbers)

    // copy.copy
    newNumbers = numbers // 포인터만 바껴서 numbers 에 push 하면 new 도 바뀜
    newNumbers = [...numbers] // 새로운 배열을 만드는 것

  </script>
```









## :two: DOM ( + BOM )

> HTML 요소들을 직접 만들기
>
> Event



**Bootstrap4 Card 를 만들어보자**

```js
<script>        
      function createCard() {
        const card = document.createElement('div')
        card.classList.add('card', 'col-4')

        const cardImage = document.createElement('img')
        cardImage.src = 'https://picsum.photos/200'
        cardImage.classList.add('card-img-top')
        cardImage.alt = 'random-image'

        const cardBody = document.createElement('div')
        cardBody.classList.add('card-body')

        const cardTitle = document.createElement('h5')
        cardTitle.classList.add('card-title')
        cardTitle.innerText = '<a>Test title</a>'

        const cardText = document.createElement('p') // 위에꺼랑 취사 선택
        cardText.classList.add('card-text')
        cardText.innerHTML = '<a>hi</a>'

        const cardButtom = document.createElement('a')
        cardButtom.classList.add('btn', 'btn-primary')
        cardButtom.href = '#'
        cardButtom.innerText = 'Go somewhere'

        // appendChild : Node 한개만 추가 가능 (노드만 추가해줌)
        // append : 여러 개 Node 추가 가능 + Text 도 가능
        cardBody.append(cardTitle, cardText, cardButtom)
        card.append(cardImage, cardBody)

        // div#cardArea
        const cardArea = document.querySelector('#cardArea')
        cardArea.appendChild(card)
      }
</script>
```



**만들어진 `createCard()` 함수를 실행시켜보자**

```html
<button class="btn btn-primary" onclick="createCard()">CreateCard</button>

<div class="container">
  <div id="cardArea" class="row"> <!-- id는 js에게 양보하자. -->
        <!-- Card Here ! -->
  </div>
</div>
```



## :three:  최종 카드 만드는 코드

> - 부트스트랩 CDN 코드는 너무 길어서 가독성을 위해서 임의로 제거했음
>   - 원래는 CDN 이 들어가 있는 코드임
>   - [부트스트랩 스타터 코드](https://getbootstrap.com/docs/4.5/getting-started/introduction/#starter-template) 를 복사하였음.
> - `태그의 id 속성은 js 가 쓰도록 양보하자.`
>   - 되도록 class 를 이용할것

```html
<!doctype html>
<html lang="ko">
  <head>
    <title>card</title>
  </head>
    
  <body>
      
    <!-- 임의의 Form 을 만들어줘서 사용자 입력데이터를 받아 온다. -->
    <div class="form-group">
      <label for="cardTitleInput">Card Title</label>
      <input id="cardTitleInput" class="form-control" type="text">
      <label for="">Card Text</label>
      <input id="cardTextInput" class="form-control" type="text">
    </div>

    <button id="createCardButton" class="btn btn-primary">CreateCard</button>

    <div class="container mt-3">
      <div id="cardArea" class="row"> <!-- id는 js에게 양보하자. -->
        <!-- Card Here ! -->
      </div>
    </div>

	<!-- 내가 짠 JS 코드 -->
    <script>
      function createCard(title, content) {
        const card = document.createElement('div')
        card.classList.add('card', 'col-4')

        const cardImage = document.createElement('img')
        cardImage.src = 'https://picsum.photos/200'
        cardImage.classList.add('card-img-top')
        cardImage.alt = 'random-image'

        const cardBody = document.createElement('div')
        cardBody.classList.add('card-body')

        const cardTitle = document.createElement('h5')
        cardTitle.classList.add('card-title')
        cardTitle.innerText = title

        const cardText = document.createElement('p') // 위에꺼랑 취사 선택
        cardText.classList.add('card-text')
        cardText.innerHTML = content

        const cardButtom = document.createElement('a')
        cardButtom.classList.add('btn', 'btn-primary')
        cardButtom.href = '#'
        cardButtom.innerText = 'Go somewhere'

        // appendChild : Node 한개만 추가 가능 (노드만 추가해줌)
        // append : 여러 개 Node 추가 가능 + Text 도 가능
        cardBody.append(cardTitle, cardText, cardButtom)
        card.append(cardImage, cardBody)

        // div#cardArea
        const cardArea = document.querySelector('#cardArea')
        cardArea.appendChild(card)
      }


      const createCardButton = document.querySelector('#createCardButton')
      // 대상, 이벤트, 해야할 일
      createCardButton.addEventListener('click', function() {
        const cardTitleInput = document.querySelector('#cardTitleInput')
        const cardTextInput = document.querySelector('#cardTextInput')
        createCard(cardTitleInput.value, cardTextInput.value)

        cardTitleInput.value = null
        cardTextInput.value = null
      })
    </script>
  </body>
</html>
```

