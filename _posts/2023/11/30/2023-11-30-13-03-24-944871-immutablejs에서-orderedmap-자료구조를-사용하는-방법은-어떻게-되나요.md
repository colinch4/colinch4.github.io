---
layout: post
title: "[javascript] Immutable.js에서 OrderedMap 자료구조를 사용하는 방법은 어떻게 되나요?"
description: " "
date: 2023-11-30
tags: [javascript]
comments: true
share: true
---

OrderedMap을 사용하기 위해서는 먼저 Immutable 라이브러리를 설치해야 합니다. 다음의 명령을 실행하여 Immutable 라이브러리를 설치합니다.

```javascript
npm install immutable
```

설치가 완료되었다면, Immutable.js를 다음과 같이 가져올 수 있습니다.

```javascript
import { OrderedMap } from 'immutable';
```

이제 OrderedMap을 사용하여 데이터를 생성하고 수정하는 방법을 살펴보겠습니다.

#### OrderedMap 생성하기
```javascript
const orderedMap = OrderedMap({
  key1: 'value1',
  key2: 'value2',
  key3: 'value3'
});
```

#### 값 추가하기/수정하기
```javascript
const updatedMap = orderedMap.set('key4', 'value4');
```

#### 값 가져오기
```javascript
const value = orderedMap.get('key1');
```

#### 모든 키-값 쌍 가져오기
```javascript
const entries = orderedMap.entries();
```

OrderedMap은 불변성을 유지하므로 값을 수정하려면 항상 `set()` 메서드를 통해 새로운 OrderedMap을 반환받아야 합니다.

이렇게 OrderedMap을 사용하여 데이터를 관리할 수 있습니다. Immutable.js에는 다양한 자료구조와 메서드가 제공되므로, 자세한 내용은 [Immutable.js 공식 문서](https://immutable-js.github.io/immutable-js/)를 참조하시기 바랍니다.