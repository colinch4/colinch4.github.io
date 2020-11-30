---
layout: post
title: "Vue 시작하기 1"
description: " "
date: 2020-11-16
tags: [vue]
comments: true
share: true
---

### Vue 강의 들으면서 내용 정리하기 !
- [실습내용](https://github.com/jina95/vueStudy_learnVueJs)
<hr/>
object.defineproperty(대상객체, 객체의 속성, {

// 정의할 내용이 들어간다.

get // 속성에 접근했을때의 동작을 정의<br/>
<br/>
set // 속성에 값을 할당했을때의 동작을 정의(new value 라는 새로 할당 된 값이 인자로 필요.)
})

객체의 동작을 재정의 하는 api ( 동작을 우리 맘대로 바꿀 수 있다는 뜻)

<b>할당할때마다 값이 reactivity 된다. 뷰의 핵심 !! <br/>
데이터의 변화를 라이브러리에서 감지해서 알아서 화면을 자동으로 그려주는것이 리액티비티</b>

<hr/>

[즉시실행함수 MDN](https://developer.mozilla.org/ko/docs/Glossary/IIFE)
- 역할 : 기본적으로 어플리케이션 로직에 노출되지 않게 또다른 스코프,유효범위에 넣어주는것. 일반적인 오픈소스라이브러리에서 변수를 이런식으로 관리.

함수의 이름이 대문자다 >> 생성자 함수를 의미
함수를 이용해서 어떤 정보를 담은 객체를 생성하는게 객체생성패턴

[생성자 함수 MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Obsolete_Pages/Core_JavaScript_1.5_Guide/Creating_New_Objects/Using_a_Constructor_Function) / 
[prototype MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

<hr/>

vue 인스턴스에서는 <br/>
key : value 형식으로 존재 <br/>
생성자 안에 인자는 객체

뷰 컴포넌트: 화면의 영역을 영역별로 구분해서 코드로 관리하는 것, **재사용성**이 올라감

인스턴스를 생성하면 개발자도구에서 root 컴포넌트로 인식 > 이때 root 는 상위컴포넌트, 부모컴포넌트라고 부른다.

vue.component('컴포넌트 이름', 컴포넌트 내용) > **전역컴포넌트** / 실제로는 많이 사용되지 않는다 <br/>
new Vue 인스턴스 안에 components 안에 객체로 넣어준다 // ('컴포넌트 이름', 컴포넌트 내용) > **지역 컴포넌트**(보통 컴포넌트를 여러개를 등록하기 때문에 s가 붙는다.)

차이점 : 지역컴포넌트는 특정 컴포넌트 하단에 어떤 컴포넌트가 등록됬는지 컴포넌츠 속성으로 바로 알수가 있다. 전역을 사용할 시에는 라이브러리나, 플러그인으로 사용하게 된다. 그렇기 때문에 일반적으로는 지역으로 사용을 한다. 또한 새로운 인스턴스에 컴포넌트를 추가하고 싶다면, 지역은 생성할때마다 등록해줘야하지만, 전역은 그럴 필요가 없다.

상위컴포넌트와 하위컴포넌트 : 위에서는 아래로 내려주고(프롭스 속성), 밑에서는 위로 이벤트를 올려줌(이벤트 발생)

**프롭스** 사용법 : 
- <하위컴포넌트태그 v-bind:프롭스 속성 이름 = "상위컴포넌트의 데이터 이름">

- 프롭스 속성 이름은 하위컴포넌트에 프롭스를 정의해주고 배열을 연다(props:['ex'])

- 이때 상위 컴포넌트 데이터에서 내용을 바꿔준다면 하위컴포넌트에도 반영이된다.

**이벤트** 사용법 : 
- 만약 하위컴포넌트를 버튼이라고 정의했을때, 템플릿에서 <button v-on:click="이벤트이름"> 이벤트를 실행해주고
  
- 하위 컴포넌트 methods 에 이벤트이름을 선언해준다. 그 이벤트이름에서 this.$emit('이벤트') 를 보낸다

- vue events 탭에서 이벤트 이력을 확인할 수 있다.

- this.$emit 은 vue.js에서 제공해주는 api, 기능이다.

- 위에서 받을 수 있게 컴포넌트 태그에 입력해 줘야 한다. 

- <컴포넌트태그 v-on:하위컴포넌트에서 발생한 이벤트 이름 = "상위컴포넌트의 메서드 이름">

