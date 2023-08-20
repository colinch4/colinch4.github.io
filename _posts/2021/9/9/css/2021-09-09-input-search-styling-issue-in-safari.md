---
layout: post
title: "[css] input tpe=search일 경우 safari에서 스타일링 문제 해결"
description: " "
date: 2021-09-09
tags: [css]
comments: true
share: true
---

## input tpe="search"일 경우 safari에서 스타일링 문제 해결

`<input>` 태그에 값이 입력되면 삭제(cancel) 버튼이 자동으로 보여지기 위해 속성을 `type="search"` 로 선언했다.

 크롬과 파이어폭스는 기존 `<input>` 에 정의된 스타일이 잘 출력되지만 safari에서는 높이, 테두리 값이 달라지는 상황이 발견되었다.

MDN에 따르면,

> [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) elements of type `search` are text fields designed for the user to enter search queries into. These are functionally identical to [text](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/text) inputs, but may be styled differently by the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/user_agent).

User Agent에 따라 다르게 스타일링되도록 설계되어 있는것이 원인으로, 아래와 같은 코드로 `appearance` 를 변경해준다

```css
input[type="search"] {
    -webkit-appearance: textfield;
}

input[type="search"]::-webkit-search-decoration {
    -webkit-appearance: none;
}
```

위 코드로 User Agent의 기본적인 모양을 제거해줌으로써 CSS에 선언된 `inpu` 의 스타일을 적용할 수 있다.



📖 **참고 자료**

* [input type="search"](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/search)

