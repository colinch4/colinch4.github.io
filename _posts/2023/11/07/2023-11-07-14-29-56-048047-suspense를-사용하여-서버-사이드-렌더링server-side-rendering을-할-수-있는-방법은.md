---
layout: post
title: "Suspense를 사용하여 서버 사이드 렌더링(Server-side rendering)을 할 수 있는 방법은?"
description: " "
date: 2023-11-07
tags: [componentdidmount, reactsuspense]
comments: true
share: true
---

서버 사이드 렌더링(Server-side rendering)은 웹 애플리케이션의 초기 로딩 속도를 개선하고 검색 엔진 최적화(SEO)를 향상시키기 위해 사용되는 중요한 기술입니다. Suspense는 React에서 비동기 처리를 단순화하고 컴포넌트의 렌더링을 지연시킬 수 있는 기능으로, 서버 사이드 렌더링과 함께 사용할 수 있습니다. 이 글에서는 Suspense를 사용하여 서버 사이드 렌더링을 할 수 있는 방법을 알아보겠습니다.

## 1. React Server Components 이용하기
React Server Components는 React를 사용하여 서버 사이드 렌더링을 구현하기 위한 새로운 기능입니다. Suspense와 함께 사용되면 컴포넌트의 렌더링을 지연시킬 수 있습니다.

예를 들어, 다음과 같이 Suspense를 사용하여 서버 사이드 렌더링된 컴포넌트를 구현할 수 있습니다:

```jsx
import { Suspense } from 'react';

function ServerRenderedComponent() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <ServerComponent />
    </Suspense>
  );
}
```

위 예제에서는 `Suspense` 컴포넌트로 감싼 `ServerComponent`를 렌더링하고 있습니다. 만약 `ServerComponent`가 서버에서 비동기적으로 데이터를 가져와야 한다면, `fallback` 프로퍼티를 사용하여 로딩 상태를 보여줄 수 있습니다.

## 2. 서버 사이드 렌더링에 대한 코드 스플리팅 적용하기
서버 사이드 렌더링과 코드 스플리팅을 함께 사용하면 초기 로딩 시점에 필요한 컴포넌트들만 렌더링할 수 있습니다. Suspense는 이를 더욱 간단하게 구현할 수 있도록 도와줍니다.

예를 들어, 다음과 같이 코드 스플리팅을 적용한 서버 사이드 렌더링 코드를 작성할 수 있습니다:

```jsx
import { Suspense } from 'react';
import { unstable_createResource as createResource } from 'react-cache';

const fetchData = createResource(async () => {
  const response = await fetch('https://api.example.com/data');
  return response.json();
});

function ServerRenderedComponent() {
  const data = fetchData.read();

  return (
    <Suspense fallback={<div>Loading...</div>}>
      <ComponentWithData data={data} />
    </Suspense>
  );
}
```

위 예제에서는 `createResource` 함수를 사용하여 데이터 가져오기 로직을 정의하고 있습니다. 이를 통해 Suspense를 사용하여 데이터를 로딩하는 동안 로딩 상태를 보여줄 수 있습니다.

## 마무리
위에서 언급한 방법을 사용하여 Suspense를 이용한 서버 사이드 렌더링을 구현할 수 있습니다. Suspense는 React에서 비동기 처리를 효과적으로 다룰 수 있는 강력한 도구입니다. 이를 적절히 활용하여 웹 애플리케이션의 성능과 사용자 경험을 개선할 수 있습니다. 자세한 내용은 React 공식 문서를 참조하시기 바랍니다.

자료 참조:
- [React 공식 문서](https://reactjs.org/docs/react-component.html#componentdidmount)
- [React Server Components](https://reactjs.org/server-components)
- [React Suspense](https://reactjs.org/docs/react-api.html#reactsuspense)