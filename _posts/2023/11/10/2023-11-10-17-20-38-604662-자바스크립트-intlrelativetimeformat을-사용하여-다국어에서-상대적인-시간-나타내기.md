---
layout: post
title: "자바스크립트 Intl.RelativeTimeFormat을 사용하여 다국어에서 상대적인 시간 나타내기"
description: " "
date: 2023-11-10
tags: [javascript, Intl]
comments: true
share: true
---

웹 애플리케이션에서 사용자에게 상대적인 시간을 표시하는 것은 중요한 기능입니다. 예를 들어, "방금 전", "5분 전", "2시간 전"과 같이 시간을 간략하게 표시하여 사용자가 쉽게 이해할 수 있도록 도와줍니다. 이러한 기능을 제공하기 위해서는 다국어를 지원하는 것이 필요합니다. 자바스크립트에서는 Intl.RelativeTimeFormat을 사용하여 상대적인 시간을 다국어로 표시할 수 있습니다.

## Intl.RelativeTimeFormat 개요

Intl.RelativeTimeFormat은 자바스크립트에서 다국어로 상대적인 시간을 표시하기 위한 API입니다. 이 API를 사용하면 지난 시간 또는 남은 시간을 자연스러운 형태로 표현할 수 있습니다. 현재는 몇가지 브라우저에서 지원하지만, 폴리필을 통해 지원하지 않는 브라우저에서도 사용할 수 있습니다.

## 기본 사용법

아래는 Intl.RelativeTimeFormat을 사용하여 상대적인 시간을 표시하는 간단한 예제입니다.

```javascript
const rtf = new Intl.RelativeTimeFormat('en', { numeric: 'auto' });

// 1 hour ago
console.log(rtf.format(-1, 'hour'));

// 5 minutes ago
console.log(rtf.format(-5, 'minute'));

// in 2 days
console.log(rtf.format(2, 'day'));
```

위의 예제에서는 'en'을 로케일로 설정하고, 'hour', 'minute', 'day'를 단위로 사용하여 상대적인 시간을 표시하였습니다. 로케일을 변경하면 해당 언어에 맞는 형식으로 시간을 표시할 수 있습니다.

## 다국어 지원

Intl.RelativeTimeFormat은 다국어 지원을 위해 다양한 로케일을 제공합니다. 로케일은 ISO 639-1 언어 코드와 ISO 3166-1 국가 코드로 구성됩니다. 예를 들어, 'en-US', 'ko-KR', 'ja-JP'와 같은 형식으로 사용됩니다.

다국어로 상대적인 시간을 표시하기 위해서는 해당 로케일을 지정하면 됩니다. 아래는 한국어로 상대적인 시간을 표시하는 예제입니다.

```javascript
const rtf = new Intl.RelativeTimeFormat('ko', { numeric: 'auto' });

// 1시간 전
console.log(rtf.format(-1, 'hour'));

// 5분 전
console.log(rtf.format(-5, 'minute'));

// 2일 후
console.log(rtf.format(2, 'day'));
```

위의 예제에서는 'ko'를 로케일로 설정하여 한국어로 상대적인 시간을 표시하였습니다.

## Conclusion

Intl.RelativeTimeFormat은 자바스크립트에서 상대적인 시간을 다국어로 표시하는 강력한 도구입니다. 이를 사용하여 웹 애플리케이션에서 사용자들에게 보다 사용하기 쉬운 시간 표현을 제공할 수 있습니다. 다국어 지원을 통해 전 세계의 사용자에게 원활한 경험을 제공할 수 있으며, 로케일을 바꾸는 것만으로 다양한 언어로 시간을 표현할 수 있습니다.

[#javascript](https://twitter.com/hashtag/javascript) [#Intl.RelativeTimeFormat](https://twitter.com/hashtag/Intl.RelativeTimeFormat)