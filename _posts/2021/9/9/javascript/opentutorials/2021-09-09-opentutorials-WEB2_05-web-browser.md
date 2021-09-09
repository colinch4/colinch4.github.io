---
layout: post
title: "[JavaScript] 웹브라우저 제어"
description: " "
date: 2021-09-09
tags: [JavaScript]
comments: true
share: true
---

# 웹브라우저 제어

## 웹브라우저 제어

JavaScript를 이용해서 할 수 있는 일 중 하나인 웹브라우저 제어! 앞으로는 아래 내용을 배울것이다.

1. CSS의 주요 문법
2. JavaScript를 이용해 제어하고자 하는 태그를 선택하는 방법

## **CSS 기초**

간단한 질의응답에 대답하는것 부터 시작한다. 내가 생각하는 대답을 작성하고, 수업을 수강하며 깨닫는 정답을 밑에 추가 기입하겠다.

- CSS는 어떤 목적의 언어인가요?
  - HTML 문서를 디자인적, 시각적으로 꾸며주는 역할
- CSS를 웹페이지에 삽입하는 방법은 무엇인가요?
  - HTML의 `<head>` 영역에 `<link>` 태그를 사용해 삽입한다. 혹은 `<style>` 태그로 문서에 직접 작성할 수 있고, inline으로도 작성할 수 있으나 재사용성이 떨어진다
- style 속성은 무엇인가요?
  - HTML문서에 인라인으로 꾸밀 수 있도록 해주는 속성
  - A. HTML의 문법인 style 속성  안에는 CSS가 온다고 약속되어 있다.
- 선택자가 무엇인가요?
  - 특정 엘리먼트를 고를 수 있는 CSS의 문법
  - A. 여러 개의 태그를 선택해서 스타일링 하는 효율적인 방법. class = 그룹핑 한다. id = 식별한다. 절대 중복될 수 없다.

## **제어할 태그 선택하기**

`<body>` 태그에 style 속성을 동적인 상호작용에 의해 추가하려고 한다. JavaScript 문법으로 body 태그를 선택하도록 해보자 

[javascript select tag by css selector](https://developer.mozilla.org/ko/docs/Web/API/Document/querySelector) 로 검색!

`document.querySelector('body');` 로 바디 태그 선택

자바스크립트로 배경색상을 바꿔주고 싶다 → [javascript style background color](https://www.w3schools.com/jsref/prop_style_backgroundcolor.asp) 검색

[실습 예제](https://codepen.io/onlyeon/pen/GRpdaVN)를 작업하며, 처음 영상을 따라하며 만든 코드가 제대로 돌아가지 않고 `Uncaught SyntaxError: Unexpected end of input` 라는 오류 메시지가 나왔다. (JavaScript 패널에) 완성된 예제를 살펴보고 `"` 이 아닌 `'` 홑 따옴표로 작업했다. w3school 등의 예제에는 쌍따옴표로도 작성되어있는데, 내가 코드를 HTML안에 inline으로 작성하면서 `<input>` 태그를 강제로 닫아버려 발생한 문제였다.