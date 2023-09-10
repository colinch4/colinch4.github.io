---
layout: post
title: "자바스크립트 함수의 성공과 실패 처리 (Handling Success and Failure in Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 함수를 작성할 때, 성공적으로 실행되었을 때와 실패했을 때 각각 다르게 처리해야 하는 경우가 종종 있습니다. 예를 들어, 서버에서 데이터를 가져와야 하는 경우 성공적으로 데이터를 받아왔을 때는 데이터를 가공하고 화면에 표시해야 하며, 실패했을 때는 에러 처리를 해야 할 수도 있습니다. 이러한 상황에서 함수 내에서 성공과 실패를 처리하는 방법에 대해 알아보도록 하겠습니다.

## 성공적인 경우의 처리 (Handling Success)

성공적으로 실행된 함수에서 반환된 결과를 처리하는 방법은 다양할 수 있습니다. 가장 일반적인 방법 중 하나는 **콜백 함수**를 사용하는 것입니다. 예를 들어, 비동기적으로 데이터를 가져오는 `getData` 함수가 있다고 가정해봅시다.

```javascript
function getData(callback) {
  // 데이터를 비동기적으로 가져오는 코드
  // ...

  // 데이터를 가져왔을 때
  if (data) {
    callback(null, data); // 첫 번째 매개변수는 에러를 전달하지 않음을 의미
  } else {
    callback(new Error('데이터를 가져올 수 없습니다.'), null);
  }
}

function processData(error, data) {
  if (error) {
    console.error('에러가 발생했습니다.', error);
    // 에러 처리 로직
  } else {
    console.log('데이터를 가공하고 화면에 표시합니다.', data);
    // 데이터 가공 및 표시 로직
  }
}

getData(processData);
```

위 예제에서 `getData` 함수가 데이터를 가져와서 성공적으로 가져왔을 경우, 콜백 함수 `processData`에 `null`과 함께 데이터를 전달합니다. 그렇지 않은 경우, `new Error('데이터를 가져올 수 없습니다.')`와 함께 `callback` 함수를 호출하여 에러를 전달합니다. `processData` 함수에서는 `error`를 검사하여 에러가 있는지 확인하고, 있을 경우 에러 처리 로직을 수행합니다. 성공적으로 데이터를 가져왔을 경우에는 데이터를 가공하고 화면에 표시하는 로직을 수행합니다.

## 실패한 경우의 처리 (Handling Failure)

함수에서 실패한 경우에도 적절한 처리가 필요합니다. 실패의 원인에는 다양한 상황이 포함될 수 있으며, 이에 대한 처리 방식도 다양할 수 있습니다. 예를 들어, 파일을 읽어오는 `readFile` 함수가 있을 때, 파일이 존재하지 않는 경우 실패로 간주되고 이를 처리해야 합니다.

```javascript
function readFile(filepath) {
  // 파일을 읽어오는 코드
  // ...

  // 파일을 읽어왔을 때
  if (file) {
    return file;
  } else {
    throw new Error('파일이 존재하지 않습니다.');
  }
}

try {
  const file = readFile('path/to/file.txt');
  // 파일 읽기 성공의 경우 로직
} catch (error) {
  console.error('에러가 발생했습니다.', error);
  // 실패한 경우에 대한 에러 처리 로직
}
```

위 예제에서 `readFile` 함수는 파일을 읽어오는데, 파일이 존재하지 않을 경우 `new Error('파일이 존재하지 않습니다.')`와 함께 에러를 던집니다. 호출하는 부분에서는 `try-catch` 문을 사용하여 `readFile` 함수에서 발생하는 에러를 잡아 처리합니다. 에러가 발생한 경우 `catch` 블록이 실행되며, 실패한 경우에 대한 에러 처리 로직을 수행합니다.

## 결론 (Conclusion)

자바스크립트에서는 함수 내에서 성공과 실패의 경우를 따로 처리하는 방법들이 다양하게 존재합니다. 이 글에서는 콜백 함수를 사용하여 성공적인 경우와 실패한 경우를 처리하는 방법을 알아보았습니다. 성공한 경우에는 콜백 함수를 호출하고 데이터를 전달하며, 실패한 경우에는 적절한 에러를 던지거나, 에러 객체를 생성하여 처리합니다. 적절한 성공과 실패의 처리를 통해 프로그램의 안정성과 신뢰성을 높일 수 있습니다.