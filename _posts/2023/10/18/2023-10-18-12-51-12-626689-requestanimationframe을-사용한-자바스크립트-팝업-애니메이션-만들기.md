---
layout: post
title: "requestAnimationFrame을 사용한 자바스크립트 팝업 애니메이션 만들기"
description: " "
date: 2023-10-18
tags: [javascript]
comments: true
share: true
---

![popup animation](image_link)

이번 포스트에서는 requestAnimationFrame을 사용하여 자바스크립트로 팝업 애니메이션을 만드는 방법에 대해 알아보겠습니다.

## 개요

팝업 애니메이션은 웹페이지에서 사용자에게 중요한 정보를 알리거나 강조하기 위해 일시적으로 화면에 표시되는 UI 요소입니다. 이번 예제에서는 팝업이 나타나고 사라지는 애니메이션 효과를 구현해보겠습니다. 

## HTML 구조

팝업을 만들기 위해 가장 먼저 HTML 구조를 설정해야 합니다. 예제에서는 단순한 구조로 div 요소를 사용하여 팝업의 내용과 스타일을 관리합니다.

```html
<div id="popup" class="hidden">
  <div id="popup-content">
    <!-- 팝업 내용 -->
  </div>
</div>
```

## CSS 스타일 설정

팝업의 초기 상태는 가려진(hidden) 상태로 설정해야 합니다. 이를 위해 CSS 스타일에서 `display: none;` 속성을 사용합니다. 추가적으로 팝업 내용을 가운데 정렬하거나 원하는 스타일을 적용할 수 있습니다.

```css
#popup {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 999;
}

#popup-content {
  /* 팝업 내용에 대한 스타일 */
}

.hidden {
  display: none;
}
```

## 자바스크립트 애니메이션 구현

이제 팝업 애니메이션을 자바스크립트로 구현해보겠습니다. 애니메이션을 시작하거나 종료하기 위해 두 개의 함수를 만들어 사용할 것입니다.

```javascript
const popup = document.getElementById("popup");

function showPopup() {
  popup.classList.remove("hidden");
  animatePopup();
}

function hidePopup() {
  popup.classList.add("hidden");
}

function animatePopup() {
  // 애니메이션 로직 작성
}
```

애니메이션 로직을 작성하기 전에 requestAnimationFrame을 사용하여 애니메이션 프레임마다 호출되는 함수를 만들어야 합니다.

```javascript
function animatePopup() {
  // 애니메이션 로직
  requestAnimationFrame(animatePopup);
}
```

팝업이 나타나는 애니메이션을 구현하려면 팝업 요소의 높이를 천천히 증가시켜야 합니다. 이를 위해 애니메이션 진행에 따라 높이 값을 조정하는 코드를 작성합니다.

```javascript
function animatePopup() {
  const popupContent = document.getElementById("popup-content");
  let height = 0;

  function increaseHeight() {
    height += 10;
    popupContent.style.height = height + "px";
    
    if (height < 200) {
      requestAnimationFrame(increaseHeight);
    }
  }

  increaseHeight();
}
```

팝업이 나타났다가 사라지는 애니메이션을 구현하려면, 팝업 요소의 투명도(opacity)값을 천천히 조정해야 합니다.

```javascript
function animatePopup() {
  const popupContent = document.getElementById("popup-content");
  let opacity = 0;

  function fadeIn() {
    opacity += 0.1;
    popupContent.style.opacity = opacity;
    
    if (opacity < 1) {
      requestAnimationFrame(fadeIn);
    }
  }

  function fadeOut() {
    opacity -= 0.1;
    popupContent.style.opacity = opacity;
    
    if (opacity > 0) {
      requestAnimationFrame(fadeOut);
    } else {
      hidePopup();
    }
  }

  fadeIn();

  setTimeout(() => {
    fadeOut();
  }, 3000);
}
```

## 요약

이렇게 requestAnimationFrame을 사용하여 자바스크립트 팝업 애니메이션을 구현할 수 있습니다. 팝업이 나타나는 애니메이션과 사라지는 애니메이션을 각각 구현하고 조합하여 원하는 효과를 만들 수 있습니다. 추가로 CSS 애니메이션 효과와 조합하여 보다 다양한 팝업 애니메이션을 만들 수도 있습니다.

## 참고 자료

- [Mozilla Developer Network: requestAnimationFrame](https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame)