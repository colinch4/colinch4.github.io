---
layout: post
title: "Svelte 입문 강의 - A부터 Z까지 1"
description: " "
date: 2020-08-17
tags: [Svelte]
comments: true
share: true
---


## 1️⃣
### 🖥 svelte 소개
#### 0 - 2. Svelte 특징
- 다른 프레임 워크에 비해 더 적은양의 코드로 같은 동작을 구현할 수 있다.
- 장점 : 
	1. 생성되는 번들의 크기가 줄어든다. ( SPA 는 첫 로딩시에 모든 리소스를 다운받아야 해서 시간소요가 있는것에 비해, svelte 는 코드수 자체가 적기 때문에 번들 크기가 감소된다.)
	2. 유지보수 비용 감소
- no vitual DOM ( 가상돔 X) => 가상돔을 사용하지 않기 때문에 런타임을 포함하지 않아서 번들의 크기가 더 줄어든다.

> 런타임이란 ? 어플리케이션이 동작하는 동안 가상돔을 비교해서 변경된 내용을 알기위해 사용

- svelte 는 진짜 반응형 프레임 워크이다. : 변경된 위치를 찾아서 변경하는것이 아닌, 변경된 위치를 정확하게 아는 진짜 반응형

#### 0 - 3. Svelte 사용시 유의사항
- **CDN 사용 불가** : 런타임이 있어야 CDN, 웹 IDE 에서 사용이 가능한데, svelte 는 런타임을 포함하고 있지 않다.
- svelte 는 빌드 타임에 반응형이 결정된다.
- **브라우저 지원 체크** : 공식문서에서 어느 브라우저까지 지원한다고 말하고 있지 않기때문에, 크로스브라우징에 민감한 서비스는 svelte 를 추천하지 않는다.

> IE 11 이하의 구형 브라우저에서는 별도의 설정 작업 필요

- **생태계가 작음** : 신규 프레임 워크이기 때문에 기존 react, vue 에 비해 좁음 

> router : svelte 에서 공식적으로 제공하는 router 가 없다. svelte-spa-router 많이 이용하는 라이브러리
> store : svelte 안에 store 기능 포함
> cli : cli 존재 X, 다만 github에 rollup, webpack 번들러 2가지 버전의 보일러 플레이트가 올라와 있어, 클론으로 프로젝트 생성 가능 

#### 0 - 4. Quick Start Guide
- REPL 사용 : [공식문서](https://svelte.dev/repl/hello-world?version=3.24.1)에서 제공 => 코딩 후 다운로드 받으면 svelte-app.zip 으로 저장 => 프로젝트 실행 

<pre><code>$ npm i
$ npm run dev</code></pre>

- Degit 사용 
	1. Rollup 프로젝트 
    
<pre><code>$ npx degit sveltejs/template 프로젝트이름
$ cd 생성프로젝트
$ npm i
$ npm run dev</code></pre>

	2. Webpack 프로젝트  

<pre><code>$ npx degit sveltejs/template-webpack 프로젝트이름
$ cd 생성프로젝트
$ npm i
$ npm run dev</code></pre>

> Rollup 의 경우 localhost 5000 이지만, Webpack의 경우는 localhost 8080 


### 🖥 기초 문법
#### 1 - 1. 데이터 정의

```javascript
<script>
let  name  =  "JJ"
</script>

<div>Hello, {name}! </div>

<style></style>
```

- vue 와 달리 svelte 는 { } 

> vscode에서 svelte 문법 적용을 위해 setting.json 에 아래와 같이 추가 해 주었다 

<pre><code>"files.associations": {
	"*.svelte": "html"
}, </code></pre>

- 참고 사이트 : [편집기 설정](https://svelte.dev/blog/setting-up-your-editor)

#### 1 - 2. 속성 정의

<img src="https://github.com/jina95/TIL/blob/master/images/svelte/svelte_%EC%86%8D%EC%84%B1%EC%A0%95%EC%9D%98.png" width="80%">

#### 1 - 3. 스타일 정의

```javascript
<div class="active">My name is Jina </div>

<style>
	.active {
		color: red;
	}
:global(.active) {
	color: blue;
	}
</style>
```

- .active 로 스타일을 줄때 개발자도구로 보면 해쉬태그(?)값이 붙는것을 확인 할 수 있다.

<img src="https://github.com/jina95/TIL/blob/master/images/svelte/svelte_%EC%8A%A4%ED%83%80%EC%9D%BC%EC%A0%95%EC%9D%98_%ED%95%B4%EC%89%AC%ED%83%9C%EA%B7%B8.png" width="30%">

- svelte에서는 기본적으로 해당 컴포넌트 안에서만 적용되는 스타일로 적용되기 때문/ 이때 글로벌 기능을 사용하여 전역으로 사용 할 수 있다 ( ex :global(😀))

#### 1-4. 컴포넌트 정의

```javascript
<script>
import Child from  './Child.svelte'
</script>

<Child></Child>
<div>This is parent</div>
```

#### 1-5. HTML 문자열 표현

```javascript
<script>
	let  string  =  'My name is <strong>JJ</strong>.'
</script>

<div>{ @html string }</div>
<!-- html 요소로 변환 됨 -->
```

### 🖥 반응형을 위한 문법
#### 2 - 1. 이벤트 리스너

```javascript
<script>
	let count = 0;

	function handleClick() {
		count ++;
	}
	function handleMouseDown(){
		console.log('down!');
		
	}
</script>

<button 
	on:click={handleClick}
	on:mousedown={handleMouseDown}
	>
	Clicked {count}
</button>
```

#### 2 - 2. $ 문법
- vue에서 computed와 watch를 합쳐놓은 문법이라고 생각하면 이해하기 쉬움!

<img src="https://github.com/jina95/TIL/blob/master/images/svelte/svelte_%24%EB%AC%B8%EB%B2%95.png" width="80%">

- [label](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/label)

#### 2 - 3. 주의해야할 것들
- 반응형 문법을 사용할때 주의해야할 두가지 !
- [reduce](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)

<img src="https://github.com/jina95/TIL/blob/master/images/svelte/svelte_%EC%A3%BC%EC%9D%98%ED%95%B4%EC%95%BC%ED%95%A0%EA%B2%83%EB%93%A4.png" width="80%">
