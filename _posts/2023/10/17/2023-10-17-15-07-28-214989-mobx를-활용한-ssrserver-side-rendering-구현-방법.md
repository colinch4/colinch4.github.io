---
layout: post
title: "MobX를 활용한 SSR(Server-Side Rendering) 구현 방법"
description: " "
date: 2023-10-17
tags: [mobx]
comments: true
share: true
---

React 애플리케이션에서 MobX를 사용하여 Server-Side Rendering(SSR)을 구현하는 방법을 알아보겠습니다.

## MobX란?

MobX는 React 애플리케이션의 상태 관리를 간단하게 만들어주는 상태 관리 라이브러리입니다. 데이터의 변화를 감지하고 상태 업데이트에 대한 반응을 자동으로 처리해줍니다. 이로써 애플리케이션의 상태가 변경될 때 마다 자동으로 화면을 업데이트할 수 있습니다.

## SSR(Server-Side Rendering)

SSR은 서버에서 초기 렌더링을 수행하는 방법으로, 클라이언트와 서버 간의 트래픽을 줄이고 초기 로딩 속도를 향상시키는 장점이 있습니다. React를 사용하는 경우 CSR(Client-Side Rendering) 방식으로 애플리케이션을 개발하기 때문에, 서버에서 React 애플리케이션을 실행하여 초기 렌더링을 수행해야합니다.

## MobX와 SSR

MobX를 SSR과 통합하기 위해서는 아래와 같은 단계를 따라야합니다.

1. 서버 사이드에서 애플리케이션 상태를 초기화합니다.
2. 서버 사이드에서 라우팅 정보를 수집합니다.
3. 서버 사이드에서 애플리케이션을 렌더링하고 초기 상태를 수집합니다.
4. 수집된 초기 상태를 클라이언트에 전달합니다.
5. 클라이언트 사이드에서 애플리케이션을 초기화하고 전달받은 초기 상태를 사용합니다.

이제 각 단계에 대해 자세히 알아보겠습니다.

### 1. 서버 사이드에서 애플리케이션 상태를 초기화합니다.

서버 사이드에서 애플리케이션의 상태를 초기화하기 위해, MobX 스토어를 생성하고 필요한 데이터를 불러옵니다. 이때, 필요한 데이터가 비동기적으로 불러와지는 경우 `async`/`await`를 사용하여 데이터가 로딩될 때까지 기다릴 수 있습니다.

```javascript
import { makeObservable, observable } from 'mobx';

class AppStore {
  @observable data = [];

  constructor() {
    makeObservable(this);
  }

  async fetchData() {
    // 비동기적으로 데이터를 불러옴
    this.data = await fetch('/api/data').then(response => response.json());
  }
}

const store = new AppStore();
await store.fetchData();
```

### 2. 서버 사이드에서 라우팅 정보를 수집합니다.

서버 사이드에서 라우팅 정보를 수집하여 애플리케이션에 사용될 수 있도록 저장해야합니다. 이 방법은 각각의 라우트가 서로 다른 컴포넌트를 가리키도록 설정하는 라우트 구성을 통해 수행됩니다.

### 3. 서버 사이드에서 애플리케이션을 렌더링하고 초기 상태를 수집합니다.

서버 사이드에서 애플리케이션을 렌더링하고 초기 상태를 수집해야합니다. 이를 위해 React의 `renderToString` 함수를 사용하여 애플리케이션을 문자열로 변환하고, MobX 스토어의 현재 상태를 JSON 형식으로 추출합니다.

```javascript
import React from 'react';
import { renderToString } from 'react-dom/server';
import { Provider } from 'mobx-react';

import App from './App';
import { store } from './AppStore';

const html = renderToString(
  <Provider store={store}>
    <App />
  </Provider>
);

const initialState = JSON.stringify(store);
```

### 4. 수집된 초기 상태를 클라이언트에 전달합니다.

서버에서 수집된 초기 상태를 클라이언트에 전달해야합니다. 일반적으로 이는 HTML의 특정 속성 또는 `<script>` 태그를 통해 수행됩니다.

```html
<script>
  const initialState = ${initialState};
  // 클라이언트에서 초기 상태를 사용하기 위한 코드
</script>
```

### 5. 클라이언트 사이드에서 애플리케이션을 초기화하고 전달받은 초기 상태를 사용합니다.

클라이언트 사이드에서는 수집된 초기 상태를 사용하여 애플리케이션을 초기화합니다. MobX의 `store` 함수를 사용하여 초기 상태를 재생성하고, `Provider` 컴포넌트를 통해 애플리케이션에 상태를 주입합니다.

```javascript
import React from 'react';
import { hydrate } from 'react-dom';
import { Provider } from 'mobx-react';

import App from './App';
import { store } from './AppStore';

// 초기 상태를 가져옴
const initialState = window.initialState;

// 애플리케이션을 초기화하고 상태를 주입함
hydrate(
  <Provider store={store.rehydrate(initialState)}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

위의 단계를 따라 MobX를 사용하여 SSR을 구현할 수 있습니다. MobX의 강력한 상태 관리 기능을 활용하여 React 애플리케이션의 성능을 향상시킬 수 있습니다.

## 추가 참고 자료

- [MobX 공식 문서](https://mobx.js.org/README.html)
- [React 공식 문서](https://reactjs.org/)