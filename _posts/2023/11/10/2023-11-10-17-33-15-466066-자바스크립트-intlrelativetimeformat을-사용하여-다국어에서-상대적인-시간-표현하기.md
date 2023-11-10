---
layout: post
title: "자바스크립트 Intl.RelativeTimeFormat을 사용하여 다국어에서 상대적인 시간 표현하기"
description: " "
date: 2023-11-10
tags: [intl]
comments: true
share: true
---

현대적인 웹 애플리케이션에서 다국어 지원은 매우 중요합니다. 사용자가 언어를 변경할 때, 애플리케이션은 해당 언어에 맞게 텍스트를 표시해야 합니다. 이러한 다국어 지원 중 하나는 상대적인 시간을 표현하는 것입니다. 예를 들어, "방금 전"이나 "5분 전"과 같은 표현은 사용자에게 보다 직관적인 시간 정보를 제공할 수 있습니다.

자바스크립트에서는 Intl.RelativeTimeFormat을 사용하여 다국어에서 상대적인 시간을 표현할 수 있습니다. 이는 ECMA-402 표준의 일부분으로, 다양한 언어와 지역에 맞는 형식으로 상대적인 시간을 표시할 수 있습니다.

## Intl.RelativeTimeFormat 사용법

Intl.RelativeTimeFormat 객체를 생성하기 위해서는 언어와 옵션을 파라미터로 전달해야 합니다. 다음은 사용법을 보여주는 예제 코드입니다.

```javascript
const rtf = new Intl.RelativeTimeFormat('ko', { numeric: 'auto' });

console.log(rtf.format(-1, 'day'));
console.log(rtf.format(3, 'month'));
```

이 예제에서는 'ko'를 통해 한국어를 사용하고, `numeric` 옵션을 `auto`로 설정하여 특정 수치에 따라 자동으로 표기해줍니다. `rtf.format` 함수를 사용하여 해당 시간과 단위를 전달하면, 해당 언어에 맞는 상대적인 시간을 반환합니다.

## 브라우저 호환성

Intl.RelativeTimeFormat은 모든 최신 브라우저에서 지원되지만, IE와 같은 구형 브라우저에서는 지원되지 않을 수 있습니다. 이런 경우에는 polyfill 라이브러리를 사용하여 호환성을 유지할 수 있습니다.

## 요약

다국어 지원은 현대적인 웹 애플리케이션에서 매우 중요한 요소입니다. 자바스크립트의 Intl.RelativeTimeFormat을 사용하면 다국어에서 상대적인 시간을 표현할 수 있고, 사용자에게 보다 직관적인 시간 정보를 제공할 수 있습니다. 다양한 언어와 지역에 맞춘 상대적인 시간 표현을 위해 Intl.RelativeTimeFormat을 활용해보세요.

## 참조

- [Intl.RelativeTimeFormat - MDN web docs](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/RelativeTimeFormat)
- [ECMAScript® 2022 Language Specification - Intl.RelativeTimeFormat](https://tc39.es/ecma402/#intl-relativetimeformat-constructor)