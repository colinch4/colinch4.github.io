---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 성능 개선 방법"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript에서는 `setTimeout`과 `setInterval`을 사용하여 비동기적인 작업을 수행할 수 있습니다. 그러나 이러한 함수들을 잘못 사용하면 성능 문제가 발생할 수 있으며, 이를 개선하기 위해 몇 가지 방법을 살펴보겠습니다.

## 1. 적절한 딜레이 값을 설정하기

`setTimeout`과 `setInterval`의 첫 번째 인수로 전달하는 딜레이 값은 실행 간격을 결정합니다. 너무 작은 딜레이 값은 불필요한 호출을 유발하며, 너무 큰 딜레이 값은 반응성을 떨어뜨릴 수 있습니다. 따라서 적절한 딜레이 값을 설정해야 합니다. 예를 들어, 애니메이션을 구현할 때는 16ms(60FPS)를 딜레이 값으로 사용하는 것이 좋습니다.

```javascript
setTimeout(() => {
  // 실행할 작업
}, 16);
```

## 2. setInterval 대신 setTimeout 사용하기

`setInterval`은 정해진 시간 간격으로 함수를 반복 실행합니다. 그러나 첫 번째 실행 이후의 반복 실행 간격이 정확하지 않을 수 있습니다. 이를 해결하기 위해 `setInterval` 대신 재귀적으로 `setTimeout`을 사용하는 방법을 고려해보세요. 이렇게 하면 이전 호출이 완료된 후 정확히 지정된 딜레이 이후에 함수가 호출됩니다.

```javascript
function repeatTask() {
  // 실행할 작업

  setTimeout(repeatTask, 1000);
}

setTimeout(repeatTask, 1000); // 초기 호출
```

## 3. clear함수를 활용하여 정확한 제어하기

`setTimeout`이나 `setInterval`을 사용한 이후에 제어를 해제하기 위해 `clearTimeout`, `clearInterval` 함수를 사용하세요. 이러한 함수들은 타이머를 취소하고 실행을 중지시킵니다. 만약 작업이 완료된 후에 타이머를 중지시키기 위해 `clearTimeout` 또는 `clearInterval` 함수를 사용하지 않으면, 메모리 누수와 같은 문제가 발생할 수 있습니다.

```javascript
const timerId = setTimeout(() => {
  // 실행할 작업
}, 1000);

// 실행을 중지시키려면 아래와 같이 clearTimeout 함수를 사용합니다.
clearTimeout(timerId);
```

## 결론

`setTimeout`과 `setInterval`은 JavaScript에서 매우 유용한 함수입니다. 그러나 사용 방법을 신중히 고려해야 합니다. 적절한 딜레이 값을 설정하고, `setInterval`보다는 `setTimeout`을 사용하며, 타이머 실행을 중지시키기 위해 `clearTimeout` 또는 `clearInterval` 함수를 활용하는 등의 방법을 적용하여 성능 문제를 해결할 수 있습니다.

## 참고문서
- [setTimeout - MDN Web Docs](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [setInterval - MDN Web Docs](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)