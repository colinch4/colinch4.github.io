---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 윈도우 리사이징(Window Resizing) 처리 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [react]
comments: true
share: true
---

React에서는 컴포넌트 기능을 확장하고 코드의 재사용성을 높일 수 있는 여러 가지 패턴과 기술을 제공합니다. 그 중 하나가 `React.forwardRef()` 함수입니다. `React.forwardRef()` 함수는 부모 컴포넌트로부터 전달받은 `ref`를 자식 컴포넌트에 전달하여 사용할 수 있게 해줍니다.

이번 기술 블로그에서는 `React.forwardRef()`를 활용하여 컴포넌트의 윈도우 리사이징(Window Resizing) 처리 방법에 대해 알아보겠습니다. 

## 1. 컴포넌트 생성하기
먼저 윈도우 리사이징 처리를 해야하는 컴포넌트를 생성합니다. 이 예제에서는 `ResizableComponent`라는 컴포넌트를 사용합니다. 

```jsx
import React, { useEffect } from 'react';

const ResizableComponent = React.forwardRef((props, ref) => {
  const handleResize = () => {
    // 리사이징 이벤트 처리 로직
  };

  useEffect(() => {
    window.addEventListener("resize", handleResize);
    
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);
  
  return <div ref={ref}>{props.children}</div>
});

export default ResizableComponent;
```

## 2. 부모 컴포넌트에서 사용하기
`ResizableComponent`를 사용하는 부모 컴포넌트에서는 `ref`를 생성하여 `ResizableComponent`에 전달해야 합니다. 

```jsx
import React, { useRef } from 'react';
import ResizableComponent from './ResizableComponent';

const ParentComponent = () => {
  const ref = useRef();

  return (
    <div>
      <h1>부모 컴포넌트</h1>
      <ResizableComponent ref={ref}>
        <p>리사이징 처리가 필요한 컨텐츠</p>
      </ResizableComponent>
    </div>
  );
};

export default ParentComponent;
```

위 예제에서 `ref`를 생성하고 `ResizableComponent`의 `ref` prop에 전달하는 것을 볼 수 있습니다. 이렇게 하면 `ResizableComponent` 내부의 `div` 요소가 생성된 후에도 `ref`로 참조할 수 있습니다.

## 3. 윈도우 리사이징 처리 로직 구현하기
`ResizableComponent` 컴포넌트에서는 useEffect 훅을 사용하여 윈도우 리사이징 이벤트를 감지하고 처리하는 로직을 구현합니다.

```jsx
const ResizableComponent = React.forwardRef((props, ref) => {
  const handleResize = () => {
    // 리사이징 이벤트 처리 로직
    // ref.current를 사용하여 div 요소에 접근 가능
  };

  useEffect(() => {
    window.addEventListener("resize", handleResize);
    
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);
  
  return <div ref={ref}>{props.children}</div>
});
```

위 예제에서는 `handleResize` 함수를 정의하여 윈도우 리사이징 이벤트가 발생했을 때 로직을 처리할 수 있습니다. `ref.current`를 사용하여 `div` 요소에 접근하여 원하는 작업을 수행할 수 있습니다.

## 결론
`React.forwardRef()`를 활용하여 컴포넌트의 윈도우 리사이징 처리 방법을 알아보았습니다. 이를 통해 코드의 재사용성을 높이고 리사이징과 관련된 로직을 컴포넌트 내부에서 처리할 수 있습니다. 윈도우 리사이징과 같은 이벤트 처리를 위해 `React.forwardRef()`를 적극적으로 활용해보세요!

<sup>참고문서: [React 공식 문서 - React.forwardRef()](https://reactjs.org/docs/forwarding-refs.html)</sup>
<sup>해시태그: #React #윈도우리사이징</sup>