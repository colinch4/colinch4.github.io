---
layout: post
title: "Nullish Coalescing과 쇼트 서킷(Short Circuit) 평가의 차이점 이해하기"
description: " "
date: 2023-09-29
tags: [JavaScript]
comments: true
share: true
---

최신 JavaScript 버전인 ES11(ES2020)에서 "Nullish Coalescing" 연산자가 도입되었습니다. 이 연산자는 쇼트 서킷(Short Circuit) 평가와 함께 자주 사용되지만, 이 두 가지 개념에는 몇 가지 중요한 차이점이 있습니다.

## 쇼트 서킷(Short Circuit) 평가

쇼트 서킷(Short Circuit) 평가는 논리 연산자 중 하나인 "둘 다(and)"(`&&`)와 "하나만(or)"(`||`)를 사용하여 조건식을 평가하는 프로그래밍 기법입니다. 이때, 조건식에서 첫 번째 값이 결과를 결정하는 경우, 즉 첫 번째 값이 `false`일 때 `&&` 연산자로 인해 결과가 `false`가 되었거나, 첫 번째 값이 `true`일 때 `||` 연산자로 인해 결과가 `true`가 되었을 때, 두 번째 값은 평가되지 않습니다.

쇼트 서킷 평가의 예제 코드는 아래와 같습니다.

```javascript
const value = a || b;
```

위의 코드에서 `a`가 `true`이면 `value`는 `a`의 값이 되고, `a`가 `false`이면 `value`는 `b`의 값이 됩니다. 이때, `a`의 값이 결정되면 `b`는 평가되지 않습니다.

## Nullish Coalescing 연산자

Nullish Coalescing 연산자(`??`)는 새로 도입된 연산자로, 왼쪽 피연산자가 `null` 또는 `undefined`인 경우 오른쪽 피연산자를 반환합니다. 그 외에는 왼쪽 피연산자 값을 반환합니다. 이 연산자는 쇼트 서킷 평가와 함께 사용되는 경우, 쇼트 서킷 평가의 결과값이 `undefined` 또는 `null`인지 구분하여 다른 값으로 대체합니다.

Nullish Coalescing 연산자의 예제 코드는 아래와 같습니다.

```javascript
const value = a ?? b;
```

위의 코드에서 `a`가 `null` 또는 `undefined`이면 `value`는 `b`의 값이 되고, `a`가 `null` 또는 `undefined`가 아니면 `value`는 `a`의 값이 됩니다.

## Nullish Coalescing과 쇼트 서킷 평가의 차이점

이제 Nullish Coalescing과 쇼트 서킷 평가의 주요 차이점을 정리해보겠습니다.

1. Nullish Coalescing은 `null` 또는 `undefined`를 확인하여 대체하는데 사용되지만, 쇼트 서킷 평가는 조건식의 결과값이 `false`인지 확인하여 대체합니다.
2. Nullish Coalescing은 오른쪽 피연산자에 상관없이 항상 왼쪽 피연산자 값이 반환되지만, 쇼트 서킷 평가는 첫 번째 값이 `false`일 때만 두 번째 값이 반환됩니다.
3. Nullish Coalescing은 명시적으로 `null` 또는 `undefined`인지 확인하는 연산자이며, 쇼트 서킷 평가는 조건식의 결과값에 따라 다양한 상황에서 동작합니다.

앞으로 JavaScript 개발을 할 때, Nullish Coalescing과 쇼트 서킷 평가를 올바르게 이해하고 사용해야 합니다. 이 두 가지 개념을 적절히 활용하면, 코드의 가독성과 유지 보수성을 향상시킬 수 있을 것입니다.

#WebDevelopment #JavaScript