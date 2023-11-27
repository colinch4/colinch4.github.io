---
layout: post
title: "[javascript] ScrollMagic과 GSAP(TweenMax)을 함께 사용하는 방법"
description: " "
date: 2023-11-27
tags: [javascript]
comments: true
share: true
---

이번 포스트에서는 ScrollMagic과 GSAP(TweenMax)을 함께 사용하여 스크롤 이벤트에 따라 요소를 애니메이션하는 방법을 알아보겠습니다.

## ScrollMagic과 GSAP 소개

**ScrollMagic**은 JavaScript 라이브러리로, 스크롤 이벤트를 감지하고 이에 따른 애니메이션 효과를 쉽게 적용할 수 있습니다. ScrollMagic은 요소의 스크롤 위치, 스크롤 속도 등을 기반으로 다양한 애니메이션 효과를 제어합니다.

**GSAP(TweenMax)**은 GreenSock Animation Platform의 일부입니다. GSAP은 매끄럽고 강력한 JavaScript 애니메이션 라이브러리로, 다양한 애니메이션 이펙트와 타이밍을 지원합니다.

## Step 1: ScrollMagic 및 GSAP 라이브러리 추가

먼저 ScrollMagic과 GSAP을 사용하기 위해 해당 라이브러리를 웹 페이지에 추가해야 합니다. 아래의 코드를 HTML 문서의 `<head>` 태그 내에 추가합니다.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/ScrollMagic/2.0.8/ScrollMagic.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/2.1.3/TweenMax.min.js"></script>
```

## Step 2: 애니메이션 대상 설정

Animate할 대상 요소를 선택합니다. 예를 들어, `#myElement`라는 id를 가진 요소를 애니메이션 대상으로 설정하겠습니다.

```html
<div id="myElement">
  <!-- 애니메이션 대상 -->
</div>
```

## Step 3: ScrollMagic 컨트롤러 생성

ScrollMagic 컨트롤러를 생성하여 스크롤 이벤트를 제어합니다.

```javascript
var controller = new ScrollMagic.Controller();
```

## Step 4: GSAP 애니메이션 생성

TweenMax를 사용하여 GSAP 애니메이션을 생성합니다. 예를 들어, 요소를 오른쪽으로 300px만큼 이동하는 애니메이션을 생성하겠습니다.

```javascript
var myTween = TweenMax.to("#myElement", 1, {x: 300});
```

## Step 5: ScrollMagic 시나리오 생성

ScrollMagic 시나리오를 생성하여 ScrollMagic 컨트롤러와 GSAP 애니메이션을 연결합니다. 이때, 애니메이션을 특정 스크롤 위치에서 시작하기 위해 `triggerElement`와 `triggerHook`을 설정합니다.

```javascript
new ScrollMagic.Scene({
  triggerElement: "#myElement",
  triggerHook: "onEnter" // 애니메이션 시작 위치 설정
})
.setTween(myTween) // 애니메이션 설정
.addTo(controller); // 컨트롤러에 시나리오 추가
```

## 완성된 코드

다음은 ScrollMagic과 GSAP을 함께 사용하여 스크롤 이벤트에 따라 요소를 애니메이션하는 완성된 예제 코드입니다.

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/ScrollMagic/2.0.8/ScrollMagic.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/2.1.3/TweenMax.min.js"></script>
</head>
<body>
  <style>
    #myElement {
      width: 100px;
      height: 100px;
      background-color: red;
      position: fixed;
      left: 0;
      top: 50%;
      margin-top: -50px;
    }
  </style>
  
  <div id="myElement"></div>
  
  <script>
    var controller = new ScrollMagic.Controller();
    var myTween = TweenMax.to("#myElement", 1, {x: 300});
    
    new ScrollMagic.Scene({
      triggerElement: "#myElement",
      triggerHook: "onEnter"
    })
    .setTween(myTween)
    .addTo(controller);
  </script>
</body>
</html>
```

이제 위의 코드를 HTML 파일로 저장하고 웹 브라우저에서 실행하면 스크롤 이벤트에 따라 요소가 애니메이션되는 것을 확인할 수 있습니다. ScrollMagic과 GSAP을 함께 사용하면 더욱 다양하고 동적인 웹 페이지 애니메이션을 구현할 수 있습니다.

참고 자료:
- ScrollMagic 공식 문서: [https://scrollmagic.io/](https://scrollmagic.io/)
- GSAP 공식 문서: [https://greensock.com/docs/](https://greensock.com/docs/)