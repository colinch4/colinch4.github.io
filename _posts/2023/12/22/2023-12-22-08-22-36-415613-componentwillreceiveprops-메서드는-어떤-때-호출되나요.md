---
layout: post
title: "[react] componentWillReceiveProps 메서드는 어떤 때 호출되나요?"
description: " "
date: 2023-12-22
tags: [react]
comments: true
share: true
---

아래는 `componentWillReceiveProps` 메서드의 사용 예시입니다.

```javascript
class MyComponent extends React.Component {
  componentWillReceiveProps(nextProps) {
    // 이 메서드에서는 이전 props와 새로운 props에 대한 처리를 수행합니다
    // 예: 이전 props와 새로운 props를 비교하여 상태를 업데이트하거나 사이드 이펙트 처리
  }
  // ...다른 메서드들
}
```

이후의 React 버전에서는 `componentWillReceiveProps` 대신 `getDerivedStateFromProps` 또는 `componentDidUpdate`를 사용할 것을 권장하므로, 새로운 React 애플리케이션을 개발한다면 이를 고려하는 것이 좋습니다(출처: [React 공식 문서](https://reactjs.org/docs/react-component.html)).