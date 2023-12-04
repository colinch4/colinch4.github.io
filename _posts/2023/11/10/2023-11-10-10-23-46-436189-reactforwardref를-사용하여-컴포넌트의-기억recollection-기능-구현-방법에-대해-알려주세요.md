---
layout: post
title: "React.forwardRef()를 사용하여 컴포넌트의 기억(Recollection) 기능 구현 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [reactjs]
comments: true
share: true
---

React는 개발자에게 많은 유용한 기능과 도구를 제공합니다. 그 중 하나는 React.forwardRef() 함수입니다. 이 함수를 사용하면 ref를 자식 컴포넌트로 전달할 수 있습니다. 이를 이용하여 컴포넌트의 기억(Recollection) 기능을 구현할 수 있습니다.

## Recollection이란?

Recollection은 컴포넌트가 자신의 상태를 "기억"하여 다시 렌더링될 때 이전 상태를 복원하는 기능입니다. 예를 들어, 사용자가 폼을 작성하다가 다른 페이지로 이동했다가 돌아올 때 이전에 작성한 내용을 다시 보여주는 것이 Recollection의 대표적인 예입니다.

## React.forwardRef()를 사용한 Recollection 구현 방법

React.forwardRef()를 사용하여 Recollection 기능을 구현하는 방법은 다음과 같습니다.

1. Recollection을 적용할 컴포넌트를 생성합니다.
2. 컴포넌트의 상태(State)를 관리하기 위한 useRef()를 사용하여 ref의 초기값을 설정합니다.
3. React.forwardRef() 함수를 사용하여 ref를 자식 컴포넌트로 전달할 수 있는 HOC(Higher Order Component)를 생성합니다.
4. HOC로 감싸진 자식 컴포넌트에서 ref를 직접 사용하여 상태를 기억하고 업데이트합니다.

아래는 React.forwardRef()를 사용하여 Recollection 기능을 구현하는 예제 코드입니다.

```javascript
import React, { useState, useRef, useImperativeHandle, forwardRef } from 'react';

const RecollectionComponent = forwardRef((props, ref) => {
  // ref를 사용하여 상태 기억
  const [value, setValue] = useState('');

  // ref로 컴포넌트의 상태를 외부에서 업데이트할 수 있도록 함
  useImperativeHandle(ref, () => ({
    getValue: () => value,
    setValue: (newValue) => setValue(newValue)
  }));

  return (
    <input
      type="text"
      value={value}
      onChange={(event) => setValue(event.target.value)}
    />
  );
});

// 컴포넌트를 사용하는 측에서 ref를 사용하여 상태 업데이트
const ParentComponent = () => {
  const recollectionRef = useRef();

  const handleClick = () => {
    console.log(recollectionRef.current.getValue());
  };

  return (
    <div>
      <RecollectionComponent ref={recollectionRef} />
      <button onClick={handleClick}>Get Value</button>
    </div>
  );
};

export default ParentComponent;
```

위의 코드에서 RecollectionComponent는 값을 입력받는 `<input>` 요소를 포함하는 컴포넌트입니다. ref를 사용하여 상태를 기억하고, useImperativeHandle을 통해 외부에서 상태를 업데이트할 수 있는 인터페이스를 제공합니다.

ParentComponent에서는 RecollectionComponent를 사용할 때 ref를 사용하여 RecollectionComponent의 상태에 접근하고 업데이트할 수 있습니다. 위의 예제에서는 버튼을 클릭할 때 RecollectionComponent의 값(value)을 콘솔에 출력하는 방식으로 확인할 수 있습니다.

React.forwardRef()를 사용하여 Recollection 기능을 구현하면, 자식 컴포넌트에서도 부모 컴포넌트의 상태를 간단하게 업데이트할 수 있습니다.

더 자세한 내용은 React 공식 문서 [React.forwardRef()](https://ko.reactjs.org/docs/react-api.html#reactforwardref)를 참고해주세요.

#Recollection #React