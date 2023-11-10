---
layout: post
title: "React.forwardRef()를 사용하여 컴포넌트의 드래그 앤 드롭(Draggable) 처리 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

## 소개

React에서 컴포넌트를 개발할 때 드래그 앤 드롭 기능을 구현해야 하는 경우가 있습니다. 이러한 경우, React.forwardRef()를 사용하면 부모 컴포넌트로부터 ref를 전달받아 자식 컴포넌트에서 DOM 요소를 조작할 수 있습니다.

## React.forwardRef()란?

React.forwardRef()는 React 16.3 버전에서 도입된 기능으로, 함수형 컴포넌트에서 ref를 사용할 수 있도록 해줍니다. 이를 통해 ref를 전달받아 하위 컴포넌트에서 해당 DOM 요소에 접근할 수 있습니다.

## 사용법

먼저, draggable 기능을 구현할 Draggable 컴포넌트를 작성합니다.

```jsx
{% raw %}
import React from 'react';

const Draggable = React.forwardRef((props, ref) => {
  return (
    <div ref={ref} style={{ width: '100px', height: '100px', backgroundColor: 'red' }}>
      Drag me!
    </div>
  );
});

export default Draggable;
{% endraw %}
```

위의 코드에서는 React.forwardRef()를 사용하여 ref를 전달받는 컴포넌트를 생성하고 있습니다. 이 컴포넌트는 `ref`라는 props를 전달받아 `<div>` 요소의 `ref`에 설정하고 있습니다.

다음으로, 부모 컴포넌트에서 Draggable 컴포넌트를 사용하여 드래그 앤 드롭 기능을 구현할 수 있습니다.

```jsx
import React, { useRef } from 'react';
import Draggable from './Draggable';

const App = () => {
  const draggableRef = useRef(null);

  const handleDragStart = (event) => {
    // 드래그 시작 시 실행할 로직을 작성합니다.
    console.log('Drag started!');
  };

  return (
    <div>
      <Draggable ref={draggableRef} onDragStart={handleDragStart} />
    </div>
  );
};

export default App;
```

위의 코드에서는 `useRef` 훅을 사용하여 `draggableRef`라는 ref 객체를 생성하고, `handleDragStart` 함수를 만들어 드래그 시작 시 실행될 로직을 작성했습니다. Draggable 컴포넌트에서 ref 속성을 사용하여 `draggableRef`를 전달하였습니다.

## 결론

React.forwardRef()를 사용하여 컴포넌트의 드래그 앤 드롭 기능을 구현하는 방법에 대해 알아보았습니다. 이를 활용하면 부모 컴포넌트로부터 전달된 ref를 통해 DOM 요소에 접근하고, 드래그 앤 드롭과 같은 기능을 구현할 수 있습니다.

[#React](react) [#ForwardRef](forwardref)