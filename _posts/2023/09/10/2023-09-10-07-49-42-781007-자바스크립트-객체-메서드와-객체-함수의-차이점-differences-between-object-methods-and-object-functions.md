---
layout: post
title: "자바스크립트 객체 메서드와 객체 함수의 차이점 (Differences between Object Methods and Object Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 객체는 데이터와 해당 데이터를 조작하는 동작을 포함하는 속성들의 집합입니다. 객체 내의 동작은 메서드 또는 함수로 구현될 수 있습니다. 하지만 객체 메서드와 객체 함수 사이에는 몇 가지 중요한 차이점이 있습니다.

## 객체 메서드 (Object Methods)

**객체 메서드**란, 객체에 속한 함수를 의미합니다. 이러한 함수는 해당 객체의 속성을 조작하거나, 객체에 대한 동작을 수행합니다. 일반적으로 메서드는 객체 내부에 정의되어 있으며, 객체의 속성으로서 접근할 수 있습니다.

예를 들어, 자동차 객체의 메서드로 "시동 걸기"라는 동작을 정의할 수 있습니다. 이 메서드는 자동차 객체가 가지고 있는 속성인 "엔진 상태"를 조작하게 됩니다.

```javascript
let car = {
  engineStatus: "off",
  startEngine: function() {
    this.engineStatus = "on";
    console.log("Engine started!");
  }
};

car.startEngine(); // Output: Engine started!
console.log(car.engineStatus); // Output: on
```

위 예제에서, `startEngine`은 `car` 객체의 메서드입니다. `startEngine` 메서드는 자동차의 `engineStatus` 속성을 조작하며, "Engine started!"라는 메시지를 출력합니다.

## 객체 함수 (Object Functions)

**객체 함수**는 객체와 독립적으로 정의된 함수입니다. 객체 함수는 객체 자체를 인자로 받아 해당 객체의 속성을 조작하거나, 객체에 대한 동작을 수행합니다. 객체 함수는 객체와는 별도로 정의되므로, 일반 함수 호출과 동일한 방식으로 사용됩니다.

아래 예제는 앞선 자동차 예제에서 `startEngine`을 객체 함수로 변경한 코드입니다.

```javascript
function startEngine(car) {
  car.engineStatus = "on";
  console.log("Engine started!");
}

let car = {
  engineStatus: "off"
};

startEngine(car); // Output: Engine started!
console.log(car.engineStatus); // Output: on
```

위 예제에서, `startEngine`은 객체 함수로 정의되었습니다. 이 함수는 자동차 객체를 인자로 받아 `engineStatus` 속성을 조작하며, "Engine started!"라는 메시지를 출력합니다. 

`startEngine` 함수는 객체 함수이기 때문에 객체와 단독으로 호출될 수 있습니다. 이는 객체 메서드와 대조적인 특징입니다.

## 결론

자바스크립트에서 객체 메서드와 객체 함수는 객체의 동작을 구현하는 데 사용됩니다. 차이점은 객체 메서드는 객체 내부에 정의되어 객체에 속한 함수로서 사용되는 반면, 객체 함수는 객체와는 별개로 정의되어 독립적으로 사용됩니다. 이러한 차이점을 이해하고 적절하게 활용함으로써 자바스크립트 객체를 효과적으로 조작하고 다룰 수 있습니다.