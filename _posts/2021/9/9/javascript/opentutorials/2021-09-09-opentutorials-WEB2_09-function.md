---
layout: post
title: "[JavaScript] 함수"
description: " "
date: 2021-09-09
tags: [javascript]
comments: true
share: true
---

## 함수

## 함수 예고

함수의 이미지는 수납상자! 코드가 많아지만 그걸 잘 정리정돈 하기 위한 도구이다.

```jsx
function functionName(..){..}
```

함수를 정의하고, 실행 시키고 싶을 땐 해당하는 엘리먼트에 함수를 붙여넣는다.

함수로 정의된 원본 코드에서 로직을 바꾸는걸로 문서 내의 모든 결과를 바꿀 수 있고, 코드량이 줄어드는것도 가능하다. 또한 함수 이름을 통해 로직이 동일할 것과 로직의 정체를 확신하고 이해할 수 있게 된다.

## 함수

Function

어떤 코드가 연속적이지 않게 반복될 경우 반복문을 사용하기 불가능하거나 어려워진다. 이럴 때 함수를 활용할 수 있다. 

```jsx
// Before
document.write("<li>1</li>");
document.write("<li>2-1</li>");
document.write("<li>2-2</li>");
document.write("<li>3</li>");
document.write("<li>2-1</li>");
document.write("<li>2-2</li>");

// After - 함수 사용
function two() {
  document.write("<li>2-1</li>");
  document.write("<li>2-2</li>");
}
document.write("<li>1</li>");
two();
document.write("<li>3</li>");
two();
```

### 매개변수(parameter)와 인자(argument)

자판기에 물건을 선택 (입력)하면 물건이 나온다(출력). 수학적으로는 함수를 입력과 출력이라고 볼 수 있다. 입력은 매개변수와 인자, 출력은 리턴과 관련된다.

```jsx
function onePlusOne() {
  document.write(1+1+'<br>');
}
onePlusOne(); //2

// 매개변수와 인자를 사용해 인자에 따라 결과가 바뀌는 코드
function sum(left, right) { //(left, right) 는 매개변수(parameter)
  document.write(left+right+'<br>');
}
sum(2, 3); // 5
sum(3, 4); // 7
```

단지 `sum` 의 괄호 안에 있는 값을 수정하는 것 만으로 함수는 쳐다보지도 않고 원하는 값을 만들어낼 수 있다. 이 값을 인자 (argument) 라고 부른다.

인자의 값을 받아 함수 안으로 매개시키는 변수들을 매개변수(parameter)라고 한다.

### 리턴(return)

`1+1` 은 2에 대한 표현식이다. `1===1` 은 `true` 의 표현식이다. `sum(2, 5)` 가 `5` 가 되는 표현식을 만들고 싶다면 리턴을 이해하고 있어야한다.

```jsx
function sum2(left, right) {
  return left+right;
}
// sum2(2, 3); // 결과 5에 대한 표현식
document.write(sum2(2,3)+'<br>');
document.write('<div style="color:red">'+sum2(2,3)+'</div>');
document.write('<div style="font-size: 3rem">'+sum2(2,3)+'</div>');
```

`sum2` 라는 함수가 left, right 매개변수로 들어가는 값을 return으로 출력해 다양한 용도로 활용할 수 있게 된다.

## 함수의 활용

NightDay 리팩토링을 통해 함수 활용을 연습해본다.

```jsx
// 기존 스크립트를 함수로 선언
function nightDayHandler(params) {
  var target = document.querySelector('body');
  if (this.value === 'night') {
    target.style.backgroundColor = 'black';
    target.style.color = 'white';
    this.value = 'day';
    var alist = document.querySelectorAll('a');
    var i = 0;
    while (i < alist.length){
        alist[i].style.color='powderblue';
        i = i + 1;
    }
  } else {
    target.style.backgroundColor = 'white';
    target.style.color = '#0ebeff';q
    this.value = 'night';
    var alist = document.querySelectorAll('a');
    var i = 0;
    while (i < alist.length){
        alist[i].style.color='blue';
        i = i + 1;
    }
  }
}
// input에 적용
<input
  id="night_day"
  type="button"
  value="night"
  onclick="nightDayHandler();"
/>
```

위 코드를 실행하면 버튼을 눌렀을 때 바로 night 모드로 변하지 않고 한번 더 클릭해야 변하는 오류가 발생한다. 기존 스크립트가 `<input>`  태그 내부에있었기 때문에 `this` 는 `<input>` 태그를 가르키도록 약속 되어있었는데, 독립된 함수를 만들면서 더이상 인풋 엘리먼트가 아닌 *전역 객체(윈도우)* 를 가리키게 된다.

 문제 해결 방법은 아래와 같다.

```jsx
function nightDayHandler(self) {
  var target = document.querySelector('body');
  if (self.value === 'night') {
    target.style.backgroundColor = 'black';
    target.style.color = 'white';
    self.value = 'day';

    var alist = document.querySelectorAll('a');
    var i = 0;
    while (i < alist.length){
        alist[i].style.color='powderblue';
        i = i + 1;
    }
  } else {
    target.style.backgroundColor = 'white';
    target.style.color = '#0ebeff';
    self.value = 'night';
    var alist = document.querySelectorAll('a');
    var i = 0;
    while (i < alist.length){
        alist[i].style.color='blue';
        i = i + 1;
    }
  }
}
// input에 적용
<input
  id="night_day"
  type="button"
  value="night"
  onclick="nightDayHandler(this);"
/>
```

함수에 매개변수를 `self` 라고 정의하고 `this` 를 `self` 로 대치해준다. `<input>` 에는 인자로 `this` 를 넣어 **이 인풋에 스크립트가 적용 된도록** 한다. 인풋에 `onclick` 액션이 일어나면 `this` 가 함수의 `self` 로 매개 되어 정확하게 동작 할 수 있게 된다.

 이렇게 리팩토링을 통해

- 코드 수를 줄이고
- 함수 이름을 통한 기능을 유추할 수 있게 되었고
- 함수의 내용 수정을 통해 앞으로 반복될 여러 코드를 한번에 수정할 수 있게 되었다