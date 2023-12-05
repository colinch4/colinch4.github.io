---
layout: post
title: "[javascript] setTimeout과 setInterval의 차이점"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript에서 `setTimeout`과 `setInterval`은 두 가지 다른 시간 지연 메서드입니다. 각각의 기능과 사용 방법을 이해하는 것은 중요합니다. 이 글에서는 두 메서드의 차이점에 대해 설명하고 어떤 상황에서 어떻게 사용해야 하는지 알아보겠습니다.

## setTimeout
`setTimeout`은 일정한 시간 후에 한 번만 함수를 실행하는 메서드입니다. 즉, 일정한 시간 간격(interval)마다 함수가 실행되지 않습니다. 예를 들어, 다음과 같이 `setTimeout`을 사용하여 함수를 1초 후에 실행할 수 있습니다:

```javascript
setTimeout(() => {
  console.log("1초 후에 실행됩니다.");
}, 1000);
```

위의 코드는 1초 후에 `console.log("1초 후에 실행됩니다.")`를 실행합니다.

## setInterval
`setInterval`은 일정한 시간 간격으로 반복적으로 함수를 실행하는 메서드입니다. 즉, 설정한 시간 간격마다 함수가 실행됩니다. 예를 들어, 다음과 같이 `setInterval`을 사용하여 함수를 1초 간격으로 실행할 수 있습니다:

```javascript
let counter = 0;

const interval = setInterval(() => {
  console.log(`${counter}번째 실행`);
  counter++;

  if (counter === 5) {
    clearInterval(interval); // 5번 실행 후 setInterval 종료
  }
}, 1000);
```

위의 코드는 1초 간격으로 `console.log()`를 실행하고, `counter`를 증가시킵니다. `counter`가 5가 될 때 `clearInterval(interval)`을 호출하여 `setInterval`을 멈춥니다.

## 언제 어떻게 사용해야 할까요?
- `setTimeout`은 한 번만 함수를 실행하고 싶을 때 유용합니다. 예를 들어, 클릭 이벤트 후에 알림 메시지를 표시하거나, 페이지가 로드된 후에 초기화 작업을 수행할 때 사용할 수 있습니다.

- `setInterval`은 주기적으로 함수를 실행하고 싶을 때 유용합니다. 예를 들어, 실시간 데이터를 업데이트하거나 애니메이션을 구현할 때 사용할 수 있습니다. 그러나 `setInterval`을 사용할 때는 주의해야 합니다. 사소한 실수로 인해 메모리 누수(memory leak)가 발생할 수 있으므로, `clearInterval`을 적절하게 사용하여 중지시키는 것이 중요합니다.

## 결론
`setTimeout`과 `setInterval`은 JavaScript에서 시간 기반 함수를 사용하는 두 가지 메서드입니다. `setTimeout`은 한 번만 함수를 실행하고, `setInterval`은 주기적으로 함수를 반복 실행합니다. 각각의 기능과 사용 방법을 이해하고 적절하게 사용하여 원하는 동작을 구현할 수 있습니다.