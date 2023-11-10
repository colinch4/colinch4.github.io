---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 캘린더(Calendar) 기능을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [React]
comments: true
share: true
---

React.forwardRef() 함수는 리액트에서 사용자 정의 컴포넌트를 생성할 때 유용한 기능입니다. 이 함수를 활용하면 부모 컴포넌트에서 자식 컴포넌트에 접근하여 직접 프로퍼티나 메서드를 호출할 수 있습니다.

## 캘린더 컴포넌트의 기능 설계

캘린더 컴포넌트를 구현하기 위해 다음과 같은 기능을 설계해야 합니다:

1. 년/월 선택 기능
2. 특정 날짜 선택 및 강조 표시 기능
3. 이전/다음 달로 이동 기능

## 캘린더 컴포넌트 구현하기

먼저, 캘린더 컴포넌트를 작성하기 위해 다음과 같은 파일 구조를 가정합니다:

```
- Calendar.js
- CalendarMonth.js
- CalendarDay.js
```

### Calendar.js

먼저, Calendar.js 파일을 생성하고 다음과 같은 코드를 작성합니다:

```jsx
import React, { forwardRef } from 'react';
import CalendarMonth from './CalendarMonth';

const Calendar = forwardRef((props, ref) => {
  // 캘린더 로직 구현

  return (
    <div ref={ref}>
      {/* 캘린더 UI 구현 */}
      <CalendarMonth />
    </div>
  );
});

export default Calendar;
```

### CalendarMonth.js

다음으로, CalendarMonth.js 파일을 생성하고 다음과 같은 코드를 작성합니다:

```jsx
import React from 'react';
import CalendarDay from './CalendarDay';

const CalendarMonth = () => {
  // 달력 월별 구현 로직

  return (
    <div>
      {/* 달력 월별 UI 구현 */}
      <CalendarDay />
    </div>
  );
};

export default CalendarMonth;
```

### CalendarDay.js

마지막으로, CalendarDay.js 파일을 생성하고 다음과 같은 코드를 작성합니다:

```jsx
import React from 'react';

const CalendarDay = () => {
  // 달력 일별 구현 로직

  return (
    <div>
      {/* 달력 일별 UI 구현 */}
    </div>
  );
};

export default CalendarDay;
```

## 캘린더 컴포넌트 사용하기

캘린더 컴포넌트를 사용하기 위해 다음과 같이 부모 컴포넌트에서 호출할 수 있습니다:

```jsx
import React, { useRef } from 'react';
import Calendar from './Calendar';

const App = () => {
  const calendarRef = useRef();

  const handleButtonClick = () => {
    // 캘린더 컴포넌트의 메서드 호출 예시
    calendarRef.current.customMethod();
  };

  return (
    <div>
      <button onClick={handleButtonClick}>캘린더 메서드 호출</button>
      <Calendar ref={calendarRef} />
    </div>
  );
};

export default App;
```

## 결론

React.forwardRef()를 활용하여 캘린더 컴포넌트를 구현하는 방법을 알아보았습니다. 이러한 방식으로 캘린더 컴포넌트를 개발하면 부모 컴포넌트에서 직접 컴포넌트에 접근하여 원하는 기능을 수행할 수 있습니다. 다양한 기능을 추가하여 유연하고 재사용 가능한 캘린더 컴포넌트를 만들어 보세요.

[React 공식 문서 - forwardRef](https://ko.reactjs.org/docs/forwarding-refs.html)

#React #캘린더