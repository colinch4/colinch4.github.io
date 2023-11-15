---
layout: post
title: "자바스크립트 Intl.RelativeTimeFormat을 사용하여 다국어에서 상대적 시간 표현하기"
description: " "
date: 2023-11-10
tags: [javascript]
comments: true
share: true
---

현대의 웹 애플리케이션은 글로벌 사용자들을 대상으로 하기 때문에, 다양한 언어와 문화를 반영해야 합니다. 강력한 도구로써 동적인 상대적 시간 표현은 이러한 다국어 환경에서 사용자 경험을 향상시키는 데 도움이 됩니다. 

자바스크립트에서는 `Intl` 객체를 사용하여 다국어를 지원하는 여러가지 기능을 제공합니다. 그 중 하나가 `Intl.RelativeTimeFormat`입니다. 이 기능은 상대적인 시간을 다국어로 표현할 수 있게 해줍니다.

## Intl.RelativeTimeFormat 이란?

`Intl.RelativeTimeFormat`은 자바스크립트의 내장 객체로, 다양한 언어 및 지역 설정에서 날짜 및 시간을 상대적으로 표현할 수 있습니다. 이 객체를 사용하여 표현하려는 시간 값을 전달하면, 해당 언어에 맞는 상대적인 시간 표현이 생성됩니다.

## 사용 방법

`Intl.RelativeTimeFormat`을 사용하여 상대적인 시간을 다국어로 표현하는 방법을 알아보겠습니다.

우선, `Intl.RelativeTimeFormat` 객체를 생성하고 원하는 언어 및 문화권에 맞는 로케일을 설정해야 합니다. 아래의 예제에서는 'ko-KR' 로케일을 사용합니다.

```javascript
const rtf = new Intl.RelativeTimeFormat('ko-KR');
```

이제 `format()` 메소드를 사용하여 표현하려는 상대적인 시간을 지정합니다. 첫 번째 매개변수로 시간 값을 전달하고, 두 번째 매개변수로 시간 단위를 전달합니다. 마지막으로 `format()` 메소드를 호출하여 상대적인 시간 표현을 얻을 수 있습니다.

```javascript
console.log(rtf.format(-1, 'day')); // '1일 전'
console.log(rtf.format(2, 'hour')); // '2시간 후'
```

상대적인 시간 표현은 각 언어 및 문화권에 따라 다를 수 있습니다. `Intl.RelativeTimeFormat`은 이러한 다양한 표현을 자동으로 처리해줍니다.

## 지원되는 언어

`Intl.RelativeTimeFormat`은 대부분의 주요 언어를 지원합니다. 자세한 내용은 [MDN web docs](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat#%EC%A7%80%EC%9B%90)에서 확인할 수 있습니다.

## 결론

자바스크립트의 `Intl.RelativeTimeFormat`을 사용하면 다국어 환경에서 상대적인 시간을 표현하는 것이 간단하고 효율적입니다. 이 기능을 사용하여 웹 애플리케이션에서 다국어 사용자 경험을 향상시킬 수 있습니다.

> #javascript #다국어 #상대적시간