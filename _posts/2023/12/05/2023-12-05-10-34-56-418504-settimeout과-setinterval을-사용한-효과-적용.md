---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 효과 적용"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript는 setTimeout과 setInterval 함수를 사용하여 웹 페이지에 효과적인 동작을 적용할 수 있습니다. setTimeout 함수는 일정 시간이 지난 후에 특정 함수를 실행하며, setInterval 함수는 일정 시간 간격으로 반복적으로 특정 함수를 실행합니다. 이러한 함수들을 활용하여 다양한 효과를 만들어보겠습니다.

## setTimeout을 사용한 효과

```javascript
setTimeout(() => {
  // 해당 함수 안에 원하는 효과를 작성합니다.
}, 2000);
```

위의 예제 코드에서 `() => { ... }`은 실행하고자 하는 함수를 익명으로 정의한 것입니다. setTimeout 함수는 첫 번째 인자로 전달된 함수를 두 번째 인자로 전달된 시간(밀리초 단위)만큼 지난 후에 실행합니다. 따라서 위 예제 코드는 2초(2000밀리초)가 지나면 해당 함수가 실행되게 됩니다.

## setInterval을 사용한 효과

```javascript
setInterval(() => {
  // 해당 함수 안에 원하는 효과를 작성합니다.
}, 1000);
```

위의 예제 코드는 setInterval 함수를 사용하여 1초(1000밀리초)마다 해당 함수를 실행하는 방식을 보여줍니다. setInterval 함수는 setTimeout 함수와 동일한 방식으로 동작하지만, 전달된 함수를 일정 간격으로 반복해서 실행합니다.

## clearInterval을 사용하여 실행 중단하기

일정 시간 간격으로 효과를 반복 실행하고자 할 때, clearInterval 함수를 사용하여 실행을 중단할 수 있습니다. setTimeout과 setInterval 함수는 실행 시에 고유한 ID를 반환하는데, 이 ID를 활용하여 중단할 수 있습니다.

```javascript
const intervalId = setInterval(() => {
  // 해당 함수 안에 원하는 효과를 작성합니다.
}, 1000);

// 특정 조건이 만족되면 실행 중단
if (조건) {
  clearInterval(intervalId);
}
```

위의 예제 코드에서는 setInterval 함수가 실행될 때 반환된 ID를 변수 `intervalId`에 저장하였습니다. 특정 조건이 만족되면 clearInterval 함수를 사용하여 실행을 중단하는 방법을 보여주고 있습니다.

위에서는 setTimeout과 setInterval 함수를 간단하게 사용한 예제를 보여주었지만, 이러한 함수들을 활용하여 애니메이션, 자동 변경 등 다양한 효과를 적용할 수 있습니다. 자세한 내용은 [MDN 문서](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)를 참고하시기 바랍니다.