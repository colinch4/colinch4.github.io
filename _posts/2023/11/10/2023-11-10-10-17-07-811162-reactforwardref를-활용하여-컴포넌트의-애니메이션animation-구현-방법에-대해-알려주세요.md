---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 애니메이션(Animation) 구현 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [애니메이션]
comments: true
share: true
---

리액트는 싱글 페이지 애플리케이션(SPA) 개발에 많이 사용되는 인기있는 프론트엔드 라이브러리입니다. 리액트 컴포넌트를 사용하여 웹 애플리케이션을 구축할 때, 사용자 경험을 향상시키기 위해 애니메이션이 중요한 역할을 합니다. 애니메이션을 구현하는 방법 중 하나는 React.forwardRef()를 활용하는 것입니다.

## React.forwardRef()란?

React.forwardRef()는 리액트의 고급 기능 중 하나로, 부모 컴포넌트에서 자식 컴포넌트로 ref를 전달할 수 있도록 해줍니다. 이를 통해 부모 컴포넌트에서 자식 컴포넌트의 DOM 요소에 직접적인 접근이 가능해집니다. 이 기능을 사용하면 컴포넌트의 애니메이션을 더욱 유연하게 구현할 수 있습니다.

## 컴포넌트 애니메이션 구현 방법

1. 부모 컴포넌트에서 자식 컴포넌트의 ref를 생성합니다. 이때 React.createRef() 메서드를 사용하여 ref 객체를 생성합니다.

   ```jsx
   import React, { useRef } from 'react';

   const ParentComponent = () => {
     const childRef = useRef(null);

     // ...

     return (
       <div>
         <ChildComponent ref={childRef} />
       </div>
     );
   };
   ```

2. 자식 컴포넌트에서 애니메이션을 적용할 DOM 요소에 ref를 연결합니다. 이때 forwardRef() 함수를 사용하여 ref 속성을 전달합니다.

   ```jsx
   import React, { forwardRef } from 'react';

   const ChildComponent = forwardRef((props, ref) => {
     return (
       <div ref={ref}>
         {/* 애니메이션을 적용할 DOM 요소 */}
       </div>
     );
   });
   ```

3. 애니메이션을 구현할 때, ref.current를 사용하여 DOM 요소에 접근합니다. 예를 들어, CSS 트랜지션을 사용하여 애니메이션을 적용할 수 있습니다.

   ```jsx
   import { useEffect } from 'react';

   const ChildComponent = forwardRef((props, ref) => {
     useEffect(() => {
       // ref.current를 사용하여 DOM 요소에 접근
       const element = ref.current;

       // 애니메이션 적용
       element.style.transition = 'opacity 1s';
       element.style.opacity = '0.5';

       return () => {
         // 컴포넌트가 언마운트 될 때 애니메이션 초기화
         element.style.opacity = '1';
       };
     }, []);

     return (
       <div ref={ref}>
         {/* 애니메이션을 적용할 DOM 요소 */}
       </div>
     );
   });
   ```

위의 예시에서는 자식 컴포넌트인 `ChildComponent`에서 ref를 전달받아 애니메이션을 구현했습니다. `ChildComponent`에서는 useEffect 훅을 사용하여 컴포넌트가 마운트될 때와 언마운트될 때 애니메이션을 적용하고 초기화하는 작업을 수행합니다.

이제 부모 컴포넌트인 `ParentComponent`에서 `ChildComponent`의 ref를 생성하고 사용할 수 있게 되었습니다. 이를 통해 `ChildComponent`의 DOM 요소에 직접적인 접근이 가능해지며, 애니메이션을 보다 유연하게 구현할 수 있습니다.

위 예시를 참고하여 React.forwardRef()를 활용하여 컴포넌트 애니메이션을 구현해 보세요! #리액트 #애니메이션