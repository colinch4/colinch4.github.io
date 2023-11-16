---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 레이지 로딩(Lazy Loading) 기능을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [react]
comments: true
share: true
---

React.forwardRef()는 React에서 제공하는 특별한 함수이며, 함수형 컴포넌트에서 ref 속성을 사용할 수 있도록 도와줍니다. 이 기능을 활용하여 컴포넌트의 레이지 로딩 기능을 구현할 수 있습니다. 레이지 로딩은 페이지의 초기 로딩 시간을 줄이고 사용자 경험을 향상시킬 수 있는 방법 중 하나입니다. 이제 React에서 React.forwardRef()를 활용하여 컴포넌트의 레이지 로딩을 구현하는 방법을 알아보겠습니다.

## 1. 레이지로딩할 컴포넌트 생성

```jsx
import React from "react";

const LazyComponent = React.lazy(() => import("./LazyComponent"));

const MyComponent = () => {
  return (
    <React.Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </React.Suspense>
  );
};

export default MyComponent;
```

위 코드에서는 `React.lazy()` 함수를 사용하여 `LazyComponent`를 동적으로 가져올 수 있도록 합니다. `MyComponent` 내부에서 `React.Suspense` 컴포넌트를 사용하여 로딩 중에 표시할 fallback 컴포넌트를 지정할 수 있습니다. 로딩 중에는 `<div>Loading...</div>`가 보여지고, 로딩이 완료되면 `LazyComponent`가 렌더링됩니다.

## 2. 컴포넌트에 ref 속성 적용

이제 ref 속성을 사용할 수 있도록 하기 위해 `React.forwardRef()` 함수를 사용하여 `MyComponent`를 수정하겠습니다.

```jsx
import React from "react";

const LazyComponent = React.lazy(() => import("./LazyComponent"));

const MyComponent = React.forwardRef((props, ref) => {
  return (
    <React.Suspense fallback={<div>Loading...</div>}>
      <LazyComponent ref={ref} {...props} />
    </React.Suspense>
  );
});

export default MyComponent;
```

위 코드에서는 `React.forwardRef()`를 사용하여 `ref` 매개변수를 받아들이도록 `MyComponent`를 수정했습니다. 그리고 `LazyComponent`에 `ref={ref}`를 전달하여 ref 속성을 적용하였습니다. 이제 `MyComponent`를 사용할 때 ref를 사용하여 `LazyComponent` 인스턴스에 접근할 수 있습니다.

## 3. 컴포넌트 사용하기

이제 `MyComponent`를 다른 컴포넌트에서 사용해보겠습니다.

```jsx
import React, { useRef, useEffect } from "react";
import MyComponent from "./MyComponent";

const App = () => {
  const myComponentRef = useRef();

  useEffect(() => {
    // myComponentRef를 사용하여 컴포넌트 메서드 호출 또는 인스턴스에 접근할 수 있습니다.
    myComponentRef.current.method();
  }, []);

  return (
    <div>
      <h1>Lazy Loading Example</h1>
      <MyComponent ref={myComponentRef} />
    </div>
  );
};

export default App;
```

위 코드에서는 `MyComponent`를 `App` 컴포넌트에서 사용하고 있습니다. `useRef` 훅을 사용하여 `myComponentRef`를 생성하고, 이를 `MyComponent`의 ref 속성으로 전달합니다. 그리고 `useEffect`를 사용하여 컴포넌트가 렌더링된 후에 `myComponentRef.current`를 사용하여 `MyComponent`의 메서드를 호출하거나 인스턴스에 접근할 수 있습니다.

이제 위의 코드를 실행하면 페이지가 로딩될 때 `LazyComponent`가 동적으로 가져와지는 것을 확인할 수 있습니다. 이렇게 React.forwardRef()를 사용하여 컴포넌트의 레이지 로딩 기능을 구현할 수 있습니다. 자세한 내용은 [공식 React 문서](https://ko.reactjs.org/docs/react-api.html#reactforwardref)를 참조하세요.

#React #레이지로딩