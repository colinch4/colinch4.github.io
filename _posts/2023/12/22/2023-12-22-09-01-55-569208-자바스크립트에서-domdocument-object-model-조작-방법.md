---
layout: post
title: "[javascript] 자바스크립트에서 DOM(Document Object Model) 조작 방법"
description: " "
date: 2023-12-22
tags: [javascript]
comments: true
share: true
---

웹 페이지의 동적인 요소를 변경하거나 조작하기 위해서는 **DOM(Document Object Model)**을 사용해야 합니다. 자바스크립트를 사용하여 DOM을 조작하는 방법에 대해 알아봅시다.

## 1. 요소 선택하기

특정 요소를 선택하여 조작하기 위해서는 `document.querySelector()`나 `document.getElementById()`와 같은 메서드를 사용합니다.

예를 들어, 아이디가 "myElement"인 요소를 선택하려면:

```javascript
const element = document.getElementById('myElement');
```

## 2. 요소 조작하기

선택한 요소를 조작하기 위해서는 해당 요소의 속성을 변경하거나 새로운 HTML을 삽입할 수 있습니다.

### 2.1. 텍스트 내용 변경

```javascript
element.textContent = '새로운 텍스트';
```

### 2.2. HTML 내용 변경

```javascript
element.innerHTML = '<p>새로운 HTML</p>';
```

### 2.3. 클래스 추가/제거

```javascript
element.classList.add('newClass');
element.classList.remove('oldClass');
```

### 2.4. 속성 변경

```javascript
element.setAttribute('속성명', '새로운값');
```

### 2.5. 새로운 요소 추가

```javascript
const newElement = document.createElement('div');
newElement.textContent = '새로운 요소';
element.appendChild(newElement);
```

## 3. 이벤트 처리하기

특정 이벤트(클릭, 마우스 오버 등)가 발생했을 때 처리할 함수를 등록할 수 있습니다.

```javascript
element.addEventListener('click', () => {
  // 처리할 내용
});
```

위와 같은 방법으로 자바스크립트를 사용하여 DOM을 조작할 수 있습니다. 이를 통해 웹 페이지의 동적인 요소를 자유롭게 변경하고 조작할 수 있습니다.

<!-- 출처: MDN Web Docs - https://developer.mozilla.org/ko/docs/Web/API/Document_Object_Model -->

## 참고 자료
- [MDN Web Docs - Document Object Model(DOM)](https://developer.mozilla.org/ko/docs/Web/API/Document_Object_Model)
- [JavaScript.info - DOM과 노드](https://ko.javascript.info/dom-nodes)