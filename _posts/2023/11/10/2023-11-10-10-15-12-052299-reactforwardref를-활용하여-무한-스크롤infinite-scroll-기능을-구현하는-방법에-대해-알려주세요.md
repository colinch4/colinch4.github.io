---
layout: post
title: "React.forwardRef()를 활용하여 무한 스크롤(Infinite Scroll) 기능을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [reactjs]
comments: true
share: true
---

React.forwardRef()는 리액트에서 컴포넌트 간의 ref 전달을 가능하게 해주는 함수입니다. 이를 활용하여 무한 스크롤 기능을 구현할 수 있습니다. 무한 스크롤은 사용자가 스크롤을 내릴 때마다 새로운 데이터를 동적으로 로드하여 화면에 표시하는 기능입니다. 아래에 React.forwardRef()를 활용하여 무한 스크롤 기능을 구현하는 방법을 설명하겠습니다.

## 1. 컴포넌트 구조 설정

첫 번째로, 무한 스크롤 기능을 사용할 컴포넌트의 구조를 설정해야 합니다. 일반적으로 스크롤되는 컨테이너 컴포넌트와 데이터를 표시하는 아이템 컴포넌트로 구성됩니다.

```jsx
{% raw %}
import React, { forwardRef, useRef, useEffect } from 'react';

const ScrollContainer = forwardRef((props, ref) => {
  const containerRef = useRef();

  // 스크롤 이벤트 핸들러
  const handleScroll = () => {
    const { scrollTop, clientHeight, scrollHeight } = containerRef.current;
    if (scrollHeight - scrollTop === clientHeight) {
      props.onScrollToEnd();
    }
  };

  useEffect(() => {
    containerRef.current.addEventListener('scroll', handleScroll);
    return () => {
      containerRef.current.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div ref={ref} style={{ height: '400px', overflow: 'auto' }} ref={containerRef}>
      {props.children}
    </div>
  );
});

const ScrollItem = ({ data }) => {
  return <div>{data}</div>;
};
{% endraw %}
```

위의 코드에서는 ScrollContainer라는 스크롤 컨테이너 컴포넌트와 ScrollItem이라는 데이터를 표시하는 아이템 컴포넌트가 선언되어 있습니다. ScrollContainer 컴포넌트에서는 ref와 스크롤 이벤트를 처리하는 로직이 작성되어 있습니다.

## 2. 무한 스크롤 기능 구현

다음으로, 무한 스크롤 기능을 구현해보겠습니다. ScrollContainer 컴포넌트의 스크롤 이벤트 핸들러에서 스크롤이 페이지 끝에 도달했을 때마다 새로운 데이터를 로드하도록 처리합니다. 이를 위해 부모 컴포넌트에서 ScrollContainer 컴포넌트를 렌더링할 때 onScrollToEnd props를 전달해줘야 합니다.

```jsx
const ParentComponent = () => {
  const scrollContainerRef = useRef();

  const handleScrollToEnd = () => {
    // 새로운 데이터 로드 로직
    // ...

    // 스크롤 컨테이너를 새로운 높이로 갱신
    scrollContainerRef.current.style.height = `${newHeight}px`;
  };

  return (
    <div>
      {/* ScrollContainer 컴포넌트 렌더링 */}
      <ScrollContainer ref={scrollContainerRef} onScrollToEnd={handleScrollToEnd}>
        {/* 데이터 아이템 렌더링 */}
        {data.map((item, index) => (
          <ScrollItem key={index} data={item} />
        ))}
      </ScrollContainer>
    </div>
  );
};
```

위의 코드에서는 ParentComponent에서 ScrollContainer를 렌더링하고, handleScrollToEnd 함수를 ScrollContainer 컴포넌트의 onScrollToEnd props로 전달합니다. handleScrollToEnd 함수에서는 새로운 데이터를 로드하고, 스크롤 컨테이너의 높이를 갱신하는 로직을 작성하면 됩니다.

무한 스크롤 기능을 위한 React.forwardRef()를 활용한 구현 방법을 살펴보았습니다. 이를 통해 사용자가 스크롤을 내릴 때마다 새로운 데이터를 동적으로 로드하여 무한 스크롤 기능을 구현할 수 있습니다.

자세한 내용은 [React 공식 문서](https://reactjs.org/docs/forwarding-refs.html)를 참고하여 구현해보세요!

#React #무한스크롤