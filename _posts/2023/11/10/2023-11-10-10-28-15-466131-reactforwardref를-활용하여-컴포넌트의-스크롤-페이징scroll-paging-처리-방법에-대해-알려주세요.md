---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 스크롤 페이징(Scroll Paging) 처리 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [reactforwardref]
comments: true
share: true
---

React는 컴포넌트 기반의 JavaScript 라이브러리로, 사용자 인터페이스를 구축하기 위한 많은 기능을 제공합니다. 이 중 하나는 스크롤 페이징(Scroll Paging)입니다. 스크롤 페이징은 웹페이지나 앱에서 스크롤을 내리면 새로운 데이터를 로드하여 연속적인 페이지 스크롤을 구현하는 기능을 말합니다.

React에서 스크롤 페이징을 구현하기 위해서는 `React.forwardRef()`를 활용할 수 있습니다. `React.forwardRef()` 메소드는 렌더링할 컴포넌트를 반환하는 함수 컴포넌트를 생성할 때 사용됩니다. 이를 통해 부모 컴포넌트에서 자식 컴포넌트에 접근할 수 있게 됩니다.

아래는 `React.forwardRef()`를 사용하여 스크롤 페이징을 처리하는 예시 코드입니다.

```javascript
{% raw %}
import React, { useRef, useEffect, forwardRef } from 'react';

const ScrollPagingComponent = forwardRef((props, ref) => {
  const containerRef = useRef(null);

  // 스크롤 이벤트 핸들러
  const handleScroll = () => {
    const container = containerRef.current;
    if (container.scrollHeight - container.scrollTop === container.clientHeight) {
      // 스크롤이 마지막 위치에 도달하면 새로운 데이터를 로드하는 로직
      props.loadMoreData();
    }
  };

  useEffect(() => {
    const container = containerRef.current;
    container.addEventListener('scroll', handleScroll);

    return () => {
      container.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div ref={ref} style={{ height: '400px', overflowY: 'scroll' }}>
      <div ref={containerRef}>
        {props.children}
      </div>
    </div>
  );
});

export default ScrollPagingComponent;
{% endraw %}
```

위 코드에서 `ScrollPagingComponent` 컴포넌트는 부모 컴포넌트에서 `ref`를 사용하여 스크롤 이벤트를 처리합니다. `ref`를 사용하여 부모 컴포넌트에서 접근할 수 있게 되며, `loadMoreData()` 함수로 새로운 데이터를 로드하는 로직을 실행할 수 있습니다.

아래는 `ScrollPagingComponent`를 사용하는 부모 컴포넌트의 예시 코드입니다.

```javascript
import React, { useRef, useEffect, useState } from 'react';
import ScrollPagingComponent from './ScrollPagingComponent';

const ParentComponent = () => {
  const scrollContainerRef = useRef(null);
  const [data, setData] = useState([]);

  // 새로운 데이터를 로드하는 함수
  const loadMoreData = () => {
    // 데이터 로딩 로직
    // ...
    // 로딩된 데이터를 State에 저장
    setData([...data, ...newData]);
  };

  useEffect(() => {
    // 초기 데이터 로딩 로직
    // ...
    // 로딩된 데이터를 State에 저장
    setData(initialData);
  }, []);

  return (
    <div>
      <ScrollPagingComponent ref={scrollContainerRef} loadMoreData={loadMoreData}>
        {data.map((item, index) => (
          // 데이터를 모델링한 컴포넌트 출력
          // ...
        ))}
      </ScrollPagingComponent>
    </div>
  );
};

export default ParentComponent;
```

위 코드에서 `ParentComponent`는 `ScrollPagingComponent`를 사용하여 스크롤 페이징을 처리합니다. `ScrollPagingComponent`에 `ref`를 사용하여 부모 컴포넌트에서 접근하고, `loadMoreData()` 함수를 전달하여 새로운 데이터를 로드할 수 있습니다.

이와 같이 `React.forwardRef()`를 활용하여 스크롤 페이징을 처리할 수 있는 방법을 알아보았습니다. 이를 이용하면 웹페이지나 앱에서 대용량 데이터를 효율적으로 로딩하고 처리할 수 있습니다.

참고 문서:
- [React.forwardRef() 공식 문서](https://ko.reactjs.org/docs/react-api.html#reactforwardref)