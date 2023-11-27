---
layout: post
title: "[javascript] ScrollMagic과 Animate.css을 함께 사용하는 방법"
description: " "
date: 2023-11-27
tags: [javascript]
comments: true
share: true
---

ScrollMagic과 Animate.css은 웹 애니메이션을 구현하기 위해 자주 사용되는 도구입니다. ScrollMagic은 스크롤 이벤트에 반응하여 요소를 제어하고 애니메이션을 적용하는 라이브러리입니다. Animate.css은 사전에 정의된 CSS 애니메이션 클래스를 사용하여 요소에 애니메이션 효과를 적용하는 라이브러리입니다.

이 문서에서는 ScrollMagic과 Animate.css을 함께 사용하는 간단한 예제를 제공합니다.

## 1. ScrollMagic 및 Animate.css 추가

우선 ScrollMagic과 Animate.css을 HTML 파일에 추가해야 합니다. 다음과 같이 `<head>` 태그 내에 다음 코드를 추가하세요:

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/ScrollMagic/2.0.7/ScrollMagic.min.js"></script>
```

이 코드는 Animate.css와 ScrollMagic의 최신 버전을 사용하기 위해 CDN 링크를 포함하고 있습니다. 원하는 경우 로컬에 다운로드한 파일을 사용할 수도 있습니다.

## 2. HTML 요소 준비

ScrollMagic과 Animate.css를 적용할 HTML 요소를 준비해야 합니다. 아래는 예제로 사용할 단일 `<div>` 요소입니다:

```html
<div class="box">Scroll down</div>
```

## 3. CSS 스타일 적용

다음으로, ScrollMagic과 Animate.css에 의해 적용될 CSS 스타일을 정의해야 합니다. 아래는 예제에 사용할 스타일입니다:

```css
.box {
  width: 100px;
  height: 100px;
  background-color: red;
}
```

## 4. ScrollMagic 및 Animate.css 설정

JavaScript 코드를 사용하여 ScrollMagic과 Animate.css를 설정합니다. 아래는 예제 코드입니다:

```javascript
// ScrollMagic 생성
var controller = new ScrollMagic.Controller();

// ScrollMagic Scene 생성
var scene = new ScrollMagic.Scene({
  triggerElement: ".box",
  reverse: false,
})
  .setClassToggle(".box", "animate__fadeInUp")
  .addTo(controller);
```

위 코드에서 `controller`는 ScrollMagic 컨트롤러를, `scene`은 ScrollMagic 씬을 생성합니다. `triggerElement` 속성은 스크롤 이벤트를 감지할 요소를 선택합니다. `reverse` 속성은 애니메이션을 롤백할 지 여부를 결정합니다. `setClassToggle` 메소드는 요소 목록에 지정된 클래스를 토글링합니다. 이 예제에서는 `.box` 요소에 `animate__fadeInUp` 클래스를 추가/제거하여 애니메이션을 적용합니다.

## 5. 결과 확인

웹 브라우저에서 HTML 파일을 열고 스크롤을 내리면 `.box` 요소가 애니메이션 효과와 함께 나타나는 것을 확인할 수 있습니다.

## 참고 자료

- ScrollMagic 공식 문서: [https://scrollmagic.io/docs/index.html](https://scrollmagic.io/docs/index.html)
- Animate.css 공식 문서: [https://animate.style/](https://animate.style/)