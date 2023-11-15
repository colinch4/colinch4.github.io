---
layout: post
title: "자바스크립트 Intl.RelativeTimeFormat을 사용하여 다국어에서 상대적인 시간 표현하기"
description: " "
date: 2023-11-10
tags: [javascript]
comments: true
share: true
---

많은 웹 애플리케이션과 소셜 미디어 플랫폼에서는 상대적인 시간 표현이 중요합니다. 사용자에게 현재 시간과 과거 또는 미래 사건 사이의 차이를 알려주는 것은 매우 유용합니다. 이러한 요구를 충족시키기 위해 자바스크립트에서는 Intl.RelativeTimeFormat라는 새로운 API를 도입했습니다. 이를 활용하여 다국어 환경에서도 상대적인 시간을 표현할 수 있습니다.

## Intl.RelativeTimeFormat API 소개

Intl.RelativeTimeFormat는 자바스크립트의 표준 내장 API입니다. 이 API는 현재 시간과 다른 시간의 상대적인 차이를 표현하기 위해 사용됩니다. 이를 통해 "1시간 전", "5분 후"와 같은 상대적인 시간을 다국어로 표현할 수 있습니다.

## 사용법

1. `Intl.RelativeTimeFormat` 객체 생성하기

   ```javascript
   const rtf = new Intl.RelativeTimeFormat('ko', { style: 'long' });
   ```

   이 예제에서는 `ko`를 사용하여 한국어로 상대적인 시간을 표현하는 `Intl.RelativeTimeFormat` 객체를 생성합니다. `style` 옵션은 "long", "short", "narrow" 중 하나를 선택할 수 있으며, 각각 긴 형식, 짧은 형식, 압축된 형식을 나타냅니다.

2. 상대적인 시간 표현하기

   ```javascript
   const timeDifference = -3;
   const unit = 'hour';

   const relativeTime = rtf.format(timeDifference, unit);
   console.log(relativeTime);
   // 출력 결과: 3시간 전
   ```

   `format` 메서드를 사용하여 상대적인 시간을 표현할 수 있습니다. 첫 번째 인자는 시간 차이를 나타내는 숫자이고, 두 번째 인자는 시간 단위를 나타내는 문자열입니다. 여기서는 `timeDifference` 변수에 -3을, `unit` 변수에는 'hour'를 전달하여 "3시간 전"이라는 결과를 얻었습니다.

3. 다국어 지원하기

   ```javascript
   const timeDifference = 2;
   const unit = 'day';

   const relativeTime = rtf.format(timeDifference, unit);
   console.log(relativeTime);
   // 출력 결과: 2일 후
   ```

   `Intl.RelativeTimeFormat`은 현재 시스템 언어를 자동으로 감지합니다. 따라서 `new Intl.RelativeTimeFormat()`의 첫 번째 인자로 언어 코드를 전달하지 않아도 되지만, 다른 언어로 표현하고 싶다면 인자로 해당 언어 코드를 전달할 수 있습니다.

## 결론

자바스크립트 `Intl.RelativeTimeFormat` API를 사용하면 다국어에서도 상대적인 시간을 표현할 수 있습니다. 이는 웹 애플리케이션에서 다국어 지원을 제공하는 데 큰 도움이 됩니다. 또한, `style` 옵션을 조정하여 텍스트의 길이를 변경하는 등 다양한 스타일을 적용할 수도 있습니다.

자세한 내용은 [MDN 웹 문서](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/RelativeTimeFormat)를 참조해주세요.

#자바스크립트 #다국어 #RelativeTimeFormat