---
layout: post
title: "[python] JSX(JavaScript XML)와 React 컴포넌트"
description: " "
date: 2023-12-08
tags: [python]
comments: true
share: true
---

JSX는 JavaScript의 확장 문법으로, XML과 비슷한 구조를 갖는다. 이것은 React에서 UI를 렌더링하기 위한 구문으로 사용된다.

JSX는 JavaScript 코드 안에서 HTML 코드를 직접 작성할 수 있도록 해주며, 컴포넌트를 쉽게 작성하고 렌더링할 수 있도록 도와준다.

## JSX의 기본 구조

JSX는 간단한 HTML 코드와 매우 유사하게 생겼다. 예를 들면 다음과 같다.

```jsx
const element = <h1>Hello, World!</h1>;
```

위의 코드는 JavaScript 코드 안에 보기에는 HTML 태그처럼 생겼지만, 사실은 JSX로 작성된 것이다.

## JSX의 장점

JSX를 사용하면 JavaScript와 HTML을 혼합해서 사용할 수 있으므로, UI를 표현하기가 매우 간편해진다. 또한 동적 데이터를 표시하거나 조작하기가 용이하다.

또한 JSX를 사용하면 코드의 가독성이 좋아지고, 디버깅이 용이해지는 등의 장점이 있다.

## React 컴포넌트 작성하기

React에서 UI를 표현하기 위해서는 JSX를 사용한 컴포넌트를 작성해야 한다. 간단한 예제를 살펴보자.

```jsx
import React from 'react';

class MyComponent extends React.Component {
  render() {
    return <h1>Hello, World!</h1>;
  }
}
```

위의 예제에서 `MyComponent`는 React 컴포넌트로, `render` 메서드 안에 JSX를 사용하여 UI를 정의하고 있다.

## 결론

JSX는 JavaScript와 HTML을 혼합하여 사용할 수 있도록 도와주는 확장 문법이다. React에서 UI를 표현하기 위한 핵심 요소이며, 컴포넌트를 작성하고 렌더링하는 데 매우 유용하게 활용된다.

참조: [React 공식 문서](https://reactjs.org/docs/introducing-jsx.html)