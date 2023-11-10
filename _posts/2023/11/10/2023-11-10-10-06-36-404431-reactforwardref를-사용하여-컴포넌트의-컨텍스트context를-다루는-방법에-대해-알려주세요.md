---
layout: post
title: "React.forwardRef()를 사용하여 컴포넌트의 컨텍스트(Context)를 다루는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

컨텍스트(Context)는 React 애플리케이션 내에서 전역적으로 데이터를 공유하기 위한 방법입니다. 일반적으로 컨텍스트를 사용할 때, 클래스 컴포넌트에서만 사용할 수 있는 `contextType`을 사용해야 했습니다. 그러나, React 16.3 이후부터는 `React.forwardRef()`를 사용하여 함수형 컴포넌트에서도 컨텍스트를 다룰 수 있습니다.

## 컨텍스트(Context)란?

컨텍스트(Context)는 React 컴포넌트 트리 내에서 데이터를 전달하는 방법입니다. 일반적으로 `props`를 통해 데이터를 하위 컴포넌트에 전달하는 방식과는 달리, 컨텍스트를 사용하면 중첩된 컴포넌트에게 데이터를 타고 넘겨줄 수 있습니다. 이를 통해 불필요한 `props` 전달을 줄이고, 코드를 더 깔끔하고 유지 보수하기 쉽게 만들 수 있습니다.

## React.forwardRef()를 사용한 컨텍스트 다루기

`React.forwardRef()`는 `ref`를 하위 컴포넌트로 전달하기 위해 사용됩니다. 이를 통해 함수형 컴포넌트에서도 `ref`를 사용할 수 있습니다. 따라서, 컨텍스트를 사용하는 컴포넌트에서 `ref`를 사용할 수 있도록 만들기 위해서 `React.forwardRef()`를 사용할 수 있습니다.

다음은 `React.forwardRef()`를 사용하여 컨텍스트를 다루는 예제입니다.

```jsx
import React, { createContext, forwardRef } from 'react';

// 컨텍스트 생성
const MyContext = createContext();

// 컨텍스트를 사용하는 하위 컴포넌트
const ChildComponent = forwardRef((props, ref) => {
  return (
    <MyContext.Consumer>
      {(contextValue) => (
        <div ref={ref}>
          {contextValue}
        </div>
      )}
    </MyContext.Consumer>
  );
});

// 주 컴포넌트
const ParentComponent = () => {
  // 컨텍스트 값 설정
  const contextValue = 'Hello, Context!';

  return (
    <MyContext.Provider value={contextValue}>
      <ChildComponent />
    </MyContext.Provider>
  );
};

export default ParentComponent;
```

위의 예제에서는 `React.forwardRef()`를 사용하여 `ChildComponent` 컴포넌트를 정의합니다. `ChildComponent` 컴포넌트는 `ref`를 사용하는 div 요소를 렌더링하기 전에 컨텍스트 값을 가져와서 렌더링합니다. 이렇게 하면 `ChildComponent`의 `ref`를 사용하여 해당 컴포넌트에 접근할 수 있습니다.

이제 `ParentComponent`에서 `MyContext.Provider`를 사용하여 컨텍스트 값을 설정하고, `ChildComponent`에서 `MyContext.Consumer`를 사용하여 해당 값을 사용할 수 있습니다.

## 결론

`React.forwardRef()`를 사용하면 함수형 컴포넌트에서도 `ref`를 사용할 수 있게 됩니다. 이를 활용하여 컨텍스트를 다루는 컴포넌트를 작성할 수 있습니다. 이렇게 하면 코드를 더 깔끔하고 유지 보수하기 쉽게 만들 수 있습니다.

#React #컨텍스트