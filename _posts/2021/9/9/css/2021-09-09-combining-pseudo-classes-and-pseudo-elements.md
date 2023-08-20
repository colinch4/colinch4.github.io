---
layout: post
title: "[css] 가상 클래스와 가상 요소 클래스 조합하여 사용하기"
description: " "
date: 2021-09-09
tags: [css]
comments: true
share: true
---

## 가상 클래스와 가상 요소 클래스 조합하여 사용하기

## 문제 상황

- 기존에 잘 보이던 팝업 메뉴의 흰색 화살표가 회색 화살표로 변경됨 (`::before`, `::after` 가상 요소 CSS 로 스타일링 된 화살표)
- 팝업 메뉴 리스트에 의문의 검은 사각형이 생기는 문제

## 시도한 것 들

1. `::before` 에 들어간 클래스 때문에 검은 사각형이 발생하는 것 같아 해당 요소를 `clip` 처리 하거나 `display: none;` 처리함. 사각형은 사라지지만 화살표가 회색으로 보이는 문제는 해결되지 않았다.
2. 결과물 스타일에서 관련 구문 긁어 보니, CSS에는 `.popup::before:lang(en){border-color: #fff trans)` 와 같이 스타일이 선언되어 있지만 요소에 제대로 선언되지 않고 있었다. 😨
3. `lang(en)` 과 `::before` 선택자 순서를 바꿔 보니 제대로 적용되는 것을 확인했다.

## 해결 방안
즉, 가상 클래스 (`:lang(en)`) 과 가상 요소 클래스 (`::before`) 를 결합해 사용한 선택자에 문제가 발생해 CSS가 정상적으로 나오지 않는 상황이었다.

 가상 클래스는 어떠한 요소의 특정한 상태를 선택하기 위한 클래스이다. 마우스 오버 `:hover`, 해당하지 않는 요소 `:not()`, 첫 번째 요소 `:first-child` , 특정 언어를 선택하는 `:lang()` 등이 있다.

 반면 가상 요소 클래스는 HTML이 포함하지 않는 요소를 만들거나, 존재하는 요소의 일부분만 선택하는 키워드이다. 주로 `::before`, `::after` 를 많이 사용한다.

  W3C 문서 스펙에 따르면, 가상 클래스는 선택자의 모든 위치에서 사용할 수 있지만, 가상 요소 클래스는 선택자의 마지막에 위치해야 한다고 정의 된 내용을 확인했다.

> Pseudo-classes are allowed anywhere in selectors while pseudo-elements may only be appended after the last simple selector of the selector.

```scss
// 스타일 적용되지 않음 X
.popup::before:lang(en) {
  ...
}

// 스타일 적용됨 O
.popup:lang(en)::before {
  ...
}
```

이렇게 가상 클래스와 가상 요소 클래스 작성 순서가 문제가 되는 이유는 브라우저가 선택자를 해석하는 방식에서 기인한 것 같다. 

브라우저는 선택자를 오른쪽에서 왼쪽으로 이동하며 해석 하게 되는데, 가상 요소 선택자가 가상 선택자보다 앞에 있다면 브라우저는 마크업되지 않은(DOM에 존재하지 않는) 요소에 대해서는 선택할 수 있는 방법이 없다. 

1차로 돔을 만들어 주고, 그 후에 그 돔이 영어 문서에 있는건지, 한국어 문서에 있는건지 판단할 수 있기 때문일 것이다.

## 정리

**조금 더 근본적인 원인을 정리 해보자**: 소스에 Webpack을 적용하기 이전에는 엉망으로 작성된 CSS도 정리되지 않은 상태로 얼기설기 문제가 없는 듯 보여지고 있었다. (`:lang(en)` 으로 재선언한 스타일만 깨지고 있는 상황. 영문이라 눈치채지 못했다). 결국 엉망으로 작성된 CSS가 원인이 되어, Webpack을 적용하며 설치한 postcss 패키지가 중복된 스타일을 정리하는 과정에서 해당하는 스타일이 CSS 규칙에 어긋난 선택자 하위로 선언 되며 불거진 이슈였다.

**배운것:** 컴파일 된 CSS에는 있지만, 브라우저에서 적용되지 않을때! 마냥 신기해 할 게 아니라 선택자가 잘못 작성된 건 아닐지 의심하자.

## 참고 자료

- [Pseudo-elements and pseudo-classes](https://www.w3.org/TR/CSS2/selector.html#pseudo-elements)
- [MDN - 의사 요소(가상 요소)](https://developer.mozilla.org/ko/docs/Web/CSS/Pseudo-elements)
- [MDN - 의사 클래스(가상 클래스)](https://developer.mozilla.org/ko/docs/Web/CSS/Pseudo-classes)
- [MDN - Combining pseudo-classes and pseudo-elements](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Pseudo-classes_and_pseudo-elements#Combining_pseudo-classes_and_pseudo-elements)
