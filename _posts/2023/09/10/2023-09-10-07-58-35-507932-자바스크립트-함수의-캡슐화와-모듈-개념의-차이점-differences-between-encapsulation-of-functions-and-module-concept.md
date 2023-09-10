---
layout: post
title: "자바스크립트 함수의 캡슐화와 모듈 개념의 차이점 (Differences between Encapsulation of Functions and Module Concept)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 함수의 캡슐화와 모듈 개념은 코드의 구조화 및 재사용성을 향상시키는 데 도움을 주는 중요한 개념입니다. 이 두 가지 개념은 비슷해 보일 수 있지만 실제로 목적과 사용법에서 차이가 있습니다. 이번 글에서는 자바스크립트 함수의 캡슐화와 모듈 개념의 차이점을 알아보겠습니다.

## 1. 캡슐화 (Encapsulation) 의미

캡슐화는 함수를 사용하여 데이터와 기능을 하나로 묶는 것을 의미합니다. 자바스크립트에서 캡슐화를 통해 변수와 함수를 하나의 객체에 담아 외부로부터 보호할 수 있습니다. 이는 변수와 함수들이 객체 내부에 존재하므로 외부에서 직접 접근하지 못하고 객체를 통한 간접 접근만 가능하게 됩니다.

```javascript
function Calculator() {
  var result = 0;

  function add(num) {
    result += num;
  }

  function subtract(num) {
    result -= num;
  }

  function getResult() {
    return result;
  }

  return {
    add: add,
    subtract: subtract,
    getResult: getResult
  };
}

var calculator = Calculator();
calculator.add(5);
calculator.subtract(3);
console.log(calculator.getResult()); // 2
```

위의 예시에서 `Calculator` 함수는 `add`, `subtract`, `getResult`라는 세 가지 함수를 내부에 가지고 있습니다. 이 함수들은 `result`라는 변수와 함께 객체로 반환되어 외부에서 사용됩니다. 이렇게 함수들이 캡슐화되어 외부에 단 하나의 인터페이스를 제공하므로 코드의 유지보수성과 재사용성을 높일 수 있습니다.

## 2. 모듈 (Module) 개념의 의미

모듈은 프로그램을 구성하는 독립적인 구성 요소를 의미하며, 다른 코드와 격리되어 작동합니다. 자바스크립트에서 모듈은 캡슐화된 함수를 사용하여 구현할 수 있습니다. 모듈은 독립적인 네임스페이스를 가지기 때문에 전역 네임스페이스의 충돌 문제를 방지할 수 있습니다.

```javascript
var calculatorModule = (function () {
  var result = 0;

  function add(num) {
    result += num;
  }

  function subtract(num) {
    result -= num;
  }

  function getResult() {
    return result;
  }

  return {
    add: add,
    subtract: subtract,
    getResult: getResult
  };
})();

calculatorModule.add(5);
calculatorModule.subtract(3);
console.log(calculatorModule.getResult()); // 2
```

위의 예시에서 `calculatorModule` 변수는 익명 즉시 실행 함수로 생성된 객체를 가리킵니다. 이 객체는 `add`, `subtract`, `getResult`라는 외부에 노출된 함수들을 가지고 있습니다. 이렇게 모듈을 사용하면 전역 네임스페이스를 더 깔끔하게 유지하고, 코드의 재사용성과 유지보수성을 개선할 수 있습니다.

## 3. 캡슐화와 모듈 개념의 차이점

- **목적**: 캡슐화는 함수와 변수를 객체로 묶어 데이터와 기능을 관리하고 외부로부터 보호하는 데 목적이 있습니다. 모듈은 독립적인 구성 요소로서 격리되는 데 목적이 있습니다.
- **구현 방법**: 캡슐화는 함수를 사용하여 객체를 반환하는 방식으로 구현됩니다. 모듈은 캡슐화된 함수를 즉시 실행하여 생성된 객체를 변수에 할당하는 방식으로 구현됩니다.
- **네임스페이스**: 캡슐화된 함수는 전역 네임스페이스에 존재하며, 객체의 속성을 통해 접근됩니다. 모듈은 독립적인 네임스페이스를 가지므로 전역 네임스페이스의 충돌 문제를 방지합니다.

캡슐화와 모듈은 자바스크립트에서 코드의 구조화, 재사용성, 유지보수성을 향상시키는 중요한 개념입니다. 올바르게 이해하고 적절하게 적용함으로써 코드의 품질과 개발 생산성을 향상시킬 수 있습니다.