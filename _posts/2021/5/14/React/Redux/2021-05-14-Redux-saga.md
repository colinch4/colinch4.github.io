---
layout: post
title: "[redux] Redux-Saga"
description: " "
date: 2021-05-14
tags: [redux]
comments: true
share: true
---


## Redux-Saga
## Structure

- worker saga
- watcher saga
- root saga

Redux-saga는 기본적으로 3가지의 saga를 가지고 동작하게 된다.

worker saga : action에 따른 task를 하는 역할을 한다.

watcher saga : action을 listening 하는 saga. action이 발생시, 등록되어 있는 worker saga를 실행시킨다.

root saga : saga 함수의 값들을 모아서 미들웨에게 전달해주는 역할을 한다.

## description

Saga는 generator 함수로 구현되어 있고,

generator 함수가 yield 하는 객체를  (이를  Effect라고 한다) redux-saga middleware로 보내준다.

그리고 yield된 객체(Effect)를 saga middleware가 처리를 하게 된다.

saga의 yield keyword 옆에 오는 expression은 saga 에서 제공하는 함수들, promise 등이 올 수 있다.

즉, 예를들어 saga에서 제공되는 `put` 함수의 경우의 경우 반환 값이 js object이다. 이 js object는  middle ware에서 어떻게 처리되어야 하는지에 대한 instruction을 주고 이에 따라 미들웨어에서 처리가 된다.


> Effect
> saga에서 saga middleware에게 특정한 동작을 실행하도록 해주는  instruction 이다. action 객체가 redux에게 이를 알려주는 것과 비슷한 개념으로,  effect에는 비동기 함수 처리, action dispatch와 같은 동작을 줄 수 있다.
> effect를 생성하기 위해서는 `redux-saga/effects` 패키지에서 제공해주는 함수를 사용할 수 있다.


###  AJAX 통신

```javascript
import { takeEvery } from 'redux-saga/effects'
import Api from './path/to/api'

function* watchFetchProducts() {
  yield takeEvery('PRODUCTS_REQUESTED', fetchProducts)
}

function* fetchProducts() {
  const products = yield Api.fetch('/products')
  console.log(products)
}
```

위와 같이 일반적인 경우에는  Api 호출을 직접적으로 하게된다. 이렇게 하면,  Api  호출이 즉각적으로 일어나면서,  Promise를 반환하게 된다.


We're using now the call(fn, ...args) function. The difference from the preceding example is that now we're not executing the fetch call immediately, instead, call creates a description of the effect. Just as in Redux you use action creators to create a plain object describing the action that will get executed by the Store, call creates a plain object describing the function call. The redux-saga middleware takes care of executing the function call and resuming the generator with the resolved response.
This allows us to easily test the Generator outside the Redux environment. Because call is just a function which returns a plain Object.



```javascript
import { call } from 'redux-saga/effects'

function* fetchProducts() {
  const products = yield call(Api.fetch, '/products')
  // ...
}
 
```

#리덕스/Redux-saga

