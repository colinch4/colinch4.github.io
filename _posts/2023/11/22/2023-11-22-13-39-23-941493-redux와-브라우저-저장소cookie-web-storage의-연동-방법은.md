---
layout: post
title: "[javascript] Redux와 브라우저 저장소(Cookie, Web Storage)의 연동 방법은?"
description: " "
date: 2023-11-22
tags: [javascript]
comments: true
share: true
---

Redux는 JavaScript 애플리케이션의 상태를 관리하기 위한 상태 관리 라이브러리입니다. 하지만 브라우저 저장소(Cookie, Web Storage)를 통해 데이터를 영구적으로 저장하고자 할 때 Redux와의 연동 방법을 알아야 합니다. 이번 글에서는 Redux와 브라우저 저장소를 연동하는 방법을 알아보겠습니다.

### 1. Redux Persist 라이브러리

Redux Persist는 Redux와 브라우저 저장소를 연동하기 위한 라이브러리입니다. 이를 사용하면 Redux 상태를 브라우저 저장소에 자동으로 저장하고 가져올 수 있습니다.

먼저 Redux Persist를 설치해야 합니다.

```javascript
npm install redux-persist
```

### 2. Redux Persist 설정

Redux Persist를 사용하기 전에 Redux Persist가 루트 리듀서에서 어떤 방식으로 동작해야 하는지 설정해야 합니다.

```javascript
import { persistStore, persistReducer } from 'redux-persist'
import storage from 'redux-persist/lib/storage'

// 기존의 루트 리듀서
import rootReducer from './reducers'

// Redux Persist 설정
const persistConfig = {
  key: 'root',
  storage
}

const persistedReducer = persistReducer(persistConfig, rootReducer)
```

위에서 `persistConfig` 객체를 생성하여 Redux Persist에 필요한 설정을 지정합니다. `key`는 저장소의 키 이름으로 사용됩니다. 이는 저장소에 저장되는 상태의 이름을 의미합니다. `storage`는 브라우저 저장소로 사용할 저장소 객체를 지정합니다. 위의 예제에서는 `redux-persist/lib/storage`에서 제공하는 기본 저장소를 사용하였습니다.

그리고 `persistReducer` 함수를 통해 기존의 루트 리듀서와 Redux Persist 설정을 결합하여 새로운 향상된 리듀서를 생성합니다.

### 3. Persist 스토어 생성

Redux Persist 설정이 완료되면, Redux Store를 생성하기 전에 Redux Persist에 의해 보호되는 Persist 스토어를 생성해야 합니다.

```javascript
import { createStore } from 'redux'
import { persistStore, persistReducer } from 'redux-persist'
import storage from 'redux-persist/lib/storage'

import rootReducer from './reducers'

const persistConfig = {
  key: 'root',
  storage
}

const persistedReducer = persistReducer(persistConfig, rootReducer)

const store = createStore(persistedReducer)
const persistor = persistStore(store)
```

여기서 `persistStore` 함수를 사용하여 Redux Store를 지속시키는 작업을 수행합니다. 이를 통해 Redux 상태가 브라우저 저장소에 저장되고, 새로 고침이나 페이지 이동과 같은 작업에도 상태가 보존됩니다.

### 4. Persist 스토어를 Provider로 제공

마지막으로, 생성한 Persist 스토어를 Redux Provider로 제공하여 애플리케이션에 Redux Persist를 적용합니다.

```javascript
import React from 'react'
import { Provider } from 'react-redux'
import { PersistGate } from 'redux-persist/integration/react'

import store, { persistor } from './store'
import App from './App'

const Root = () => (
  <Provider store={store}>
    <PersistGate loading={null} persistor={persistor}>
      <App />
    </PersistGate>
  </Provider>
)

export default Root
```

위의 예제에서는 `PersistGate` 컴포넌트를 사용하여 Persist 스토어를 부모 컴포넌트로 제공하고, 로딩 중일 때 어떤 컴포넌트를 표시할지 설정할 수 있습니다. `persistor`는 이전 단계에서 생성한 Persist 스토어입니다.

이제 Redux Persist가 브라우저 저장소와 연동되어, Redux 상태가 지속되도록 설정되었습니다.

### 참고 자료

- [Redux Persist GitHub 저장소](https://github.com/rt2zz/redux-persist)
- [Redux Persist 공식 문서](https://github.com/rt2zz/redux-persist)