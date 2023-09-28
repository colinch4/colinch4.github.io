---
layout: post
title: "자바스크립트에서의 Nullish Coalescing과 Optional Chaining의 차이점"
description: " "
date: 2023-09-29
tags: [javascript, nullishcoalescing, optionalchaining]
comments: true
share: true
---

자바스크립트는 ES2020부터 Nullish Coalescing과 Optional Chaining이라는 두 가지 새로운 기능을 도입했습니다. 이러한 기능은 코드의 간결성과 안전성을 향상시키는 데 도움이 됩니다. 하지만 Nullish Coalescing과 Optional Chaining이 서로 다른 기능을 수행하므로, 이들의 차이점을 명확히 이해하는 것이 중요합니다.

## Nullish Coalescing (널 병합 연산자)

Nullish Coalescing 연산자 `??`는 첫 번째 피연산자가 `null` 또는 `undefined`인 경우에만 두 번째 피연산자를 반환합니다. 다음은 Nullish Coalescing의 예시입니다.

```javascript
const foo = null ?? 'default value';
console.log(foo); // 'default value'

const bar = 0 ?? 42;
console.log(bar); // 0

const baz = '' ?? 'empty string';
console.log(baz); // ''

const qux = undefined ?? 'fallback';
console.log(qux); // 'fallback'
```

Nullish Coalescing은 변수나 속성이 null 또는 undefined인 경우에 기본값을 제공하고 싶을 때 유용합니다. 이 기능은 falsy한 값들인 0, 빈 문자열, false와는 다르게 동작합니다.  

## Optional Chaining (옵셔널 체이닝)

Optional Chaining 연산자 `?.`는 객체의 속성에 접근할 때, 해당 속성이 존재하지 않는 경우 undefined를 반환합니다. 이를 통해 객체 안에 여러 단계의 속성을 체이닝하면서 안전하게 접근할 수 있습니다. 예시 코드는 다음과 같습니다.

```javascript
const person = {
  name: 'John Doe',
  address: {
    city: 'New York',
    zipCode: 12345
  }
};

const cityName = person.address?.city;
console.log(cityName); // 'New York'

const zipCode = person.address?.zipCode;
console.log(zipCode); // 12345

const age = person.age?.years; // 속성이 존재하지 않으므로 undefined 반환
console.log(age); // undefined
```

Optional Chaining은 코드 내에서 속성이나 메소드가 있는지 확인하지 않고도 접근할 수 있도록 도와줍니다. 이는 코드를 더욱 간결하고 가독성있게 만들어줍니다.

## 결론

Nullish Coalescing과 Optional Chaining은 자바스크립트 코드를 간결하고 안전하게 만드는 데 도움을 줍니다. Nullish Coalescing은 변수나 속성이 null 또는 undefined일 때 기본값을 제공하며, Optional Chaining은 객체의 속성에 안전하게 접근할 수 있게 해줍니다. 이 두 가지 기능은 필요에 따라 적절히 활용하여 코드의 안정성과 가독성을 높일 수 있습니다.

#javascript #nullishcoalescing #optionalchaining