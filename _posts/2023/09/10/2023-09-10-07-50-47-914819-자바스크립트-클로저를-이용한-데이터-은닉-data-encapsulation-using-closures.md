---
layout: post
title: "자바스크립트 클로저를 이용한 데이터 은닉 (Data Encapsulation using Closures)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

클로저는 자바스크립트에서 매우 강력하고 유용한 개념입니다. 그 중 하나인 데이터 은닉은 객체지향 프로그래밍에서 중요한 개념 중 하나입니다. 자바스크립트 클로저를 이용하여 데이터를 은닉하고 보호하는 방법에 대해 알아보겠습니다.

## 클로저(Closures)란?

클로저는 함수와 그 함수가 선언된 렉시컬 환경의 조합입니다. 클로저는 외부 함수에 접근할 수 있는 내부 함수로 구성됩니다. 내부 함수는 외부 함수의 변수에 접근할 수 있으며, 외부 함수가 반환된 후에도 그 변수에 접근할 수 있습니다.

자바스크립트에서 클로저를 사용하면 내부 변수를 외부로 공개하지 않고도 접근할 수 있습니다. 이것은 데이터의 은닉에 매우 유용합니다.

## 데이터 은닉 (Data Encapsulation)이란?

데이터 은닉은 객체의 상태를 외부에서 접근하지 못하도록 하는 것을 의미합니다. 이는 객체의 내부 상태를 보호하고 결합도를 낮추는 역할을 합니다. 데이터 은닉을 사용하면 객체의 내부 데이터를 직접 변경하는 것을 방지할 수 있으며, 객체의 내부 로직이 외부에 노출되지 않습니다.

## 클로저를 이용한 데이터 은닉 예제

```javascript
function Counter() {
  let count = 0;

  function increase() {
    count++;
    console.log(count);
  }

  function decrease() {
    count--;
    console.log(count);
  }

  return {
    increase,
    decrease,
  };
}

let counter = Counter();
counter.increase(); // 1
counter.increase(); // 2
counter.decrease(); // 1
```

위 예제에서 `Counter` 함수에서는 `count`라는 변수를 선언하고, 내부 함수로 `increase`와 `decrease`를 정의합니다. 이렇게 함으로써 `count` 변수는 외부에서 접근할 수 없는 상태가 됩니다.

`Counter` 함수는 객체를 반환하며, 반환된 객체에는 `increase`와 `decrease` 함수가 포함되어 있습니다. 외부에서는 `increase`와 `decrease` 함수를 통해 `count` 변수의 값을 변경할 수 있으며, `increase` 함수를 호출할 때마다 `count` 변수가 증가하고, `decrease` 함수를 호출할 때마다 `count` 변수가 감소합니다.

이 예제에서 `count` 변수는 클로저의 일부이기 때문에 외부에서 직접 접근할 수 없고, 오직 `increase`와 `decrease` 함수를 통해만 접근할 수 있습니다. 이로써 `count` 변수는 데이터 은닉이 되며, 외부에서는 `increase`와 `decrease` 함수를 통해 제한된 방식으로만 `count` 변수에 접근할 수 있습니다.

## 결론

자바스크립트 클로저는 데이터 은닉을 구현하는 데 매우 유용한 도구입니다. 클로저를 이용하여 외부에서 직접 접근할 수 없는 내부 변수를 만들고, 제한된 방식으로만 접근할 수 있도록 할 수 있습니다. 이를 통해 객체의 내부 상태를 보호하고, 코드의 결합도를 낮추는 등의 이점을 얻을 수 있습니다.