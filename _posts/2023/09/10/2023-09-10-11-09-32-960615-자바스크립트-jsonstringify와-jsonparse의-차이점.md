---
layout: post
title: "자바스크립트 JSON.stringify()와 JSON.parse()의 차이점"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

JSON(JavaScript Object Notation)은 데이터 교환을 위해 널리 사용되는 형식입니다. 자바스크립트에서는 JSON 데이터를 처리하기 위해 `JSON.stringify()`와 `JSON.parse()` 메서드를 제공합니다. 이 두 메서드는 각각 JSON 데이터를 문자열로 변환하고 문자열을 JSON 객체로 파싱하는데 사용됩니다. 하지만 `JSON.stringify()`와 `JSON.parse()`는 목적과 반환값에서 차이가 있습니다.

## `JSON.stringify()`

`JSON.stringify()` 메서드는 JavaScript 객체를 JSON 문자열로 변환합니다. 이 메서드를 사용하여 객체를 문자열로 직렬화할 수 있습니다. 다음은 `JSON.stringify()`의 사용 예시입니다.

```javascript
const obj = { name: "John", age: 30 };
const jsonString = JSON.stringify(obj);
console.log(jsonString); // "{"name":"John","age":30}"
```

위의 예시에서 `obj` 객체는 `JSON.stringify()`를 사용하여 JSON 문자열로 변환됩니다. `jsonString` 변수에 할당된 문자열은 JSON 형식을 따릅니다.

`JSON.stringify()` 메서드는 선택적으로 변환할 속성을 필터링하거나 들여쓰기된 형식으로 출력하는 인수를 전달할 수 있습니다. 더 자세한 내용은 공식 [문서](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify)를 참조하세요.

## `JSON.parse()`

`JSON.parse()` 메서드는 JSON 문자열을 JavaScript 객체로 변환합니다. 이 메서드는 문자열을 파싱하여 JSON 형식을 따르는 객체로 변환합니다. 다음은 `JSON.parse()`의 사용 예시입니다.

```javascript
const jsonString = '{"name":"John","age":30}';
const obj = JSON.parse(jsonString);
console.log(obj); // { name: 'John', age: 30 }
```

위의 예시에서 `jsonString` 변수에 할당된 JSON 문자열은 `JSON.parse()`를 사용하여 자바스크립트 객체로 변환됩니다.

`JSON.parse()` 메서드는 선택적으로 변환 후에 수행할 리바이스(Reviver) 함수를 전달할 수도 있습니다. 리바이스 함수는 각 값을 변환하거나 필터링하는 데 사용될 수 있습니다. 더 자세한 내용은 공식 [문서](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse)를 참조하세요.

## 요약

`JSON.stringify()`와 `JSON.parse()`는 JSON 데이터와 자바스크립트 간의 상호 작용에 사용되는 중요한 메서드입니다.

- `JSON.stringify()`는 자바스크립트 객체를 JSON 문자열로 직렬화합니다.
- `JSON.parse()`는 JSON 문자열을 자바스크립트 객체로 파싱합니다.

이 두 메서드를 활용하여 프런트엔드 또는 백엔드 개발 시 JSON 데이터의 변환과 처리를 용이하게 할 수 있습니다.