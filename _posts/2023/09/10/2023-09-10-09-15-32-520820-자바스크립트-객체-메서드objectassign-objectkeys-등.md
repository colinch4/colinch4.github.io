---
layout: post
title: "자바스크립트 객체 메서드(Object.assign, Object.keys 등)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 객체를 다루는 것은 매우 중요합니다. 객체는 키와 값으로 이루어진 속성들의 집합이며, 자바스크립트에서는 다양한 메서드를 통해 객체를 다룰 수 있습니다. 이번 글에서는 주로 사용되는 `Object.assign`, `Object.keys`와 같은 자바스크립트 객체의 유용한 메서드들을 알아보겠습니다.

## Object.assign

`Object.assign` 메서드는 객체를 병합하는 데 사용되는 메서드입니다. 이 메서드는 원본 객체와 하나 이상의 소스 객체를 받아서 원본 객체에 소스 객체의 속성들을 병합합니다.

예를 들어, 다음과 같이 사용할 수 있습니다.

```javascript
const target = { name: "John" };
const source = { age: 30 };
const result = Object.assign(target, source);

console.log(result);
// 출력: { name: "John", age: 30 }
```

이 예제에서는 `target` 객체와 `source` 객체를 병합하여 `result` 변수에 저장하였습니다. `target` 객체에는 `name` 속성이 있고, `source` 객체에는 `age` 속성이 있습니다. `Object.assign`을 사용하여 소스 객체인 `source`의 속성들을 `target` 객체에 병합할 수 있습니다. 결과적으로 `result` 객체에는 `name`과 `age` 속성이 모두 포함된 객체가 생성됩니다.

## Object.keys

`Object.keys` 메서드는 객체의 속성들의 키들을 배열로 반환합니다. 이 메서드는 객체의 속성 개수를 파악하거나 객체를 순회하는 데 사용됩니다.

다음은 `Object.keys`를 사용한 예제입니다.

```javascript
const person = {
  name: "John",
  age: 30,
  occupation: "Developer"
};

const keys = Object.keys(person);
console.log(keys);
// 출력: ["name", "age", "occupation"]
```

이 예제에서는 `person` 객체의 속성들을 배열로 반환하는 `Object.keys`를 사용하여 `keys` 변수에 저장합니다. 그리고 `keys` 배열을 출력하면 `name`, `age`, `occupation`과 같은 속성들의 키들이 포함된 배열이 출력됩니다.

`Object.keys`를 사용하면 객체의 속성 개수를 파악하고, 객체를 순회할 수 있어서 유용하게 활용할 수 있습니다.

## 마무리

`Object.assign`, `Object.keys`와 같은 자바스크립트 객체 메서드들을 효과적으로 사용하면 객체를 다루는 작업을 간편하게 할 수 있습니다. 이번 글에서 다룬 메서드 외에도 다양한 자바스크립트 객체 메서드들이 존재하므로, 필요에 따라서 다양한 메서드를 활용해보세요. 객체를 다루는 데 있어서 이러한 메서드들은 매우 유용한 도구입니다.