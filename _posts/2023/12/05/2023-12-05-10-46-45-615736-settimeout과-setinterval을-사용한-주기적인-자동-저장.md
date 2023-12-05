---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 주기적인 자동 저장"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

웹 애플리케이션을 개발하다 보면, 사용자의 작업을 주기적으로 자동으로 저장해야 하는 경우가 있습니다. 이를 위해 JavaScript의 setTimeout과 setInterval 함수를 사용할 수 있습니다. 이 블로그 포스트에서는 setTimeout과 setInterval을 사용하여 주기적인 자동 저장을 구현하는 방법을 알아보겠습니다.

## setTimeout 함수

setTimeout 함수는 일정한 시간 경과 후에 한 번만 특정한 동작을 실행하기 위해 사용됩니다. 아래는 setTimeout 함수의 기본적인 사용법입니다.

```javascript
setTimeout(function() {
    // 실행될 동작
}, 지연시간);
```

예를 들어, 5초 후에 "자동 저장되었습니다."라는 메시지를 출력하고 싶다면 아래와 같이 코드를 작성할 수 있습니다.

```javascript
setTimeout(function() {
    console.log("자동 저장되었습니다.");
}, 5000);
```

위의 코드는 setTimeout 함수를 호출한 후, 5초(5000밀리초)가 경과한 후에 함수 내부의 동작을 실행합니다.

## setInterval 함수

setInterval 함수는 일정한 시간 간격으로 반복적으로 특정한 동작을 실행하기 위해 사용됩니다. 아래는 setInterval 함수의 기본적인 사용법입니다.

```javascript
setInterval(function() {
    // 실행될 동작
}, 간격시간);
```

예를 들어, 1분마다 자동으로 저장하는 동작을 수행하고 싶다면 아래와 같이 코드를 작성할 수 있습니다.

```javascript
setInterval(function() {
    console.log("자동 저장되었습니다.");
}, 60000);
```

위의 코드는 setInterval 함수를 호출한 후, 1분마다 함수 내부의 동작을 실행합니다.

## 자동 저장 예시

이제 setTimeout과 setInterval 함수를 활용하여 주기적인 자동 저장을 구현하는 예시를 살펴보겠습니다.

```javascript
let saveTime = 10000; // 10초
let saveTimer = null;

function startAutoSave() {
    saveTimer = setInterval(function() {
        saveData();
    }, saveTime);
}

function stopAutoSave() {
    clearInterval(saveTimer);
}

function saveData() {
    // 데이터를 저장하는 동작
    console.log("자동 저장되었습니다.");
}

// 자동 저장 시작
startAutoSave();

// 30초 후에 자동 저장 중지
setTimeout(function() {
    stopAutoSave();
}, 30000);
```

위의 예시는 10초마다 `saveData` 함수를 실행하여 자동으로 데이터를 저장하는 동작을 수행합니다. 자동 저장을 시작할 때 `startAutoSave` 함수를 호출하고, 자동 저장을 중지할 때 `stopAutoSave` 함수를 호출합니다.

또한, 위의 예시 코드에서는 30초 후에 자동 저장을 중지하는 예시도 제공합니다. `setTimeout` 함수를 사용하여 30초 후에 `stopAutoSave` 함수를 호출하면 자동 저장이 중지됩니다.

위의 예시 코드를 수정하여 자신의 웹 애플리케이션에 적용해보세요. 사용자의 작업을 자동으로 저장함으로써 데이터 손실을 방지할 수 있습니다.