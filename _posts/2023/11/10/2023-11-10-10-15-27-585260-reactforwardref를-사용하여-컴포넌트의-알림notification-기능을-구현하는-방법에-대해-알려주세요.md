---
layout: post
title: "React.forwardRef()를 사용하여 컴포넌트의 알림(Notification) 기능을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

React는 사용자 정의 컴포넌트를 만들기 위해 `forwardRef()`라는 유용한 메서드를 제공합니다. 이 메서드를 사용하면 다른 컴포넌트에게 Ref를 전달할 수 있습니다. 이번 가이드에서는 `forwardRef()`를 사용하여 알림 기능을 가진 컴포넌트를 구현하는 방법에 대해 알아보겠습니다.

### 1. 알림 컴포넌트 생성하기

먼저, 알림 컴포넌트를 생성합니다. 알림 컴포넌트는 사용자가 전달한 메시지와 스타일을 표시하는 역할을 합니다. 아래는 예시 코드입니다.

```jsx
import React from 'react';

const Notification = React.forwardRef((props, ref) => {
  return (
    <div ref={ref} style={props.style}>
      {props.message}
    </div>
  );
});

export default Notification;
```

### 2. 알림 컴포넌트 사용하기

이제 생성한 알림 컴포넌트를 다른 컴포넌트에서 사용할 수 있습니다. 아래는 사용 예시입니다.

```jsx
{% raw %}
import React, { useRef } from 'react';
import Notification from './Notification';

const App = () => {
  const notificationRef = useRef(null);

  const handleShowNotification = () => {
    notificationRef.current.style.display = 'block';
  };

  const handleHideNotification = () => {
    notificationRef.current.style.display = 'none';
  };

  return (
    <div>
      <button onClick={handleShowNotification}>Show Notification</button>
      <button onClick={handleHideNotification}>Hide Notification</button>

      <Notification
        ref={notificationRef}
        style={{ display: 'none' }}
        message="This is a notification"
      />
    </div>
  );
};

export default App;
{% endraw %}
```

위의 예시 코드에서는 `useRef()`를 사용하여 알림 컴포넌트의 Ref를 생성하고, `handleShowNotification()` 및 `handleHideNotification()` 함수를 사용하여 알림을 보여주거나 숨기는 기능을 구현했습니다.

### 결론

이렇게 `React.forwardRef()`를 사용하여 알림 기능을 가진 컴포넌트를 구현할 수 있습니다. `forwardRef()`를 사용하면 다른 컴포넌트로 Ref를 전달할 수 있어 좀 더 유연한 컴포넌트 구조를 만들 수 있습니다.

> 참고: [React 공식 문서 - Forwarding Refs](https://reactjs.org/docs/forwarding-refs.html)

#react #컴포넌트