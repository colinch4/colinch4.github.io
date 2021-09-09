---
layout: post
title: "[css] Outline 둥글게 만들기"
description: " "
date: 2021-09-09
tags: [css]
comments: true
share: true
---

# Outline 둥글게 만들기

`<div>` 에 CSS로 `border-radous` 를 적용하면, 엘리먼트의 사방 모서리가 곡률을 갖고 둥글게 표현된다. 이 상태의 엘리먼트에 `outline` 을 주면 요소의 곡률을 잊고 직각 사각형으로 보여진다.

`input` 이나 `button` 을 둥글게 디자인했다면 이런 Outline이 `input` 형태에 비교해 더욱 직각으로 보이게 된다. 

이런 경우 `outline`을 보이지 않도록 처리하고, `box-shadow` 를 사용하는 방법으로 대신 사용할 수 있다.

```css
input:focus {
  outline: none;
  box-shadow: 0 0 0 3px blue;
}
```

위와 같이 처리하는 경우 엘리먼트의 테두리 곡률에 따라 자연스럽게 바깥으로 focus 효과를 줄 수 있다.

## Borders vs. outlines

Border와 Outline은 비슷해보이지만 다음과 같은 차이점을 갖는다:

* Outline은 요소의 컨텐트 외부에 그려지기 때문에 공간을 차지하지 않는다.
* Spec에 따르면, Outline은 대개 직사각형이지만 꼭 직사각형일 필요는 없다.

## 참고

[Outline radius? - Stack overflow](https://stackoverflow.com/questions/5394116/outline-radius)

[MDN outline](https://developer.mozilla.org/ko/docs/Web/CSS/outline)

