---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 이벤트 위임(Event Delegation) 기능을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [react]
comments: true
share: true
---

React.forwardRef()는 리액트에서 사용되는 고급 기능 중 하나로, 부모 컴포넌트로부터 자식 컴포넌트로 ref를 전달하기 위해 사용됩니다. 이 기능을 활용하여 이벤트 위임(Event Delegation) 기능을 간편하게 구현할 수 있습니다.

## 이벤트 위임이란?

이벤트 위임은 여러 하위 요소들에 동일한 이벤트 핸들러를 적용하고, 이벤트가 발생했을 때 해당 하위 요소를 직접 찾아가는 것이 아니라 상위 요소에서 이벤트를 처리하는 방식입니다. 이를 통해 코드의 가독성을 높이고, 성능 개선을 이룰 수 있습니다.

## forwardRef()를 사용하여 이벤트 위임 구현하기

먼저, 부모 컴포넌트에서 ref를 생성하고 자식 컴포넌트로 전달하는 방법을 알아보겠습니다.

```jsx
import React, { forwardRef } from 'react';

const ChildComponent = forwardRef((props, ref) => {
  // 자식 컴포넌트 로직 작성 
  return <div ref={ref}>자식 컴포넌트</div>;
});

const ParentComponent = () => {
  const childRef = useRef(null);

  const handleClick = () => {
    console.log(`자식 컴포넌트의 노드:`, childRef.current);
  };

  return (
    <div onClick={handleClick}>
      <ChildComponent ref={childRef} />
    </div>
  );
};
```

위 코드에서 `react` 모듈에서 `forwardRef`를 가져온 후, 자식 컴포넌트를 선언할 때 `forwardRef` 함수로 감싸줍니다. 이렇게 함으로써 부모 컴포넌트에서 ref를 전달할 수 있게 됩니다.

부모 컴포넌트에서는 `useRef()`를 사용하여 ref 객체를 생성하고, 해당 ref 객체를 자식 컴포넌트의 ref prop으로 전달해 줍니다. 그리고 이벤트 핸들러에서 `childRef.current`를 통해 자식 컴포넌트의 DOM 노드에 접근할 수 있게 됩니다.

이제 클릭 이벤트가 발생할 때 자식 컴포넌트의 노드를 출력하는 `handleClick` 함수가 실행됩니다.

## 결론

React.forwardRef()를 사용하여 컴포넌트의 이벤트 위임 기능을 구현할 수 있습니다. 이를 통해 코드의 가독성과 성능 개선을 이룰 수 있으며, 다양한 상황에서 유연하게 활용할 수 있습니다.

#React #이벤트위임