---
layout: post
title: "[redux] 리듀서, 스토어"
description: " "
date: 2021-05-14
tags: [jreduxs]
comments: true
share: true
---


##  리듀서, 스토어
리듀서는 특정 액션에 따라 상태를 변경해주는 함수이다.

스토어에 저장되어 있는 state는 액션 디스패치를 통해서 리듀서를 거쳐서 변경이 이루어 져야한다.

리덕스의 스토어에 있는 state들도 immutable로 값을 변경시켜주어야 한다.


## 리듀서

일반적인 리듀서의 코드.

```js
// immer 라이브러리 적용
function reducer(state = INIT_STATE, action) {
	return produce(state, draft => {
		switch (action.type) {
			case ADD:
				draft.todos.push(action.todo);
				break;
			case REMOVE_ALL:
				draft.todos = [];
				break;
			case REMOVE:
				draft.todos = 
					 draft.todos
						.filter(todo => todo.id !== action.id);
				break;
			default: 
				break;
		}
	});
}	
```


이를 `createReducer` 함수를 만들어서 가독성이 좋은 코드로 만들 수 있다.

위의 코드를 통해서 createReducer 함수를 만든다고 생각해보자.

우선 리듀서 함수를 반환하는 함수를 만들어 준다.

```js
function createReducer(INIT_STATE) {
	return function reducer(state = INIT_STATE, action) {
		return produce(state, draft => {
			// ...
		});	
	}	
}
```

그리고 특정 `case` 마다 그것을 처리하는 함수, 즉 `handler`가 변하고 있다. 이를 `map` 과 같은 자료구조를 통해서 처리해줄 수 있다.


```javascript
function createReducer(INIT_STATE, handlerMap) {
	return function reducer(state = INIT_STATE, action) {
		return produce(state, draft => {
			const handler = handlerMap[action.type]
			if(handler) {
				handler(draft, action);
			}
		});	
	}
```


- 사용법

```javascript
const reducer = createReducer(INIT_STATE, {
	[ADD]: (state, action) => state.todos.push(action.todo),
	[REMOVE_ALL]: state => (state.todos = [] ),
	[REMOVE]: (state, action) =>
		(state.todos = state.todos
				.filter(todo => todo.id !== action.id)),
	});
});
```



#리덕스/리듀서-스토어
