---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 모바일 앱 개발"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

모바일 앱 개발에서 시간에 따라 동작을 제어해야 할 때, setTimeout과 setInterval 함수는 매우 유용한 도구입니다. 이러한 함수들은 자바스크립트에서 제공되는 타이머 함수로, 특정 시간이 경과하면 원하는 동작을 실행할 수 있도록 도와줍니다.

## setTimeout

setTimeout은 일정 시간이 지난 후에 한 번만 동작을 실행하는 데 사용됩니다. 예를 들어, 앱에서 사용자가 버튼을 클릭한 후 3초가 지나면 다음 동작을 실행하고 싶다면 setTimeout 함수를 사용할 수 있습니다.

아래는 setTimeout 함수를 사용한 예시 코드입니다.

```javascript
setTimeout(function() {
  // 실행할 동작 작성
}, 3000); // 3초 후에 실행
```

위 코드에서 첫 번째 인자로 전달되는 함수는 3초 후에 실행될 동작을 작성하는 부분입니다. 두 번째 인자로는 지연 시간을 밀리초 단위로 입력합니다.

## setInterval

setInterval은 일정한 시간 간격으로 동작을 반복적으로 실행하는 데 사용됩니다. 예를 들어, 앱에서 실시간으로 데이터를 업데이트하고 싶을 때 setInterval 함수를 사용할 수 있습니다.

아래는 setInterval 함수를 사용한 예시 코드입니다.

```javascript
setInterval(function() {
  // 반복적으로 실행할 동작 작성
}, 1000); // 1초마다 실행
```

위 코드에서도 첫 번째 인자로 전달되는 함수에 반복적으로 실행할 동작을 작성합니다. 두 번째 인자로는 반복 간격을 밀리초 단위로 입력합니다.

## 주의사항

setTimeout과 setInterval 함수를 사용할 때 주의해야 할 몇 가지 사항이 있습니다.

- 타이머를 제어하기 위해서는 clearTimout 또는 clearInterval 함수를 사용해야 합니다. 이 함수들은 타이머 식별자를 인자로 받아 해당 타이머를 정지시킵니다.
- 일정 시간 마다 동작을 실행하는 setInterval 함수는 잦은 호출로 인해 성능 저하를 유발할 수 있습니다. 따라서 반복 간격을 적절히 조정해야 합니다.
- 모바일 앱에서는 배터리 수명에 영향을 미치는 요소이므로, setInterval의 사용은 신중히 고려되어야 합니다. 불필요한 반복 호출을 피하고 최적화된 방식을 사용하는 것이 중요합니다.

이처럼 setTimeout과 setInterval을 제대로 활용하면 모바일 앱 개발에서 시간에 따른 동작 제어를 효과적으로 수행할 수 있습니다.