---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 카운터(Counter) 기능을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

React.forwardRef()는 React에서 제공하는 기능을 사용하여 컴포넌트 간의 속성을 전달할 수 있습니다. 이 기능을 활용하여 카운터(Counter) 컴포넌트를 구현해보겠습니다.

## 1. Counter 컴포넌트 생성

```javascript
import React, { forwardRef } from 'react';

const Counter = forwardRef((props, ref) => {
  const [count, setCount] = React.useState(0);

  const increment = () => {
    setCount(count + 1);
  };

  const decrement = () => {
    setCount(count - 1);
  };

  return (
    <div>
      <button onClick={increment}>+</button>
      <span>{count}</span>
      <button onClick={decrement}>-</button>
    </div>
  );
});

export default Counter;
```

위의 코드에서는 `React.forwardRef()`를 사용하여 카운터(Counter) 컴포넌트를 생성합니다. 이 컴포넌트는 `count` 상태와 `increment`, `decrement` 함수를 갖고 있으며, 버튼을 클릭할 때마다 `count`의 값을 증가/감소시킵니다.

## 2. Counter 컴포넌트 사용

```javascript
import React, { useRef } from 'react';
import Counter from './Counter';

const App = () => {
  const counterRef = useRef();

  const handleClick = () => {
    counterRef.current.increment();
  };

  return (
    <div>
      <Counter ref={counterRef} />
      <button onClick={handleClick}>Increment Counter</button>
    </div>
  );
}

export default App;
```

위의 코드에서는 `Counter` 컴포넌트를 사용하여 카운터를 렌더링합니다. `Counter` 컴포넌트의 ref 속성에 `counterRef.current`를 할당하여 ref 객체에 접근할 수 있습니다. `handleClick` 함수에서는 `counterRef.current.increment()`을 호출하여 카운터를 증가시킬 수 있습니다.

위와 같이 `React.forwardRef()`를 사용하면 컴포넌트 간의 속성 전달을 보다 편리하게 구현할 수 있습니다.

## 참고 자료
- [React Documentation - Forwarding Refs](https://reactjs.org/docs/forwarding-refs.html)