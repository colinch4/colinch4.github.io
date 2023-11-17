---
layout: post
title: "requestAnimationFrame을 이용한 반짝이는 애니메이션 만들기"
description: " "
date: 2023-10-18
tags: [javascript]
comments: true
share: true
---

이번 포스트에서는 JavaScript의 requestAnimationFrame 메서드를 사용하여 반짝이는 애니메이션을 만드는 방법을 알아보겠습니다.

## 1. requestAnimationFrame 이란?

requestAnimationFrame은 웹 브라우저가 다음 리페인트(repaint)를 수행하기 전에 애니메이션을 업데이트하기 위해 호출하는 메서드입니다. 이 메서드는 브라우저가 최적화된 타이밍으로 애니메이션을 처리할 수 있도록 도와줍니다.

## 2. 예제 코드

아래는 requestAnimationFrame을 사용하여 반짝이는 애니메이션을 만드는 예제 코드입니다.

```javascript
<!DOCTYPE html>
<html>
<head>
  <style>
    .box {
      width: 100px;
      height: 100px;
      background-color: red;
    }
  </style>
</head>
<body>
  <div class="box"></div>

  <script>
    const box = document.querySelector('.box');
    let increasing = true;
    let opacity = 0;

    function animate() {
      if (increasing) {
        opacity += 0.01;
      } else {
        opacity -= 0.01;
      }

      if (opacity >= 1) {
        increasing = false;
      } else if (opacity <= 0) {
        increasing = true;
      }

      box.style.opacity = opacity;

      requestAnimationFrame(animate);
    }

    animate();
  </script>
</body>
</html>
```

위의 예제 코드는 CSS 스타일 시트를 이용하여 `.box` 클래스의 사각형 요소를 만들고, JavaScript를 통해 `animate` 함수를 호출하여 애니메이션 효과를 구현합니다. `animate` 함수에서는 `opacity` 값을 증가 또는 감소시켜 요소의 투명도를 조절하고, `requestAnimationFrame`을 통해 애니메이션을 반복적으로 업데이트합니다.

## 3. 결과 확인

위의 코드를 웹 브라우저에서 실행하면, 사각형이 부드럽게 반짝이는 애니메이션 효과를 보여줍니다. `opacity` 변수를 조절함으로써 애니메이션의 속도나 효과를 변화시킬 수 있습니다.

## 4. 결론

이번 포스트에서는 `requestAnimationFrame`을 이용하여 반짝이는 애니메이션을 만드는 방법을 살펴보았습니다. 이 메서드를 사용하면 웹 애니메이션의 성능을 향상시킬 수 있으며, 부드럽고 자연스러운 애니메이션 효과를 구현할 수 있습니다.

자세한 내용은 [MDN web docs](https://developer.mozilla.org/ko/docs/Web/API/Window/requestAnimationFrame)를 참고해주세요.

#애니메이션 #requestAnimationFrame