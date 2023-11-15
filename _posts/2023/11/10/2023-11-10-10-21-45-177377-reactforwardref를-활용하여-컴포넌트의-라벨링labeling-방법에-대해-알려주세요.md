---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 라벨링(Labeling) 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [react]
comments: true
share: true
---

컴포넌트의 라벨링(Labeling)은 웹 애플리케이션에서 접근성을 개선하는 중요한 요소 중 하나입니다. 접근성은 모든 사용자가 웹 사이트나 애플리케이션에 쉽게 접근할 수 있도록 하는 것을 의미합니다.

React에서는 `React.forwardRef()`라는 API를 제공하여, 라벨링을 구현할 수 있습니다. 이를 사용하여 컴포넌트를 라벨과 연결하고, 스크린 리더(Screen Reader) 또는 키보드 사용자에게 해당 라벨을 전달할 수 있습니다.

## `React.forwardRef()`란?

`React.forwardRef()`는 React 함수 컴포넌트에서 ref를 전달하는 방법을 제공합니다. 이를 사용하면 자식 컴포넌트 내부의 DOM 요소에 직접 접근할 수 있습니다. 또한, ref를 통해 부모 컴포넌트에서 자식 컴포넌트의 DOM 요소를 조작하거나 정보를 가져올 수 있습니다. 

아래는 `React.forwardRef()`를 사용한 예시입니다.

```jsx
const CustomInput = React.forwardRef((props, ref) => {
  return <input ref={ref} {...props} />;
});

const App = () => {
  const inputRef = React.useRef();

  const handleClick = () => {
    inputRef.current.focus();
  };

  return (
    <div>
      <CustomInput ref={inputRef} />
      <button onClick={handleClick}>Focus Input</button>
    </div>
  );
}
```

위의 코드에서 `CustomInput` 컴포넌트는 `input` 요소를 렌더링합니다. `CustomInput` 컴포넌트에 `ref`를 전달하여, 부모 컴포넌트에서 `input` 요소에 접근할 수 있습니다. `App` 컴포넌트에서는 `button`을 클릭하면 `input`을 포커스시키는 `handleClick` 함수를 정의했습니다.

## 컴포넌트 라벨링 구현 방법

아래는 `React.forwardRef()`를 활용하여 컴포넌트의 라벨링을 구현하는 일반적인 방법입니다:

1. 부모 컴포넌트에서 `React.createRef()` 또는 `useRef()`를 사용하여 ref를 생성합니다.
2. 생성한 ref를 자식 컴포넌트에 `ref` prop으로 전달합니다.
3. 자식 컴포넌트에서 `React.forwardRef()`를 사용하여 `ref`를 받아옵니다.
4. 자식 컴포넌트 내부의 DOM 요소에 `ref`를 적용합니다.

```jsx
const ChildComponent = React.forwardRef((props, ref) => {
  return (
    <div>
      <input ref={ref} type="text" />
      <label>{props.label}</label>
    </div>
  );
});

const ParentComponent = () => {
  const inputRef = React.useRef();

  const handleClick = () => {
    inputRef.current.focus();
  };

  return (
    <div>
      <ChildComponent ref={inputRef} label="Name" />
      <button onClick={handleClick}>Focus Input</button>
    </div>
  );
}
```

위의 예시에서 `ChildComponent`는 `input` 요소와 `label`을 렌더링합니다. `ChildComponent`에 `ref`를 적용하여, 부모 컴포넌트에서 `inputRef`로 `input` 요소에 접근할 수 있습니다. 라벨은 `props.label`을 통해 전달됩니다.

이렇게 구현한 라벨링은 접근성을 높일 뿐만 아니라, 코드의 재사용성과 유지보수성도 향상시킵니다.

더 자세한 내용을 알고 싶다면, [React 공식 문서](https://reactjs.org/docs/forwarding-refs.html)를 참조하시기 바랍니다.

#React #ReactForwardRef