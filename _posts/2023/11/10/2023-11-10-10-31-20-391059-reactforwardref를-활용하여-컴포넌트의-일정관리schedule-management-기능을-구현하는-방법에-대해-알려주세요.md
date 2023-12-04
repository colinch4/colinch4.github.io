---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 일정관리(Schedule Management) 기능을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [reactjs]
comments: true
share: true
---

React.forwardRef()는 React에서 함수형 컴포넌트에서 Ref 속성을 사용할 수 있도록 해주는 기능입니다. Ref는 DOM 요소나 컴포넌트 인스턴스에 직접 접근할 수 있는 방법을 제공합니다. 이 기능을 활용하여 컴포넌트의 일정관리 기능을 구현하는 방법을 알아보겠습니다.

## 1. 컴포넌트 생성

일정관리 기능을 구현하기 위해 `ScheduleManager`라는 컴포넌트를 생성합니다. 이 컴포넌트는 일정을 추가하고 보여주는 기능을 포함하도록 설계합니다.

```jsx
import React, { useState, forwardRef } from 'react';

const ScheduleManager = forwardRef((props, ref) => {
  const [schedule, setSchedule] = useState('');

  const addSchedule = () => {
    // 일정을 추가하는 로직
  };

  return (
    <div>
      <input type="text" value={schedule} onChange={e => setSchedule(e.target.value)} />
      <button onClick={addSchedule}>일정 추가</button>
      <ul>
        {/* 일정을 보여주는 로직 */}
      </ul>
    </div>
  );
});

export default ScheduleManager;
```

`ScheduleManager` 컴포넌트는 내부적으로 `schedule`이라는 상태값을 관리합니다. `addSchedule` 함수는 버튼을 클릭했을 때 새로운 일정을 추가하는 로직을 구현하면 됩니다.

## 2. Ref 사용하기

`ScheduleManager` 컴포넌트를 사용할 부모 컴포넌트에서 Ref를 생성하고, Ref 속성을 `ScheduleManager` 컴포넌트에 전달합니다.

```jsx
import React, { useRef } from 'react';
import ScheduleManager from './ScheduleManager';

const App = () => {
  const scheduleManagerRef = useRef(null);

  const handleButtonClick = () => {
    // ScheduleManager 컴포넌트에서 Ref를 이용하여 일정 추가 로직 실행
    scheduleManagerRef.current.addSchedule();
  };

  return (
    <div>
      <h1>일정 관리</h1>
      <ScheduleManager ref={scheduleManagerRef} />
      <button onClick={handleButtonClick}>일정 추가</button>
    </div>
  );
};

export default App;
```

부모 컴포넌트에서는 `useRef`를 사용하여 `scheduleManagerRef` Ref 객체를 생성합니다. `handleButtonClick` 함수에서는 `ScheduleManager` 컴포넌트에서 Ref를 이용하여 일정 추가 로직을 실행할 수 있습니다. 이렇게 Ref를 사용하면 부모 컴포넌트에서 자식 컴포넌트의 메서드 또는 속성에 접근할 수 있게 됩니다.

## 마무리

React.forwardRef()를 활용하여 컴포넌트의 일정관리 기능을 구현하는 방법에 대해 알아보았습니다. Ref를 사용하여 컴포넌트 간의 상호작용을 쉽게 구현할 수 있습니다. 추가로 필요한 기능을 구현하거나 디자인을 적용하는 등의 작업을 진행하여 원하는 일정관리 기능을 완성할 수 있습니다.

**참고문서:**
- React 공식 문서: [Forwarding Refs](https://ko.reactjs.org/docs/forwarding-refs.html) 
- Velopert's Blog: [React 포워딩 레퍼런스로 문제 해결하기](https://velog.io/@velopert/ref-forwarding-in-react) 

#React #ReactForwardRef #일정관리