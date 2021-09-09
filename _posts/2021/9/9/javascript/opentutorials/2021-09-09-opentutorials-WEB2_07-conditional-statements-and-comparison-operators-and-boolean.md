---
layout: post
title: "[JavaScript] 조건문과 비교 연산자 그리고 불리언"
description: " "
date: 2021-09-09
tags: [JavaScript]
comments: true
share: true
---


# 조건문과 비교 연산자 그리고 불리언

## **조건문 예고**

하나의 프로그램이 하나의 흐름으로 가는것이 아니라 조건에 따라 다른 순서의 기능들이 실행되도록 하는 것. 프로그래밍을 통해 반복적인 일을 하지 않게 되었다면, 조건문은 단순 반복문이 아니라 복잡한 업무에서도 해방시켜주는 혁명적인 도구!

## **비교 연산자와 Boolean 데이터 타입**

비교 연산자, Boolean(데이터 타입), 조건문을 연달아 학습

```html
<h1>Comparison operators & Boolean</h1>
<h2>=== 동등 비교 연산자</h2>
<h3>1===1</h3>
<script>
  document.write(1===1);
</script>

<h3>1===2</h3>
<script>
  document.write(1===2);
</script>

<h3>1&lt;2</h3>
<script>
  document.write(1<2);
</script>

<h3>1&lt;1</h3>
<script>
  document.write(1<1);
</script>
```

왼쪽과 오른쪽 항(좌항, 우항)의 관계에 따라 `true` 혹은 `false`를 나타내는 연산자이다. `true`와 `false`는 Boolean형의 데이터 (데이터 타입)이다.

비교연산자를 통해 Boolean형 데이터(`true`, `false`)를 만들 수 있다. 이 Boolean을 조건문, 반복문을 통한다면 큰 가능성을 마주할 수 있다.

```html
<h1>Conditional statements</h1>
  <h2>program</h2>
  <script>
    document.write("1<br>");
    document.write("2<br>");
    document.write("3<br>");
    document.write("4<br>");
  </script>

  <h2>IF-true</h2>
  <script>
    document.write("1<br>");
    if (true) {
      document.write("2<br>");
    } else {
      document.write("3<br>");
    }
    document.write("4<br>");
  </script>

  <h2>IF-false</h2>
  <script>
    document.write("1<br>");
    if (false) {
      document.write("2<br>");
    } else {
      document.write("3<br>");
    }
    document.write("4<br>");
  </script>
```

if문 뒤에는 boolean이 오며 true라면 if문 안에 있는 코드가 실행, false라면 else문 안에 있는 코드가 실행된다. `if(condition)` 괄호안에 어떤 조건(참, 거짓을 알 수 있는 데이터)을 넣는지에 따라 똑똑한 프로그래밍을 할 수 있게된다.

## **조건문의 활용**

[실습 예제](https://codepen.io/onlyeon/pen/zYvLNqy)

Javascript에서 vlalue값을 가져오는 방법. javascript element get value

```jsx
document.querySelector('#night_day').value === 'night'
```

ID가 `night_day` 인 엘리먼트를 찾고 그 엘리먼트의 `value`가 `night` 인지 확인한다.

## **리팩토링(refactoring)**

코딩을 하고나서 동작은 그대로 두고 코드를 효율적으로 개선하기 위한 작업. 가독성을 높이고 중복된 코드를 제거해 유지보수를 편리하게 만든다.

엘리먼트 그 자체를 선택하기 위해 `id`로 선택할 필요 없이 `this` 로 선택이 가능하며, 반복되는 부분은 변수로 선언해준다.

```jsx
// before
onclick="
  if (document.querySelector('#night_day').value === 'night') {
    document.querySelector('body').style.backgroundColor = 'black';
    document.querySelector('body').style.color = 'white';
    document.querySelector('#night_day').value = 'day';
  } 
  else {
    document.querySelector('body').style.backgroundColor = 'white';
    document.querySelector('body').style.color = '#0ebeff';
    document.querySelector('#night_day').value = 'night';
}"

// after
onclick="
  var target = document.querySelector('body');
  if (this.value === 'night') {
    target.style.backgroundColor = 'black';
    target.style.color = 'white';
    this.value = 'day';
  } 
  else {
    target.style.backgroundColor = 'white';
    target.style.color = '#0ebeff';
    this.value = 'night';
  }"
```

📌 코딩 잘 하는 방법! 중복을 끝까지 쫓아가서 다 없애라!