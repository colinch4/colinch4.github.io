---
layout: post
title: "자바스크립트 Intl.RelativeTimeFormat을 사용하여 상대적인 시간 표시하기"
description: " "
date: 2023-11-10
tags: [javascript, 자바스크립트]
comments: true
share: true
---

최근에 발표된 자바스크립트의 새로운 기능 중 하나는 `Intl.RelativeTimeFormat`입니다. 이 기능을 사용하면 상대적인 시간을 표시하는 것이 간단해집니다. 이 기능은 날짜 간의 차이를 텍스트로 표시하는 데 사용됩니다. 예를 들어 "2일 전"이나 "5분 전"과 같은 형태입니다.

이 기능을 사용하기 위해서는 먼저 `Intl.RelativeTimeFormat` 객체를 생성해야 합니다. 다음은 기본 예제입니다.

```javascript
const rtf = new Intl.RelativeTimeFormat('ko', { numeric: 'auto' });

console.log(rtf.format(-2, 'day'));
// 출력: 2일 전

console.log(rtf.format(5, 'minute'));
// 출력: 5분 후
```

위의 예제에서는 `ko`를 사용하여 한국어로 지역화된 형태로 결과를 출력합니다. `numeric` 옵션은 상대적인 시간을 숫자 형태로 표시할지, 텍스트 형태로 표시할지를 결정하는 옵션입니다. "auto"로 설정하면 `-1`, `0`, `1` 등 숫자 3개를 표기하고 그 외의 경우에는 텍스트로 표시합니다.

`rtl.format()` 메서드의 첫 번째 매개변수는 날짜 간의 차이를 나타내는 숫자이며, 두 번째 매개변수는 시간 단위를 나타내는 문자열입니다. 시간 단위는 `year`, `quarter`, `month`, `week`, `day`, `hour`, `minute`, `second` 등 다양한 값을 사용할 수 있습니다.

- `year`: 연도
- `quarter`: 분기
- `month`: 월
- `week`: 주
- `day`: 일
- `hour`: 시간
- `minute`: 분
- `second`: 초

`Intl.RelativeTimeFormat`의 기능을 활용하면 쉽고 간편하게 상대적인 시간을 표시할 수 있습니다. 이 기능을 활용하여 사용자에게 더 직관적이고 쉽게 이해할 수 있는 상대적인 시간 표시를 제공해 보세요.

**참고 자료:**
- [MDN web docs: Intl.RelativeTimeFormat](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)

#javascript #자바스크립트 #날짜 #상대적인시간