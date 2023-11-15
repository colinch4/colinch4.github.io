---
layout: post
title: "자바스크립트에서의 Nullish Coalescing과 Option 객체의 연동 방법"
description: " "
date: 2023-09-29
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 Nullish Coalescing 연산자는 변수가 null 또는 undefined일 경우 대체 값을 지정할 수 있는 기능을 제공합니다. 이 기능은 코드의 가독성과 안정성을 높이는 데 도움이 됩니다.

## Nullish Coalescing 연산자

Nullish Coalescing 연산자는 `??`로 표기되며, 다음과 같은 문법으로 사용합니다:

```javascript
const result = variableA ?? variableB;
```

위 코드에서 `variableA`가 null 또는 undefined일 경우 `variableB`의 값을 `result`에 할당합니다.

예를 들어, 다음 코드에서는 `name`이 null 또는 undefined일 경우 "Unknown"을 디폴트 값으로 사용합니다:

```javascript
const name = null;
const defaultName = "Unknown";

const result = name ?? defaultName;

console.log(result); // 출력 결과: "Unknown"
```

## Option 객체를 활용한 연동 방법

때로는 Nullish Coalescing을 사용하여 여러 개의 변수를 대체 값으로 설정해야 할 수도 있습니다. 이 때, Option 객체를 활용하면 더욱 효과적으로 코드를 작성할 수 있습니다.

Option 객체는 다음과 같은 구조를 가지고 있습니다:

```javascript
const option = {
  value: null,
  defaultValue: "Default",
};
```

위 예시에서 `option.value`가 null 또는 undefined일 경우, `option.defaultValue`를 대체 값으로 사용합니다.

```javascript
const option = {
  value: null,
  defaultValue: "Default",
};

const result = option.value ?? option.defaultValue;

console.log(result); // 출력 결과: "Default"
```

이 방법을 활용하면 복잡한 대체 로직을 간결하게 작성할 수 있으며, 코드 유지보수성이 향상됩니다.

## 정리

Nullish Coalescing 연산자와 Option 객체를 함께 사용하면 자바스크립트에서 null 또는 undefined일 경우의 대체 값을 쉽게 설정할 수 있습니다. 이를 활용하여 코드를 간결하게 작성하고 가독성과 유지보수성을 높일 수 있습니다.

#javascript #nullish-coalescing #option-object