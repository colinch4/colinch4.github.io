---
layout: post
title: "React.forwardRef()를 활용하여 컴포넌트의 검색 필터(Search Filter) 기능을 구현하는 방법에 대해 알려주세요."
description: " "
date: 2023-11-10
tags: [forwarding]
comments: true
share: true
---

React에서 `forwardRef` 함수는 ref를 자식 컴포넌트로 전달하기 위해 사용됩니다. 이를 활용하여 검색 필터 기능이 있는 컴포넌트를 구현할 수 있습니다. 이번 블로그 포스트에서는 `forwardRef`를 사용하여 간단한 검색 필터 기능을 가진 컴포넌트를 만드는 방법에 대해 알아보겠습니다.

## 1. `SearchFilter` 컴포넌트 생성

먼저, `SearchFilter`라고 불리는 새로운 컴포넌트를 생성합니다. 이 컴포넌트는 검색 필터 기능을 담당하고 있습니다. 다음은 예시 코드입니다.

```jsx
import React, { forwardRef } from 'react';

const SearchFilter = forwardRef((props, ref) => {
  const handleInputChange = (e) => {
    const searchText = e.target.value;
    // 검색어 변경 시 동작할 로직
    // ...
  };

  return (
    <div>
      <input type="text" onChange={handleInputChange} ref={ref} />
    </div>
  );
});

export default SearchFilter;
```

위 코드에서 `forwardRef` 함수를 사용하여 `SearchFilter` 컴포넌트를 생성했습니다. `forwardRef`의 콜백 함수에서는 `ref`를 받아와서 input 요소에 연결해주었습니다. 또한 `onChange` 핸들러를 통해 검색어가 변경될 때마다 동작하는 로직을 추가할 수 있습니다.

## 2. 부모 컴포넌트에서 사용

이제 `SearchFilter` 컴포넌트를 부모 컴포넌트에서 사용해보겠습니다. 다음은 예시 코드입니다.

```jsx
import React, { useRef } from 'react';
import SearchFilter from './SearchFilter';

const ParentComponent = () => {
  const searchFilterRef = useRef(null);

  const handleSearch = () => {
    const searchValue = searchFilterRef.current.value;
    // 검색 필터 적용 및 검색 동작
    // ...
  };

  return (
    <div>
      <SearchFilter ref={searchFilterRef} />
      <button onClick={handleSearch}>검색</button>
    </div>
  );
};

export default ParentComponent;
```

위 코드에서는 `SearchFilter` 컴포넌트를 `ParentComponent`에서 사용하고 있습니다. `useRef` 훅을 사용하여 `searchFilterRef`를 생성한 후, `SearchFilter` 컴포넌트의 `ref` prop에 연결해줍니다. 이렇게 하면 `SearchFilter` 컴포넌트 내부의 input 요소에 접근할 수 있습니다.

`handleSearch` 함수에서는 검색 버튼 클릭 시 `searchFilterRef.current.value`를 통해 검색어를 가져올 수 있습니다. 이를 활용하여 실제 검색 필터 적용 및 검색 동작을 수행할 수 있습니다.

## 마무리

이번 블로그 포스트에서는 `React.forwardRef()`를 사용하여 검색 필터 기능이 있는 컴포넌트를 구현하는 방법에 대해 알아보았습니다. `forwardRef`를 사용하면 부모 컴포넌트에서 자식 컴포넌트의 ref에 접근할 수 있으므로, 다양한 상황에서 유용하게 활용할 수 있습니다. 이 기능을 활용하여 다양한 입력 요소나 컴포넌트를 구현해보세요!

### References
- [React 문서 - forwardRef](https://ko.reactjs.org/docs/forwarding-refs.html)
- [React 코드 예시 - forwardRef](https://reactjs.org/docs/forwarding-refs.html#forwarding-refs-in-higher-order-components)