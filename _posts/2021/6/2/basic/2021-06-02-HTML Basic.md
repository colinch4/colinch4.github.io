---
layout: post
title: "[css] 기초 HTML"
description: " "
date: 2021-06-02
tags: [css]
comments: true
share: true
---

# 기초 HTML

<br>

## HTML이란 ?

- HTML(HyperText Markup Language)은 웹페이지를 기술하기 위한 마크업 언어 이다.
  좀더 자세히 말하자면 웹페이지의 내용(content)과 구조(structure)을 담당하는 언어로써 HTML 태그를 통해 정보를 구조화하는 것이다.

- 최근 HTML5 버전까지 업데이트 되었다.
- [HTML의 등장과 배경](https://webclub.tistory.com/491)

## HTML5

- HTML5는 문서는 `<!DOCTYPE html>`으로 시작하여 문서형식(document type)을 HTML5로 지정한다.
- HTML은 크게 2가 파트로 나뉘어지는데 **외부적으로 보여지지 않는 설정을 하는** `<head></head>` 부분과  
  **사용자가 볼 수 있는** `<body></body>` 부분이다.
- 예시

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8" />
      <title>Hello World</title>
    </head>
    <body>
      <h1>Hello World</h1>
      <p>안녕하세요 HTML5 입니다.</p>
    </body>
  </html>
  ```

<br>

## 기본문법

### 1. 태그

- <태그이름> 으로 시작하여 <태그이름/> 으로 끝나고 태그 사이에 내용이 있는 구조를 요소라고 합니다.
- 끝 태그가 필요없는 것은 태그가 그 자체로 요소가 됩니다.
  ![HTML 요소](https://poiemaweb.com/img/tag.png)

- 한글, 일본어, 중국어가 포함된 페이지라면 utf-8 이라는 값으로 문자 인코딩을 추가해줘야 합니다.

  ```html
  <meta charset="utf-8" />
  ```

- 디바이스의 가로 크기가 곧 웹 페이지의 가로와 같다는 의미입니다. 모바일에서 웹사이트가 예쁘게 잘 보이려면 추가해야 하는 정보입니다. 해당 정보를 추가하지 않으면 데스크탑 버전의 웹페이지가 축소되어 보이는 현상이 나타납니다.

  ```html
  <meta name="viewport" content="width=device-width" />
  ```

<br>

### 2. 어트리뷰트 (Attribute)

- 어트리뷰트(Attribute 속성)이란 요소의 성질, 특징을 정의하는 명세이다. 요소는 어트리뷰트를 가질 수 있으며 어트리뷰트는 요소에 추가적 정보(이미지 파일의 경로, 크기 등..)를 제공한다.
  ![Attribute](https://poiemaweb.com/img/html-attribute.png)

<br>

### 3. 주석 (Comments)

- 주석은 주로 개발자에게 코드를 설명하기 위해 사용되며 브라우저는 주석을 화면에 표시하지 않는다.
<pre><code>
<!-- Lorem ipsum dolor sit amet consectetur adipisicing elit. Maiores, cum? -->
<!-- 내용 -->
</code></pre>

<br>

## 4. HTML 구문

### ol 태그와 ul태그

- ul(unordered list) : 순서가 없는 목록 리스트
- ol(ordered list) : 순서가 있는 목록 리스트
- 예시

  ```html
  <ul>
    <li>감자</li>
    <li>고구마</li>
  </ul>
  <ol>
    <li>웨이트</li>
    <li>내추럴</li>
  </ol>
  ```

> <ul>
>   <li>감자</li>
>   <li>고구마</li>
> </ul>
> <ol>
>   <li>웨이트</li>
>   <li>내추럴</li>
> </ol>

<br>

### a(anchor) 태그

- anchor는 다른 웹사이트로 이동하는 방법이다.
- anchor를 클릭하게 하기위해 **href attribute** 를 준다.
- **href란** "HTTP reference" 혹은 "Hyperlink reference"라고 한다. (이동할 곳을 알려주는 attribute)
- target attribute는 링크를 클릭 할 떄 창을 어떻게 열지 결정한다.

  - `_self` : 연결 문서를 클릭한창에서 연다 (기본 값)
  - `_black` : 연결 문서를 새탭에서 연다.

- 예시

  ```html
  <a href="https://github.com/kdh92417" target="_black">Go to my github</a>
  ```

  => <a href="https://github.com/kdh92417" target="_black">Go to my github</a>

<br>

### img 태그

- "self-closing tag" (자체 닫기 태그)여서 닫는 태그가 없고 태그사이에 content가 필요없다.
- src 어트리뷰트에 해당 이미지 URL주소를 집어넣으면 된다.
- img태그의 content가 src attribute이다.
- 인터넷에 올려져있는 이미지만 보여주는 것이 아니라 Local에 있는 이미지도 이미지주소를 넣음으로써 보여줄 수 있다.

  - html파일과 같은 폴더안에 위치해 있으면 파일명을 src에 넣어서 이미지를 보여줄 수 있다.

- 예시

  ```html
  <img src="https://i.pinimg.com/originals/73/ca/b8/73cab8e4aae721370e266e8bb6ffbd1a.jpg"/>

  <img src="gogh.jpg"/>
  <img src="img/gogh.jpg"> <!-- path notation(경로 표기법)을 이용한 방법 : img폴더안에 이미지가 있을경우
  ```

> <img src="https://i.pinimg.com/originals/73/ca/b8/73cab8e4aae721370e266e8bb6ffbd1a.jpg" width=20%/>

> <img src="gogh.jpg"/>

<br>

### meta 태그

- 부가적인 정보를 입력하는 태그이다.
- name, content, charset 등의 attributes등을 갖고있다.

<br>

### Semantic HTML

- 문서를 보기만 해도 그의미를 짐작할 수 있는 걸 semantic이라고 한다.
- `header`, `main`, `footer` , `aside`, etc..
- Non-Semantic tag
  - `div` tag (division) : 아무런 의마가 없는 태그 (block element : 한줄을 다차지)
  - `span` tag : 짦은 text를 위한 태그 (inline element : 한줄에 이어서 나오는 태그)
- 예시

  ```html
  <header>
    <h1>The Adam Times</h1>
  </header>
  <main>
    <p>Hello!</p>
  </main>
  ```

  <header>
    <h1>The Adam Times</h1>
  </header>
  <main>
    <p>Hello!</p>
  </main>
  <footer>
    &copy; 2020 Adam
  </footer>

#### 되도로 이면 이해하기 쉬운 html 문서를 만드는게 좋다.

- 사방팔방 `div` 또는 `span`으로 하지않고 **`semantic`** 태그를 사용하면 된다.

<br>

### Reference

- https://poiemaweb.com
- https://nomadcoders.com
