---
layout: post
title: "자바스크립트에서의 Nullish Coalescing과 try-catch문의 사용 비교"
description: " "
date: 2023-09-29
tags: [javascript]
comments: true
share: true
---

자바스크립트에서는 Nullish Coalescing 연산자와 try-catch문을 사용하여 예외 처리 및 값 할당에 대한 유연성을 제공합니다. 이 두 가지 기능은 각자의 역할과 장단점이 있으며, 이를 비교하여 어떤 상황에서 어떻게 사용하는지 알아보도록 하겠습니다.

## Nullish Coalescing 연산자

Nullish Coalescing 연산자 `??`는 변수가 `null` 또는 `undefined`인 경우에만 대체 값으로 지정된 값을 반환하는 데 사용됩니다. 이를테면, 다음과 같은 코드를 예로 들 수 있습니다.

```javascript
const defaultValue = 'Default Value';
const value = null ?? defaultValue;

console.log(value); // 'Default Value'
```

위의 코드에서 `value` 변수는 `null`이기 때문에 Nullish Coalescing 연산자를 사용하여 `defaultValue` 값을 할당받게 됩니다. 따라서 `value`의 값은 'Default Value'가 됩니다.

Nullish Coalescing 연산자의 주요 장점은 빈 문자열(`''`)이나 숫자 0(`0`)과 같은 Falsy한 값들을 대체 값으로 취급하지 않는다는 점입니다. 이로 인해 값 할당의 목적으로 사용될 때 더욱 신뢰할 수 있는 코드를 작성할 수 있습니다.

## try-catch문

try-catch문은 예외 처리를 위해 사용됩니다. 예외가 발생할 수 있는 코드 부분을 `try` 블록 안에 작성하고, 예외 발생 시 처리할 코드를 `catch` 블록 안에 작성합니다. 아래의 예제를 살펴보겠습니다.

```javascript
const riskyOperation = () => {
  // 예외가 발생할 수 있는 코드
  throw new Error('Something went wrong');
};

try {
  riskyOperation();
} catch (error) {
  // 예외가 발생했을 때 실행될 코드
  console.log('Caught an error:', error.message);
}
```

위의 코드에서 `riskyOperation` 함수는 의도적으로 예외를 발생시키는 함수입니다. `try` 블록 안에서 이 함수를 호출하면서 예외를 처리할 `catch` 블록을 지정해주었습니다. 예외가 발생하면 프로그램이 멈추지 않고, 예외 메시지와 함께 `catch` 블록이 실행됩니다.

try-catch문의 주요 장점은 코드 실행 중에 발생한 예외를 처리하고, 프로그램의 정상 실행을 유지하는 데 있습니다. 예외 처리를 통해 코드의 안정성을 높일 수 있으며, 오류에 대한 정보를 수집하고 로깅할 수도 있습니다.

## 비교와 사용 사례

Nullish Coalescing과 try-catch문은 서로 다른 기능을 제공합니다. Nullish Coalescing은 주로 값 할당 시 기본값을 설정하는 용도로 사용되며, try-catch문은 예외 처리 시 사용됩니다.

Nullish Coalescing은 값이 `null` 또는 `undefined`인지 확인하고 대체 값으로 지정된 값을 반환합니다. 반면에 try-catch문은 코드 실행 중에 발생한 예외를 캐치하여 처리하고, 정상적인 프로그램 흐름을 유지합니다.

이 두 기능은 각각의 장점을 가지고 있으며, 어떤 상황에서 어떻게 사용할지는 개발자에게 달려있습니다. 더 안정적인 코드를 작성하고자 한다면 Nullish Coalescing을 사용하여 예외를 방지할 수 있으며, 예외 처리가 필요한 코드에는 try-catch문을 사용하여 예외 상황을 처리할 수 있습니다.

방어적인 프로그래밍을 위해서는 Nullish Coalescing과 try-catch문을 적절히 조합하여 사용하는 것이 좋습니다.

#javascript #nullish-coalescing #try-catch