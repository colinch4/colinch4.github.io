---
layout: post
title: "requestAnimationFrame을 사용한 자바스크립트 피버 애니메이션 만들기"
description: " "
date: 2023-10-18
tags: [javascript]
comments: true
share: true
---

애니메이션은 웹 개발에서 매우 중요한 요소 중 하나입니다. 움직이는 그림이나 효과를 추가하여 웹 페이지를 더 생동감 있게 만들 수 있습니다. 이번 포스팅에서는 자바스크립트의 `requestAnimationFrame` 메서드를 사용하여 간단한 피버 애니메이션을 만드는 방법을 알아보겠습니다. 

## requestAnimationFrame란?

`requestAnimationFrame`은 웹 브라우저가 애니메이션에 적합한 주기로 화면을 다시 그리도록 알려주는 메서드입니다. 웹 브라우저의 내부 타이머에 의해 호출되며, 사용자의 디스플레이 주사율에 맞게 최적화되어 동작합니다. 이를 사용하면 부드러운 애니메이션을 만들 수 있습니다.

## 예제 코드

```javascript
// 캔버스 엘리먼트 생성
const canvas = document.createElement("canvas");
const ctx = canvas.getContext("2d");
document.body.appendChild(canvas);

// 캔버스 크기 조절
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// 피버 애니메이션 구현
function draw() {
  // 캔버스 초기화
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // 각각의 원 그리기
  for (let i = 0; i < 100; i++) {
    // 원의 위치 및 속도 설정
    const x = Math.random() * canvas.width;
    const y = Math.random() * canvas.height;
    const speed = Math.random() * 5 + 1;

    // 원 그리기
    ctx.beginPath();
    ctx.arc(x, y, 10, 0, Math.PI * 2);
    ctx.fillStyle = "red";
    ctx.fill();
    ctx.closePath();

    // 원의 위치 업데이트
    y += speed;
  }

  // 애니메이션 반복 호출
  requestAnimationFrame(draw);
}

// 애니메이션 시작
draw();
```

위 예제 코드는 `requestAnimationFrame`을 사용하여 캔버스에 무작위로 움직이는 100개의 빨간색 원을 그리는 피버 애니메이션을 구현한 것입니다. `draw` 함수에서는 매번 원을 그리고 그 위치를 갱신하여 애니메이션이 부드럽게 동작하도록 합니다. `requestAnimationFrame`을 사용하면 브라우저의 화면 갱신 주기에 맞게 애니메이션을 업데이트할 수 있습니다.

## 마치며

`requestAnimationFrame`을 사용하면 자바스크립트로 간단한 애니메이션을 만드는 것이 가능해집니다. 이를 활용하여 보다 생동감있는 웹 페이지를 구현할 수 있습니다. 애니메이션은 사용자 경험을 향상시키고 웹 페이지의 시각적 효과를 더욱 돋보이게 만들어줍니다. 자세한 내용은 [MDN 문서](https://developer.mozilla.org/ko/docs/Web/API/Window/requestAnimationFrame)를 참고하세요. #JavaScript #애니메이션