---
layout: post
title: "React.forwardRef()를 사용하여 컴포넌트의 키 입력(Key Input) 이벤트 처리 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [React]
comments: true
share: true
---

리액트에서 컴포넌트의 키 입력(Key Input) 이벤트를 처리하는 방법은 여러 가지가 있습니다. 그 중에서도 React.forwardRef() 메서드를 사용하여 컴포넌트를 감싸는 고차 컴포넌트(Higher-Order Component)를 만들어 이벤트 처리를 구현할 수 있습니다. React.forwardRef()는 함수형 컴포넌트에서 Ref를 전달할 수 있도록 해주는 메서드입니다.

## React.forwardRef()란?

React.forwardRef()는 리액트에서 제공하는 고급 API 중 하나로, 함수형 컴포넌트에서 Ref를 전달할 수 있도록 해주는 메서드입니다. 일반적인 컴포넌트의 경우, Ref를 전달하려면 클래스형 컴포넌트에서 React.createRef()를 사용해야 했지만, 함수형 컴포넌트에서는 이를 직접 사용할 수 없습니다. 이 때 React.forwardRef() 메서드를 사용하면 함수형 컴포넌트에서도 Ref를 전달할 수 있게 됩니다.

## Key Input 이벤트 처리하기

1. 먼저, Key Input 이벤트를 처리할 함수형 컴포넌트를 작성합니다. 예를 들어, 다음과 같이 KeyInput 컴포넌트를 만듭니다.

```jsx
import React, { useRef } from 'react';

const KeyInput = React.forwardRef((props, ref) => {
  const inputRef = useRef(null);

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      alert('Enter 키가 입력되었습니다!');
    }
  };

  React.useImperativeHandle(ref, () => ({
    setInputFocus: () => {
      inputRef.current.focus();
    }
  }));

  return (
    <input ref={inputRef} onKeyDown={handleKeyDown} />
  );
});

export default KeyInput;
```

2. 위 코드에서는 React.forwardRef() 메서드를 사용하여 KeyInput 컴포넌트를 생성하였습니다. Ref를 전달하기 위해 useRef() 훅을 사용하였고, handleKeyDown 함수에서는 Enter 키 입력 시 알림창을 띄우도록 처리했습니다.

3. 마지막으로, KeyInput 컴포넌트를 사용하는 부모 컴포넌트에서 Ref를 생성하고 이벤트를 처리할 수 있습니다. 예를 들어, 다음과 같이 Parent 컴포넌트를 작성합니다.

```jsx
import React, { useRef } from 'react';
import KeyInput from './KeyInput';

const Parent = () => {
  const keyInputRef = useRef(null);

  const handleClick = () => {
    keyInputRef.current.setInputFocus();
  };

  return (
    <>
      <KeyInput ref={keyInputRef} />
      <button onClick={handleClick}>입력 포커스 설정</button>
    </>
  );
};

export default Parent;
```

위 코드에서는 useRef() 훅을 사용하여 keyInputRef를 생성하고, Parent 컴포넌트에서 버튼을 클릭할 시 KeyInput 컴포넌트의 setInputFocus 함수를 호출하여 입력 포커스를 설정합니다.

위와 같이 React.forwardRef()를 사용하여 Key Input 이벤트를 처리할 수 있고, Ref를 사용하여 컴포넌트 간 상호작용을 구현할 수 있습니다.

---
References:
- [React Documentation - Refs and the DOM](https://reactjs.org/docs/refs-and-the-dom.html)
- [React Documentation - Forwarding Refs](https://reactjs.org/docs/forwarding-refs.html)