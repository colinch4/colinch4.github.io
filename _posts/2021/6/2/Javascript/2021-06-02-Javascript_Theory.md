---
layout: post
title: "[javascript] Javascript Theory"
description: " "
date: 2021-06-02
tags: [javascript]
comments: true
share: true
---

## Javascript 학습

구공 팩토리에서 공부한 내용으로 기본 Javascript 이론입니다.

## 목차

1. [이론](#-이론)
2. [DOM](#-DOM)
3. [이벤트](#-이벤트)
4. [DOM](#-DOM-라이프-사이클)

<br>
<br>
<br>

---

# 이론

## 배경

- 자바스크립트의 탄생 : 1995년 Brendam Eich
- 초기 자스 개발자들은 사실 이게 뭔지 모르고 썼다.
- 있어빌리티를 위해 ECMAScript 표준에 넣었다.
- 2000년도 중반이 되어서야 '진짜 언어'로 받아들여 지기 시작했지만
- 여전히 언어 같지 않은 모습을 갖추고 있었다.
- 2016년 기준 92%의 브라우저가 자스를 사용한다.

<br>

## 학습

- 처음에는 쉽지만 갈수록 급격히 어려워 지는 이유 → 이제 자스 하나만 배워도 만들 수 있는 것들이 많아졌다.
- 하지만 자스는 애초에 그러라고 만들어 진 언어가 아닙니다.

<br>

## 자스와 ES

- ES = ESMAScript = 자바스크립트 표준 버전
- ESI-4 : 1997년부터 2009년 11월까지
- 실질적인 변화는 2009년 12월에 공개된 ES5부터
- 2015년 6월 ES6(ES2015)의 등장
- 그 뒤로 계속 새로운 버전이 나오고 있음
- ES5 : 안정
- ES6 : 새로움(지원 안하는 브라우저도 있다.)

<br>

## 생태계

- 자스는 숙주 없이는 생존할 수 없다.
  - 돌아가는 환경 and 개발하는 환경

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/64c41026-7375-40fa-a11f-a012d486dad0/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/64c41026-7375-40fa-a11f-a012d486dad0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210302T095959Z&X-Amz-Expires=86400&X-Amz-Signature=813c5b79f34198a7b1810f198897dee231bcafe3c8f712d628050a68f8b47674&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

<br>

## 학습 목표 : 일단은 본연의 기능에 초점을 맞추자

- 원래 자스는 html과 css를 거드는 역할을 했다.
- DOM : 마크업 언어를 구조화 하고, 파싱하고, 이용한다.
- Core COM / XML DOM / HTML DOM
- API(web or XML page) = DOM + JS

<br>

<br>

# DOM

### 자바스크립트로

- 페이지 내의 모든 HTML 엘리먼트와 속성을 변경할 수 있다.
- 페이지 내의 모든 CSS 스타일을 변경할 수 있다.
- HTML 엘리먼트와 속성을 제거하고 추가할 수 있다.
- 페이지 내의 모든 HTML 이벤트와 상호작용할 수 있다.
- 페이지 내에서 동작하는 HTML 이벤트를 생성할 수 있다.

## HTML DOM

- html을 위한 표준 객체 모델이자, 프로그래밍 인터페이스
- 핵심 용어

  - 객체 = html 앨리먼트
  - 프로퍼티 = 변화시키려는 값(속성)
  - 메소드 = 목표 작업

  ```jsx
  <p id="demo"></p>

  <script>
  	document.geetElementById("demo").innerHTML = "Hello World!";
  </script>
  ```

- DOM 문서 객체 : document.XXX

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7f7def0c-86bf-4a4c-b841-002e8e42016d/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7f7def0c-86bf-4a4c-b841-002e8e42016d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210302T100119Z&X-Amz-Expires=86400&X-Amz-Signature=120306fce836d604fc87d41a9c670a37572e9e252181101a2b1cdb8854362578&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

**주의 ) 모든 스타일 속성은 CamelCase로 작성 ex) background-color ⇒ backgroundColor**

<br>
<br>

# 이벤트

- 이벤트 : 브라우저 내에서 일어나는 변화, 사용자 행위
- HTML 이벤트 속성
  - window : 문서 로드, 사이즈 변경, 문서 표시 에러 등
  - Form : 폼 변화, 포커스, 선택, 제출 등
  - Keyboard : 키를 누르거나, 눌렀거나 뗐거나
  - Mouse : 마우스 좌/우 클릭, 휠, 올려놓기 등
  - Drag : 끌어놓기 - 시작 / 종료 , 스크롤, 가져다 놓기
  - Clipboard : 복사, 잘라내기, 붙여넣기
  - Media : 비디오, 이미지, 오디오, 엘레멘트 관련 이벤트
  - Misc : 세부내용 열기 또는 닫기

### `getElementById()`

- 예제 : [https://codepen.io/kdh92417/pen/poNVWZr](https://codepen.io/kdh92417/pen/poNVWZr)

### 인풋창에서 입력한 값을 가지고 출력해보기

- 예제 : [https://codepen.io/kdh92417/pen/yLVjzqz?editors=1111](https://codepen.io/kdh92417/pen/yLVjzqz?editors=1111)

### EventListener()

- 이벤트를 듣고 있다가 특정 이벤트가 발생하면 무언가를 수행
- addEventListener() : 이벤트 핸들러와 엘리먼트를 연결
- removeEventListener() : 연결 해제

### addEventListener vs 인라인 이벤트

- 리스너 사용
  - 단일 엘리먼트에 무한대의 이벤트 등록 가능
  - 전역 이벤트를 일괄적으로 관리할 수 있음
  - 너무 많은 이벤트를 등록할 경우 퍼포먼스 영향을 줄 수 있음
- 인라인 이벤트

  - 단일 엘리먼트에 하나의 이벤트만 등록
  - 직관적이고 심플한 구조(눈에 보임)
  - 오직 하나를 위한 이벤트 → 중복, 유사 엘리먼트 처리에 어려움

- 예제 : [https://codepen.io/kdh92417/pen/xxRjpER](https://codepen.io/kdh92417/pen/xxRjpER)

<br>
<br>

# DOM 라이프 사이클

## DOM은 언제 해석되고, 언제 로드 되는가?

- DOMContentLoaded

  - 브라우저가 html을 모두 로드했고, DOM 트리가 완성이 되었지만 이미지와 같은 외부 리소스는 로드되지 않은 상태
  - 크롬과 오페라 브라우저의 자동완성 기능이 동작하는 시점

- load : html 뿐만 아니라, 이미지와 스타일도 모두 로드된 상태
- beforeunload(이페이지를 나갈려는 순간)/unload(페이지를 나갈때) 사용자가 페이지를 떠난 상태

**각각의 상태를 이벤트로 잡아서 처리할 수도 있음**

**컨텐츠 로드 라이프사이클을 이해하는 것은 매우 중요!!**

<br>

## 페이지가 다 로드 되었는지 확인하고 싶다면?

- document.readyState 호출
- loading = 문서 불러오는 중
- interactive = 문서 로드만 완료
- complete = 문서 로드 및 모든 리소스 로드 완료

<br>

## window

- onload : 스타일, 이미지 리소스들을 포함한 모든 페이지 로드가 완료된 상태
- onunload : 사용자가 페이지를 떠날 때(구글 아날리틱스)
- onbeforeunload : 페이지 떠나기 전(진짜 떠날꺼에요?)

- 예제 : [https://codepen.io/kdh92417/pen/JjbvMwO](https://codepen.io/kdh92417/pen/JjbvMwO)

<br>

## DOM 노드

### Again, DOM 트리

- 노드 : 트리 상에 위치한 하나의 엘리먼트
- body는 html의 자식이자 p의 부모 노드

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9b7bafce-7df2-4392-8e7b-f9677d3739ac/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9b7bafce-7df2-4392-8e7b-f9677d3739ac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210302T100327Z&X-Amz-Expires=86400&X-Amz-Signature=9ad77fc03fa3ca918b3596532609c5f82d1af07edccf7f91ca1d259593373ad4&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

<br>

### 브라우저 객체 모델(The Browser Object Model)

- 자바스크립트가 브라우저와 대화할 수 있도록 해주는 기능
- 객체 단위로 유용한 기능들이 묶여 있다.

  - window : 브라우저 윈도우의 모든 것(다른 모든 객체를 내포)
  - screen : 사용자 스크린에 대한 정보를 가지고 있음
  - location : 현재 페이지 주소 확인과 새로운 페이지 이동
  - history : 페이지 접근 기록 및 이동
  - navigator : 방문한 사용자의 브라우저 정보를담고 있다.
  - popup alert : alert(), confirm(), prompt()
  - cookies : 방문한 사용자의 쿠기 정보 (document.cooke)

- javascript로 태그 생성하기

- 예제 : [https://codepen.io/kdh92417/pen/LYbmdYK?editors=1010](https://codepen.io/kdh92417/pen/LYbmdYK?editors=1010)
