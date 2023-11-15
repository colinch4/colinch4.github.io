---
layout: post
title: "requestAnimationFrame을 사용한 자바스크립트 선발동안 애니메이션 만들기"
description: " "
date: 2023-10-18
tags: [javascript]
comments: true
share: true
---

애니메이션은 사용자 경험을 향상시키는 데에 매우 유용한 요소입니다. 자바스크립트를 사용하여 웹 페이지에 애니메이션을 만드는 방법은 여러 가지가 있지만, requestAnimationFrame을 사용하는 것이 가장 효율적입니다. requestAnimationFrame은 웹 브라우저의 리페인트 주기에 맞춰 애니메이션을 업데이트할 수 있는 API입니다.

## requestAnimationFrame 개요

requestAnimationFrame은 웹 브라우저가 화면을 갱신하기 전에 호출할 함수를 등록하는 역할을 합니다. 이 함수는 브라우저의 리페인트 주기에 맞춰 호출되므로, 애니메이션을 부드럽게 업데이트할 수 있습니다. 또한, 애니메이션 재생 중에 사용자가 다른 탭으로 이동하거나 페이지를 숨겼을 때, requestAnimationFrame은 자동으로 일시 중지되어 불필요한 계산 자원을 아낄 수 있습니다.

## requestAnimationFrame을 사용한 애니메이션 만들기

다음은 자바스크립트를 사용하여 requestAnimationFrame을 활용한 간단한 애니메이션 예시입니다. 이 예시는 화면에 원을 그려 움직이는 애니메이션을 구현합니다.

```javascript
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

let posX = 0;
const velocity = 2;

function drawCircle(x) {
  context.clearRect(0, 0, canvas.width, canvas.height);
  context.beginPath();
  context.arc(x, canvas.height / 2, 50, 0, 2 * Math.PI);
  context.fillStyle = 'blue';
  context.fill();
  context.closePath();
}

function animate() {
  posX += velocity;
  
  if (posX > canvas.width) {
    posX = 0;
  }
  
  drawCircle(posX);
  
  requestAnimationFrame(animate);
}

animate();
```

이 코드에서는 `canvas` 엘리먼트를 사용하여 애니메이션을 렌더링합니다. `drawCircle` 함수는 매 프레임마다 원을 그리는 역할을 하며, `animate` 함수는 프레임마다 호출되어 원의 위치를 업데이트하고 다시 그립니다. `requestAnimationFrame(animate)`은 다음 프레임이 그려지기 전에 `animate` 함수를 호출하도록 스케줄링합니다.

이 예시를 실행하면 웹 페이지에 움직이는 원이 그려지는 애니메이션을 확인할 수 있습니다.

## 마무리

requestAnimationFrame을 활용하여 자바스크립트 애니메이션을 만들면 부드럽고 효율적으로 애니메이션을 제어할 수 있습니다. 이를 통해 웹 페이지의 사용자 경험을 향상시킬 수 있습니다. 자바스크립트로 애니메이션을 구현하는 경우 requestAnimationFrame을 사용하는 것을 권장합니다.

References:
- [requestAnimationFrame - MDN Web Docs](https://developer.mozilla.org/ko/docs/Web/API/Window/requestAnimationFrame)