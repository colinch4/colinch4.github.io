---
layout: post
title: "React.forwardRef()를 활용하여 코드 스플리팅(Code Splitting)을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [React]
comments: true
share: true
---

React는 대규모 애플리케이션에서 발생하는 성능 문제를 해결하기 위해 코드 스플리팅을 지원합니다. 코드 스플리팅이란 애플리케이션을 여러 개의 작은 번들로 분할하여 사용자가 필요하지 않은 코드를 로드하지 않고 초기 로딩 시간을 최적화하는 기법입니다. React에서는 `React.lazy()`와 `React.Suspense`를 통해 코드 스플리팅을 할 수 있지만, 여기서는 `React.forwardRef()`를 이용한 방법에 대해 알려드리겠습니다.

## React.forwardRef()란?

`React.forwardRef()`는 React 컴포넌트에 ref를 전달하기 위해 사용되는 함수입니다. 일반적으로 자식 컴포넌트에서 부모 컴포넌트로 ref를 전달할 때 사용됩니다. 그러나 코드 스플리팅을 구현할 때에도 `React.forwardRef()`를 활용할 수 있습니다.

## 코드 스플리팅을 위한 React.forwardRef() 활용하기

먼저, 코드 스플리팅을 위한 컴포넌트를 만들기 위해 `React.lazy()`와 함께 `import()` 함수를 사용해 동적으로 모듈을 불러옵니다. 이렇게 모듈을 불러오면 해당 모듈은 별도의 번들로 생성됩니다.

```jsx
import React from 'react';

const MyComponent = React.lazy(() => import('./MyComponent'));
```

그리고, 코드 스플리팅이 필요한 곳에서 `React.forwardRef()`를 사용하여 `MyComponent`에 ref를 전달할 수 있도록 만들어 줍니다. 

```jsx
const ForwardRefComponent = React.forwardRef((props, ref) => (
  <MyComponent {...props} forwardedRef={ref} />
));
```

그리고 `ForwardRefComponent`를 사용하는 부모 컴포넌트에서 ref를 전달하여 사용할 수 있습니다.

```jsx
class ParentComponent extends React.Component {
  constructor(props) {
    super(props);
    this.myComponentRef = React.createRef();
  }

  render() {
    return (
      <div>
        <ForwardRefComponent ref={this.myComponentRef} />
        <button onClick={() => this.myComponentRef.current.focus()}>Focus MyComponent</button>
      </div>
    );
  }
}
```

위의 예제에서는 `ForwardRefComponent`를 사용하여 `MyComponent`에 ref를 전달하였고, 부모 컴포넌트에서 `this.myComponentRef`를 통해 `MyComponent`에 접근할 수 있게 되었습니다.

## 요약

React.forwardRef()를 사용하면 컴포넌트 간의 ref 전달을 위해 코드 스플리팅을 할 수 있습니다. `React.lazy()`와 `React.Suspense`를 사용하는 방법 외에도 이를 활용하여 애플리케이션 초기 로딩 속도를 최적화할 수 있습니다. `React.forwardRef()`를 사용하여 코드 스플리팅을 구현해보세요.

### 참고 자료

- [React 공식 문서: React.forwardRef()](https://reactjs.org/docs/forwarding-refs.html)
- [Code-Splitting - React](https://ko.reactjs.org/docs/code-splitting.html) #React #CodeSplitting