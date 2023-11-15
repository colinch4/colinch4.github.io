---
layout: post
title: "requestAnimationFrame으로 애니메이션 제어하기"
description: " "
date: 2023-10-18
tags: [javascript]
comments: true
share: true
---

애니메이션은 웹 개발에서 많이 사용되는 기능 중 하나입니다. JavaScript를 이용하여 애니메이션을 제어할 때, requestAnimationFrame 메소드를 사용하면 브라우저의 성능을 더욱 효율적으로 활용할 수 있습니다. 이를 활용하여 애니메이션을 부드럽게 제어하는 방법을 알아보겠습니다.

## requestAnimationFrame이란?
`requestAnimationFrame`은 브라우저에게 애니메이션을 수행하고자 한다는 것을 알리는 메소드입니다. 이 메소드는 브라우저의 리플로우(reflow)와 리페인트(repaint) 주기에 맞게 애니메이션 프레임을 업데이트합니다. 이로 인해 부드러운 애니메이션 효과를 구현할 수 있습니다.

## requestAnimationFrame 사용법
requestAnimationFrame에 콜백 함수를 전달하여 애니메이션을 제어할 수 있습니다. 콜백 함수는 브라우저가 각 프레임을 그릴 때마다 호출됩니다.

```javascript
function animate() {
  // 애니메이션 로직 실행

  requestAnimationFrame(animate);
}

animate();
```

위의 코드에서 `animate` 함수는 애니메이션의 로직을 실행하는 함수입니다. 이 함수 내부에서는 애니메이션을 수행할 요소의 스타일을 업데이트하거나 변화시키는 작업을 수행합니다. 그리고 `requestAnimationFrame` 메소드를 호출하여 다음 프레임을 요청합니다. 이렇게 함으로써 브라우저는 다음 프레임을 그리기 전에 콜백 함수를 실행하도록 설정합니다.

## 애니메이션 제어
애니메이션을 제어할 때에는 `requestAnimationFrame`의 호출을 조건문과 결합하여 원하는 타이밍에 애니메이션을 실행하거나 중지할 수 있습니다. 예를 들어, 특정 조건이 충족되었을 때 애니메이션을 실행하고자 한다면 다음과 같은 방법을 사용할 수 있습니다.

```javascript
let shouldAnimate = false;

function startAnimation() {
  shouldAnimate = true;
  animate();
}

function stopAnimation() {
  shouldAnimate = false;
}

function animate() {
  if (shouldAnimate) {
    // 애니메이션 로직 실행

    requestAnimationFrame(animate);
  }
}
```

위의 코드에서 `shouldAnimate` 변수를 사용하여 애니메이션을 제어하고 있습니다. `startAnimation` 함수를 호출하면 `shouldAnimate` 변수가 true로 설정되고, 이후 `animate` 함수가 다시 호출되며 애니메이션이 실행됩니다. `stopAnimation` 함수를 호출하면 `shouldAnimate` 변수가 false로 설정되어 애니메이션을 중지시킬 수 있습니다.

## 요약
requestAnimationFrame 메소드를 사용하여 웹 애니메이션을 부드럽게 제어할 수 있습니다. 콜백 함수를 활용하여 애니메이션 로직을 구현하고, 요소의 스타일을 업데이트하거나 변화시킵니다. 조건문을 활용하여 애니메이션의 실행과 중지를 제어할 수 있습니다. 이를 활용하여 다양한 유형의 웹 애니메이션을 구현할 수 있습니다.

더 많은 자세한 내용은 [MDN web docs](https://developer.mozilla.org/ko/docs/Web/API/window/requestAnimationFrame)를 참고하십시오.

\#JavaScript \#Animation