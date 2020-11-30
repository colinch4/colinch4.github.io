---
layout: post
title: "Vue 시작하기 2"
description: " "
date: 2020-11-16
tags: [vue]
comments: true
share: true
---

## 20200511
### Vue 강의 들으면서 내용 정리하기 ! 2
- [실습내용](https://github.com/jina95/vueStudy_learnVueJs)

상위컴포넌트 하위컴포넌트가 아닌 같은컴포넌트 레벨간의 통신 방법
- 하위컴포넌트에서 상위로 올려준뒤(event), 다른 하위컴포넌트로 내려야한다.(props)
- 이때 상위컴포넌트인 root에 데이터와 메서드를 선언해 주고 연결해 줘야 한다.
- 이후 넘길 같은컴포넌트 레벨에 v-bind:프롭스 속성 이름 ="상위컴포넌트의 데이터 이름"
- 넘길 같은컴포넌트 레벨에 props: ['프롭스 속성 이름'] 을 정의해준다.

**router** 
- new VueRouter 인스턴스로 변수에 정의해주고 vue 인스턴스에 el,methods 처럼 router 속성에 변수를 연결해준다.
- root 안에 $route 를 확인할 수 있다. 
- new VueRouter 안에는 속성을 정의 할 수있는데, 첫번째로는 routes > 페이지의 라우팅정보(어떤 url 로 들어갔을때 어떤 페이지가 뿌려질지)가 배열로 들어간다. 각각 정보는 배열안 객체로 들어간다.
- 그 안에는 path > 페이지의 url 이름 / component > 해당 url 에서 표시될 컴포넌트 이 들어간다./ name 을 넣으면 더 의미있는 컴포넌트가 됨. (모든 형태는 key:value) 
- mode : 'history' 가 들어가면 #가 없어진다(url)
- url에 따라서 뿌려지는 영역을 태그 <router-view> 로 정의할 수 있다.(vue 인스턴스에 router 인스턴스를 연결해야지만 가능 )
- <router-link> : router에서 페이지 이동을 하기 위한 링크 태그, to="이동할 url"

**axios**
- Ajax 비동기적인 웹 어플리케이션 제작
- axios 는 vue 에서 권고하는 http 통신 라이브러리 (promise란 자바스크립트의 비동기처리패턴을 의미)

**http 통신구조**
- 요청이 가고 오는것이 http (요청과 응답/ 브라우저에서 서버단으로 요청(request)를 보내고 서버에서 브라우저로 응답(response)를 보낸다)

**개발자 도구 - 네트워크패널 보는 방법**
- NetWork 패널 > XHR 
- Header 에는 일반적인 정보를 담는, 특정 요청에 대한 정보나 응답에 대한 부가적인 정보를 담는 곳 
- get 으로 보냈기 때문에 response 에 항상 정보가 담겨져 있다. > preview 로 보면 더 편함
[프런트엔드 개발자가 알아야 하는 HTTP 프로토콜](https://joshua1988.github.io/web-development/http-part1/)

**템플릿 문법**
- 데이터 바인딩 : 콧수염 괄호
- 디렉티브 : v- ~로 붙는 속성들 (v-bind:id > id를 연결하겠다.)
- computed : 계산된 속성


