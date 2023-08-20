---
layout: post
title: "[css] CSS 레이아웃"
description: " "
date: 2021-09-09
tags: [css]
comments: true
share: true
---

## CSS 레이아웃

CSS 레이아웃 초창기, 우리는 다음과 같이 Box Model을 공부했다

* Block 형태의 요소
* Inline 형태의 요소
* `display` 속성을 사용해 Block을 Inline으로 바꾸거나 반대의 경우도 마찬가지로 변경할 수 있다

 이 경우, CSS에 바로 뛰어들어 레이아웃을 구성하고 우리가 원하는 형태로 레이아웃을 구성할 수 있도는 이상한 형태의 핵(hack)을 학습하게 된다. 

 Box Model은 레이아웃을 구성하기 위해 CSS가 가지고 있는 모든것 이었다. 크기를 지정하고, 조절하고 원하는 위치에 밀어넣는 방법의 핵심이었다. 표준 박스 모델을 이해하고 신중하게 계산한 퍼센트 단위로 설정한 width가 아니라면, 거의 100%의 확률로 나쁜 일이 발생하게 된다.

 최근 몇년 사이, Flexbox와 Grid라는 도구가 등장해 CSS를 위해 설계된 레이아웃 시스템을 제공한다. 이것은 박스 모델에서 레이아웃을 위해 사용하던 핵 모음을 리팩토링하여 응집력 있는 시스템으로 변경한 것이며, CSS 레이아웃을 설명할 수 있는 실질적인 개념이다. `display` 속성에 값을 변경하는것 만으로 이 새로운 2가지를 충분히 활용할 수 있다.

다양한 writing mode를 지원하기 위해`start`와 `end`개념이 논의 되었다.

`block`과 `inline`은 스크린에 물리적인 `top` , `right`,` bottom`,` left`에 위치한다. 이러한 내용을 이해한다면 Flexbox와 Grid에서의 align과 Grid에서의 라인 기반 포지셔닝에 대해 더 쉽게 이해할 수 있다.

박스 모델은 `content-box`와 관련있는 `width`와 `hieght`(혹은 `inline-size`와 `block-size`) 그리고 `box-sizing` 속성의 `border-box`를 통해 그 관계를 수정하는 방식이었다고 요약 할 수 있다.

크기를 지정하지 않고 레이아웃을 구성하는환경에서, 박스 모델은 박스의 사이즈를 위한 일부가 되며, Flexbox와 Grid와 함께 동작할 때 더욱 유용해진다.



📖 **참고자료**

* [CSS 레이아웃을 배웁시다](https://ko.learnlayout.com/)
* [Position : Flexbox](http://www.beautifulcss.com/archives/2812)
* [CSS Grid Layout Guidebook](https://uid.gitbook.io/css-grid/)
* [Learn CSS Grid for free](https://scrimba.com/g/gR8PTE)