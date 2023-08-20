---
layout: post
title: "[js] Async / await"
description: " "
date: 2021-05-14
tags: [js]
comments: true
share: true
---


## Async / await
## Async / await

```js
async function name(...args) { }
```

위와 같이 함수의 앞에 async 키워드가 붙으면 해당 함수는 비동기 함수의 일종으로  `AsyncFunction` 객체가 된다. (함수의 반환 타입이 아니라, 객체의 타입이)

해당 함수의 리턴 타입은 Promise가 된다.

아래의 두 함수는 모두 같은 값을 반환하는데, 만약 리턴의 타입이 프로미스의 타입이 아니라면, 내부적으로 프로미스를 만들어서 반환을 해준다.

```js
async function foo() {
	return 'bar'; 
} 

async function foo() {
	return Promise.resolve('bar');
}
```


###  await

await  키워드가 붙은 문장의 경우에는 해당 expression (Promise)가 이행되거나, 실패될때까지 async 함수의 실행을 멈추고, settled 상태가 되면 함수를 다시 실행하게 된다.



## 실수했던 경험

```js

```



#javascript/비동기함수