---
layout: post
title: "자바스크립트 객체 메서드(Object.assign, Object.keys 등)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 객체 지향 프로그래밍 언어로써, 객체를 다루는데 다양한 메서드들을 제공합니다. 이번 포스트에서는 자바스크립트 객체 메서드 중 Object.assign과 Object.keys를 다뤄보겠습니다.

## Object.assign

Object.assign은 하나 이상의 소스 객체로부터 대상 객체로 속성을 복사할 때 사용됩니다. 이 메서드는 대상 객체를 반환하며, 소스 객체의 속성이 대상 객체의 속성과 중복될 경우 덮어씁니다.

다음은 Object.assign 메서드의 사용 예시입니다:

```javascript
const target = { a: 1, b: 2 };
const source = { b: 4, c: 5 };

const result = Object.assign(target, source);

console.log(target); // { a: 1, b: 4, c: 5 }
console.log(result); // { a: 1, b: 4, c: 5 }
```

위 예시에서 target 객체에 source 객체의 속성을 복사한 결과를 반환합니다. 소스 객체의 `b` 속성은 target 객체의 `b` 속성을 덮어씌우게 됩니다.

## Object.keys

Object.keys 메서드는 주어진 객체의 속성들을 배열로 반환합니다. 이 배열에는 객체의 열거 가능한 속성들만 포함됩니다.

다음은 Object.keys 메서드의 사용 예시입니다:

```javascript
const object = {
  a: 'foo',
  b: 42,
  c: false
};

const keys = Object.keys(object);

console.log(keys); // ['a', 'b', 'c']
```

위 예시에서 object 객체의 속성들을 배열로 반환하여 keys 변수에 저장합니다. 따라서 keys 변수에는 객체의 속성명인 `a`, `b`, `c`가 문자열로 담기게 됩니다.

## 결론

Object.assign과 Object.keys는 자바스크립트 객체를 다루는데 유용한 메서드입니다. Object.assign을 사용하여 속성을 복사하거나, Object.keys를 사용하여 객체의 속성들을 배열로 추출할 수 있습니다. 이러한 메서드들은 객체 기반의 개발에서 꼭 알아두면 유용하게 사용할 수 있습니다.