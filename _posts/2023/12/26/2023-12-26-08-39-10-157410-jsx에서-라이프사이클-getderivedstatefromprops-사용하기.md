---
layout: post
title: "[react] JSX에서 라이프사이클, getDerivedStateFromProps 사용하기"
description: " "
date: 2023-12-26
tags: [react]
comments: true
share: true
---

React에서는 컴포넌트가 생성, 업데이트, 파괴되는 과정을 라이프사이클 메소드를 통해 제어할 수 있습니다. JSX를 사용하여 React 컴포넌트 내에서 컴포넌트가 라이프사이클에 따라 상황에 맞게 동작하도록 설정할 수 있습니다. 이번 글에서는 라이프사이클 중 getDerivedStateFromProps 메소드를 다뤄보겠습니다.

## 라이프사이클 메소드란 무엇인가요?

라이프사이클 메소드는 React 컴포넌트가 생성, 업데이트, 파괴될 때 특정한 시점에 호출되는 메소드입니다. 이를 활용하여 컴포넌트의 상태나 UI를 관리할 수 있습니다.

## getDerivedStateFromProps 메소드

`getDerivedStateFromProps` 메소드는 props로 전달받은 값을 state에 동기화하는 역할을 합니다. 이 메소드는 컴포넌트가 생성되거나 업데이트될 때 호출되며, 이를 통해 state를 props에 맞게 업데이트할 수 있습니다.

아래는 `getDerivedStateFromProps` 메소드의 사용 예시입니다.

```jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      derivedValue: ''
    };
  }

  static getDerivedStateFromProps(props, state) {
    // props를 기반으로 state를 업데이트
    if (props.value !== state.derivedValue) {
      return {
        derivedValue: props.value
      };
    }
    // state를 업데이트하지 않는 경우
    return null;
  }

  render() {
    return <div>{this.state.derivedValue}</div>;
  }
}
```

위 예시에서 `getDerivedStateFromProps` 메소드는 `props.value`를 기반으로 `state.derivedValue`를 업데이트합니다. 이를 통해 컴포넌트가 업데이트될 때마다 해당 값을 동기화할 수 있습니다.

## 마무리

`getDerivedStateFromProps` 메소드를 사용하여 React 컴포넌트의 상태를 props와 동기화할 수 있습니다. 이를 통해 컴포넌트의 업데이트 시 상태를 일관되게 유지하고 UI를 제어할 수 있습니다. 라이프사이클 메소드를 활용하여 React 애플리케이션을 보다 효율적으로 관리할 수 있으니, 활용에 참고하시기 바랍니다.

참고 자료:

- [React 공식 문서 - 라이프사이클 메소드](https://ko.reactjs.org/docs/react-component.html#the-component-lifecycle)
- [React 공식 문서 - getDerivedStateFromProps](https://ko.reactjs.org/docs/react-component.html#static-getderivedstatefromprops)