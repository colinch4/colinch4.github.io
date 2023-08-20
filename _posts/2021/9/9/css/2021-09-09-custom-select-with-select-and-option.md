---
layout: post
title: "[css] select와 option으로 커스텀 셀렉트 만들기"
description: " "
date: 2021-09-09
tags: [css]
comments: true
share: true
---

## select와 option으로 커스텀 셀렉트 만들기

 CSS로 만든 셀렉트박스에서 발생하는 주요 이슈로 인해 브라우저 기본인 `<select>` 와 `<option>` 을 사용해 드롭다운 되는 셀렉트 박스를 구현하고자 한다.

기본 구조

```html
<select>
	<option>option 1</option>
	<option>option 2</option>
	<option>option 3</option>
</select>
```

브라우저마다 각기 다른 네이티브 디자인을 초기화한다.

```css
select {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}

/* IE에서 화살표 제거 */
select::-ms-expand {
  display: none;
}
```

 Select의 기본 디자인을 변형하고, 화살표를 제거한 후 원하는 아이콘 혹은 CSS 쉐입으로 대체하는게 가능하지만, `<option>` 의 디자인 커스텀에는 한계가 있다. 

 이는 `<option>`이 CSS의 범위를 벗어나는 [객원 요소](https://developer.mozilla.org/ko/docs/Web/CSS/Replaced_element) 이기 때문이다. 객원 요소는 OS에 영향을 받으며, HTML이나 브라우저의 일부분이 아니다. 그래서 CSS를 통해 스타일링할 수 없다.