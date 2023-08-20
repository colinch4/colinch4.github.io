---
layout: post
title: "[javascript] ajax 1"
description: " "
date: 2021-06-18
tags: [javascript]
comments: true
share: true
---

## JS - 비동기처리

> - 자바스크립트는 싱글쓰레드이다?
>   - 브라우저가 싱글쓰레드이다. ( Tab 단위 )
> - 브라우저 콘솔에 `while(1) {}` 명령을 치면 다른 작업을 못한다.
>   - 브라우저 1개의 탭은 1명에 일꾼만 있어서 ( 싱글스레드 )





## :one: Ajax 요청 

> **A**synchronous **J**avascript **A**nd **X**ml
>
> 자바스크립트로 **비동기 요청**을 보낸다.
>
> 1 요청 => 1 새로고침
>
> 무한스크롤



**:cupid: 사용목적**

- 사용자 경험이 좋아진다. ( UI UX )





**:cupid: XML 이 자꾸 나오는 이유?**

json 등장 이전에는 xml 이 가장 널리 사용되어서 관습적으로 남아있다.





**:cupid: Ajax 요청을 보내기 위해서는 무엇을 써야 하나?**

- XHR
  - Xml Http Request



## :two: Axios 사용

> Promise based HTTP client for the broswer and node.js
>
> axios는 node.js 와 브라우저를 위한 http통신 javascript 라이브러리이다.
>
> 대부분의 브라우저를 지원한다.
>
> [참고블로그]([https://velog.io/@sss5793/axios-%EC%82%AC%EC%9A%A9%ED%95%B4%EB%B3%B4%EA%B8%B0-uuk5elxk88](https://velog.io/@sss5793/axios-사용해보기-uuk5elxk88))



**:cupid: 특징**

- 불확실성
  - 언제 끝날지?
  - 성공 / 실패
- 브라우저에선 `XMLHttpRequests` 을 node.js 에선 `http` 요청 생성
- `Promise API 지원`
- 요청과 응답을 중단
- JSON 데이터 자동 변환
- 요청 취소
- XSRF 로부터 보호하기위한 클라이언트 측 지원



**:cupid: 설치**

```shell
## npm
$ npm install axios

## bower
$ bower install axios

## yarn
$ yarn add axios

## CDN
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```



**:cupid: Promise**

- `.then()`
  - 성공했을 때, 어떤 일을 한다.

- `.catch`
  - 실패했을 때, 어떤일을 한다.



**:cupid: 코드**

```html
<script>
    // promise => 성공 or 실패
    // 성공했을 때, 어떤 일을 한다 .then()
    // 실패했을 때, 어떤 일을 한다 .catch()
    console.log(1)
    axios.get('https:koreanjson.com/posts/1')
        .then(function (res) { return res.data })
        .then(function (data) { return data.content })
        .then(function (content) { console.log(content) })
    console.log(2)
</script>

출력
<!--
1
2
content
-->
```



**:cupid: JS 작성이 어려운점**

- python
  - django
  - algo



- JS
  - **백지코딩이라서 어렵다.**
    - 바닐라JS, ES6
  - `Front-End Framework` 필요성이 절실해짐..
    - `vue.js , react.js , acgular.js`







## :three: 프로젝트에 적용하기

- python -m venv venv
- source venv/Scripts/activate
- python -m pip install --upgrade pip
- pip install django==2.1.15
- touch .gitignore
  - .git 폴더가 있는 프로젝트 최상단에 파일생성할 것
  - gitignore.io => venv django python
  - venv/
- pip install art