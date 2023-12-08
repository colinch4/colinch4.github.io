---
layout: post
title: "[javascript] setTimeout과 setInterval의 최적화 방법"
description: " "
date: 2023-12-08
tags: [javascript]
comments: true
share: true
---

JavaScript에서 `setTimeout`과 `setInterval`은 일정 시간 후에 코드를 실행하거나 주기적으로 코드를 실행할 수 있게 해줍니다. 하지만 이러한 함수들은 과도한 사용으로 인해 성능 문제를 발생시킬 수 있습니다. 

우리는 코드를 실행하고 성능을 최적화하기 위해 `setTimeout`과 `setInterval`을 적절히 사용하는 방법에 대해 알아볼 것입니다.

## 1. `setTimeout`과 `setInterval`를 적게 사용하기
`setTimeout`과 `setInterval`를 사용할 때,  너무 빈번하게 호출하는 것은 좋지 않습니다. 이는 브라우저의 성능에 부담을 주게 됩니다. 대신, 가능하면 최소한으로 사용하고 코드를 최적화해야 합니다. 

## 2. `setTimeout`과 `setInterval`을 취소하기
`setTimeout`과 `setInterval`을 더 이상 필요하지 않을 때에는 해제하여야 합니다. 이것은 불필요한 작업을 줄여주고 메모리 누수를 방지합니다. 다음은 `setTimeout`를 해제하는 예제입니다.

```javascript
const timerId = setTimeout(function() {
  // 실행할 코드
}, 1000);

// 타이머 해제
clearTimeout(timerId);
```

## 3. `requestAnimationFrame` 사용하기
`setInterval` 대신 `requestAnimationFrame`을 사용하는 것이 더 효율적일 수 있습니다. `requestAnimationFrame`은 브라우저의 다음 리페인팅이 일어나기 직전에 실행되기 때문에 애니메이션 및 인터랙티브 웹 앱을 개발할 때 유용합니다.

## 4. 작업을 배치하기
연속적으로 발생하는 이벤트나 작업에 대해 여러 개의 `setTimeout`을 사용하는 대신, 작업을 배치하여 한꺼번에 처리하는 것이 더 효율적입니다. 

## 5. 성능 모니터링
마지막으로, 코드를 변경하고 최적화한 후에도 여전히 성능 문제가 있는지 계속해서 모니터링해야 합니다. 웹 브라우저의 개발자 도구를 사용하여 CPU 및 메모리 사용량 등을 확인하고 성능 모니터링을 진행해야 합니다.

`setTimeout`과 `setInterval`을 사용할 때 위의 내용을 고려하면서 최적화된 코드를 작성할 수 있을 것입니다. 성능을 중시하면서 코드를 작성하고, 필요하다면 대안적인 방법을 고려하여 성능을 향상시키는 것이 중요합니다.

- 참고 문서: [MDN Web Docs](https://developer.mozilla.org/ko/)