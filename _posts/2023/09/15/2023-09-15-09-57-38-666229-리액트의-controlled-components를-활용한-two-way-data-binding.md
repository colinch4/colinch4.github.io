---
layout: post
title: "리액트의 Controlled Components를 활용한 Two-way Data Binding"
description: " "
date: 2023-09-15
tags: [React, ControlledComponents, TwoWayDataBinding]
comments: true
share: true
---

리액트는 사용자 입력과 컴포넌트 상태(state)를 손쉽게 연결시켜주는 Controlled Components를 제공합니다. 이를 활용하면 사용자의 입력이 컴포넌트 상태에 반영되는 동시에, 상태의 변경이 입력 값에도 자동으로 반영될 수 있습니다. 이로 인해 Two-way Data Binding을 구현하는데 큰 도움이 됩니다.

이 기능을 활용해 입력 양식 폼(form)을 만들거나 사용자의 입력을 실시간으로 반영해야 하는 경우, Controlled Components를 사용하는 것이 좋습니다. 아래는 Controlled Components를 활용하여 입력 필드와 상태(state) 간의 양방향 데이터 바인딩을 구현하는 예시입니다.

```jsx
import React, { useState } from 'react';

const MyForm = () => {
  const [name, setName] = useState('');

  const handleChange = (e) => {
    setName(e.target.value);
  };

  return (
    <form>
      <label>
        이름:
        <input type="text" value={name} onChange={handleChange} />
      </label>
      <p>입력한 이름: {name}</p>
    </form>
  );
};

export default MyForm;
```

위의 예시에서는 `useState` 훅을 활용하여 `name` 상태를 선언합니다. 이후 `onChange` 이벤트 핸들러를 통해 사용자의 입력 값을 `name` 상태에 반영합니다. 이렇게 상태와 입력 필드를 연결한다면, 사용자가 입력한 값은 `value={name}`을 통해 입력 필드에 반영되며, 입력 필드의 값이 변경되는 경우 `onChange` 이벤트 핸들러를 통해 상태 업데이트가 이루어집니다.

이처럼 Controlled Components를 활용하면 데이터를 효율적으로 관리하고, 입력 값의 변경을 쉽게 추적할 수 있습니다. 또한, Two-way Data Binding을 구현하여 사용자의 입력과 상태 간의 실시간 동기화를 가능하게 합니다.

#React #리액트 #ControlledComponents #TwoWayDataBinding