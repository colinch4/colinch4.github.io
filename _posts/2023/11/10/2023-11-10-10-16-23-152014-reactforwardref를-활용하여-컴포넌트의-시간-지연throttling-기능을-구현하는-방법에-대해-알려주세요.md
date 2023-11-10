---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 시간 지연(Throttling) 기능을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

React는 효율적인 웹 애플리케이션 개발을 위한 많은 기능을 제공합니다. 그 중 하나가 `React.forwardRef()`입니다. 이 기능을 활용하면 부모 컴포넌트로부터 자식 컴포넌트로 함께 전달된 ref를 자식 컴포넌트에서 직접 접근할 수 있게 됩니다. 이러한 기능을 이용하여 컴포넌트의 시간 지연 기능을 구현해보겠습니다.

## 시간 지연 기능 구현하기

시간 지연 기능은 특정 동작이 반복적으로 실행될 때, 일정 시간 동안 마지막 동작만을 실행하도록 제어하는 기능입니다. 이를 위해 우리는 `React.forwardRef()`를 사용해서 컴포넌트를 만들고, 내부적으로 `setTimeout()` 함수를 활용하여 시간 지연을 설정할 수 있습니다.

### 1. 시간 지연 컴포넌트 생성하기

```jsx
import React, { useEffect, useRef } from 'react';

const DelayedComponent = React.forwardRef((props, ref) => {
  const timeoutRef = useRef(null);

  useEffect(() => {
    return () => clearTimeout(timeoutRef.current);
  }, []);

  const delayedAction = () => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }

    timeoutRef.current = setTimeout(() => {
      // 지연된 동작을 수행하는 코드 작성
      console.log('Delayed action');
    }, props.delay);
  };

  return (
    <div ref={ref}>
      <button onClick={delayedAction}>Click me</button>
    </div>
  );
});
```

위 코드에서 우리는 `React.forwardRef()`를 사용하여 `DelayedComponent`라는 컴포넌트를 만들었습니다. 이 컴포넌트는 `props`와 `ref`를 인자로 받고, 내부적으로 `setTimeout()` 함수를 활용하여 시간 지연을 처리하고 `delayedAction` 함수를 호출합니다.

### 2. 시간 지연 컴포넌트 사용하기

```jsx
import React, { useRef } from 'react';
import DelayedComponent from './DelayedComponent';

const App = () => {
  const childRef = useRef(null);

  const handleClick = () => {
    childRef.current.delayedAction();
  };

  return (
    <div>
      <h1>시간 지연 기능 구현하기</h1>
      <DelayedComponent ref={childRef} delay={1000} />
      <button onClick={handleClick}>Trigger delayed action</button>
    </div>
  );
};
```

위 코드에서는 `App` 컴포넌트에서 `DelayedComponent`를 사용하는 예시입니다. `DelayedComponent`에 `ref`를 `useRef()`를 통해 생성하고, 해당 `ref`를 통해 시간 지연 동작을 호출하는 예시입니다.

## 결론

`React.forwardRef()`를 활용하여 컴포넌트의 시간 지연 기능을 구현하는 방법에 대해 알아보았습니다. 이를 통해 효율적인 웹 애플리케이션을 개발할 수 있습니다. 자세한 내용은 React 공식 문서에서 확인할 수 있습니다. #React #시간지연