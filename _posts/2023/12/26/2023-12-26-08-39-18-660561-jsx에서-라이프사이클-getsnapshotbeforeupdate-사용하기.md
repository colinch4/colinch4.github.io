---
layout: post
title: "[react] JSX에서 라이프사이클, getSnapshotBeforeUpdate 사용하기"
description: " "
date: 2023-12-26
tags: [react]
comments: true
share: true
---

React 컴포넌트는 여러 라이프사이클 메서드를 가지고 있어요. 라이프사이클 메서드는 컴포넌트가 생성되고 제거될 때, 그리고 업데이트될 때 특정한 동작을 수행할 수 있도록 도와줘요. **getSnapshotBeforeUpdate**도 마찬가지로 라이프사이클에 속한 하나의 메서드인데, 이 메서드를 이용하면 업데이트되기 전에 UI 변경 사항을 캡쳐할 수 있어요.

## getSnapshotBeforeUpdate 메서드란?

**getSnapshotBeforeUpdate** 메서드는 컴포넌트가 업데이트 되기 직전에 호출되는 메서드에요. 이 메서드를 사용하면 DOM 업데이트가 일어나기 직전의 상태를 캡쳐할 수 있어요. 주로 이전의 scroll 위치 같은 값들을 캡쳐하여, 업데이트 이후에도 유지시키기 위해 활용됩니다.

```jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.myRef = React.createRef();
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    // 컴포넌트 업데이트 이전의 DOM 상태를 캡쳐한다.
    if (prevProps.list.length < this.props.list.length) {
      const list = this.myRef.current;
      return list.scrollHeight - list.scrollTop;
    }
    return null;
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    // snapshot을 이용하여 업데이트 이후에도 스크롤 위치를 유지한다.
    if (snapshot !== null) {
      const list = this.myRef.current;
      list.scrollTop = list.scrollHeight - snapshot;
    }
  }

  render() {
    return <div ref={this.myRef}>{/* content */}</div>;
  }
}
```

위의 코드에서, **getSnapshotBeforeUpdate** 메서드는 **componentDidUpdate** 메서드가 호출될 때 넘겨받은 **snapshot** 파라미터를 이용하여 화면에 보여지는 리스트의 스크롤 위치를 유지시키고 있어요.

## 결론

**getSnapshotBeforeUpdate** 메서드를 사용하면, 컴포넌트가 업데이트되기 전에 DOM 상태를 캡쳐하여 이후에도 일정한 상태를 유지할 수 있어요. 이를 통해 사용자 경험을 더 향상시킬 수 있을 거에요!

## 참고 자료

- [React 공식 문서 - 라이프사이클 메서드](https://ko.reactjs.org/docs/react-component.html#getsnapshotbeforeupdate)