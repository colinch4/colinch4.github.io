---
layout: post
title: "[react] JSX에서 라이프사이클, componentDidUpdate 사용하기"
description: " "
date: 2023-12-26
tags: [react]
comments: true
share: true
---

React는 컴포넌트의 상태 변화에 따라 여러 라이프사이클 메서드를 제공합니다. 이 중 `componentDidUpdate`는 컴포넌트의 업데이트 후에 호출되는 메서드로, 이를 통해 업데이트된 상태에 따라 추가적인 작업을 수행할 수 있습니다.

## 라이프사이클 이해하기

라이프사이클은 컴포넌트가 생성되고 동작하는 순서를 의미합니다. React 컴포넌트는 마운트, 업데이트, 소멸과 관련된 여러 라이프사이클 단계를 가지며, 각 단계에서 특정한 로직을 수행할 수 있습니다.

`componentDidUpdate` 메서드는 컴포넌트의 상태나 프로퍼티가 변경되어 업데이트가 발생한 후에 호출됩니다.

## componentDidUpdate 메서드 활용하기

다음은 `componentDidUpdate` 메서드를 사용하여 이전 상태와 새로운 상태를 비교하여 업데이트된 경우에만 추가적인 작업을 수행하는 예제 코드입니다.

```jsx
class MyComponent extends React.Component {
  componentDidUpdate(prevProps, prevState) {
    // 이전 상태와 새로운 상태를 비교하여 업데이트된 경우에만 작업 수행
    if (this.props.someValue !== prevProps.someValue) {
      // 업데이트된 경우에 수행할 작업
    }
  }

  render() {
    // 컴포넌트 렌더링 로직
  }
}
```

위 예제에서 `componentDidUpdate` 메서드를 사용하여 `someValue` 프로퍼티가 변경되었을 때만 추가적인 작업을 수행하는 방법을 보여줍니다.

## 결론

`componentDidUpdate` 메서드를 통해 컴포넌트의 업데이트 후에 필요한 작업을 수행할 수 있으며, 이를 활용하여 React 애플리케이션의 동작을 세밀하게 제어할 수 있습니다.

라이프사이클 메서드에 대한 더 자세한 내용은 [React 공식 문서](https://reactjs.org/docs/react-component.html#componentdidupdate)를 참고하시기 바랍니다.