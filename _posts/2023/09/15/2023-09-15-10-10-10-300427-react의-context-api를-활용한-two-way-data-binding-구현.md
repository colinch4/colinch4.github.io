---
layout: post
title: "React의 Context API를 활용한 Two-way Data Binding 구현"
description: " "
date: 2023-09-15
tags: [React, ContextAPI]
comments: true
share: true
---

React는 JavaScript 기반의 UI 라이브러리로, 컴포넌트 기반의 개발 방식을 제공하여 화면을 구성하는 데 매우 효율적입니다. React의 Context API를 사용하면 컴포넌트 간에 데이터를 전달하고 공유할 수 있습니다. 이를 활용하여 Two-way Data Binding을 구현하는 방법에 대해 알아보겠습니다.

## Two-way Data Binding이란?

Two-way Data Binding은 데이터가 컴포넌트와 뷰 사이에서 양방향으로 전달되는 개념입니다. 즉, 데이터의 변화가 발생하면 이를 컴포넌트와 뷰 양쪽에 모두 반영하는 것을 말합니다. 이를 통해 사용자 입력과 UI 표시 간의 실시간 동기화가 가능해집니다.

## React의 Context API

React의 Context API는 컴포넌트 트리 전체에서 전역적으로 상태를 공유하기 위한 메커니즘을 제공합니다. 이를 사용하여 Two-way Data Binding을 구현할 수 있습니다. 아래는 간단한 예제 코드입니다.

```jsx
// AppContext.js
{% raw %}
import React, { createContext, useState } from 'react';

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [text, setText] = useState('');

  const handleChange = (e) => {
    setText(e.target.value);
  };

  return (
    <AppContext.Provider value={{ text, handleChange }}>
      {children}
    </AppContext.Provider>
  );
};
{% endraw %}
```

위 코드에서는 `AppContext.js` 파일에서 Context를 생성하고, `AppProvider`를 사용하여 컴포넌트 트리를 감싸는 역할을 합니다. 상태 `text`와 이를 변경하는 `handleChange` 함수를 Context에서 관리합니다.

```jsx
// InputComponent.js

import React, { useContext } from 'react';
import { AppContext } from './AppContext';

const InputComponent = () => {
  const { text, handleChange } = useContext(AppContext);

  return (
    <input type="text" value={text} onChange={handleChange} />
  );
};

export default InputComponent;
```

위 코드에서는 `InputComponent.js` 파일에서 Context를 사용하여 상태 `text`와 `handleChange` 함수를 받아옵니다. `<input>` 요소에 `value`와 `onChange` props로 연결하여 Two-way Data Binding을 구현합니다.

```jsx
// DisplayComponent.js

import React, { useContext } from 'react';
import { AppContext } from './AppContext';

const DisplayComponent = () => {
  const { text } = useContext(AppContext);

  return (
    <p>{text}</p>
  );
};

export default DisplayComponent;
```

위 코드에서는 `DisplayComponent.js` 파일에서도 Context를 사용하여 상태 `text`를 받아옵니다. `<p>` 요소에 상태 `text`를 표시하여 사용자가 입력하는 내용을 실시간으로 표시합니다.

## 마무리

React의 Context API를 활용하여 Two-way Data Binding을 구현하는 방법에 대해 알아보았습니다. Context를 사용하면 컴포넌트 간에 데이터를 전달하고 공유하는 것이 더욱 쉬워지며, 사용자 입력과 UI 표시 간의 실시간 동기화를 구현할 수 있습니다. 이를 활용하여 리액트 애플리케이션의 상태 관리를 효율적으로 할 수 있습니다.

#React #ContextAPI