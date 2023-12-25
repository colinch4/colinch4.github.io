---
layout: post
title: "[react] JSX에서 라이프사이클, getDerivedStateFromError 사용하기"
description: " "
date: 2023-12-26
tags: [react]
comments: true
share: true
---

JSX 및 React 컴포넌트의 라이프사이클을 잘 이해하고 사용하는 것은 React 애플리케이션을 개발하는 데 매우 중요합니다. 이번에는 JSX에서 라이프사이클을 다루는 방법과 `getDerivedStateFromError` 라이프사이클 메서드의 활용에 대해 알아보겠습니다.

## 라이프사이클 메서드란?

라이프사이클 메서드는 React 컴포넌트가 생성될 때부터 파괴될 때까지의 생명주기 동안 특정한 시점에 호출되는 메서드입니다. 이를 통해 컴포넌트의 상태 변화 및 UI 업데이트 등을 관리할 수 있습니다. 이 중에서 오류 처리를 위해 사용되는 `getDerivedStateFromError` 메서드에 대해 자세히 살펴보겠습니다.

## getDerivedStateFromError 메서드

`getDerivedStateFromError` 메서드는 자식 컴포넌트에서 발생한 오류를 처리하는 데 사용됩니다. 이 메서드는  React v16.6에서 새롭게 추가되었으며, 렌더링 중 발생한 자식 컴포넌트의 오류를 처리하여 UI를 업데이트할 때 유용합니다.

```jsx
static getDerivedStateFromError(error) {
  // 오류 처리 로직 작성
  return { hasError: true };
}
```

위 예제에서 `getDerivedStateFromError` 메서드는 오류가 발생했을 때 호출되며, 오류 처리 로직을 작성하여 `hasError` 상태를 true로 업데이트합니다. 이를 통해 UI를 오류 상태에 맞게 조정할 수 있습니다.

## 사용 예시

아래는 `getDerivedStateFromError` 메서드를 사용한 예시입니다.

```jsx
class MyErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children;
  }
}

class App extends React.Component {
  render() {
    return (
      <MyErrorBoundary>
        <MyComponent />
      </MyErrorBoundary>
    );
  }
}
```

`MyErrorBoundary` 컴포넌트는 `getDerivedStateFromError` 메서드를 사용하여 자식 컴포넌트에서 발생한 오류이 있다면 해당 오류를 처리하고 오류 상태를 UI에 반영합니다.

## 결론

JSX에서 라이프사이클을 다루는 것은 React 애플리케이션의 안정성과 성능을 유지하는 데 중요합니다. `getDerivedStateFromError` 메서드를 활용하여 오류 처리를 보다 효율적으로 구현할 수 있으니, 필요에 따라 적절히 활용해 보시기 바랍니다.

참고: [React 공식 문서 - 오류 경계](https://ko.reactjs.org/docs/error-boundaries.html)

---
*본 블로그 포스트는 React 공식 문서를 참고하여 작성되었습니다.*