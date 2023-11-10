---
layout: post
title: "사용자 정의 훅(Custom Hook)과 함께 React.forwardRef()를 활용하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [CustomHook]
comments: true
share: true
---

React.js는 함수형 컴포넌트와 훅(Hook)을 통해 컴포넌트를 구성하는 방법을 제공합니다. 그 중에서도 사용자 정의 훅(Custom Hook)은 컴포넌트 로직을 재사용하기 위한 강력한 도구입니다. 또한, React.forwardRef()는 다른 컴포넌트로부터 ref를 전달받기 위한 방법으로 자주 사용됩니다.

## 사용자 정의 훅(Custom Hook)이란?

사용자 정의 훅은 일반적인 컴포넌트 로직을 추상화하여 재사용 가능한 형태로 구성하는 것을 말합니다. useEffect나 useState와 같은 내장 훅을 사용하여 컴포넌트 로직을 작성한 뒤, 이를 사용자 정의 훅으로 추출하여 이후 다른 컴포넌트에서 재사용할 수 있습니다.

## React.forwardRef()란?

React.forwardRef()는 ref를 다른 컴포넌트로 전달하기 위한 함수입니다. 이 함수를 사용하면 ref를 다른 컴포넌트의 하위 컴포넌트로 전달할 수 있습니다. 이는 특히 UI 라이브러리의 컴포넌트를 사용할 때 유용합니다.

## 사용자 정의 훅과 React.forwardRef() 함께 사용하기

이제 사용자 정의 훅과 React.forwardRef()를 함께 사용하는 방법에 대해 알아보겠습니다.

먼저, 사용자 정의 훅을 작성합니다.

```javascript
import { useEffect, useState } from 'react';

const useCustomHook = (initialValue) => {
  const [value, setValue] = useState(initialValue);
  
  useEffect(() => {
    // 컴포넌트 로직 작성
    // ...
  }, []);

  return value;
};

export default useCustomHook;
```

위의 코드에서는 초기값을 매개변수로 받아 useState를 사용하여 상태를 관리합니다. 또한, useEffect를 사용하여 컴포넌트 로직을 작성합니다.

이제, forwardRef를 사용하여 ref를 전달할 컴포넌트를 작성합니다.

```javascript
import useCustomHook from './useCustomHook';

const CustomComponent = React.forwardRef((props, ref) => {
  // ref를 이용한 작업 수행
  // ...

  return (
    // 컴포넌트 JSX 작성
    // ...
  );
});

export default CustomComponent;
```

위의 코드에서는 React.forwardRef()를 이용하여 ref를 전달받을 수 있는 컴포넌트를 생성합니다. ref 매개변수를 사용하여 원하는 작업을 수행할 수 있습니다.

사용자 정의 훅을 함께 사용하기 위해서는 다음과 같이 작성합니다.

```javascript
import useCustomHook from './useCustomHook';

const CustomComponent = React.forwardRef((props, ref) => {
  // useCustomHook을 사용하여 로직 재사용
  const value = useCustomHook(props.initialValue);

  // ref를 이용한 작업 수행
  // ...

  return (
    // 컴포넌트 JSX 작성
    // ...
  );
});
```

위의 코드에서는 useCustomHook을 호출하여 컴포넌트 로직을 재사용합니다. 이를 통해 CustomComponent 내에서 사용자 정의 훅의 상태와 로직을 활용할 수 있습니다.

이제, 사용자 정의 훅과 React.forwardRef()를 함께 사용하는 방법에 대해 알아보았습니다. 이를 통해 컴포넌트 로직을 재사용하고, 다른 컴포넌트로부터 ref를 전달받을 수 있습니다.

[#React](https://reactjs.org/) [#CustomHook](https://reactjs.org/docs/hooks-custom.html)