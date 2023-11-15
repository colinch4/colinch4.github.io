---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 상태 전환(State Transition) 기능을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [react]
comments: true
share: true
---

React는 상태 전환 로직을 다루기 위해 다양한 패턴을 제공합니다. React.forwardRef()는 이 패턴 중 하나로, 컴포넌트의 상태를 관리하고 전환하는 기능을 구현하는 데 도움을 줍니다. 이 기능을 사용하면 다른 컴포넌트에서 참조하는 상태값을 손쉽게 전달하고 업데이트할 수 있습니다.

React.forwardRef() 함수는 다음과 같은 형식으로 사용할 수 있습니다:

```jsx
const ChildComponent = React.forwardRef((props, ref) => {
  // 컴포넌트의 상태와 동작을 관리하는 로직 구현
  // ...

  return (
    // 컴포넌트의 JSX 구조
    // ...
  );
});
```

위 코드에서 `ChildComponent`는 `forwardRef()` 함수로 감싸진 함수형 컴포넌트입니다. 이 함수의 첫 번째 매개변수에는 `props`와 `ref`가 전달됩니다. `props`는 다른 컴포넌트로부터 전달된 속성들을 포함하고 있으며, `ref`는 참조값을 정의하는 매개변수입니다.

`ChildComponent` 내부에서는 상태와 동작을 관리하는 로직을 구현하고, JSX 구조를 반환합니다. 이렇게 컴포넌트의 내부 로직과 상태를 캡슐화하면 외부에서 해당 컴포넌트를 사용할 때 상태 전환 로직을 간편하게 처리할 수 있습니다.

변경 가능한 상태를 가지는 `ChildComponent`를 사용하는 부모 컴포넌트에서는 다음과 같이 `ref`를 정의하고 상태값을 업데이트할 수 있습니다:

```jsx
const ParentComponent = () => {
  const childRef = React.createRef();

  const handleStateChange = () => {
    // 컴포넌트의 상태값 업데이트
    childRef.current.setState({
      // 상태값 업데이트 내용
      // ...
    });
  };

  return (
    <div>
      {/* ChildComponent를 사용하여 JSX 구조 작성 */}
      <ChildComponent ref={childRef} />

      <button onClick={handleStateChange}>상태 전환</button>
    </div>
  );
};
```

위 코드에서 `ParentComponent`는 `ChildComponent`를 렌더링하고, `childRef`를 생성하여 `ref` 속성에 할당합니다. 이후 `handleStateChange` 함수를 이용하여 `ChildComponent`의 상태를 업데이트할 수 있습니다. 클릭 이벤트가 발생하면 해당 함수가 실행되어 `childRef`의 `setState` 메소드가 호출되고, `ChildComponent`의 상태값이 업데이트됩니다.

React.forwardRef() 함수를 사용하여 컴포넌트의 상태 전환 기능을 구현하면 상태 관리가 편리해집니다. 다른 컴포넌트에서 해당 컴포넌트의 상태를 손쉽게 업데이트할 수 있으며, 컴포넌트 간의 상호작용이 원활해집니다.

참고 자료:
- [React 공식 문서 - Forwarding Refs](https://ko.reactjs.org/docs/forwarding-refs.html)
- [React.forwardRef()를 사용한 React 컴포넌트 내부의 참조 전달](https://velog.io/@velopert/use-ref-2-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%EA%B0%80-%EB%82%98%EC%9D%B4%ED%95%98%EA%B8%B0-ccfge6qr0r)
- [React함수형 컴포넌트 State 관리하는법 전파와 useImperativeHandle](https://kyounghwan01.github.io/blog/React/forwardRef-and-useImperativeHandle/)
- [React Refs: A Deep Dive](https://blog.bitsrc.io/react-refs-a-deep-dive-2c6c98c710c6)

#React #상태전환