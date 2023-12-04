---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 에러 경계(Error Boundary) 구현 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [reactjs]
comments: true
share: true
---

React는 에러 경계(Error Boundary) 기능을 통해 애플리케이션 전체를 오류로부터 보호하는 기능을 제공합니다. 에러 경계는 하위 컴포넌트에서 발생한 오류를 감지하고 이를 처리하는 역할을 합니다. 이러한 에러 경계를 구현하기 위해 `React.forwardRef()`를 활용할 수 있습니다.

## `React.forwardRef()`란?

`React.forwardRef()`는 React 컴포넌트를 반환하는 함수를 만들 때 사용되는 API입니다. 이를 사용하면 자식 컴포넌트에서 부모 컴포넌트로 ref를 직접 전달할 수 있습니다.

## 에러 경계 컴포넌트 생성

에러 경계 컴포넌트는 `componentDidCatch()` 메서드를 사용하여 하위 컴포넌트에서 발생하는 오류를 감지하고 처리합니다. 아래는 `componentDidCatch()` 메서드를 이용한 에러 경계 컴포넌트의 예제입니다.

```jsx
import React, { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  componentDidCatch(error, errorInfo) {
    this.setState({ hasError: true });
    // 에러 로깅 or 에러 리포팅 서비스로 전송
  }

  render() {
    if (this.state.hasError) {
      return <h1>앗! 오류가 발생했습니다.</h1>;
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
```

위의 예제에서 `componentDidCatch()` 메서드에서는 `hasError`라는 상태 값을 변경하여 오류가 발생했음을 알립니다. 그리고 `render()` 메서드에서 `hasError` 상태 값에 따라 에러 메시지를 출력하거나 자식 컴포넌트를 반환합니다.

## 에러 경계 컴포넌트 활용

이제 위에서 만든 에러 경계 컴포넌트를 사용하여 실제 컴포넌트를 감싸고 오류를 처리할 수 있습니다. 아래는 `ErrorBoundary` 컴포넌트를 사용한 예제입니다.

```jsx
import React from 'react';
import ErrorBoundary from './ErrorBoundary';

const App = () => {
  return (
    <div>
      <h1>애플리케이션</h1>
      <ErrorBoundary>
        <SomeComponent />
      </ErrorBoundary>
    </div>
  );
};

export default App;
```

위의 코드에서 `SomeComponent` 컴포넌트가 오류를 발생시킬 수 있는 부분이 있다면, `ErrorBoundary` 컴포넌트가 이를 감지하고 오류를 처리합니다.

## 결론

`React.forwardRef()`를 사용한 에러 경계(Error Boundary) 컴포넌트의 구현 방법에 대해 알아보았습니다. 이를 통해 애플리케이션 전체를 오류로부터 보호하고 오류 처리를 간편하게 할 수 있습니다. 자세한 내용은 [React 공식 문서](https://reactjs.org/docs/error-boundaries.html)를 참고하시기 바랍니다.

#React #에러경계