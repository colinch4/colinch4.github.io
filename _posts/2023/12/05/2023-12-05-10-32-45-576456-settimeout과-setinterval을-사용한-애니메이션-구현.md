---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 애니메이션 구현"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

애니메이션을 웹 페이지에 구현하기 위해서는 JavaScript에서 시간 지연 기능을 사용해야 합니다. 이러한 기능을 구현하는 데에 `setTimeout`과 `setInterval` 함수를 사용할 수 있습니다. 이 두 함수는 JavaScript에서 비동기적인 실행을 가능하게 해주는 함수들입니다.

## setTimeout 함수

`setTimeout` 함수는 일정 시간이 경과한 후에 한 번만 특정 함수를 실행합니다. 주어진 시간(밀리초)가 경과한 후에 함수를 실행하고자 할 때 사용됩니다. setTimeout 함수는 다음과 같이 사용할 수 있습니다:

```javascript
setTimeout(function(){
   // 실행하고자 하는 코드
}, 지연시간);
```

예를 들어, 1초 후에 'Hello, world!'라는 메시지를 출력하고자 한다면 다음과 같이 setTimeout 함수를 사용할 수 있습니다:

```javascript
setTimeout(function(){
   console.log('Hello, world!');
}, 1000);
```

## setInterval 함수

`setInterval` 함수는 일정 시간 간격으로 특정 함수를 반복해서 실행합니다. 정해진 간격마다 함수를 실행하고자 할 때 사용됩니다. setInterval 함수는 다음과 같이 사용할 수 있습니다:

```javascript
setInterval(function(){
   // 반복 실행하고자 하는 코드
}, 간격);
```

예를 들어, 1초 간격으로 현재 시간을 출력하고자 한다면 다음과 같이 setInterval 함수를 사용할 수 있습니다:

```javascript
setInterval(function(){
   var currentTime = new Date();
   console.log(currentTime);
}, 1000);
```

## 애니메이션 구현 예시

이제 setTimeout과 setInterval 함수를 사용하여 간단한 애니메이션을 구현해보겠습니다. 예를 들어, 타이틀의 색상을 일정 시간 간격으로 변화시키는 애니메이션을 만들어보겠습니다:

```html
<!DOCTYPE html>
<html>
<head>
    <script>
        function changeColor() {
            var title = document.getElementById('title');
            var currentColor = title.style.color;

            if (currentColor === 'red')
                title.style.color = 'blue';
            else
                title.style.color = 'red';
        }

        window.onload = function() {
            setInterval(changeColor, 1000);
        }
    </script>
</head>
<body>
    <h1 id="title" style="color: red;">Hello, world!</h1>
</body>
</html>
```

위 예제 코드에서는 `changeColor`라는 함수를 정의하고, 타이틀의 현재 색상을 체크하여 색상을 변경하는 로직을 구현했습니다. 그리고 `window.onload` 이벤트에서 `setInterval` 함수를 호출하여 `changeColor` 함수를 1초마다 실행하도록 설정하였습니다. 이렇게 하면 타이틀의 색상이 1초마다 빨강과 파랑 사이로 변화하게 됩니다.

이처럼 `setTimeout`과 `setInterval` 함수를 사용하면 JavaScript를 통해 간단한 애니메이션을 구현할 수 있습니다. 이러한 함수들을 활용하여 웹 페이지에 동적인 기능을 추가할 수 있습니다.