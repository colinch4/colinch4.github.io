---
layout: post
title: "[css] 셀렉트박스 커스텀하기"
description: " "
date: 2021-09-09
tags: [css]
comments: true
share: true
---

## 셀렉트박스 커스텀하기

[Codepen 예제](https://codepen.io/onlyeon/pen/RwWWWWW)

HTML5의 기본 `<select>`, `<option>` 을 사용하여 구현할 경우 가능한 디자인 커스텀.

`.select__wrap`

1. `flex` 로 선언하여 레이아웃을 잡는다
2. `align-items` 로 내부 요소를 수직 중앙 정렬 한다
3. `select__wrap`를 `relative` 로 기준을 잡고, 아이콘을 `absolute`로 포지셔닝한다



`.select__input`

4. Wrapper대신 `select__input` 에 `padding` 을 추가해 클릭 가능한 타겟의 크기를 키운다
5. 높이를 선언하다
6. `<select>` 태그의 `outline` 을 숨긴다
7. `<select>` 태그의 기본적인 스타일을 숨긴다
8. 클릭 가능성을 암시한다
9. IE10+ 에서 `<select>` 태그의 기본 화살표를 감춘다



`.select__icon`

10. icon을 `absolute` 로 포지셔닝 한다
11. icon을 우측에 위치시키는 매직 넘버
12. icon을 통해 `<select>` 가 클릭 가능하도록 한다
13. `::before` 가상 엘리먼트로 디자인 된 아이콘을 추가한다



```scss
.select__wrap {
  display: flex; // 1
  align-items: center; // 2
  position: relative; // 3
}

.select__input {
  padding: 0 24px 0 8px; // 4
  height: 26px; // 5
  
  // Styling
  background-color: #fff; 
  border: 1px solid #ddd;
  border-radius: 3px;
  font-size: 12px;
  font-weight: 500;
  text-align: left;
  transition-duration: 110ms;
  transition-timing-function: ease-in-out;
  white-space: nowrap;
  line-height: 1.25;
  outline: none; // 6
  -webkit-appearance: none; // 7
     -moz-appearance: none; // 7
          appearance: none; // 7
  cursor: pointer; // 8
  
  &:hover  {
    background-color: #eee;
  }
  
  &::-ms-expand {
    display: none; // 9
  }
  
}

.select__icon {
  position: absolute; // 10
  right: 4px; // 11
  pointer-events: none; // 12
  color: #000;
  
  &::before { // 13
    content: 'ㅜ';
  }
}
```

