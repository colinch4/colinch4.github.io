---
layout: post
title: "[javascript] 자바스크립트 클래스 기초"
description: " "
date: 2021-06-09
tags: [javascript]
comments: true
share: true
---

자바스크립트 클래스 기초
------------------------

### 클래스 소개

#### 클래스란?

-	함수가 특정 알고리즘을 포장하는 기술이라면 클래스는 이렇게 만들어진 수많은 변수와 함수 중 연관 있는 변수와 함수만을 선별해 포장하는 기술이다. 이렇게 클래스로 포장하는 이유는 객체 단위로 코드를 그룹화하고 코드를 재사용하기 위함이다.
-	프로그래밍 동네에서는 클래스 역할이 바로 시도군을 나누는 역할이다.

#### 자바스크립트에서 클래스란?

-	자바스크립트는 객체지향 프로그래밍 언어에서 기본적으로 제공하는 클래스라는 개념을 제공하지 않는다. 하지만 다행히 자바스크립트에서는 클래스처럼 사용할 수 있는 방법이 세 가지 지원한다.

-	리터럴 방식

```javascript
var 인스턴스 = {
  프로퍼티1 : 초깃값,
  프로퍼티2 : 초깃값,

  메서드1 : function(){    
  },
  메서드2 : function(){
  }
}
```

-	함수 방식

```javascript
function 클래스이름(){
  this.프러퍼티1 = 초깃값;
  this.프러퍼티2 = 초깃값;

  this.매서드1 = function(){
  }
  this.매서드2 = function(){
  }
}
```

-	프로토타입 방식

```javascript
function 클래스이름(){
  this.프러퍼티1 = 초깃값;
  this.프러퍼티2 = 초깃값;

  클래스이름.prototype.매서드1 = function(){
  }
  클래스이름.prototype.매서드2 = function(){
  }
}
```

### 클래스 관련 기본 개념과 용어정리

#### 인스턴스

-	함수를 사용하려면 함수 호출을 해줘야 하듯 클래스를 사용하려면 일반적으로 인스턴스를 생성해줘야 한다.
-	클래스는 설계도이고 인스턴스는 설계도대로 만들어진 결과물이 된다.
-	인스턴스는 주로 다음과 같이 new하는 키워드를 이용해서 만든다.

```javascript
var 인스턴스 = new TabPanel();
```

#### 객체란?

-	인스턴스와 객체는 동일한 의미를 가질 때도 있고 명확이 구분해서 사용할 때도 있으니 상황에 맞게 선택해서 사용하면 된다.

#### 프로퍼티

-	클래스 내부에 만드는(포장하는) 변수를 프로퍼티라고 부르며 멤버변수라고도 한다.

#### 메서드

-	클래스에 만드는 함수를 메서드라고 부르며 멤버함수라고도 부른다.

### 오브젝트 리터럴 방식으로 클래스 만들기

#### 사용법

##### 예제

```javascript
var user = {
    name:"ddandonge",
    age: 10,
    showInfo:function(){
        document.write("name = "+this.name+", age = "+this.age);
    }
}

//메서드 접근하기
user.showInfo();
```

##### 예제 - 함수 단위 코딩으로 만들어진 탭메뉴를 리터럴 방식 클래스를 만드시오.

-결과

![리터럴 방식 클래스 변환](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzWUNtcmhaVy1XWUk)

-	진행순서
-	클래스 생성하기

![클래스 생성하기](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzUXBSZnktMG1iV0k)

-	변수를 프로퍼티로 만들기

![변수를 프로퍼티로 만들기](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzYWswTnhZUGhKQUE)

-	함수를 메서드로 만들기

![함수를 메서드로 만들기](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEza0pmd3MtNnd0eFE)

-	객체 내부에서 프로퍼티와 메서드 사용하기

![객체 내부에서 프로퍼티와 메서드 사용하기](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzblJFYTIwVFNnMTg)

![this](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzVTR5Q0NQR3k0eTA)

-	첫 번째 탭 메뉴 인스턴스 생성하기

```javascript
var TabPanel = {

}
```

-	객체 외부에서 프로퍼티와 메서드 사용하기

```javascript
$(document)ready(function(){
  tabMenu1.init();
  tabMenu1.initEvent();
});
```

#### 특징

-	인스턴스를 여러 개 만들 수 없다.
-	주 용도는 여러 개 데이터 포장용
	-	코드 재사용 불가, 매개변수 값 전달 시 주로 사용.

```javascript

// 신규 사용자 정보값
var userlnfo = {
  userName : "김춘경",
  id : "ddandongne"
}
// 기본 사용자 정보값
var defaults = {
  age : 0,
  address :" 서울시 금천구",
  nickName : ""
}
// 함수 호출
showlnfo(userlnfo);
// 함수에서 데이터 사용

function showlnfo(userlnfo){
  // 기본 사용자 정보와 신규 사용자 정보를 합치기
  userlnfo = $.extend({} , defaults , userlnfo);
}
```

-	이 방법의 핵심은 jQuery에서 제공하는 extend()라는 메서드를 이용해 기본값이 담긴 defaults 오브젝트 리터럴과 사용자 정보값이 담긴 userInfo 리터럴을 통합해 사용한 부분이다. Extend() 기능을 사용하는 경우 특히 jQuery 플러그인 제작 시 옵션값 처리부분에서 많이 볼 수 있다.

#### 실무에서 오브젝트 리터럴 사용 예

```javascript
var $ch=$("#chl");
$ch.css("position", "absolute");
$ch.css("left", 100);
$ch.css("top", 100);
```

```javascript
var $ch=$("#chl");
$ch.css({
  "position" : "absolute",
  "left" : 100,
  "top" : 100
});

```
