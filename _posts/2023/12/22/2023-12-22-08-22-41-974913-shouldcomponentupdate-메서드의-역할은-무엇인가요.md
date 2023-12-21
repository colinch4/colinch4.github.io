---
layout: post
title: "[react] shouldComponentUpdate 메서드의 역할은 무엇인가요?"
description: " "
date: 2023-12-22
tags: [react]
comments: true
share: true
---

이 메서드를 구현하여 컴포넌트 업데이트의 성능을 최적화할 수 있습니다. 예를 들어, 컴포넌트의 `props`나 `state`가 변경되었을 때만 리렌더링을 수행하도록 로직을 작성할 수 있습니다. 이를 통해 불필요한 리렌더링을 방지하고 성능을 향상시킬 수 있습니다.

여기 예시 코드가 있습니다:

```jsx
class MyComponent extends React.Component {
  shouldComponentUpdate(nextProps, nextState) {
    if (this.props.someProp === nextProps.someProp) {
      return false; // 리렌더링을 막음
    }
    return true; // 리렌더링을 허용
  }
}
```

참고문헌:
- React 문서: https://reactjs.org/docs/react-component.html#shouldcomponentupdate