---
layout: post
title: "React.forwardRef()를 활용하여 HOC(Higher Order Component)와 컴포지션을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [reactjs]
comments: true
share: true
---

React는 컴포넌트 기반의 웹 개발을 위한 JavaScript 라이브러리로, 컴포넌트 기능을 최대한 재사용하기 위한 다양한 패턴을 제공합니다. 그 중에서도 HOC(Higher Order Component)와 컴포지션을 사용하면 컴포넌트를 더욱 유연하게 구성할 수 있습니다.

## HOC (Higher Order Component)
HOC란 하나 이상의 컴포넌트를 인자로 받아 새로운 컴포넌트를 반환하는 함수입니다. HOC는 기존 컴포넌트를 감싸고, 추가적인 props를 주입하거나 상태를 관리할 수 있습니다. 이를 통해 코드의 재사용성과 가독성을 향상시킬 수 있습니다.

아래는 HOC를 사용한 예제입니다:

```jsx
import React from 'react';

function withLogging(WrappedComponent) {
  return class extends React.Component {
    componentDidMount() {
      console.log('Component is rendered');
    }

    render() {
      return <WrappedComponent {...this.props} />;
    }
  };
}

class MyComponent extends React.Component {
  render() {
    return <div>{this.props.message}</div>;
  }
}

const EnhancedComponent = withLogging(MyComponent);

// 사용 예시
ReactDOM.render(
  <EnhancedComponent message="Hello, HOC!" />,
  document.getElementById('root')
);
```

위의 코드에서 `withLogging()` 함수는 `MyComponent`를 인자로 받아 새로운 컴포넌트를 반환합니다. 반환된 컴포넌트는 `componentDidMount()` 메소드가 추가된 것을 확인할 수 있습니다.

## 컴포지션 (Composition)
컴포지션은 여러 개의 컴포넌트를 조합하여 새로운 컴포넌트를 만드는 기법입니다. 이를 통해 컴포넌트의 재사용성이 높아지고 코드의 가독성이 향상됩니다. 

아래는 컴포지션을 사용한 예제입니다:

```jsx
import React from 'react';

function WrapperComponent(props) {
  return (
    <div className="wrapper">
      {props.children}
    </div>
  );
}

function MyComponent() {
  return (
    <WrapperComponent>
      <div>Hello, Composition!</div>
    </WrapperComponent>
  );
}

// 사용 예시
ReactDOM.render(
  <MyComponent />,
  document.getElementById('root')
);
```

위의 코드에서 `WrapperComponent` 컴포넌트는 자식 컴포넌트를 감싸는 역할을 하고 있습니다. `MyComponent`는 `WrapperComponent` 내부에 있는 `div`를 렌더링하는 예시입니다.

## React.forwardRef()를 활용한 HOC와 컴포지션
React의 `forwardRef()` 메소드를 활용하면, HOC나 컴포지션과 함께 ref를 전달할 수 있습니다. 이를 통해 ref를 사용하는 컴포넌트와의 상호작용을 보다 쉽게 처리할 수 있습니다.

예를 들어, 위에서 작성한 `withLogging()` HOC를 수정하여 ref를 전달하는 예제는 다음과 같습니다:

```jsx
import React from 'react';

function withLogging(WrappedComponent) {
  const EnhancedComponent = React.forwardRef((props, ref) => {
    React.useEffect(() => {
      console.log('Component is rendered');
    }, []);

    return <WrappedComponent {...props} ref={ref} />;
  });

  return EnhancedComponent;
}

class MyComponent extends React.Component {
  render() {
    return <div>{this.props.message}</div>;
  }
}

const ForwardedComponent = withLogging(React.forwardRef(MyComponent));

// 사용 예시
ReactDOM.render(
  <ForwardedComponent message="Hello, HOC with forwardRef!" ref={myRef} />,
  document.getElementById('root')
);
```

위의 코드에서 `withLogging()` 함수는 `React.forwardRef()` 메소드로 감싸진 함수형 컴포넌트를 반환합니다. 이렇게 하면, `ForwardedComponent`에 ref를 전달할 수 있게 됩니다.

이처럼 `React.forwardRef()`를 사용하면 HOC나 컴포지션과 함께 ref를 전달하는 기능을 손쉽게 구현할 수 있습니다.

이 글은 React의 `forwardRef()`를 활용하여 HOC와 컴포지션을 구현하는 방법에 대해 알아보았습니다. 이러한 패턴은 코드의 재사용성과 가독성을 향상시키는 데 큰 도움이 될 수 있습니다. 자유롭게 활용하여 효율적인 컴포넌트 구성을 구현해보세요!

## 참고 자료
- [React 공식 문서 - Forwarding Refs](https://ko.reactjs.org/docs/forwarding-refs.html)
- [React Higher-Order Components (HOC)](https://reactjs.org/docs/higher-order-components.html)
- [React Composition vs Inheritance](https://reactjs.org/docs/composition-vs-inheritance.html) 
- [Why React’s new Hooks API is a game changer](https://www.freecodecamp.org/news/why-reacts-hooks-api-is-a-game-changer-8731c2b0a8c/)
- [React forwardRef() Method in Detail](https://www.codingame.com/playgrounds/6517/react-forwardref-method-in-detail) 
- [Use React's ForwardRef for Better Reusable Components](https://upmostly.com/tutorials/how-to-use-reacts-forwardref-to-just-forward-ref/) 

#React #HOC #composition