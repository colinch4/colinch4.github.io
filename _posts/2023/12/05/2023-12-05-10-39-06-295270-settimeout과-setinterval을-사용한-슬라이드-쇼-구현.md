---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 슬라이드 쇼 구현"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

많은 웹사이트에서 이미지나 콘텐츠를 자동으로 슬라이드하는 슬라이드 쇼를 본 적이 있을 것입니다. 이번 블로그에서는 JavaScript의 `setTimeout`과 `setInterval` 함수를 사용하여 간단한 슬라이드 쇼를 구현하는 방법을 알아보겠습니다.

## HTML 마크업

먼저, HTML에서 슬라이드 쇼에 사용될 이미지들을 감싸는 `div` 요소를 만들어야 합니다. 아래는 예시입니다.

```html
<div class="slideshow">
  <img src="image1.jpg">
  <img src="image2.jpg">
  <img src="image3.jpg">
</div>
```

## CSS 스타일링

다음으로, 슬라이드 쇼를 스타일링하기 위해 CSS를 사용합니다. 예시 코드는 아래와 같습니다.

```css
.slideshow {
  width: 500px;
  height: 300px;
  overflow: hidden;
}

.slideshow img {
  width: 100%;
  height: auto;
  opacity: 0;
  transition: opacity 1s ease;
}

.slideshow img.active {
  opacity: 1;
}
```

위의 CSS 코드는 슬라이드 쇼를 감싸는 `div` 요소를 `overflow: hidden`으로 설정하여 이미지들을 가려주고, 각 이미지들의 너비는 100%로 설정하여 부모 요소에 맞게 조절합니다. 이미지들은 `opacity` 속성을 사용하여 페이드 인/아웃 효과를 주기 위해 초기 값은 0으로 설정합니다.

## JavaScript 슬라이드 쇼 구현

이제, JavaScript 코드를 사용하여 슬라이드 쇼를 구현할 차례입니다. 아래는 예시 코드입니다.

```javascript
var slideshow = document.querySelector('.slideshow');
var images = slideshow.querySelectorAll('img');
var currentIndex = 0;

function showSlide(index) {
  // 현재 이미지 비활성화
  images[currentIndex].classList.remove('active');
  
  // 새로운 이미지 활성화
  images[index].classList.add('active');
  
  // 현재 인덱스 갱신
  currentIndex = index;
}

function nextSlide() {
  var newIndex = (currentIndex + 1) % images.length;
  showSlide(newIndex);
}

setInterval(nextSlide, 3000); // 3초마다 슬라이드 전환

// 초기 슬라이드 표시
showSlide(currentIndex);
```

위의 JavaScript 코드는 `slideshow` 클래스를 가진 요소에 속한 이미지들을 모두 선택하여 배열로 저장합니다. `showSlide` 함수는 현재 이미지를 비활성화하고 새로운 이미지를 활성화합니다. `nextSlide` 함수는 다음 슬라이드를 보여주는 역할을 합니다. `setInterval` 함수를 사용하여 3초마다 `nextSlide` 함수를 호출하여 슬라이드를 전환합니다. 마지막으로, 초기 슬라이드를 표시하기 위해 `showSlide` 함수를 호출합니다.

이제, 웹 브라우저에서 해당 HTML 파일을 열면 3초마다 슬라이드가 자동으로 전환되는 슬라이드 쇼를 볼 수 있습니다.

위의 예시 코드는 간단한 구현이며, 더 다양한 효과나 제어를 위해서는 추가적인 로직을 구현해야 합니다. 이 예시를 기반으로 필요한 기능을 추가하여 보다 복잡한 슬라이드 쇼를 구현해보세요.

자바스크립트 `setTimeout`과 `setInterval` 함수를 사용하여 슬라이드 쇼를 구현하는 방법을 알아보았습니다. 이를 응용하여 다양한 슬라이드 쇼를 만들어보세요!

## 참고 자료

- [MDN - WindowOrWorkerGlobalScope.setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN - WindowOrWorkerGlobalScope.setInterval()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)