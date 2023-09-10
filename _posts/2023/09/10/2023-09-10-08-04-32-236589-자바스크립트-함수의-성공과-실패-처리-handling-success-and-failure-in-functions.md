---
layout: post
title: "자바스크립트 함수의 성공과 실패 처리 (Handling Success and Failure in Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 함수를 사용하여 작업을 수행할 때, 성공과 실패를 올바르게 처리하는 것은 매우 중요합니다. 이 글에서는 자바스크립트 함수에서 성공과 실패를 처리하는 방법을 알아보겠습니다.

## 성공 처리 (Handling Success)

성공적인 작업을 처리하는 함수는 다양한 방식으로 구현될 수 있습니다. 가장 일반적인 방법은 **콜백**을 사용하는 것입니다. 콜백은 함수의 실행이 완료되면 호출되는 함수로, 결과를 전달하거나 추가 작업을 수행할 수 있습니다. 예를 들어, 파일을 읽는 함수가 있다고 가정해봅시다.

```javascript
function readFile(filePath, callback) {
  // 파일을 읽는 작업을 수행하는 코드
  // 성공적으로 작업을 완료했다면 콜백함수를 호출하고 결과를 전달합니다.
  callback(null, result);
}

readFile("/path/to/file.txt", function(err, data) {
  if (err) {
    console.error("파일을 읽는 도중 오류가 발생했습니다.", err);
  } else {
    console.log("파일을 성공적으로 읽었습니다.", data);
  }
});
```

위 예제에서 `readFile` 함수는 파일을 읽는 작업을 수행하고, 작업이 성공적으로 완료되면 콜백 함수를 호출합니다. 만약 작업이 실패하면, 콜백 함수에 오류 정보가 전달됩니다.

또 다른 방법은 **프로미스**를 사용하는 것입니다. 프로미스는 비동기 작업의 상태를 나타내며, 성공적인 완료 또는 실패를 나타내는 결과를 가질 수 있습니다. 위 예제를 프로미스로 다시 작성해보겠습니다.

```javascript
function readFile(filePath) {
  return new Promise((resolve, reject) => {
    // 파일을 읽는 작업을 수행하는 코드
    // 작업이 성공적으로 완료되면 resolve 함수를 호출합니다.
    // 작업이 실패하면 reject 함수를 호출합니다.
  });
}

readFile("/path/to/file.txt")
  .then((data) => {
    console.log("파일을 성공적으로 읽었습니다.", data);
  })
  .catch((err) => {
    console.error("파일을 읽는 도중 오류가 발생했습니다.", err);
  });
```

위 예제에서 `readFile` 함수는 프로미스를 반환하고, 작업이 성공 또는 실패할 때에는 `resolve`와 `reject` 함수를 호출합니다. `then` 메서드는 성공적인 완료를 처리하고, `catch` 메서드는 실패를 처리합니다.

## 실패 처리 (Handling Failure)

함수가 실패한 경우, 오류를 제대로 처리하는 것은 중요합니다. 두 가지 주요한 방법은 예외를 throw하는 것과 오류를 콜백 또는 프로미스를 통해 전달하는 것입니다.

첫 번째 방법은 **예외**를 throw하는 것입니다. 예외를 throw하면 코드의 흐름이 중단되며, 예외를 처리하는 코드 블록으로 이동합니다.

```javascript
function divide(a, b) {
  if (b === 0) {
    throw new Error("0으로 나눌 수 없습니다.");
  }
  return a / b;
}

try {
  console.log(divide(10, 0));
} catch (err) {
  console.error("오류가 발생했습니다.", err);
}
```

위 예제에서 `divide` 함수는 `b`가 0일 때 예외를 throw합니다. `try-catch` 블록을 사용하여 예외를 처리할 수 있습니다.

두 번째 방법은 **콜백**이나 **프로미스**를 통해 오류를 전달하는 것입니다.

```javascript
function divide(a, b, callback) {
  if (b === 0) {
    callback(new Error("0으로 나눌 수 없습니다."));
  } else {
    callback(null, a / b);
  }
}

divide(10, 0, function(err, result) {
  if (err) {
    console.error("오류가 발생했습니다.", err);
  } else {
    console.log(result);
  }
});
```

위 예제에서 `divide` 함수는 `b`가 0일 때 오류 콜백을 호출하고, 그렇지 않을 경우 결과를 콜백에 전달합니다.

## 결론 (Conclusion)

자바스크립트 함수에서 성공과 실패를 올바르게 처리하는 것은 중요합니다. 성공적인 완료와 실패를 지정하여 작업을 적절히 처리할 수 있습니다. 콜백이나 프로미스를 사용하여 성공과 실패를 처리하거나, 예외를 throw하여 오류를 처리할 수 있습니다. 적절한 방법을 선택하여 코드를 작성하세요.