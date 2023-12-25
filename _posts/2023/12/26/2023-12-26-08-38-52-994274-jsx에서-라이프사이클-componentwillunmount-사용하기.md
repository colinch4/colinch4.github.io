---
layout: post
title: "[react] JSX에서 라이프사이클, componentWillUnmount 사용하기"
description: " "
date: 2023-12-26
tags: [react]
comments: true
share: true
---

React는 **라이프사이클 메서드**를 통해 컴포넌트의 생성부터 소멸까지의 과정을 다룰 수 있습니다. 이것은 컴포넌트가 마운트되거나 언마운트될 때 특정한 동작을 수행하는 데 사용됩니다. 

이 문서에서는 JSX에서 라이프사이클 메서드 중 `componentWillUnmount`을 사용하는 방법에 대해 다룰 예정입니다.

## JSX에서 componentWillUnmount 사용하기

`componentWillUnmount` 메서드는 컴포넌트가 제거되기 전에 실행됩니다. 이 메서드는 컴포넌트가 소멸되기 직전에 정리 작업을 처리하는 데 사용됩니다. 예를 들어, 리소스의 해제나 이벤트 리스너의 제거 등의 작업을 수행할 수 있습니다.

```jsx
class MyComponent extends React.Component {
  componentDidMount() {
    // 컴포넌트 마운트 후 처리할 작업
  }

  componentWillUnmount() {
    // 컴포넌트 소멸 전 수행할 작업
  }

  render() {
    // 컴포넌트 렌더링
  }
}

ReactDOM.render(<MyComponent />, document.getElementById('root'));
```

위의 코드에서 `MyComponent` 클래스 내에 `componentWillUnmount` 메서드를 정의하여 컴포넌트가 제거되기 전에 수행할 작업을 정의할 수 있습니다.

## 마치며

라이프사이클 메서드를 활용하여 React 컴포넌트의 동작을 제어할 수 있습니다. `componentWillUnmount` 메서드는 컴포넌트가 제거되기 전에 필요한 정리 작업을 처리하는 데 유용하게 활용될 수 있습니다.

라이프사이클 메서드에 대한 더 자세한 내용은 공식 React 문서를 참고해주세요.

[React 공식 문서](https://reactjs.org/docs/react-component.html#componentwillunmount)