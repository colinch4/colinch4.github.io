---
layout: post
title: "IIFE (Immediately Invoked Function Expression)의 활용"
description: " "
date: 2023-09-13
tags: [javascript]
comments: true
share: true
---

IIFE는 JavaScript에서 매우 유용한 패턴 중 하나입니다. 이는 함수를 즉시 정의하고 바로 호출하는 것을 의미합니다. 이 방법은 모듈화되고 프라이빗한 변수 및 함수를 만들 수 있으며, 전역 네임스페이스를 오염시키지 않는 것을 보장합니다. 아래에서 IIFE의 몇 가지 활용법을 살펴보겠습니다.

## 1. Module 패턴

IIFE를 사용하여 모듈을 생성하는 것은 코드를 모듈화하여 조직화하고 재사용할 수 있는 방법을 제공합니다. 또한 외부에서 접근이 제한된 변수와 함수를 생성하여 데이터 은닉화를 달성할 수 있습니다. 

```javascript
// IIFE를 사용한 모듈 생성
var myModule = (function () {
  var privateVariable = "비공개 변수";

  function privateFunction() {
    console.log("비공개 함수");
  }

  return {
    publicMethod: function () {
      console.log("공개 메서드");
    }
  };
})();

// 모듈 사용
myModule.publicMethod(); // "공개 메서드"
```

## 2. Namespacing

IIFE를 사용하여 전역 네임스페이스를 정리하고 분리된 모듈을 만들 수 있습니다. 이를 통해 전역 스코프의 변수 충돌과 오염을 방지할 수 있습니다.

```javascript
// IIFE를 사용한 네임스페이스 생성
var myNamespace = (function () {
  var privateVariable = "비공개 변수";

  function privateFunction() {
    console.log("비공개 함수");
  }

  return {
    publicMethod: function () {
      console.log("공개 메서드");
    }
  };
})();

// 네임스페이스 사용
myNamespace.publicMethod(); // "공개 메서드"
```

IIFE (Immediately Invoked Function Expression)은 JavaScript 개발에서 광범위하게 활용될 수 있는 강력한 패턴입니다. 모듈화와 변수 은닉화를 통해 코드를 더욱 구조적이고 유지보수 가능한 방향으로 개발할 수 있습니다.

[#javascript](javascript) [#IIFE](iife)