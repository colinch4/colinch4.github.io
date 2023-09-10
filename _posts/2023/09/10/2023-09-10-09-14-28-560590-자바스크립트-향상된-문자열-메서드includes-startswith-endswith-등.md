---
layout: post
title: "자바스크립트 향상된 문자열 메서드(includes, startsWith, endsWith 등)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 제공하는 문자열 메서드는 개발자들이 문자열을 다루고 조작하는 데 매우 유용합니다. 그 중에서도 `includes`, `startsWith`, `endsWith`와 같은 향상된 문자열 메서드는 특히 유용하며, 이번 글에서는 이들 메서드에 대해 자세히 살펴보겠습니다.

## `includes`

`includes` 메서드는 주어진 문자열이 다른 문자열에 포함되어 있는지 확인하는 데 사용됩니다. 이 메서드는 대소문자를 구분하며, 찾으려는 문자열이 포함된 경우 `true`를 반환하고 그렇지 않은 경우 `false`를 반환합니다.

아래는 `includes` 메서드의 간단한 예제입니다.

```javascript
const str = "Hello, World!";

console.log(str.includes("Hello"));  // true
console.log(str.includes("hello"));  // false
console.log(str.includes("World"));  // true
console.log(str.includes("JavaScript"));  // false
```

위의 예제에서 `includes` 메서드는 문자열 `str`에 주어진 문자열이 포함되어 있는지 확인합니다. "Hello"는 대소문자까지 일치하기 때문에 `true`를 반환하지만, "hello"는 소문자로 시작하므로 `false`를 반환합니다.

## `startsWith`

`startsWith` 메서드는 주어진 문자열로 시작하는지 여부를 확인하는 데 사용됩니다. 이 메서드 또한 대소문자를 구분하며, 찾으려는 문자열로 시작하는 경우 `true`를 반환하고 그렇지 않은 경우 `false`를 반환합니다.

아래는 `startsWith` 메서드의 예제입니다.

```javascript
const str = "Hello, World!";

console.log(str.startsWith("Hello"));  // true
console.log(str.startsWith("hello"));  // false
console.log(str.startsWith("World"));  // false
console.log(str.startsWith("H"));  // true
```

위의 예제에서 `startsWith` 메서드는 문자열 `str`이 주어진 문자열로 시작되는지 확인합니다. "Hello"로 시작하므로 `true`를 반환하지만, "hello"로 시작하는 것은 아니므로 `false`를 반환합니다.

## `endsWith`

`endsWith` 메서드는 주어진 문자열로 끝나는지 여부를 확인하는 데 사용됩니다. 이 메서드 역시 대소문자를 구분하며, 찾으려는 문자열로 끝나는 경우 `true`를 반환하고 그렇지 않은 경우 `false`를 반환합니다.

아래는 `endsWith` 메서드의 예제입니다.

```javascript
const str = "Hello, World!";

console.log(str.endsWith("World!"));  // true
console.log(str.endsWith("WORLD!"));  // false
console.log(str.endsWith("!"));  // true
console.log(str.endsWith("d"));  // false
```

위의 예제에서 `endsWith` 메서드는 문자열 `str`이 주어진 문자열로 끝나는지 확인합니다. "World!"로 끝나므로 `true`를 반환하지만, "WORLD!"로 끝나지 않으므로 `false`를 반환합니다.

## 결론

자바스크립트의 향상된 문자열 메서드인 `includes`, `startsWith`, `endsWith`는 문자열을 다룰 때 매우 유용합니다. 이들 메서드를 적절하게 활용하여 문자열의 존재 여부를 확인하거나, 시작 또는 끝을 기준으로 문자열을 검색할 수 있습니다. 개발 과정에서 이러한 메서드를 적절히 활용하면 보다 간편하고 효율적인 코드를 작성할 수 있습니다.