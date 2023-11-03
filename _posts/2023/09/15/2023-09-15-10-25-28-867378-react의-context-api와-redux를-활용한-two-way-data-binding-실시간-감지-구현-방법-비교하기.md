---
layout: post
title: "React의 Context API와 Redux를 활용한 Two-way Data Binding 실시간 감지 구현 방법 비교하기"
description: " "
date: 2023-09-15
tags: [React, ContextAPI, Redux, TwoWayDataBinding]
comments: true
share: true
---

React는 JavaScript 기반의 UI 라이브러리로, 컴포넌트 기반 아키텍처를 제공하여 재사용 가능한 UI 요소를 만들 수 있습니다. React에서 상위 컴포넌트로부터 하위 컴포넌트로 데이터를 전달하기 위해 Context API와 Redux라는 상태 관리 라이브러리를 사용할 수 있습니다. 이번 글에서는 두 방법을 사용하여 Two-way Data Binding을 구현하고, 실시간 감지 기능의 차이를 비교해보겠습니다.

## 1. Context API를 활용한 Two-way Data Binding 실시간 감지 구현

React의 Context API는 상위 컴포넌트에서 하위 컴포넌트로 데이터를 전달하고 싶을 때 사용할 수 있는 기능입니다. Context API를 사용하여 Two-way Data Binding을 구현하려면 다음과 같은 방법을 사용할 수 있습니다.

1. `React.createContext()`를 사용하여 Context 객체를 생성합니다.
2. 상위 컴포넌트에서 `Context.Provider`를 사용하여 데이터를 제공합니다.
3. 하위 컴포넌트에서 `Context.Consumer`를 사용하여 데이터를 사용합니다.
4. 사용자 입력을 감지하여 해당 데이터를 업데이트하고 싶을 경우, 상위 컴포넌트에서 콜백 함수를 정의하여 하위 컴포넌트에 전달합니다.

예제 코드는 다음과 같습니다.

```javascript
{% raw %}
import React, { createContext, useState } from 'react';

// Step 1: Context 생성
const DataContext = createContext(null);

// Step 2: Provider를 사용하여 데이터 제공
const ParentComponent = () => {
  const [data, setData] = useState('');

  // 데이터 업데이트 콜백 함수
  const handleDataChange = (newData) => {
    setData(newData);
  };

  return (
    <DataContext.Provider value={{ data, handleDataChange }}>
      <ChildComponent />
    </DataContext.Provider>
  );
};

// Step 3: Consumer를 사용하여 데이터 사용
const ChildComponent = () => {
  return (
    <DataContext.Consumer>
      {(context) => (
        <div>
          <input
            value={context.data}
            onChange={(e) => context.handleDataChange(e.target.value)}
          />
        </div>
      )}
    </DataContext.Consumer>
  );
};
{% endraw %}
```

## 2. Redux를 활용한 Two-way Data Binding 실시간 감지 구현

Redux는 React 상태 관리 라이브러리로, 애플리케이션의 상태를 중앙에서 관리하고 상태 변경을 예측 가능한 방식으로 처리합니다. Redux를 사용하여 Two-way Data Binding을 구현하려면 다음과 같은 방법을 사용할 수 있습니다.

1. Redux store를 생성하고, store의 상태 데이터를 정의합니다.
2. 액션(action)과 리듀서(reducer)를 사용하여 상태 변경 로직을 작성합니다.
3. 컴포넌트에서 `connect()` 함수를 사용하여 Redux store와 연결합니다.
4. 사용자 입력을 감지하여 액션을 디스패치(dispatch)하여 상태 변경을 처리합니다.

예제 코드는 다음과 같습니다.

```javascript
import React from 'react';
import { createStore } from 'redux';
import { Provider, connect } from 'react-redux';

// Step 1: Redux store 생성
const initialState = {
  data: '',
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case 'UPDATE_DATA':
      return {
        ...state,
        data: action.payload,
      };
    default:
      return state;
  }
};

const store = createStore(reducer);

// Step 3: 컴포넌트와 Redux store를 연결
const ChildComponent = ({ data, handleDataChange }) => (
  <div>
    <input value={data} onChange={(e) => handleDataChange(e.target.value)} />
  </div>
);

const mapStateToProps = (state) => ({
  data: state.data,
});

const mapDispatchToProps = (dispatch) => ({
  handleDataChange: (newData) =>
    dispatch({ type: 'UPDATE_DATA', payload: newData }),
});

const ConnectedChildComponent = connect(
  mapStateToProps,
  mapDispatchToProps
)(ChildComponent);

const ParentComponent = () => (
  <Provider store={store}>
    <ConnectedChildComponent />
  </Provider>
);
```

## 결론

두 방법 모두 Two-way Data Binding을 실시간으로 감지하는 기능을 제공합니다. Context API는 React 자체에서 제공하는 기능으로 간단하게 사용할 수 있지만, 상태 관리 로직을 직접 작성해야 하기 때문에 복잡한 애플리케이션에서는 유지보수가 어려울 수 있습니다. 반면에 Redux는 별도의 라이브러리로 사용하기 위해 추가적인 설정이 필요하지만, 중앙에서 상태를 관리하고 예측 가능한 상태 변경 로직을 작성할 수 있습니다. 프로젝트의 요구사항과 팀의 개발 경험에 따라 적절한 상태 관리 방식을 선택해야 합니다.

#React #ContextAPI #Redux #TwoWayDataBinding