---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 핑거(gestures) 인식 기능을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [react]
comments: true
share: true
---

React는 웹 애플리케이션 개발을 위한 자바스크립트 라이브러리로, 사용자 인터페이스를 구축하기 위해 컴포넌트 기반 접근 방식을 채택하고 있습니다. 이번에는 React.forwardRef()를 활용하여 핑거 인식 기능을 구현하는 방법에 대해 알아보겠습니다.

## React.forwardRef()란?
React.forwardRef() 함수는 리액트 컴포넌트에서 컴포넌트 내에 있는 DOM 요소나 리액트 컴포넌트에 직접 접근할 수 있게 해주는 기능입니다. 보통 리액트에서 ref 프로퍼티를 사용하여 컴포넌트나 DOM 요소에 접근할 수 있지만, 일반 함수형 컴포넌트에서는 사용할 수 없습니다. 이때 React.forwardRef()를 사용하면 함수형 컴포넌트에서도 ref를 통해 접근할 수 있게 됩니다.

## 핑거(gestures) 인식 기능 구현하기
핑거 인식 기능을 구현하기 위해서는 touch 이벤트와 그에 대한 핸들러 함수가 필요합니다. 이때 React.forwardRef()를 사용하여 컴포넌트를 생성하고, 해당 컴포넌트에서 touch 이벤트를 처리하는 핸들러 함수를 작성할 수 있습니다.

아래는 핑거 인식 기능을 구현한 예시 코드입니다.

```jsx
import React, { useRef, useEffect, forwardRef } from 'react';

const GestureComponent = forwardRef((props, ref) => {
  const containerRef = useRef();

  useEffect(() => {
    const handleTouchMove = (event) => {
      // 핑거 이동 처리 로직 작성
    };

    containerRef.current.addEventListener('touchmove', handleTouchMove);

    return () => {
      containerRef.current.removeEventListener('touchmove', handleTouchMove);
    };
  }, []);

  return <div ref={ref} ref={containerRef}>{props.children}</div>;
});

// GestureComponent를 부모 컴포넌트에서 사용하는 예시
const ParentComponent = () => {
  const gestureRef = useRef();

  useEffect(() => {
    // gestureRef를 사용한 핑거 인식 처리 로직 작성
  }, []);

  return <GestureComponent ref={gestureRef}>내용</GestureComponent>;
};
```

위의 코드에서는 GestureComponent라는 컴포넌트를 React.forwardRef() 함수를 사용하여 생성하였습니다. 이 컴포넌트에서는 touchmove 이벤트를 처리하는 핸들러 함수를 작성하고, 컴포넌트의 ref를 touchmove 이벤트가 적용되는 DOM 요소에 연결시켰습니다.

그리고 부모 컴포넌트에서 GestureComponent를 사용할 때 ref를 선언하여 해당 컴포넌트에 접근할 수 있게 하였습니다. 이렇게 GestureComponent를 사용하면 부모 컴포넌트에서 touch 이벤트에 대한 핸들러 함수를 구현할 수 있습니다.

이제 핑거 인식 기능을 활용하여 원하는 동작을 수행할 수 있게 되었습니다.

#React #ReactForwardRef