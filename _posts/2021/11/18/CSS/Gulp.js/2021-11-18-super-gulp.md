---
layout: post
title: "[gulp] super gulp"
description: " "
date: 2021-11-18
tags: [gulp]
comments: true
share: true
---


gulp Study
------
* [lectures](https://nomadcoders.co/gulp-for-beginners/lectures/1640)  
* [Install & Using](https://velog.io/@hwang-eunji/SASSSCSS-%EC%84%A4%EC%B9%98%EB%B6%80%ED%84%B0-%EA%B0%84%EB%8B%A8-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%A0%95%EB%A6%AC)
* [Super-Gulp Project](https://github.com/nomadcoders/super-gulp)       
* [npm Gulp-Sass](https://www.npmjs.com/package/gulp-sass)  


###  SCSS COMPILATION

* [Sass Basics](https://sass-lang.com/guide)   
* [Style Rules](https://sass-lang.com/documentation/style-rules)  


### Variables

~~~~SCSS
// 변수를 사용할때는'$변수명'을 사용
$yl: yellow;
$lg: #eee;
$border: solid black 4px;
$px800: 400px;

//example
$font-stack:    Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
~~~~~~~

### Nesting
#### scss
~~~~~~SCSS
nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  li { display: inline-block; }

  a {
    display: block;
    padding: 6px 12px;
    text-decoration: none;
  }
}
~~~~~~~

### Partials
~~~~scss
Use "_filename.scss"
⇒ 부분화하는 방법：파일명 앞에 언더바(_)입력
⇒ "_"가 없을 경우 하나의 CSS파일로 인식되어 컴파일 된다.
⇒ @import 'filename(url)'
~~~~

### Mixin
+ 선언하여, 인자전달 & 기본값 설정 가능
#### scss
~~~~scss
@mixin transform($property) {
  -webkit-transform: $property;
  -ms-transform: $property;
  transform: $property;
}
.box { @include transform(rotate(30deg)); }
~~~~
#### css
~~~css
.box {
  -webkit-transform: rotate(30deg);
  -ms-transform: rotate(30deg);
  transform: rotate(30deg);
}
~~~
#### sample
~~~~scss
@mixin flexCenter($align, $type, $color: black) {
 	/* 3개의 매개변수 지정, 마지막 컬러값에는 기본값으로 black을 지정 */
	display: flex;
	justify-content: center;
	align-items: $align;
	flex-wrap: wrap;
	&:hover {
		border: $type 4px $color;
	}
}
.color-box {
	@include flexCenter(center, none); /*인자전달 & 기본값 사용*/
	padding-top: 20px;
	.s_box {
		border: $border;
		border-radius: 50%;
		width: 100px;
		height: 100px;
		background-color: $lg;
		margin: 12px;
		@include flexCenter(center, solid, fuchsia); /*인자전달*/
		&:hover {
			background-color: $yl;
		}
	}
}
~~~~
### Extend/Inheritance
+ 공통적인 부분들을 묶어서 사용가능
+ 값을 상속받아 사용 가능
~~~~~scss
/* This CSS will print because %message-shared is extended. */
%message-shared {
  border: 1px solid #ccc;
  padding: 10px;
  color: #333;
}

// This CSS won't print because %equal-heights is never extended.
%equal-heights {
  display: flex;
  flex-wrap: wrap;
}

.message {
  @extend %message-shared;
}

.success {
  @extend %message-shared;
  border-color: green;
}

.error {
  @extend %message-shared;
  border-color: red;
}

.warning {
  @extend %message-shared;
  border-color: yellow;
}
~~~~~~

### Operators
+ 연산자 ( +, -, *, /, % ) 사용가능
~~~~~scss
.container {
  width: 100%;     // Using Operators
}

article[role="main"] {
  float: left;
  width: 600px / 960px * 100%;     // Using Operators
}

aside[role="complementary"] {
  float: right;
  width: 300px / 960px * 100%;    // Using Operators
}
~~~~~
