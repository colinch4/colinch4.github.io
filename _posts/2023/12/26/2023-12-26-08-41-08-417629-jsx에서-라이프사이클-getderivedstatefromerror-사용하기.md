---
layout: post
title: "[react] JSX에서 라이프사이클, getDerivedStateFromError 사용하기"
description: " "
date: 2023-12-26
tags: [react]
comments: true
share: true
---

React에서는 **라이프사이클 메서드**와 **에러 처리**를 다루는데 유용한 메서드를 제공합니다. **JSX**에서 이를 사용하여 컴포넌트의 상태를 관리하고 에러를 처리할 수 있습니다. 이번 글에서는 JSX에서 라이프사이클을 다루는 방법과 `getDerivedStateFromError` 메서드에 대해 알아보겠습니다. 

## 라이프사이클 메서드란?

라이프사이클 메서드는 React 컴포넌트가 생성, 업데이트, 제거되는 과정에서 호출되는 특정 함수들을 말합니다. 이를 통해 컴포넌트의 상태 변화나 화면 갱신 등을 관리할 수 있습니다.

## getDerivedStateFromError 메서드란?

`getDerivedStateFromError` 메서드는 **에러 경계**를 정의하고 에러를 처리하는 데 사용됩니다. 컴포넌트 하위 트리의 렌더링 중에 오류가 발생하면, `getDerivedStateFromError` 메서드를 사용하여 컴포넌트의 상태를 업데이트할 수 있습니다.

## JSX에서 라이프사이클 메서드 사용하기

JSX에서 라이프사이클 메서드를 사용하려면 class 컴포넌트를 정의하고, 해당 라이프사이클 메서드를 오버라이딩해야 합니다. 

예를 들어, 다음과 같이 `componentDidMount` 메서드를 사용하여 컴포넌트가 마운트된 후에 특정 동작을 수행할 수 있습니다.

```jsx
class MyComponent extends React.Component {
  componentDidMount() {
    // 컴포넌트가 마운트된 후에 실행될 동작들을 정의
  }
}
```

## getDerivedStateFromError 메서드 사용하기

`getDerivedStateFromError` 메서드를 사용하여 하위 컴포넌트에서 발생한 에러를 처리할 수 있습니다. 이 메서드를 사용하면 에러가 발생했을 때 컴포넌트의 상태를 업데이트하여 대체 UI를 렌더링할 수 있습니다.

```jsx
class ErrorBoundary extends React.Component {
  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      return <div>에러가 발생했습니다.</div>;
    }
    return this.props.children;
  }
}
```

`getDerivedStateFromError` 메서드는 에러가 발생했을 때 호출되며, 상태를 업데이트하여 대체 UI를 렌더링하게 됩니다.

## 마무리

이번 글에서는 JSX에서 라이프사이클 메서드와 `getDerivedStateFromError` 메서드의 활용 방법에 대해 알아보았습니다. 라이프사이클 메서드는 컴포넌트의 상태 변화를 관리하고, `getDerivedStateFromError` 메서드는 에러를 처리하는 데 유용하게 활용될 수 있습니다. 이러한 메서드들을 적절히 활용하여 안정적이고 유연한 React 컴포넌트를 구현할 수 있습니다.

더 자세한 내용은 [React 공식문서](https://reactjs.org/docs/react-component.html)를 참고해주세요.