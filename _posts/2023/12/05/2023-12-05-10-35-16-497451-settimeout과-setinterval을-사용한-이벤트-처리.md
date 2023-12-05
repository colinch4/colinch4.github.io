---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 이벤트 처리"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

웹 개발을 하다 보면 특정 시간 후에 작업을 수행하거나 일정한 간격으로 반복적인 작업을 수행해야 하는 경우가 있습니다. 이때 JavaScript에서 제공하는 setTimeout과 setInterval 함수를 사용하여 이벤트를 처리할 수 있습니다.

## setTimeout 함수

setTimeout 함수는 일정 시간 후에 한 번만 작업을 실행합니다. setTimeout 함수는 다음과 같은 형식으로 사용할 수 있습니다.

```javascript
setTimeout(function, delay);
```

- `function`: 실행할 함수를 정의합니다.
- `delay`: 함수를 실행하기까지의 지연 시간을 밀리초(ms) 단위로 지정합니다.

예를 들어, 3초 후에 "Hello, World!"라는 메시지를 콘솔에 출력하고 싶다면 다음과 같이 setTimeout 함수를 사용할 수 있습니다.

```javascript
setTimeout(function() {
    console.log("Hello, World!");
}, 3000);
```

## setInterval 함수

setInterval 함수는 일정한 간격으로 작업을 반복적으로 실행합니다. setInterval 함수는 다음과 같은 형식으로 사용할 수 있습니다.

```javascript
setInterval(function, delay);
```

- `function`: 실행할 함수를 정의합니다.
- `delay`: 각 작업 간의 지연 시간을 밀리초(ms) 단위로 지정합니다.

예를 들어, 1초마다 현재 시간을 콘솔에 출력하고 싶다면 다음과 같이 setInterval 함수를 사용할 수 있습니다.

```javascript
setInterval(function() {
    console.log(new Date());
}, 1000);
```

## clearTimeout과 clearInterval 함수

setTimeout과 setInterval 함수는 실행 후에 해당 작업의 식별자를 반환합니다. 이 식별자를 사용하여 작업을 중지할 수 있습니다. clearTimeout 함수와 clearInterval 함수를 사용하면 각각 setTimeout과 setInterval로 설정한 작업을 중지할 수 있습니다.

예를 들어, setTimeout 함수를 사용하여 3초 후에 메시지를 출력하는 작업을 실행했지만 2초 후에 작업을 중지하고 싶다면 다음과 같이 clearTimeout 함수를 사용할 수 있습니다.

```javascript
var timer = setTimeout(function() {
    console.log("Hello, World!");
}, 3000);

setTimeout(function() {
    clearTimeout(timer);
}, 2000);
```

위와 같은 방식으로 setInterval 함수로 설정한 작업을 중지하려면 clearInterval 함수를 사용하면 됩니다.

## 마무리

setTimeout과 setInterval 함수는 JavaScript에서 비동기적인 작업을 처리할 때 유용한 기능입니다. 이 함수들을 적절히 이용하면 웹 애플리케이션에서 다양한 이벤트를 효과적으로 처리할 수 있습니다.