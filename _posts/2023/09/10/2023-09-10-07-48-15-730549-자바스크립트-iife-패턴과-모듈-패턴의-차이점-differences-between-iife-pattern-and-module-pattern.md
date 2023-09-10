---
layout: post
title: "자바스크립트 IIFE 패턴과 모듈 패턴의 차이점 (Differences between IIFE Pattern and Module Pattern)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 IIFE (Immediately Invoked Function Expression) 패턴과 모듈 패턴은 코드를 구조화하고 변수의 범위를 지정하는 데 사용되는 두 가지 주요한 패턴입니다. 이 블로그 포스트에서는 IIFE 패턴과 모듈 패턴의 차이점을 살펴보고 언제 사용하는지 알아보겠습니다.

## IIFE 패턴

IIFE (즉시 호출되는 함수 표현식) 패턴은 함수를 정의하고 바로 호출하는 패턴입니다. 이 패턴은 전역 범위에서 변수 충돌을 방지하고 비공개 변수를 생성하기 위해 주로 사용됩니다. IIFE 패턴은 다음과 같은 형태로 작성됩니다.

```javascript
(function() {
  // IIFE의 내부 코드
})();
```

IIFE 패턴은 함수 표현식을 괄호로 둘러싸고 바로 함수를 호출하는 방식으로 동작합니다. 이를 통해 함수 내부에서 선언된 변수들은 IIFE 외부에서 접근할 수 없습니다. 다음은 IIFE 패턴의 예시입니다.

```javascript
(function() {
  var privateVariable = "I am private";

  console.log(privateVariable); // "I am private"
})();

console.log(privateVariable); // ReferenceError: privateVariable is not defined
```

IIFE 패턴은 간단하고 캡슐화를 지원하는 방식으로 코드를 구조화할 때 유용합니다.

## 모듈 패턴

모듈 패턴은 코드를 모듈화하여 재사용 가능한 코드 조각을 생성하기 위해 주로 사용됩니다. 모듈 패턴은 클로저를 활용하여 비공개 변수를 생성하고, 외부에서 접근 가능한 공개 함수를 제공합니다. 모듈 패턴은 다음과 같은 형태로 작성됩니다.

```javascript
var moduleName = (function() {
  var privateVariable = "I am private";

  function privateFunction() {
    console.log(privateVariable);
  }

  return {
    publicFunction: function() {
      privateFunction();
    }
  };
})();
```

위의 예시에서 `moduleName`은 모듈을 나타내는 변수이며, `publicFunction`은 외부에서 접근 가능한 공개 함수입니다. 모듈 내부에서 선언된 `privateVariable`과 `privateFunction`은 모듈 외부에서 접근할 수 없습니다. 다음은 모듈 패턴의 사용 예시입니다.

```javascript
console.log(moduleName.privateVariable); // undefined
moduleName.publicFunction(); // "I am private"
```

모듈 패턴은 코드를 모듈화하여 재사용성을 높이고 변수의 범위를 제어할 수 있는 강력한 패턴입니다.

## IIFE와 모듈 패턴의 차이점

이제 IIFE 패턴과 모듈 패턴의 주요 차이점을 살펴보겠습니다.

1. **변수의 범위**:
   - IIFE 패턴: IIFE 내부에서 선언된 변수는 IIFE 외부에서 접근할 수 없습니다.
   - 모듈 패턴: 공개 함수를 통해 모듈 내부 변수에 접근할 수 있습니다.

2. **재사용성**:
   - IIFE 패턴: 주로 코드를 구조화하고 캡슐화하는 데 사용됩니다.
   - 모듈 패턴: 재사용 가능한 코드 조각을 생성하여 모듈화하는 데 사용됩니다.

3. **코드 구조**:
   - IIFE 패턴: 단일 함수로 구성되어 있으며, IIFE 패턴이 전체 코드 구조를 형성합니다.
   - 모듈 패턴: 여러 개의 비공개 변수와 함수로 구성되며, 공개 함수를 통해 외부에서 접근할 수 있습니다.

각 패턴은 다른 상황에서 효율적으로 사용되는 경우가 있으므로, 코드의 목적과 요구 사항에 맞게 선택해야 합니다.

이제 자바스크립트에서 IIFE 패턴과 모듈 패턴의 차이점을 이해하셨으니, 코드 구조화와 변수 범위 지정에 유용한 이러한 패턴을 사용해보세요!