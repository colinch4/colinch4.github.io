---
layout: post
title: "Redux Thunk를 사용한 이미지 lazy loading 구현 예제"
description: " "
date: 2023-10-18
tags: [ReduxThunk]
comments: true
share: true
---

이미지 Lazy Loading은 웹 페이지에서 이미지를 동적으로 로드하여 사용자 경험을 개선하는 기술입니다. Redux Thunk를 사용하면 비동기 작업을 처리하고 상태 관리를 용이하게 할 수 있습니다. 이번 예제에서는 Redux Thunk와 이미지 lazy loading을 결합하여 간단한 구현을 해보겠습니다.

## 개요

1. React와 Redux 라이브러리 설치
2. Redux store 설정
3. Redux Thunk 미들웨어 설정
4. 이미지 lazy loading을 위한 컴포넌트 작성
5. Redux 액션 및 리듀서 작성
6. 컨테이너 컴포넌트 작성

## 세부 설명

### 1. React와 Redux 라이브러리 설치

```
npm install react redux redux-thunk
```

### 2. Redux store 설정

```javascript
// store.js

import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers';

const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;
```

### 3. Redux Thunk 미들웨어 설정

```javascript
// actions.js

import axios from 'axios';

export const fetchImage = () => {
  return (dispatch) => {
    dispatch({ type: 'FETCH_IMAGE_REQUEST' });

    axios.get('https://api.example.com/images')
      .then((response) => {
        dispatch({ type: 'FETCH_IMAGE_SUCCESS', payload: response.data });
      })
      .catch((error) => {
        dispatch({ type: 'FETCH_IMAGE_FAILURE', error: error.message });
      });
  };
};
```

### 4. 이미지 Lazy Loading을 위한 컴포넌트 작성

```javascript
// ImageLazyLoad.js

import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchImage } from './actions';

const ImageLazyLoad = () => {
  const dispatch = useDispatch();
  const imageData = useSelector((state) => state.images);

  useEffect(() => {
    dispatch(fetchImage());
  }, [dispatch]);

  return (
    <div>
      {imageData.loading ? (
        <p>Loading...</p>
      ) : imageData.error ? (
        <p>{imageData.error}</p>
      ) : (
        <img src={imageData.imageURL} alt="Lazy Loaded Image" />
      )}
    </div>
  );
};

export default ImageLazyLoad;
```

### 5. Redux 액션 및 리듀서 작성

```javascript
// reducers.js

const initialState = {
  loading: false,
  imageURL: '',
  error: '',
};

const imageReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'FETCH_IMAGE_REQUEST':
      return {
        ...state,
        loading: true,
      };
    case 'FETCH_IMAGE_SUCCESS':
      return {
        ...state,
        loading: false,
        imageURL: action.payload,
        error: '',
      };
    case 'FETCH_IMAGE_FAILURE':
      return {
        ...state,
        loading: false,
        imageURL: '',
        error: action.error,
      };
    default:
      return state;
  }
};

export default imageReducer;
```

### 6. 컨테이너 컴포넌트 작성

```javascript
// App.js

import React from 'react';
import { Provider } from 'react-redux';
import store from './store';
import ImageLazyLoad from './ImageLazyLoad';

const App = () => {
  return (
    <Provider store={store}>
      <div>
        <h1>Lazy Loaded Image</h1>
        <ImageLazyLoad />
      </div>
    </Provider>
  );
};

export default App;
```

## 결론

이 예제에서는 Redux Thunk를 활용하여 이미지 lazy loading을 구현하는 방법을 살펴보았습니다. Redux를 사용하면 비동기 작업 및 데이터 상태 관리를 효율적으로 처리할 수 있으며, 이미지 lazy loading과 같은 사용자 경험을 개선하는 기능을 쉽게 구현할 수 있습니다.

> #React #Redux #Thunk