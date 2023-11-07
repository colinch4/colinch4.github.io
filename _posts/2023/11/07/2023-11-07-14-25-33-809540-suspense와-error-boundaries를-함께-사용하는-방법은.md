---
layout: post
title: "Suspense와 Error Boundaries를 함께 사용하는 방법은?"
description: " "
date: 2023-11-07
tags: [reactsuspense]
comments: true
share: true
---

React 16.6 버전 이후로, React에는 **Suspense**와 **Error Boundaries**라는 두 가지 기능이 추가되었습니다. 이들을 함께 사용하면 애플리케이션에서 비동기적으로 로딩되는 컴포넌트나 에러가 발생할 수 있는 컴포넌트를 처리하는 데 도움을 줄 수 있습니다. 이 기능들을 사용하여 사용자 경험을 향상시킬 수 있습니다.

## Suspense란?

Suspense는 React 애플리케이션에서 **비동기 컴포넌트**를 처리하는 데 사용되는 기능입니다. Suspense 컴포넌트는 로딩 중인 컴포넌트가 나타날 때까지 fallback UI를 보여줄 수 있습니다.

```jsx
import React, { Suspense } from 'react';

const MyComponent = React.lazy(() => import('./MyComponent'));

function App() {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <MyComponent />
      </Suspense>
    </div>
  );
}

export default App;
```

Suspense 컴포넌트는 `<Suspense fallback={fallbackUI}>` 형식으로 사용됩니다. `fallbackUI`는 로딩 중인 컴포넌트가 나타날 때까지 보여줄 UI입니다.

## Error Boundaries란?

Error Boundaries는 React 애플리케이션에서 런타임 오류를 처리하는 데 사용되는 기능입니다. Error Boundaries는 컴포넌트 계층 구조의 특정 부분에서 발생하는 에러를 잡아내고 대체 UI를 렌더링할 수 있습니다.

```jsx
import React, { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // 에러 로깅 또는 다른 처리 로직을 추가할 수 있습니다.
  }

  render() {
    if (this.state.hasError) {
      return <div>에러가 발생했습니다.</div>;
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
```

Error Boundary 컴포넌트는 클래스 컴포넌트로 작성되며, `getDerivedStateFromError`와 `componentDidCatch` 메소드를 사용하여 에러를 처리합니다. `render` 메소드에서 에러 발생 여부에 따라 대체 UI를 렌더링합니다.

## Suspense와 Error Boundaries 함께 사용하기

Suspense와 Error Boundaries를 함께 사용하여 컴포넌트 로딩 중 또는 에러 발생 시 대체 UI를 표시할 수 있습니다.

```jsx
import React, { Suspense } from 'react';
import ErrorBoundary from './ErrorBoundary';

const MyComponent = React.lazy(() => import('./MyComponent'));

function App() {
  return (
    <div>
      <ErrorBoundary>
        <Suspense fallback={<div>Loading...</div>}>
          <MyComponent />
        </Suspense>
      </ErrorBoundary>
    </div>
  );
}

export default App;
```

위의 예제에서는 `ErrorBoundary` 컴포넌트로 감싸서 에러 발생 시 대체 UI를 표시하도록 설정했습니다. 이렇게 하면 Suspense 컴포넌트 및 비동기 컴포넌트에서 발생하는 에러를 처리할 수 있습니다.

이렇게 Suspense와 Error Boundaries를 함께 사용하면 애플리케이션에서 비동기 데이터를 로딩하거나, 에러를 처리할 때 사용자에게 더 나은 경험을 제공할 수 있습니다.

---

참고 자료:
- [React 공식 문서 - Suspense](https://reactjs.org/docs/react-api.html#reactsuspense) 
- [React 공식 문서 - Error Boundaries](https://reactjs.org/docs/error-boundaries.html)