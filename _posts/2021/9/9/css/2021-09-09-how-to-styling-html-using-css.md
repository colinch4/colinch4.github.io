---
layout: post
title: "[css] CSS를 사용해 HTML을 스타일링 하는 방법"
description: " "
date: 2021-09-09
tags: [css]
comments: true
share: true
---

## CSS를 사용해 HTML을 스타일링 하는 방법

사내 스터디를 위한 CSS 기초 지식을 정리 해본다. 그저 당연하게 사용하는것들에 대해 다시 곱씹어보는 계기가 되는것 같다 👏

## 인라인 스타일 (Inline style)

HTML 태그 요소(element)에 `style` 속성을 사용해 스타일링

```html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <h1 style="color: red;">Hello World</h1>
    <h2>HTML에 스타일링하는 세가지 방법</h2>
  </body>
</html>
```

## 인터널 스타일 (Internal style)
HTML 문서 `<head>` 영역 내부에 `<style>` 태그 추가 후 스타일링

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      h2 {
    	  color: blue;
      }
    </style>
  </head>
  <body>
    <h1>Hello World</h1>
    <h2>HTML에 스타일링하는 세가지 방법</h2>
  </body>
</html>
```

## 익스터널 스타일 (External style)
별도의 CSS 파일을 만들어 HTML 문서와 연결
```css
h2 {
color: blue;
}
```

```html
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="css/style.css">
  </head>
  <body>
    <h1>Hello World</h1>
    <h2>HTML에 스타일링하는 세가지 방법</h2>
    <ul>
      <li>인라인 스타일</li>
      <li>인터널 스타일</li>
      <li>익스터널 스타일</li>
    </ul>
  </body>
</html>
```



📖 참고 자료

* [How CSS works](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_works#CSS를_HTML에_적용하는_방법)

