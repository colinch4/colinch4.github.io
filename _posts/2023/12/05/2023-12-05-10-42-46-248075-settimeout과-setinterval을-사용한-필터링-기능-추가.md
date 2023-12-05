---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 필터링 기능 추가"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

1. [서론](#서론)
2. [필터링 기능 개요](#필터링-기능-개요)
3. [setTimeout과 setInterval 설명](#setTimeout과-setInterval-설명)
4. [필터링 기능 구현](#필터링-기능-구현)
5. [결론](#결론)

## 서론

이번 포스트에서는 JavaScript의 `setTimeout`과 `setInterval` 함수를 사용하여 필터링 기능을 추가하는 방법에 대해 알아보겠습니다. 필터링 기능은 많은 웹 애플리케이션에서 사용되며, 사용자의 입력에 따라 원하는 결과만 표시하는 기능입니다.

## 필터링 기능 개요

필터링 기능은 사용자가 입력한 값을 기준으로 데이터를 필터링하여 화면에 표시합니다. 이를 위해 필터링할 값을 사용자로부터 입력받고, 입력 값이 변경될 때마다 필터링을 적용해야 합니다. 이때, `setTimeout`과 `setInterval` 함수를 사용하여 일정 시간동안 사용자의 입력을 대기하고, 입력 값이 변경되지 않으면 필터링을 적용하는 방법을 사용할 수 있습니다.

## setTimeout과 setInterval 설명

`setTimeout` 함수는 지정된 시간이 지난 후에 한 번만 실행되는 함수입니다. 예를 들어, `setTimeout(func, delay)` 형식으로 사용하면 `delay` 시간이 지난 후에 `func` 함수가 실행됩니다.

`setInterval` 함수는 지정된 시간 간격으로 반복적으로 함수를 실행하는 함수입니다. 예를 들어, `setInterval(func, interval)` 형식으로 사용하면 `interval` 시간 간격으로 계속해서 `func` 함수가 실행됩니다. 이때, 필요에 따라 실행 횟수를 제한할 수도 있습니다.

## 필터링 기능 구현

이제 `setTimeout`과 `setInterval` 함수를 사용하여 필터링 기능을 구현해보겠습니다. 아래 예시 코드는 사용자가 입력한 값을 기반으로 필터링된 데이터를 화면에 표시하는 예입니다.

```javascript
// 필터링할 데이터 배열
const data = ['apple', 'banana', 'cherry', 'grape', 'orange'];

// 사용자 입력값 저장 변수
let userInput = '';

// 필터링 함수
function filterData() {
  const filteredData = data.filter(item => item.includes(userInput));
  // 필터링된 데이터를 화면에 표시하는 코드 추가
  console.log(filteredData);
}

// 사용자 입력 값이 변경되었을 때 필터링 함수 실행
function handleInputChange() {
  setTimeout(filterData, 500);
}

// 사용자 입력 창에 이벤트 리스너 추가
document.getElementById('input').addEventListener('input', handleInputChange);
```

위 코드에서 `filterData` 함수는 `data` 배열을 사용자의 입력값을 기준으로 필터링한 후, 필터링된 데이터를 화면에 표시하는 역할을 합니다. `handleInputChange` 함수는 사용자의 입력값이 변경되었을 때 `filterData` 함수를 500ms 후에 실행하도록 설정합니다.

## 결론

이번 포스트에서는 JavaScript의 `setTimeout`과 `setInterval` 함수를 사용하여 필터링 기능을 추가하는 방법을 알아보았습니다. 이러한 방법을 사용하면 사용자의 입력이 변경될 때마다 필터링을 적용할 수 있어, 보다 동적인 웹 애플리케이션을 구현할 수 있습니다. 필터링 기능은 다양한 웹 애플리케이션에서 사용되므로, 유용한 기술입니다.

## 참고 자료

- [MDN web docs - setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN web docs - setInterval()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)
- [w3schools - JavaScript Timing Events](https://www.w3schools.com/js/js_timing.asp)