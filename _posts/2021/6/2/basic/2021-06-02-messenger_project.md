---
layout: post
title: "[css] Html 과 CSS를 이용하여 Messenger Website를 만들면서 배운 것들"
description: " "
date: 2021-06-02
tags: [css]
comments: true
share: true
---

## Html 과 CSS를 이용하여 Messenger Website를 만들면서 배운 것들

## .gitignore

- `.gitignore` : 깃에 올리고싶지 않은 것들을 자동으로 올리지 제외시키게 하는 파일이다.

  - 파일을 `.gitignore`로 만든 뒤, `.확장자` 쓰면 된다.
  - 폴더는 `/폴더이름`

<br>

## index.html

- index.html : 대부분의 웹 서버가 디폴트로 index.html을 찾아보도록 설정되어 있다. (index : 첫번째)

<br>

## BEM(Block Element Modifier)

- 좀 더 쉽게 읽히는 css를 가지는 규칙이다.

- `id` 와 `class`를 사용하면서 프로그래머들이 `id`를 사용했는지 `class`를 사용했는지 햇갈리는 경우가 발생해서 이문제를 해결하고자 모든 부분에 `class` 만을 사용하기로하여 생겨난 규칙이다.

- 사용유무는 자유지만 이용하는 것을 추천

- 예시

  - `.btn`
  - `btn__price`
  - `btn--orange`
  - `btn`은 블럭이고, btn안에 정보가 담겨져있다. price, orange

<br>

## 아이콘 구하는 법

- 첫째. 직접 아이콘을 구하는

- 둘째. 직접 이미지를 만들고 추출하거나 svg 파일을 이용하여 구할 수 있다.

  - svg란 픽셀이 없는 파일형식이다 수학으로만 구성된 형식

### 참고사이트

- https://heroicons.dev/
- https://fontawesome.com/

<br>

## 리셋 CSS

- 원하든 원하지 않든 브라우저가 알아서 html에 body에 적용시키는 스타일이 있는데, 이것들을 모두 없애주는 CSS파일

- reset css 카피하여 파일로 만든뒤, styles.css 에서 @import 하면된다.

  - ```css
    @import "reset.css";
    ```

- 파일들을 새로 만들어 import하여 사용하는 법을 **분할 정복법** 이라 한다.

- [참조사이트](https://cssreset.com/scripts/eric-meyer-reset-css/)

- 먼저 브라우저 스타일을 없애고 우리가 직접 디자인 하는 것이 더 좋은 방법!

<br>

## not

- css는 원치 않는 태그만 제외시키고 적용하고싶을 때 not을 사용하여 태그들을 선택할 수 있다.

- 예시

  - input type이 submit 속성을 가진 태그만 제외시키고적용하고싶을 떄
  - ```css
    #login-form input:not([type="submit"]) {
      border-bottom: 1px solid rgba(0, 0, 0, 0.2);
      transition: border-color 0.3s ease-in-out;
    }
    ```

<br>

## form의 2가지 속성

### 1. action

- 어떤 페이지로 data를 보낼건지 지정 할 수 있다.

### 2. method

- method는 2가지 방식 중 하나를 쓸 수 있다.

  - POST : 백엔드 서버에 정보를 전송하는 방식

  - GET
    - 보안 방식에 취약, 보안정보들을 다루는 데이터들은 get으로 보내면 안된다.
    - URL에 포함되어도 상관없는 정보들을 GET방식으로 보내면 된다.

### 예시

```html
<form action="friends.html" method="get" id="login-form">
  <input name="username" type="text" placeholder="Email or phone number" />
  <input name="password" type="password" placeholder="Password" required />
  <input type="submit" value="Log In" />
  <a href="#">Find Kakao Account or Password</a>
</form>
```

- method가 get인 form에 username과 password를 입력한 뒤 submit 버튼을 누르면,

- friends.html 페이지로 옮겨지고

- `/friends.html?username=ad&password=141`

- url 뒷 부분에 입력한 username과 password가 보인다. 이것이 get방식

<br>

## box-sizing

- 어떤 box에 padding을 줘버리면 css는 padding을 주면서 box의 크기도 유지할려고 하기때문에, 전체 box사이즈가 커진다. 이것을 방지하기위해 `box-sizing:border-box` 한다.

- ```css
  태그 {
    box-sizing: border-box;
  }
  ```

- 이렇게 하면 padding을 주더라도 박스의 크기가 변하지 않는다.

- 즉, padding을 주고 싶은데 box 사이즈가 그대로 있기를 바랄때 쓰면 된다.

<br>

## Z-index

- div가 있는 위치가 맨 앞에서부터 몇번째인지 나타낸다.

- 기본값은 0

- 즉, 레이아웃(layout)과 비슷한 개념으로 절대적 위치나 고정된 위치에 대해서 설정할 수 있다.
