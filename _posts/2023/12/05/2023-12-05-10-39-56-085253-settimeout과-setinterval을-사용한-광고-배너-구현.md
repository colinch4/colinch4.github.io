---
layout: post
title: "[javascript] setTimeout과 setInterval을 사용한 광고 배너 구현"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

광고 배너는 웹사이트나 앱에서 중요한 마케팅 도구입니다. 사용자들에게 광고를 보여주고 소식을 전달하는 역할을 합니다. 이번 기사에서는 자바스크립트의 setTimeout과 setInterval 함수를 사용하여 광고 배너를 구현하는 방법을 알아보겠습니다.

## setTimeout 함수

setTimeout 함수는 일정 시간이 지난 후에 특정한 동작을 수행하는 함수입니다. 광고 배너에 한 번만 동작할 필요가 있을 때 사용하기 좋습니다. setTimeout 함수는 아래와 같이 사용할 수 있습니다.

```javascript
setTimeout(function() {
  // 광고 배너 동작 코드
}, 5000); // 5초 후에 동작
```

위의 예제에서는 5초 후에 광고 배너 동작 코드가 실행됩니다. setTimeout 함수는 첫 번째 인자로 실행할 코드를 받으며, 두 번째 인자로 지연 시간을 받습니다.

## setInterval 함수

setInterval 함수는 일정 시간마다 특정한 동작을 반복적으로 수행하는 함수입니다. 광고 배너가 일정한 간격으로 계속해서 동작해야 할 때 사용하기 좋습니다. setInterval 함수는 아래와 같이 사용할 수 있습니다.

```javascript
setInterval(function() {
  // 광고 배너 동작 코드
}, 10000); // 10초마다 반복 동작
```

위의 예제에서는 10초마다 광고 배너 동작 코드가 반복 실행됩니다. setInterval 함수도 setTimeout 함수와 마찬가지로 첫 번째 인자로 실행할 코드를 받으며, 두 번째 인자로 반복 간격을 받습니다.

## 광고 배너 구현 예시

이제 setTimeout과 setInterval 함수를 사용하여 광고 배너를 구현하는 예시 코드를 살펴보겠습니다. 다음은 5초마다 광고 배너가 변경되는 예시입니다.

```javascript
var banners = ["배너1", "배너2", "배너3"];
var currentBannerIndex = 0;

function changeBanner() {
  // 배너 변경 로직
  console.log("현재 배너:", banners[currentBannerIndex]);
  
  // 다음 배너 인덱스로 변경
  currentBannerIndex++;
  if (currentBannerIndex >= banners.length) {
    currentBannerIndex = 0;
  }
}

// 처음에 광고 배너 변경 함수 한 번 실행
changeBanner();

// 5초마다 광고 배너 변경 함수 반복 실행
setInterval(changeBanner, 5000);
```

위의 예시에서는 `banners` 배열에 광고 배너들을 저장하고, `currentBannerIndex` 변수를 사용하여 현재 배너 인덱스를 관리합니다. `changeBanner` 함수는 배너를 변경하는 로직을 수행하고, `console.log`를 사용하여 변경된 배너를 출력합니다. 마지막으로 `setInterval` 함수를 사용하여 5초마다 `changeBanner` 함수를 반복 실행합니다.

## 마치며

위의 예시를 참고하여 setTimeout과 setInterval 함수를 사용하여 광고 배너를 구현해보세요. 이를 통해 사용자들에게 다양한 광고를 보여줄 수 있고, 마케팅 전략을 효과적으로 전달할 수 있습니다.

- [setTimeout 문서](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [setInterval 문서](https://developer.mozilla.org/ko/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)