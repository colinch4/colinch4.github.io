---
layout: post
title: "[JavaScript] 반복문과 배열"
description: " "
date: 2021-09-09
tags: [JavaScript]
comments: true
share: true
---

## 반복문과 배열

## **반복문 예고**

배열, 배열을 이용한 반복문을 학습한다.

## **배열**

Array. 복잡한 내용 단순화하고 정리하기 위한 일종의 수납상자. 배열의 문법과 성격을 살펴본다.

배열 만들기

배열은 대괄호 안에 들어가며 여러개의 값을 가질 수 있다. 

```jsx
var fruits = ["바나나", "딸기", "사과"];
```

배열 가져오기

```jsx
document.write(fruits[1]);
// 결과: 딸기
```

배열에 들어있는 값이 몇 개인지 체크하기

[Javascript array count](https://www.w3schools.com/jsref/jsref_length_array.asp)

```jsx
document.write(fruits.length);
// 결과: 3
```

배열에 데이터 추가하기

```jsx
document.write(fruits.length);
// count의 결과가 4가 됨
```

참고 자료: [MDN Array](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array)

## **반복문**

순서대로 실행되는 프로그램의 실행 순서 흐름을 제어하는 제어문이라고 할 수 있음. (조건문도 마찬가지)

관습적으로 `i` 에 몇번 반복되는지 count를 선언해 둘 수 있다.

```jsx
<script>
  document.write('<li>1</li>');
  var i = 0;
  while(i < 3){
  document.write('<li>2</li>');
  document.write('<li>3</li>');
  i = i + 1;
  }
  document.write('<li>4</li>');
</script>
//결과
// 1
// 2
// 3
// 2
// 3
// 2
// 3
// 4
```

  `while(boolean)` 의 boolean 쪽에 반복될 조건을 선언해준다. 위 코드의 경우 **3 미만** 까지 2, 3이 출력되도록 작성되어있다. 그래서 3번 반복되어 출력되게 된다.

## 배열과 반복문

반복문에 배열을 넣어본다

`i` 값은 인덱스와 일치한다.

```jsx
<script>
    var fruits = ['바나나', '사과', '딸기', '수박'];
  </script>
  <h2>
    Fruits
  </h2>
  <ul>
    <script>
      var i = 0;
      while (i < 4) {
        document.write('<li>'+fruits[i]+'</li>');
        i = i + 1
      }
    </script>
  </ul>
```

리팩토링

데이터가 바뀌었다고 로직을 바꾸는것은 적절하지 않다. 

```html
<script>
    var fruits = ['바나나', '사과', '딸기', '수박', '자몽'];
  </script>
  <h2>
    Fruits
  </h2>
  <ul>
    <script>
      var i = 0;
      while (i < fruits.length) {
        document.write('<li>'+fruits[i]+'</li>');
        i = i + 1
      }
    </script>
  </ul>
```

위 코드처럼 `while`의 조건에 데이터의 길이 (갯수)를 확인할 수 잇는 `fruits.length`와 같이 작성하면 코드에는 신경쓸 필요 없이 데이터가 증가되는 것을 반영한다.

**배열과 반복문의 활용**

검색 결과를 알려주지 말고 검색 하는 방법을 알려줘라. 검색은 소프트웨어를 만드는 일의 일부임

```jsx
document.querySelector('a')
```

`querySelector` 라는 메소드(?) 함수(?) 명령(?)은 하나만 가져오는 특성을 가지고 있다. 우리가 하려는 모든 `a` 태그를 가져오려는 목적에 맞지 않다.

[javascript get element by css selector multiple](https://developer.mozilla.org/ko/docs/Web/API/Document/querySelectorAll) 검색

```jsx
document.querySelectorAll('a')
NodeList(4) [a, a, a, a]
```

`querySelectorAll` 수행하면 대괄호 안에 있는 배열이 생긴다.

```jsx
var alist = document.querySelectorAll('a');
console.log(alist[0]);
// 결과:
// <a href="index.html">WEB</a>
```

`alist` 라는 변수를 지정해준 후 콘솔 로그로 `alist[0]` 를 통해 0 번째에 있는 `a`를  출력해보면 가장 위에 있는 `a` 태그가 출력되는걸 확인할 수 있다.

```jsx
var alist = document.querySelectorAll('a');
console.log(alist.length);
// 결과:
// 4
```

마찬가지로 콘솔 로그에 `alist.length` 로 `alist` 의 개수를 확인할 수 있다.

```jsx
var alist = document.querySelectorAll('a');
var i = 0;
while (i < alist.length){
    console.log(alist[i]);
    i = i + 1;
}
// 결과:
// 모든 a 태그를 불러오고
// 4 (배열 갯수)
```

위 코드에 a 태그의 색상을 바꾸는 코드를 한줄 더 추가해준다

```jsx
var alist = document.querySelectorAll('a');
var i = 0;
while (i < alist.length){
    alist[i].style.color='powderblue';
    i = i + 1;
}
```

반복문을 사용해 다양한 일을 할 수 있다. 컴퓨터는 결과를 배열의 형태로 주는 속성이 있어서 배열, 반복문은 매우 중요한 개념이다.