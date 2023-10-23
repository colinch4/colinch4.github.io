---
layout: post
title: "requestAnimationFrame을 사용한 자바스크립트 타임라인 애니메이션 만들기"
description: " "
date: 2023-10-18
tags: [javascript]
comments: true
share: true
---

## 목차
- [개요](#개요)
- [requestAnimationFrame](#requestAnimationFrame)
- [타임라인 애니메이션 구현](#타임라인-애니메이션-구현)
- [결론](#결론)

## 개요
자바스크립트를 사용하여 웹 페이지에 애니메이션을 구현하는 경우, 일반적으로 `setTimeout`이나 `setInterval` 함수를 사용합니다. 그러나 이들 함수는 정확한 타이밍으로 애니메이션을 업데이트하기 어렵고, 성능 문제가 발생할 수 있습니다. 이를 해결하기 위해 `requestAnimationFrame`이라는 새로운 API가 도입되었습니다.

`requestAnimationFrame`은 브라우저에게 다음 프레임을 그리기 전에 애니메이션을 업데이트하라고 알리는 함수입니다. 이 함수는 모니터의 주사율에 맞춰 최적화된 갱신 주기를 선택하여 애니메이션을 부드럽게 처리합니다.

## requestAnimationFrame
`requestAnimationFrame` 함수는 콜백 함수를 인자로 받으며, 다음 프레임을 그리기 전에 호출됩니다. 콜백 함수는 `DOMHighResTimeStamp` 매개변수를 받아 사용할 수 있는데, 이는 애니메이션 시작부터 흐른 시간을 나타냅니다.

```javascript
function updateAnimation(timestamp) {
  // 애니메이션 업데이트 로직을 구현합니다.
  // ...
  
  requestAnimationFrame(updateAnimation);
}

requestAnimationFrame(updateAnimation);
```

위 코드에서 `updateAnimation` 함수는 애니메이션을 업데이트하는 로직을 구현하는 함수입니다. 이 함수는 `requestAnimationFrame`을 다시 호출함으로써 애니메이션을 반복적으로 업데이트합니다.

## 타임라인 애니메이션 구현
아래는 `requestAnimationFrame`을 사용하여 간단한 타임라인 애니메이션을 구현하는 예제입니다. 이 예제는 `div` 요소의 위치를 일정한 간격으로 변경하여 애니메이션을 만듭니다.

```javascript
const element = document.getElementById('animated-element');
let positionX = 0;

function updatePosition(timestamp) {
  positionX += 1; // X축 방향으로 1씩 이동
  element.style.transform = `translateX(${positionX}px)`;

  if (positionX < 200) { // X축 이동이 200px 이전까지 반복
    requestAnimationFrame(updatePosition);
  }
}

requestAnimationFrame(updatePosition);
```

위 코드에서는 `updatePosition` 함수가 `requestAnimationFrame`을 호출하여 반복적으로 실행됩니다. `positionX` 변수를 이용하여 요소의 위치를 변경하고, `translateX` 속성을 사용하여 애니메이션을 적용합니다. 애니메이션이 일정한 범위까지 반복하도록 `if` 문을 사용하여 조건을 설정합니다.

## 결론
`requestAnimationFrame`을 사용하면 효율적이고 부드러운 웹 애니메이션을 구현할 수 있습니다. 이를 이용하여 다양한 타임라인 애니메이션을 만들어 웹 페이지를 화려하게 꾸밀 수 있습니다. 추가로, `cancelAnimationFrame` 함수를 사용하여 애니메이션을 중지할 수도 있습니다.

자세한 내용은 [MDN Web Docs](https://developer.mozilla.org/ko/docs/Web/API/Window/requestAnimationFrame)를 참조해주세요.

#javascript #애니메이션