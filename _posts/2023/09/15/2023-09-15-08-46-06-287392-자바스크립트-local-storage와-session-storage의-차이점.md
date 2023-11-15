---
layout: post
title: "자바스크립트 Local Storage와 Session Storage의 차이점"
description: " "
date: 2023-09-15
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 로컬 스토리지(Local Storage)와 세션 스토리지(Session Storage)는 웹 애플리케이션에서 데이터를 브라우저에 저장하는 데 사용되는 기능입니다. 이 두 가지 스토리지 방법은 유사한 기능을 제공하지만 몇 가지 차이점이 있습니다.

## 로컬 스토리지 (Local Storage)

로컬 스토리지는 HTML5에서 제공하는 기능으로, 데이터를 브라우저에 영구적으로 저장할 수 있습니다. 이 데이터는 브라우저를 닫아도 유지됩니다. 로컬 스토리지는 도메인(도메인, 서브도메인, 포트)에 종속되며, 동일 도메인에서 여러 탭 또는 창 간에 데이터를 공유할 수 있습니다. 

로컬 스토리지의 사용 예시:
```javascript
// 데이터 저장
localStorage.setItem('name', 'John');
localStorage.setItem('age', '25');

// 데이터 가져오기
let name = localStorage.getItem('name');
let age = localStorage.getItem('age');
```

## 세션 스토리지 (Session Storage)

세션 스토리지는 로컬 스토리지와 비슷한 기능을 제공하지만, 데이터는 브라우저 세션이 유지되는 동안만 유효합니다. 즉, 브라우저를 닫으면 세션 스토리지에 저장된 데이터는 삭제됩니다. 세션 스토리지도 로컬 스토리지와 마찬가지로 도메인에 종속되며 동일 도메인에서 데이터를 공유할 수 있습니다.

세션 스토리지의 사용 예시:
```javascript
// 데이터 저장
sessionStorage.setItem('name', 'John');
sessionStorage.setItem('age', '25');

// 데이터 가져오기
let name = sessionStorage.getItem('name');
let age = sessionStorage.getItem('age');
```

## 결론

로컬 스토리지와 세션 스토리지는 브라우저에서 데이터를 저장하는 데 사용되는 유용한 기능입니다. 로컬 스토리지는 데이터를 영구적으로 보관하고, 세션 스토리지는 브라우저 세션이 유지되는 동안만 데이터를 저장합니다. 이러한 기능을 활용하여 웹 애플리케이션에서 필요한 데이터를 효과적으로 관리할 수 있습니다.

#JavaScript #WebDevelopment