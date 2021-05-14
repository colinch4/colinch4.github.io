---
layout: post
title: "[redux] 리덕스 미들웨어와 Thunk"
description: " "
date: 2021-05-14
tags: [redux]
comments: true
share: true
---

#  리덕스 미들웨어와 Thunk
- 미들웨어란 무엇인가?
- 미들웨어의 구조
- 미들웨어의 활용 (별도 chpater에서 다룸)
- Redux - thunk
- 결론 및 cheat-sheet


## 미들웨어란 무엇인가?

서버사이드 프레임워크 Express 에서도 미들웨어라는 개념이 있다.  이 프레임워크에서의 미들웨어는 `request` `response` 를 받아서 이를 가지고 어떠한 처리를 만들때 사용하게 된다.

리덕스의 미들웨어는 비슷한 컨셉을 가지고 있지만, 서버사이드 프레임워크의 미들웨어랑은 동작이 조금 다르다.

일반적으로 리덕스의 스토어에는 `dispatch` , `getState`, `subscribe` 라는 메서드가 제공된다.


```js
// dispatch(action) 

// 액션을 직접 넣어주는 방법
dispatch({
	type : 'INCREMENT'
})

// action creator 를 만들주는 방법
const INCREMENT = 'counter/INCREMENT';
const increment = () =>{ type : INCREMENT  };
dispatch(increment());  
```

위와 같이 dispatch는  Action을 인자로 받게 되어, dispatch 동작에 대한 커스터마이징이 어렵다.

리덕스의 미들웨어는 액션 디스패치와 리듀서 사이에서 어떤 동작을 할 수 있게 도와준다.

특정 액션이 디스패치 되었을 때, 추가적인 로직을 실행할 수 있다. 예를 들어서, 액션이나 상태에 대한 로깅을 할 수도 있다. 또는 리덕스 실행 도중에 발생하는 에러를 서버로 보내주는 것도 가능하다.
정리하자면, 아래와 같은 동작들을 미들웨어를 통해서 수행할 수 있다.

* 디스패치된 액션을 멈추거나, 수정하거나, 지연 시키거나 하는 등의 조작을 할 수 있다.
* Write extra code that has access to dispatch and getState
* Teach dispatch how to accept other values besides plain action objects, such as functions and promises, by intercepting them and dispatching real action objects instead

리덕스는 기본적으로 비동기 로직에 대해서는 아무것도 모른다.  리덕스는 기본적으로 동기적으로 액션을 디스패치하고, 이에 따라서 리듀서가 동작하여 스토어를 바꾸게 된다 .

리덕스의 미들웨어를 통해서 비동기 함수 로직을 수행하도록 할 수 있다.  리덕스의 미들웨어는 단순하게 비동기 함수 로직을 추가하기 위한 장치는 아니다.

##  미들웨어의 구조

미들웨어는 일종의 파이프라인을 만들어서 dispatch 메서드가 발생하면 이들을 연속적으로 동작시키게 된다. 일종의 `체이닝` 을 통해서 미들웨어들이 처리된다.

- 왜 미들웨어에서 비동기 처리 로직이 가능할까?  
  미들웨어는 리듀서 함수와는 다르게   side effect를 미들웨어 내부에 가질 수 있다. 즉, async logic을 품을 수 있게 되는 것이다.



```js
// es5
function middleware(storeAPI) {
	return function wrapDispatch(next) {
		return function handleAction(action) {
			// Do something			
			return next(action);
		}
	}
}

// es6 

const middleware = (store) => (next) => (action) =>{ 
	// Do something
	return next(action) 
}
```

- 미들웨어 함수의 구조

middleware / wrapDispatch 는 store 가 등록될 때, 한번 호출된다.

반면,  handleAction의 경우에는 store의 dispatch 함수에 등록되어 매 번의 dispatch마다 함수를 호출하게 된다.

`middleware` : 미들웨어 함수는 apply middleware에 의해서 호출이 된다.  해당 함수는 `createStore`로 리덕스의 스토어 객체가 만들어 지는 순간에 호출된다.

`wrapDispatch` :  해당 함수도, `createStore` 함수가 호출되는 시점에 호출이 된다. 해당 함수가 받는 인자 `next`는 함수인데, 이를 호출하는 행위는 파이프라인에 연결되어 있는 그 다음 미들웨어를 호출하라는 의미가 된다.

`handleAction` :  이 함수는 현재 발생하는 action을 받아서 Action에 따른 어떠한 행위를 취하는 함수이다.


## Redux - thunk

위에서 언급했듯, redux -thunk는 미들웨어로 이 미들웨어를 등록하면, 비동기 함수를 처리할 수 있게 된다.

redux-thunk 의 구조
간단하다. action이 일반적은 `dispatch(actioncreator());` 을 수행하게 되면 인자에 action이 객체가 되는데,  action 객체 자리에 함수가 들어갈 수 있도록 만들어 준 것이다.

```javascript
const thunk = store => next => action => {
	if(typeof action === 'function') {
		return action(store.dispatch, store.getState), 
	}
	return next(action);

export default thunk;
```


## 결론...
결과적으로는 아래의 코드를 사용할 수 있게 되는 것이다.

```javascript
const INCREMENT = 'counter/INCREMENT';
// 일반 액션 생성자
function increment() {
	return {
		type: INCREMENT
	};
}
// 비동기 액션 생성자
function incrementAsync() {
	return (dispatch, getState) =>{ 
		setTimeout(()=> {
			dispatch(increment());
		}, 2000};
	}	
}
```



#리덕스/미들웨어와Thunk 


# 미들웨어의 활용
## Logger Middleware

```js
const logger = (store) => (next) => action =>{ 
  console.log(`prev state : ${JSON.stringify(store.getState())}`);
  const result = next(action);
  console.log(`next state : ${JSON.stringify(store.getState())}`);
  return result;
}
```

액션 디스패치 직후에 state를 로그로 찍어준다.

그리고 미들웨어와 리듀서 작업이 끝나고 난 이후에, 돌아오는 과정에서 변경 이후의 state를 찍어준다.


## 리포트 기능
```js
const reportCrash = store => next => action =>{ 
	try{
		return next(action);;
	} catch(err) {
	// 서버로 예외에 대한 로그를 전송
	}
};
```


## Delay Action
```js
const delayAction = store => next=> action =>{ 
	const delay = action.meta?.delay;
	if(!delay) {
		return next(action);
	}
	const timeoutId = setTimeout(()=> next(action), delay);
		return function cancel() {
			clearTimeout(timeoutId);
	}
};
// 여기서 반환되는 cancel 함수는 dispatch 함수의 반환값이 된다.
const cancel = store.dispatch({type: 'action', meta : { delay: 	3000 }});
cancel();

// 이렇게 받은 함수를 바로 실행하면, clearTimeout이 되어서 액션 디스패치가 취소된다. 
```

## 

```js
const saveToLocalStorage = (store) => (next) => (action) => {
  if (action.meta?.localStorageKey) {
    localStorage.setItem(action.meta?.localStorageKey, JSON.stringify(action));
  }
  return next(action);
};


```
#리덕스/미들웨어-활용 


