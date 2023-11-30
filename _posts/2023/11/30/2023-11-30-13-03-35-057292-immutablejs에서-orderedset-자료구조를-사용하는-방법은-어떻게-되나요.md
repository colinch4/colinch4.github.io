---
layout: post
title: "[javascript] Immutable.js에서 OrderedSet 자료구조를 사용하는 방법은 어떻게 되나요?"
description: " "
date: 2023-11-30
tags: [javascript]
comments: true
share: true
---

1. Immutable.js 라이브러리를 프로젝트에 추가합니다. npm을 사용하는 경우, 다음과 같이 명령어를 실행하여 라이브러리를 설치할 수 있습니다:

```shell
npm install immutable
```

2. OrderedSet 자료구조를 사용할 JavaScript 파일에서 Immutable.js를 import 합니다. 다음과 같이 코드를 작성합니다:

```javascript
import { OrderedSet } from 'immutable';
```

3. OrderedSet 인스턴스를 생성하고 값을 추가 또는 제거하는 방법은 다음과 같습니다:

- OrderedSet 생성:
```javascript
const set = OrderedSet([1, 2, 3]);
```

- 값 추가:
```javascript
const newSet = set.add(4);
```

- 값 제거:
```javascript
const newSet = set.delete(2);
```

4. OrderedSet에서 값들에 접근하려면, 다음과 같이 메소드를 사용할 수 있습니다:

- 값들 가져오기:
```javascript
const values = set.values(); // [1, 3, 4]
```

- 값들 순회:
```javascript
set.forEach(value => {
  console.log(value);
});
```

OrderedSet은 중복되지 않는 값들의 순서를 유지하는 자료구조입니다. 값들의 순서가 중요한 경우에 유용하게 사용될 수 있습니다.

더 많은 OrderedSet의 메소드와 사용법에 대해서는 Immutable.js 공식 문서를 참고하시기 바랍니다. [^1^]

[^1^]: Immutable.js 공식 문서: <https://immutable-js.github.io/immutable-js/docs/#/OrderedSet>