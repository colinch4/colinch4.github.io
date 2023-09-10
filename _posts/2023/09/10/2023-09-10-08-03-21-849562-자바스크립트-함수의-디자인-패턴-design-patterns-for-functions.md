---
layout: post
title: "자바스크립트 함수의 디자인 패턴 (Design Patterns for Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트는 매우 유연한 프로그래밍 언어이기 때문에 함수를 다양한 방식으로 디자인할 수 있습니다. 함수에는 다양한 패턴이 있으며, 이러한 패턴들은 코드의 가독성, 재사용성, 유지보수성을 향상시키는데 도움을 줍니다. 이번 블로그 포스트에서는 자바스크립트 함수의 디자인 패턴에 대해 알아보겠습니다.

## 1. 셀프-인보케이션 패턴 (Self-Invoking Pattern)

셀프-인보케이션 패턴은 함수를 정의함과 동시에 즉시 실행하는 패턴입니다. 이는 함수가 한 번만 실행되어야 하는 경우에 유용합니다.

**예제:**

```javascript
(function() {
  console.log("Hello, World!");
})();
```

이 패턴은 전역 네임스페이스를 오염시키지 않으며, IIFE(Immediately Invoked Function Expression)라고도 불립니다.

## 2. 콜백 패턴 (Callback Pattern)

콜백 패턴은 비동기 작업을 처리하는 경우에 자주 사용되는 패턴입니다. 함수를 다른 함수의 매개변수로 전달하여 작업이 완료된 후에 실행되도록 할 수 있습니다.

**예제:**

```javascript
function fetchData(callback) {
  setTimeout(function() {
    const data = "Hello, World!";
    callback(data);
  }, 1000);
}

function processData(data) {
  console.log("Processed data:", data);
}

fetchData(processData);
```

## 3. 프로미스 패턴 (Promise Pattern)

프로미스는 비동기 작업을 처리하는 데 사용되는 객체입니다. 콜백 패턴보다 유연하고 가독성이 좋으며, 비동기 코드의 흐름을 보다 명확하게 관리할 수 있습니다.

**예제:**

```javascript
function fetchData() {
  return new Promise(function(resolve, reject) {
    setTimeout(function() {
      const data = "Hello, World!";
      resolve(data);
    }, 1000);
  });
}

function processData(data) {
  console.log("Processed data:", data);
}

fetchData().then(processData);
```

## 4. 메모이제이션 패턴 (Memoization Pattern)

메모이제이션은 함수의 결과를 캐시하여 동일한 입력 값에 대해 다시 계산하지 않는 패턴입니다. 이는 반복적으로 호출되는 함수의 성능을 향상시키는데 도움을 줍니다.

**예제:**

```javascript
function fibonacci(n) {
  if (n <= 1) {
    return n;
  } else {
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}

fibonacci = memoize(fibonacci);

console.log(fibonacci(10)); // 55

function memoize(fn) {
  const cache = {};
  return function(n) {
    if (n in cache) {
      return cache[n];
    } else {
      const result = fn(n);
      cache[n] = result;
      return result;
    }
  };
}
```

## 5. 옵저버 패턴 (Observer Pattern)

옵저버 패턴은 객체 간의 일대다 종속성을 정의하는 패턴입니다. 한 객체의 상태가 변경될 때, 의존하는 다른 객체들에게 알림을 보내는 방식으로 작동합니다.

**예제:**

```javascript
class Subject {
  constructor() {
    this.observers = [];
  }

  attach(observer) {
    this.observers.push(observer);
  }

  detach(observer) {
    const index = this.observers.indexOf(observer);
    if (index !== -1) {
      this.observers.splice(index, 1);
    }
  }

  notify() {
    for (const observer of this.observers) {
      observer.update();
    }
  }
}

class Observer {
  constructor(name) {
    this.name = name;
  }

  update() {
    console.log(`Observer ${this.name} has been notified.`);
  }
}

const subject = new Subject();
const observer1 = new Observer("A");
const observer2 = new Observer("B");

subject.attach(observer1);
subject.attach(observer2);
subject.notify();

subject.detach(observer2);
subject.notify();
```

자바스크립트 함수의 디자인 패턴을 통해 코드의 가독성과 유연성을 향상시킬 수 있습니다. 위에서 소개한 패턴들은 자바스크립트 개발에서 자주 사용되는 패턴들이지만, 더 많은 패턴들이 존재합니다. 적절한 패턴을 선택하여 코드를 디자인함으로써 효율적이고 유지보수 가능한 코드를 작성할 수 있습니다.