---
layout: post
title: "[JavaScript] 객체"
description: " "
date: 2021-09-09
tags: [javascript]
comments: true
share: true
---


## 객체

## 객체 예고

Object. 중요하고도 어려운 것... 여러 특성 중 하나의 기능에 집중해 코끼리 더듬듯 익혀 나가는것이 좋다.

정리정돈의 수단. 함수가 많아지다보면 그와 관계된 변수들이 증가하고 그 둘이 늘어나다보면 결국 그 둘을 다시 정리정돈이 필요해진다. 객체는 이러한 역할이 가능하다.

함수만으로 처리하기 우아하지 않은 단계.

파일을 정리할 수 있는 폴더 라고 봐도 무방하다.

함수명에 있던 특정 요소를 객체로 만들어 코드를 개선해본다.

```jsx
BodySetBackgroundColor('white');
BodySetColor('#0ebeff');
LinksSetColor('blue');
// 객체로 만들기
Body.setBackgroundColor('white');
Body.setColor('#0ebeff');
Links.setColor('blue');
```

여지껏 우리가 써온것 아래 코드도 결국은 객체였다!

```jsx
document.querySelector('body').style.backgroundColor = color;
```

위 코드의 `document` 는 객체, `querySelector('bpdy')` 는 document라는 객체에 속해있는 함수다. 객체에 속한 함수는 메소드라고 부른다.

## 객체

배열: 정보의 양이 많아졌을 때 연관된 정보를 정리정돈 하기 위한 도구

배열의 특징: 순서에 따라 정보를 정리정돈 한다

객체: 순서 없이 데이터를 저장하는 도구 (체계적으로 이름이 있는 정리정돈)

### 객체 쓰기와 읽기

객체를 만들때 사용하는 기호 = 오브젝트 리터럴 `{}`

```jsx
var fruits = {
  "red": "apple",
  "yellow": "banana"
};
document.write("programmer : "+fruits.red+"<br>");
document.write("yellow : "+fruits.yellow+"<br>");
```

`fruits.yellow` 의 `.` 은 Object Access Operator 라고 부른다.

배열에 어떤 정보를 추가하고 싶다면

```jsx
fruits.green = "lime";
document.write("green : "+fruits.green+"<br>");
// 결과
// green : lime
fruits["purple color"] = "grape";
document.write("purple color : "+fruits["purple color"]+"<br>");
// 결과
// purple color : grape
```

### 객체와 반복문

생성된 객체에 어떤 데이터가 있는지 확인해야 하는 경우가 있음 → 배열에 반복문으로 가져옴

객체에서는 어떻게 가져오는지 [javascript object iterate](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/for...in) 키워드를 검색해서 알아보았다

```jsx
for(var key in fruits) {
  document.write(key+'<br>');
}
// 결과
// red
// yellow
// green
// purple color
```

fruits 에 있는 데이터의 수 만큼 `{}` 안의 코드가 실행 되는데, 그 때마다 키값이 하나하나 변수값으로 세팅된다.

```jsx
for(var key in fruits) {
  document.write(fruits[key]+'<br>');
}
// 결과
// apple
// banana
// lime
// grape
```

fruits 객체에 `[key]` 를 써주면 값을 가지고 온다.

```jsx
for(var key in fruits) {
  document.write(key+' : '+fruits[key]+'<br>');
}
// 결과
// red : apple
// yellow : banana
// green : lime
// purple color : grape
```

### 프로퍼티와 메소드

객체에는 배열 숫자 다양한걸 담을 수 있다. 심지어 함수까지도.

```jsx
fruits.showAll = function () {
  for (var key in this) {
    document.write(key + " : " + this[key] + "<br>");
  }
};
fruits.showAll();
// 결과
// red : apple
// yellow : banana
// green : lime
// purple color : grape
// showAll : function () { for (var key in this) { document.write(key + " : " + this[key] + "
// "); } }
```

객체에 변수의 값으로 함수를 지정할 수 있고, 객체에 소속된 함수를 만들수 있다. 이 객체에 소속된 함수를 메소드라 부르고, 객체에 소속된 변수를 프로퍼티라고 한다.

🤯

## 객체 활용

```jsx
function nightDayHandler(self) {
  var target = document.querySelector("body");
  if (self.value === "night") {
    Body.setBackgroundColor("black");
    Body.setColor("white");
    self.value = "day";

    Links.setColor("powderblue");
  } else {
    Body.setBackgroundColor("white");
    Body.setColor("#0ebeff");
    self.value = "night";

    Links.setColor("blue");
  }
}
```

위 함수에 앞부분의 `Body.` , `Links.` 이런 걸 객체라고 부르며 객체는 아래와같이 선언한다.

```jsx
var Links = {
  setColor: function (color) {
    var alist = document.querySelectorAll("a");
    var i = 0;
    while (i < alist.length) {
      alist[i].style.color = color;
      i = i + 1;
    }
  }
};
var Body = {
  setColor: function (color) {
    document.querySelector("body").style.color = color;
  },
  setBackgroundColor: function (color) {
    document.querySelector("body").style.backgroundColor = color;
  }
};
```

객체의 함수(메소드)들은 여러개 선언이 가능하며, 콤마 `,` 로 구분한다.

