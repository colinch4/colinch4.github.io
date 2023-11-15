---
layout: post
title: "자바스크립트 Intl.RelativeTimeFormat을 사용하여 다국어에서 상대적 시간 표시하기"
description: " "
date: 2023-11-10
tags: [javascript]
comments: true
share: true
---

많은 웹 애플리케이션에서는 상대적인 시간을 표시하는 것이 중요합니다. 예를 들어 "방금 전에", "5분 전에" 또는 "하루 전에"와 같은 형태로 시간을 표시할 수 있어야 합니다. 이러한 기능을 구현하기 위해 자바스크립트 Intl.RelativeTimeFormat을 사용할 수 있습니다. 이 기능은 다국어 지원을 제공하여, 각 언어에 맞는 상대적인 시간을 표시할 수 있습니다.

## Intl.RelativeTimeFormat 소개

Intl.RelativeTimeFormat은 ECMA-402 표준의 일부로서, 자바스크립트에서 다국어로 상대적인 시간을 표시할 수 있도록 도와줍니다. 이 표준은 현재 날짜와 다른 날짜 사이의 상대적인 시간을 표현하는 데 사용되며, 다양한 언어와 로케일을 지원합니다.

## 사용법

Intl.RelativeTimeFormat을 사용하여 다국어에서 상대적인 시간을 표시하는 방법은 아래와 같습니다.

1. Intl.RelativeTimeFormat 객체를 생성합니다. 이때 사용할 언어와 로케일을 지정합니다.

   ```javascript
   const rtf = new Intl.RelativeTimeFormat('ko', { numeric: 'auto' });
   ```

   위의 예제에서 'ko'는 한국어로, `{ numeric: 'auto' }`는 상대적인 시간을 숫자로 표시하도록 설정합니다.

2. rtf.format() 메서드를 사용하여 상대적인 시간을 표시합니다. 이때 인자로 시간의 차이를 넘겨줍니다. 양수 값은 미래 시간을, 음수 값은 과거 시간을 의미합니다.

   ```javascript
   const timeDifference = -2;
   const relativeTime = rtf.format(timeDifference, 'day');
   console.log(relativeTime); // "2일 전"
   ```

   위의 예제에서는 현재 시간으로부터 2일 전을 표시합니다.

3. formatToParts() 메서드를 사용하여 상대적인 시간을 세부적으로 표시할 수도 있습니다. 이 메서드는 배열을 반환하며, 각 항목은 텍스트 및 유형을 포함합니다.

   ```javascript
   const timeDifference = 3;
   const relativeTimeParts = rtf.formatToParts(timeDifference, 'hour');
   console.log(relativeTimeParts); // [ { type: 'numeric', value: '3' }, { type: 'literal', value: '시간 후' } ]
   ```

   위의 예제에서는 현재 시간으로부터 3시간 후를 텍스트 및 유형으로 표시합니다.

## 다국어 지원

Intl.RelativeTimeFormat은 다양한 언어와 로케일에 대한 지원을 제공합니다. 사용자의 브라우저 환경 설정에 따라 자동으로 사용자의 언어와 로케일을 감지합니다. 또한 명시적으로 언어 코드와 로케일을 지정하여 특정 언어와 로케일을 사용할 수도 있습니다.

## 결론

Intl.RelativeTimeFormat은 다국어 환경에서 상대적인 시간을 표시하는 데 유용한 도구입니다. 이를 활용하여 웹 애플리케이션에서 다양한 언어로 상대적인 시간을 표시할 수 있습니다. 자바스크립트에서 이 기능을 사용하여 사용자 경험을 향상시키고, 다국어 지원을 통해 글로벌 사용자에게 더 나은 서비스를 제공할 수 있습니다.

> 참고: [MDN web docs - Intl.RelativeTimeFormat](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)

#JavaScript #다국어 #상대적시간표시