---
layout: post
title: "[javascript] Immutable.js에서 Collection 자료구조를 사용하는 방법은 어떻게 되나요?"
description: " "
date: 2023-11-30
tags: [javascript]
comments: true
share: true
---

Immutable.js는 변경 불가능한 자료구조를 제공하는 라이브러리입니다. Collection 자료구조를 사용하여 데이터를 효율적으로 관리할 수 있습니다.

먼저, Immutable.js를 설치하고 가져옵니다. 

```javascript
npm install immutable
```

```javascript
import { List, Map } from 'immutable';
```

List는 배열과 비슷한 자료구조이며, Map은 객체와 유사한 자료구조입니다.

List의 예시를 살펴보겠습니다.

```javascript
const list1 = List([1, 2, 3]);
const list2 = list1.push(4, 5, 6);
console.log(list1); // List [ 1, 2, 3 ]
console.log(list2); // List [ 1, 2, 3, 4, 5, 6 ]
```

위의 코드에서 `push` 메서드를 사용하여 새로운 요소를 추가할 수 있습니다. 하지만, 기존의 리스트는 변경되지 않고 새로운 리스트가 반환됩니다.

Map의 예시를 살펴보겠습니다.

```javascript
const map1 = Map({ a: 1, b: 2, c: 3 });
const map2 = map1.set('b', 4);
console.log(map1); // Map { 'a': 1, 'b': 2, 'c': 3 }
console.log(map2); // Map { 'a': 1, 'b': 4, 'c': 3 }
```

위의 코드에서 `set` 메서드를 사용하여 값을 변경할 수 있습니다. 역시 기존의 맵은 변경되지 않고 새로운 맵이 반환됩니다.

Immutable.js의 Collection 자료구조는 내부적으로 구조 공유(structural sharing)를 사용하여 변경된 부분만 복사하여 메모리를 절약합니다. 이는 대규모의 데이터를 효과적으로 다루는 데 도움이 됩니다.

Immutable.js는 불변성을 유지하면서 데이터를 효율적으로 다룰 수 있는 강력한 도구입니다. Collection 자료구조를 사용하여 변경 불가능한 상태를 유지하면서 데이터를 조작할 수 있습니다.

더 자세한 내용은 [Immutable.js 공식 문서](https://immutable-js.github.io/immutable-js/)를 참고하세요.