---
layout: post
title: "[react] JSX에서 Component Lifecycle 다루기"
description: " "
date: 2023-12-26
tags: [react]
comments: true
share: true
---

React의 컴포넌트 라이프사이클은 컴포넌트가 생성될 때, 업데이트될 때, 제거될 때 일어나는 다양한 단계를 다룹니다. 이러한 라이프사이클 단계를 알면 컴포넌트의 동작을 더 잘 이해하고 조절할 수 있습니다.

## 컴포넌트 라이프사이클 메소드

### Mounting (마운팅)

컴포넌트가 생성되어 DOM에 삽입될 때 발생하는 단계입니다.

- `constructor`: 컴포넌트가 생성될 때 호출됩니다.
- `render`: 컴포넌트가 마운트될 때, 업데이트될 때 호출되며 UI를 반환합니다.
- `componentDidMount`: 컴포넌트가 DOM에 삽입된 후 호출됩니다.

### Updating (업데이팅)

컴포넌트가 업데이트되었을 때 발생하는 단계입니다.

- `shouldComponentUpdate`: 리렌더링을 할지 말지를 결정합니다.
- `render`: 새로운 UI를 반환합니다.
- `componentDidUpdate`: 컴포넌트 업데이트가 끝난 후 호출됩니다.

### Unmounting (언마운팅)

컴포넌트가 DOM에서 제거될 때 발생하는 단계입니다.

- `componentWillUnmount`: 컴포넌트가 제거되기 직전에 호출됩니다.

## 라이프사이클 메소드 활용

컴포넌트 라이프사이클 메소드를 활용하여 다양한 작업을 수행할 수 있습니다. 예를 들어, `componentDidMount`에서 외부 데이터를 가져와서 상태를 업데이트하거나, `componentWillUnmount`에서 리소스를 정리하는 작업을 수행할 수 있습니다.

```jsx
import React, { Component } from 'react';

class MyComponent extends Component {
  constructor(props) {
    super(props);
    // 초기 상태 설정
  }

  componentDidMount() {
    // 외부 데이터 가져와서 상태 업데이트
  }

  componentWillUnmount() {
    // 리소스 정리
  }

  render() {
    // UI 반환
  }
}
```

## 결론

컴포넌트 라이프사이클 메소드를 이해하고 활용하면 React 애플리케이션을 더 효과적으로 관리할 수 있습니다. **컴포넌트 라이프사이클은 React 애플리케이션의 핵심 부분이므로 정확히 이해하는 것이 중요합니다**.

이러한 라이프사이클 메소드를 사용하는 방법에 대해 자세히 배우고 업데이트에 대처하는 방법을 알아가는 것이 중요합니다.

참고문헌:
- [React 공식 문서](https://reactjs.org/docs/react-component.html)