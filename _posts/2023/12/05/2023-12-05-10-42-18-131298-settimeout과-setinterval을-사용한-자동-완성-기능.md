---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 자동 완성 기능"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

이번 포스트에서는 JavaScript의 setTimeout과 setInterval 함수를 사용하여 자동 완성 기능을 구현하는 방법에 대해 알아보겠습니다.

## 1. setTimeout 함수란?

setTimeout 함수는 주어진 시간이 지난 후에 한 번만 실행되는 함수입니다. 다음은 setTimeout 함수의 사용 예시입니다.

```javascript
setTimeout(function() {
  console.log('이 함수는 1초 후에 실행됩니다.');
}, 1000);
```

위의 코드에서는 setTimeout 함수를 사용하여 1초 후에 console.log 함수를 실행하고 있습니다.

## 2. setInterval 함수란?

setInterval 함수는 주어진 시간 간격으로 반복해서 실행되는 함수입니다. 다음은 setInterval 함수의 사용 예시입니다.

```javascript
var count = 0;
var intervalId = setInterval(function() {
  count++;
  console.log(count);
}, 1000);
```

위의 코드에서 setInterval 함수를 사용하여 1초마다 count 변수를 증가시키고, 현재 count 값을 출력하고 있습니다.

## 3. 자동 완성 기능 구현하기

setTimeout과 setInterval 함수를 사용하여 자동 완성 기능을 구현하는 방법을 알아보겠습니다. 자동 완성 기능은 사용자가 입력한 텍스트에 대해 일정 시간이 경과된 후에 자동으로 완성된 결과를 보여주는 기능입니다.

```javascript
var inputElement = document.getElementById('input');
var resultElement = document.getElementById('result');

var timeoutId;
inputElement.addEventListener('input', function() {
  clearTimeout(timeoutId);
  
  timeoutId = setTimeout(function() {
    // 입력된 텍스트를 기반으로 자동 완성된 결과를 계산하는 로직을 작성합니다.
    var result = inputElement.value + ' 자동 완성 결과';
    resultElement.textContent = result;
  }, 1000);
});
```

위의 코드에서는 input 요소의 입력 이벤트에 대한 리스너를 등록하여 사용자가 텍스트를 입력할 때마다 clearTimeout 함수를 호출하여 이전의 setTimeout을 취소합니다. 그리고 setTimeout 함수를 사용하여 일정 시간이 경과된 후에 자동 완성 결과를 계산하고, 결과를 resultElement에 표시합니다.

## 4. 결론

JavaScript의 setTimeout과 setInterval 함수를 사용하면 일정 시간이 지난 후에 코드를 실행하거나 반복해서 실행할 수 있습니다. 이를 활용하여 자동 완성 기능을 구현할 수 있습니다. 다른 이벤트와 조합하여 다양한 기능을 구현할 수 있으니, 창의적인 활용 방법을 고민해보시기 바랍니다.

**참고 자료:**

- [MDN Web Docs - setTimeout](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs - setInterval](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)