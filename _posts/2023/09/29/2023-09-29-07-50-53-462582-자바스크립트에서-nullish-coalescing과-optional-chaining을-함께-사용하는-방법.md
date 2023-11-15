---
layout: post
title: "자바스크립트에서 Nullish Coalescing과 Optional Chaining을 함께 사용하는 방법"
description: " "
date: 2023-09-29
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 Nullish Coalescing(`??`)과 Optional Chaining(`?.`)은 각각 null 및 undefined 값을 다루는 데 사용되는 편리한 기능입니다. 이 두 가지 기능을 함께 사용하면 코드의 가독성을 향상시키고 예외 처리를 간소화할 수 있습니다.

## Nullish Coalescing(`??`)

Nullish Coalescing(`??`)은 값이 null 또는 undefined인 경우 대체 값을 반환하는 연산자입니다. 기본적으로 값이 null 또는 undefined가 아닌 경우 좌측 피연산자의 값을 반환합니다.

```javascript
const name = user.name ?? 'Unknown';
console.log(name); // user.name이 유효한 경우 user.name의 값을 출력, 그렇지 않은 경우 'Unknown'을 출력
```

위의 코드에서 `user.name`이 null 또는 undefined인 경우 'Unknown'을 대체 값으로 사용하여 변수 `name`에 할당합니다.

## Optional Chaining(`?.`)

Optional Chaining(`?.`)은 프로퍼티 접근 시 중첩된 객체에서 에러를 방지하기 위한 연산자입니다. 중첩된 객체의 프로퍼티에 접근할 때 해당 프로퍼티가 존재하지 않는 경우 undefined를 반환합니다.

```javascript
const age = user?.details?.age;
console.log(age); // user.details.age가 유효한 경우 user.details.age의 값을 출력, 그렇지 않은 경우 undefined를 출력
```

위의 코드에서 `user`, `user.details`, `user.details.age`가 모두 유효한 경우 `age` 변수에 해당 값이 할당되고, 그렇지 않은 경우 `undefined`가 할당됩니다.

## Nullish Coalescing과 Optional Chaining 함께 사용하기

Nullish Coalescing과 Optional Chaining은 함께 사용할 때 코드의 가독성을 크게 향상시킵니다. 아래의 예제는 이 두 기능을 함께 사용하여 변수 `name`과 `age`를 가져오는 예입니다.

```javascript
const name = user?.name ?? 'Unknown';
const age = user?.details?.age ?? 0;
console.log(name, age); // user.name과 user.details.age가 유효한 경우 해당 값을 출력, 그렇지 않은 경우 각각 'Unknown'과 0을 출력
```

위의 코드에서 `user` 객체와 `user.details` 객체가 존재하지 않거나, `user.name` 및 `user.details.age`가 null 또는 undefined인 경우 `name`과 `age` 변수에 대체 값으로 각각 'Unknown'과 0을 할당합니다.

이렇게 함께 사용하면 코드를 간소화하고 예외 상황을 처리할 수 있기 때문에, 자바스크립트에서 Nullish Coalescing과 Optional Chaining을 함께 사용하는 것은 권장되는 방법입니다.

---

hashtags: #javascript #codingtips