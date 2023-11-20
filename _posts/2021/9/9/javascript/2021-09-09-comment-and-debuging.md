---
layout: post
title: "[JavaScript] 코멘트 / 디버깅"
description: " "
date: 2021-09-09
tags: [javascript]
comments: true
share: true
---

## 코멘트 / 디버깅

Debug = 문제 해결

JavaScript는 오류가 표시되기 때문에 HTML과 CSS와는 다르게 디버깅이 요긴하다.👏

## 기본

JavaScript는 문법의 대부분을 Java와 C, C++로부터 차용하고 있으며, Awk, Perl, Python의 영향도 받았다. 

JavaScript는 **대소문자를 구별**하며 **유니코드** 문자셋을 이용한다. 따라서 다음과 같은 코드도 유효하다.

```js
var 갑을 = "병정";
var Früh = "foobar"; // Früh: 독일어로 "이른"
```

하지만 대소문자를 구분하기 때문 `Früh`는 `früh`와 다르다.

JavaScript에서는 명령을 명령문(statement)이라고 부르며, 세미콜론(`;`)으로 구분한다.

명령문이 한 줄을 다 차지할 경우에는 세미콜론이 필요하지 않다. 그러나 한 줄에 두 개 이상의 명령문이 필요하다면 세미콜론으로 구분해야 한다. ECMAScript는 세미콜론을 자동으로 삽입해 명령문을 끝내는 규칙(ASI)도 가지고 있다. (더 많은 정보는 JavaScript의 [어휘 문법 에 대한 자세한 참고서](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Lexical_grammar)를 참고) 

하지만, 세미콜론이 필요하지 않은 경우라도 항상 세미콜론으로 끝마치는 편이 버그 예방 차원에서 더 좋은 습관이라고 여겨진다.

JavaScript의 스크립트 소스는 왼쪽에서 오른쪽으로 탐색하면서 토큰, 제어 문자, 줄바꿈 문자, 주석이나 공백으로 이루어진 입력 element의 시퀀스로 변환된다. 스페이스, 탭, 줄바꿈 문자는 공백으로 간주된다.

## 주석

```js
// 한 줄 주석

/* 이건 더 긴,
 * 여러 줄 주석입니다.
 */

/* 그러나, /* 중첩된 주석은 쓸 수 없습니다 */ SyntaxError */
```

## 참고

- [문법과 타입](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Values,_variables,_and_literals)