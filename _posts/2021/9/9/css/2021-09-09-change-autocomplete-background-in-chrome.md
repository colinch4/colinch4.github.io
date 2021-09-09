---
layout: post
title: "[css] 크롬 자동완성의 배경색상 변경하기"
description: " "
date: 2021-09-09
tags: [css]
comments: true
share: true
---

# 크롬 자동완성의 배경색상 변경하기

크롬 브라우저 및 webkit 기반 브라우저에서 자동완성기능 사용시 `input` 요소에 특정 배경색상이 적용된다.  가상 선택자 `:-webkit-autofill` 을 이용해 다음 CSS로 색상 수정 가능하다. 다만  `background-color` 속성이 아닌 `box-shadow` 속성을 사용해 배경색상이 변경되어 보이도록 하는 일종의 Hack이다.

```css
input:-webkit-autofill {
   -webkit-box-shadow: 0 0 0 1000px #fff inset;
}
```

`autofill` 속성을 선택하지 않고 `input`요소에 바로 `box-shadow` 속성을 지정해주더라도 동일하게 보여진다. 하지만 자동완성 기능이 적용된 상황 외에도 `box-shadow` 색상이 지정된다는 점을 고려해보면 특정 상태의 선택자를 사용하는것이 더 올바른 방법이라 생각한다.

만약 디자인에서 input요소에 마우스가 진입하거나, 포커스되었을 때 별도의 색상이 적용되는 디자인이라면 아래와같이 정의한다.

```css
input:-webkit-autofill:hover,
input:-webkit-autofill:focus,
input:-webkit-autofill:active {
   -webkit-box-shadow: 0 0 0 1000px #eee inset;
}
```



📖 더 읽으면 좋은 자료:

* [The ultimate list of hacks for Chrome’s forced yellow background on autocompleted inputs](http://webagility.com/posts/the-ultimate-list-of-hacks-for-chromes-forced-yellow-background-on-autocompleted-inputs)