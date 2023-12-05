---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 실시간 데이터 처리"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

JavaScript는 동적인 웹 애플리케이션을 만들 때 많이 사용되는 스크립트 언어입니다. 특히 실시간 데이터 처리를 위해 setTimeout과 setInterval 함수를 사용할 수 있습니다. 이 둘은 비동기적으로 코드를 실행하는 방법을 제공합니다.

## setTimeout 함수

setTimeout 함수는 일정한 시간 후에 한 번만 특정 코드를 실행하고자 할 때 사용됩니다. 다음은 setTimeout 함수를 사용한 예제입니다.

```javascript
setTimeout(() => {
    console.log('1초 후에 실행되는 코드');  
}, 1000);
```

위 예제에서 setTimeout 함수는 1초 후에 주어진 콜백 함수를 실행합니다. 따라서 '1초 후에 실행되는 코드'라는 메시지가 콘솔에 출력됩니다.

## setInterval 함수

setInterval 함수는 일정한 시간 간격으로 특정 코드를 반복적으로 실행하고자 할 때 사용됩니다. 다음은 setInterval 함수를 사용한 예제입니다.

```javascript
let count = 0;

let intervalId = setInterval(() => {
    count++;
    console.log('현재 count 값:', count);

    if (count >= 5) {
        clearInterval(intervalId);
        console.log('count가 5 이상이 되어 setInterval이 중지되었습니다.');
    }
}, 1000);
```

위 예제에서 setInterval 함수는 1초 간격으로 count 값을 증가시키고, 현재 count 값을 출력합니다. count가 5 이상이 되면 clearInterval 함수를 사용하여 setInterval을 중지합니다.

## setTimeout과 setInterval의 차이점

setTimeout 함수는 한 번만 실행되고 종료되지만, setInterval 함수는 주어진 시간 간격마다 반복적으로 실행됩니다. 따라서 실시간 데이터를 처리할 때는 필요에 맞는 함수를 선택하여 사용해야 합니다.

## 결론

JavaScript에서 실시간 데이터를 처리하기 위해 setTimeout과 setInterval 함수를 사용할 수 있습니다. setTimeout은 일정 시간 후 단 한 번만 코드를 실행할 때 사용되고, setInterval은 일정 시간 간격으로 코드를 반복실행할 때 사용됩니다. 이 두 함수를 적절히 활용하여 웹 애플리케이션에서 원하는 동작을 구현할 수 있습니다.

## 참고 자료
- [JavaScript Timers](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN Web Docs: setInterval](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)