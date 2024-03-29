---
layout: post
title: "[js] JS와 브라우저"
description: " "
date: 2021-05-14
tags: [javascript]
comments: true
share: true
---

## JS와 브라우저
## 브라우저의 기본 구조
1. UI
2. 브라우저 엔진
3. 렌더링 엔진
4. 통신
5. UI 백엔드
6. 자바스크립트 해석기
7. 자료 저장소

### 브라우저 엔진

### 자바스크립트 엔진

### 렌더링 엔진

HTML, CSS를 파싱하여 각각 DOM, CSSOM을 생성하여 화면에 표시할 수 있도록 렌더 트리를 형성해주는 역할.

크롬과 사파리에서는 Webkit 엔진을 사용하고, 파이어폭스의 경우 Gecko 엔진을 사용한다.

1. HTML 파싱 후 DOM 트리 구축 / Style(CSS) 파싱 후 CSSOM 트리 구축
2. 1번에서 HTML 부분과 CSS 부분을 합치는 과정
3. 렌더 트리 형성 (render tree)
4. 렌더 트리 배치 (layout or reflow)
5. 렌더 트리 paint

## 컴파일

1.  파싱

파싱은 크게  `lexical analysis`,  `syntax analysis` 두개의 과정으로 나뉘게 된다. 이 두 과정을 통해서 고차언어를 `파스 트리(parse tree or syntax tree)`로 변환하는 것을 파싱이라고 한다.

- lexical analysis : `tokenizer`를 통해 고차 언어를 토큰으로 분해하는 과정
- syntax analysis: 토큰을 바탕으로 해당 언어의 규칙에 맞게 해석하여 트리를 만드는 과정

2. 기계 코드로 변환

파스 트리가 생성된 이후 이를 기계 코드(여기서는 바이트코드)로 변환된다.


## 브라우저는 어떻게 렌더링되는가
1. 특정 라우트에 필요한 리소스를 서버로부터 받아온다.
2. 렌더링 엔진은 HTML, CSS를 토대로 DOM과 CSSOM을 생성. 렌더 트리를 형성한다.
3. 자바스크립트 엔진은 자바스크립트를 compilation하여 (파싱하여 AST 구성 후 바이트 코드 생성과 실행 등) 2번에서 실행된 렌더 트리를 수정 및 병합하게 된다.
4. 렌더 트리를 바탕으로 화면을 그린다.


## HTML 파싱과 DOM 생성
1. HTML 문서를 응답으로 받아온다.

2. 이를 파싱하여 DOM 객체를 만든다.
    1. 각 태그를 tokenize하여 노드를 만든다.
    2. 노드를 트리 구조로 관계를 만들어준다.

## CSS 파싱과 CSSOM 생성
HTML 문서를 파싱하는 도중에 link 태그나 style 태그를 통해 CSS 로드 관련 로직을 만나면 DOM 생성을 멈추고 CSS 파일을 요청, 로드 후 파싱한다.

CSS를 파싱하여 CSSOM으로 만드는 과정도 HTML과 비슷하게 진행된다.

1. 요청을 통해 CSS 파일을 받아온다.
2. 이를 파싱하여 CSSOM 객체를 만든다.
    1. 토크나이징하여 노드를 만든다.
    2. 노드를 트리 구조로 만든다.

## 렌더트리 형성 / 배치 / 페인팅

위의 HTML과 CSS 파싱으로 생성된 DOM과 CSSOM을 결합(attachment)하여 렌더 트리를 만들게 된다.

해당 렌더트리가 형성되면 이 렌더 트리를 바탕으로 브라우저 위에 각 요소를 레이아웃하고, 페인팅하게 된다.

만약 아래의 경우에 해당하는 경우 렌더링 과정이 다시 진행된다.

- JS를 통한 DOM 조작으로 노드가 추가되거나 삭제.
- 뷰포트 변경
- HTML 요소의 레이아웃을 변경하는 CSS 스타일 변경(position, display, width, height 등)

위 과정이 실행되는 경우에는 렌더링이 다시 발생하게 되는데,  렌더트리를 배치(layout)하고, 페인팅하는 과정은 비용이 많이 드는 작업이기 때문에, 불필요한 리렌더링이 발생하지 않도록 조심해야한다.

> 참고: 렌더트리와 DOM 트리는 항상 일치하는 것은 아니다. DOM 트리 요소 중 비시각적인 태그, 예를들어 <head>, <meta>와 같은 요소나, display: none 속성을 가진 요소들은 렌더 트리에 반영되지 않는다.


## 자바스크립트 파싱, 실행

html을 실행하는 도중에 자바스크립트 관련 코드 (<script> 태그와 같은) 를 만나게 되면, DOM 생성이 일시 중지되고, 자바스크립트 관련 코드를 받아오게 된다.

해당 자바스크립트 파일을 받아오게 되면, 이 파일은 렌더링 엔진이 아닌 자바스크립트 엔진을 통해 해석되고, 렌더링 엔진은 작업으로 돌아가게 된다.

1. 자바스크립트 코드 파싱
    1. lexical analysis. 소스코드를 토크나이징하여 토큰으로 분해한다.
    2. syntatic analysis. 위 과정으로부터 나온 토큰을 언어의 규칙을 바탕으로 해석하여 AST(Absctract Syntax Tree)를 생성
2. AST를 바탕으로 바이트코드로 변환
3. 인터프리터에 의해 실행

### 리플로우, 리페인트

자바스크립트에서 DOM API를 통해서 DOM을 조작하는 경우에, 렌더 트리가 변경되어, 배치(layout), paint 과정이 다시 발생할 수 있다.

만약에 layout을 바꾸는 position, width, height, 노드의 추가 및 삭제 등이 일어나는 경우에는 reflow가 발생한다.

만약 layout을 변경하지 않는 경우라면 reflow는 일어나지 않고 repaint만 발생한다.


## 왜 <script> 태그는 하단에 위치할까?
스크립트 태그를 하단에 위치시키는 이유는 두가지로 요약할 수 있다.

1. 페이지 로딩 속도 개선

위에서 설명한 렌더링 엔진과 자바스크립트 엔진은 병렬처리를 하지 않는다. 위에서 설명한 것과 같이, HTML 문서를 파싱하는 도중에 CSS, JS와 관련된 부분을 만나면 파싱을 멈추고, CSS, JS 관련 부분을 처리(파싱, 실행)하게된다.

이로 인해서, HTML 파싱이 지연되면 그만큼 페이지의 로딩이 느려진다.  실제 렌더링 엔진은 렌더 트리가 모두 완성된 후 요소를 배치하고 페인트하는 것이 아니라, 점진적으로 이를 그려나가는데,  만약 블로킹이 되는 경우에는 이마저도 진행되지 않는다.

2. DOM API 사용

만약 <script> 태그 내에서 DOM API를 통해서 DOM을 직접 조작하려고하는데, 아직 HTML 파싱이 되지 않은 상황이라 DOM에 해당 요소(태그)가 존재하지 않는 경우에는 에러가 날 수 있다.  따라서 스크립트 태그가 CSS와 같이 <head> 태그 내부에 존재한다면, 이로 인해 에러가 발생할  수도 있다.



#javascript