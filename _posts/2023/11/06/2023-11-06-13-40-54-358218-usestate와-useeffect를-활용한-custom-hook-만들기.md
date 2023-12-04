---
layout: post
title: "useState와 useEffect를 활용한 Custom Hook 만들기"
description: " "
date: 2023-11-06
tags: [reactjs]
comments: true
share: true
---

React에서는 `useState`와 `useEffect`를 활용하여 상태 관리와 사이드 이펙트 처리를 간편하게 할 수 있습니다. 이번에는 이 두 가지 훅을 활용하여 Custom Hook을 만들어 보겠습니다.

## Custom Hook이란?

Custom Hook은 여러 컴포넌트에서 재사용할 수 있는 로직을 분리하여 작성하는 것을 말합니다. 이로써 코드의 재사용성과 가독성을 향상시킬 수 있습니다. 

## useState와 useEffect 이해하기

`useState`는 컴포넌트의 상태를 추가하고 관리할 수 있는 훅입니다. `useEffect`는 컴포넌트가 렌더링 될 때마다 수행되는 사이드 이펙트를 처리할 수 있는 훅입니다.

## Custom Hook 만들기

간단한 예제로, 로딩 상태를 처리하는 Custom Hook을 만들어보겠습니다.

```jsx
import { useState, useEffect } from 'react';

const useLoading = () => {
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    setIsLoading(true);

    // 로딩 처리 작업
    // 예를 들어, 데이터를 가져오기 위한 API 호출이나 이미지 로딩 등

    setIsLoading(false);
  }, []);

  return isLoading;
};

export default useLoading;
```

위의 코드에서는 `useState`를 이용하여 `isLoading` 상태를 관리하고 있습니다. `useEffect`를 이용하여 로딩 처리 작업을 수행한 후에 `isLoading` 상태를 업데이트합니다. 빈 의존성 배열(`[]`)을 두 번째 인자로 전달함으로써 컴포넌트가 처음 렌더링 될 때만 이펙트를 실행하도록 설정하였습니다.

## Custom Hook 사용하기

이제 위에서 만든 `useLoading` Custom Hook을 사용해보겠습니다.

```jsx
import React from 'react';
import useLoading from './useLoading';

const App = () => {
  const isLoading = useLoading();

  return (
    <div>
      {isLoading ? '로딩 중...' : '로딩 완료!'}
    </div>
  );
};

export default App;
```

위의 코드에서는 `useLoading` Hook을 `isLoading` 변수에 할당하여 사용하고 있습니다. `isLoading` 변수의 값에 따라 로딩 중 메시지 또는 로딩 완료 메시지가 렌더링됩니다.

## 마무리

Custom Hook을 사용하면 로직을 분리하여 재사용성과 가독성을 개선할 수 있습니다. `useState`와 `useEffect`를 포함한 다른 훅들과 함께 사용하면 훨씬 더 효율적인 React 애플리케이션을 개발할 수 있습니다.

더 자세한 내용은 React 공식 문서를 참고하시기 바랍니다.

- [React 공식 문서 - useState](https://ko.reactjs.org/docs/hooks-state.html)
- [React 공식 문서 - useEffect](https://ko.reactjs.org/docs/hooks-effect.html)

[#React](https://www.example.com/hashtags/react) [#CustomHook](https://www.example.com/hashtags/customhook)