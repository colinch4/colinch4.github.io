---
layout: post
title: "Nullish Coalescing과 Optional Chaining을 사용하여 자바스크립트에서의 데이터 변환 처리하기"
description: " "
date: 2023-09-29
tags: [JavaScript, NullishCoalescing, OptionalChaining]
comments: true
share: true
---

자바스크립트에서 데이터 처리는 종종 null 또는 undefined 값을 다루어야 하는 상황에서 발생합니다. 이러한 값들의 처리는 예기치 않은 오류를 초래할 수 있으므로 처리 방법을 알고 있는 것이 중요합니다. 이를 위해 ES2020에서는 Nullish Coalescing 연산자와 Optional Chaining 기능이 도입되었습니다.

## Nullish Coalescing 연산자

Nullish Coalescing 연산자는 null 또는 undefined 값을 다룰 때 유용합니다. 이 연산자는 두 개의 값 중에서 null 또는 undefined가 아닌 값을 반환하는 연산을 수행합니다. 만약 양쪽 값이 모두 null 또는 undefined인 경우, 연산자의 오른쪽 값을 반환합니다.

```javascript
const name = null ?? "John";
console.log(name);  // 출력 결과: "John"

const age = 0 ?? 25;
console.log(age);   // 출력 결과: 0

const city = undefined ?? "Seoul";
console.log(city);  // 출력 결과: "Seoul"
```

위의 예제에서는 Nullish Coalescing 연산자인 `??`를 사용하여 null 또는 undefined 값을 적절한 값을 할당하는 예를 보여줍니다. 이를 통해 변수에 기본값을 설정하거나, API로부터 받은 값을 처리할 때 유용하게 사용할 수 있습니다.

## Optional Chaining

Optional Chaining은 객체의 속성에 접근할 때 null 또는 undefined인지 확인하지 않고 연속적으로 속성에 접근할 수 있게 합니다. 이를 통해 속성이 없거나 null 또는 undefined인 경우 코드가 중단되지 않고 계속 실행될 수 있습니다.

```javascript
const user = {
  name: "John",
  address: {
    city: "Seoul"
  }
};

console.log(user.address?.city);  // 출력 결과: "Seoul"
console.log(user.address?.country);  // 출력 결과: undefined
```

위의 예제에서는 Optional Chaining 연산자인 `?.`를 사용하여 `user` 객체의 `address` 속성에 접근합니다. 만약 `address`가 존재하지 않거나 null 또는 undefined인 경우에는 그 결과로 undefined를 반환합니다. 이를 통해 객체에서 원하는 속성을 안전하게 접근할 수 있습니다.

## 데이터 변환 처리에 활용하기

Nullish Coalescing과 Optional Chaining을 함께 사용하여 데이터 변환 처리를 보다 안전하고 간결하게 할 수 있습니다. 아래는 사용자 이름과 나이를 가진 객체를 가지고 데이터를 변환하는 예시입니다.

```javascript
const user = {
  profile: {
    name: null,
    age: 25
  }
};

const name = user.profile.name ?? "Unknown";
const age = user.profile.age ?? 0;

console.log(`Name: ${name}, Age: ${age}`);
// 출력 결과: "Name: Unknown, Age: 25"
```

위의 예제에서는 Nullish Coalescing 연산자를 사용하여 이름과 나이를 변환할 때 기본값을 설정합니다. 만약 이름이 null 또는 undefined인 경우 "Unknown"을, 나이가 null 또는 undefined인 경우 0을 할당합니다. 이를 통해 데이터 변환 중에 발생할 수 있는 오류를 방지할 수 있습니다.

Nullish Coalescing과 Optional Chaining은 자바스크립트 코드에서 유용한 기능으로서 데이터 처리에서 발생할 수 있는 예기치 않은 오류를 방지할 수 있습니다. 이를 활용하여 안전하고 더욱 신뢰할 수 있는 코드를 작성해 보세요.

#JavaScript #NullishCoalescing #OptionalChaining