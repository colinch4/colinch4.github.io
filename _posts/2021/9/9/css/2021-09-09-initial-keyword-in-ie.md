---
layout: post
title: "[css] IE에서 initial 대응하기"
description: " "
date: 2021-09-09
tags: [css]
comments: true
share: true
---

# IE에서 initial 대응하기

IE 크로스브라우징시 레이아웃이 깨지는 현상의 많은 경우가 CSS의 `initial` 값을 사용했을 때 발생했다. `initial`은 부모요소가 주는 모든 상속값을 건너뛰어 CSS 초기값을 되돌리는데 사용할 수 있다.

하지만! Internet Explorer은 이 값을 지원하지 않는다.

이를 해결하기 위해 `initial`대신 속성의 초기값이나, 초기화 혹은 없애는 값을 사용하는것을 권장하며 자주 사용하는 속성의 초기값은 아래와 같다.

* `position: static`
* `overflow: visible`
* `line-height: normal`
* `color: transparent`
* `border: none` 혹은 `0`
* `width, height 등 수치값` 은 `auto`

 초기 값이 없는 경우, 가장 가까운 부모로부터 상속받을 수 있도록  `inherit` 를 사용할 수 있다. 



