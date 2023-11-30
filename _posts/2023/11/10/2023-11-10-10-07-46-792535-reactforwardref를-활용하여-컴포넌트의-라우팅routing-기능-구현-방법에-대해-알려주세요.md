---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 라우팅(Routing) 기능 구현 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [react]
comments: true
share: true
---

React는 라우팅 기능을 제공하는 React Router와 함께 사용되는 경우가 많습니다. 하지만 React의 forwardRef() 메서드를 사용하면 간단한 컴포넌트 라우팅 기능을 구현할 수 있습니다. 이번 글에서는 React.forwardRef()를 활용하여 컴포넌트 라우팅을 구현하는 방법에 대해 알아보겠습니다.

## React.forwardRef()란?

React.forwardRef()는 컴포넌트에 ref 속성을 전달하기 위해 사용되는 메서드입니다. 일반적으로 ref 속성은 DOM 요소에 직접 접근하거나 컴포넌트 간의 통신에 사용됩니다. 하지만 이번에는 ref 속성을 사용하여 컴포넌트 간의 라우팅을 구현해보겠습니다.

## 컴포넌트 라우팅 구현 방법

1. 라우팅 컴포넌트 생성하기

   ```jsx
   import React, { forwardRef } from 'react';

   const RoutingComponent = forwardRef((props, ref) => {
     // 라우팅 컴포넌트의 내용을 구현할 부분
     return (
       <div ref={ref}>
         // 라우팅 컴포넌트의 내용
       </div>
     );
   });

   export default RoutingComponent;
   ```

2. 라우터 컴포넌트에서 라우팅 컴포넌트 사용하기

   ```jsx
   import React, { useRef } from 'react';
   import RoutingComponent from './RoutingComponent';

   const RouterComponent = () => {
     const ref = useRef();

     const handleRouting = () => {
       // 라우팅 컴포넌트에 접근하여 필요한 라우팅 로직 구현
       ref.current.scrollTo(0, 0);
     };

     return (
       <div>
         <button onClick={handleRouting}>라우팅</button>
         <RoutingComponent ref={ref} />
       </div>
     );
   };

   export default RouterComponent;
   ```

3. 컴포넌트 라우팅 확인하기

   RouterComponent에서 라우팅 버튼을 클릭하면 RoutingComponent의 scrollTo() 메서드를 호출하여 페이지의 맨 위로 스크롤됩니다. 이처럼 React.forwardRef()를 사용하여 라우팅 컴포넌트를 구현하면, 컴포넌트 간의 통신을 통해 간단한 라우팅 기능을 구현할 수 있습니다.

이와 같이 React.forwardRef()를 사용하여 컴포넌트 라우팅을 구현하는 방법에 대해 알아보았습니다. React의 공식 문서에서도 라우팅 기능에 대한 더 자세한 내용을 확인할 수 있으니 참고하시기 바랍니다. #React #라우팅