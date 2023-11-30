---
layout: post
title: "React.forwardRef()와 함께 사용하는 useImperativeHandle()의 역할은 무엇인가요?"
description: " "
date: 2023-11-10
tags: [react]
comments: true
share: true
---

하지만, 자식 컴포넌트에서 ref를 정의하고 싶을 때는 useImperativeHandle()을 함께 사용해야 합니다. useImperativeHandle()은 내부에서 생성한 ref 객체를 부모 컴포넌트에서 접근할 수 있도록 해줍니다. 

useImperativeHandle()은 useState나 useEffect와 같이 리액트의 hook 함수 중 하나이며, 두 개의 인자를 받습니다. 첫번째 인자는 자식 컴포넌트에서 정의한 ref 객체이고, 두번째 인자는 자식 컴포넌트의 ref 객체 메소드를 정의하는 콜백 함수입니다.

예를 들어, 자식 컴포넌트에서 버튼 클릭에 따른 특정 함수를 실행하고 싶다면, useImperativeHandle()을 사용하여 자식 컴포넌트의 함수를 부모 컴포넌트에서 호출할 수 있습니다.

```jsx
// 자식 컴포넌트
import React, { forwardRef, useImperativeHandle } from 'react';

const ChildComponent = forwardRef((props, ref) => {
  const handleClick = () => {
    // 버튼 클릭 시 실행되는 로직
  };

  useImperativeHandle(ref, () => ({
    handleClick
  }));

  return <button onClick={handleClick}>버튼</button>;
});

export default ChildComponent;
```

```jsx
// 부모 컴포넌트
import React, { useRef } from 'react';
import ChildComponent from './ChildComponent';

const ParentComponent = () => {
  const childRef = useRef();

  const handleClick = () => {
    childRef.current.handleClick();
  };

  return (
    <>
      <ChildComponent ref={childRef} />
      <button onClick={handleClick}>자식 컴포넌트 함수 호출</button>
    </>
  );
};

export default ParentComponent;
```

부모 컴포넌트에서 useRef를 사용하여 자식 컴포넌트의 ref를 생성하고, handleClick 함수를 정의하여 자식 컴포넌트의 함수를 호출할 수 있습니다. 이를 통해 자식 컴포넌트의 기능을 외부에서 제어할 수 있게 됩니다.

이와 같이 React.forwardRef()와 useImperativeHandle()을 함께 사용하면, 특정 컴포넌트의 메소드나 변수에 접근할 수 있게 되어 더욱 유연하고 강력한 컴포넌트 구조를 만들 수 있습니다.

[#React](https://reactjs.org/) [#Ref](https://reactjs.org/docs/forwarding-refs.html)