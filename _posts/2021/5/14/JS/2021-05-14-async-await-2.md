---
layout: post
title: "[js] Async / await2"
description: " "
date: 2021-05-14
tags: [javascript]
comments: true
share: true
---


## Async / await2
비동기 프로그래밍을 동기 프로그래밍처럼 사용할 수 있게 해준다.

Promise가 더 큰 개념이기 때문에, async/ await가 이를 완전 대체하는 것은 아니다.


```javascript
async function getData() {
	return 123;
}
getData().then(data => console.log(data));
```

async await 함수가 반환하는 값은 Promise이다.

```javascript
async function getData() {
	return 123;
}
async function getData() {
	return Promise.resolve(123);
}
async function getData() {
	return Promise.reject(123);
}
getData()
	.then(data => console.log(data));
	.catch(error => console.error(error));
```


await 키워드 옆에 프로미스가 오게되면, 해당 프로미스가 settled 상태가 될때까지 기다린다.

```javascript 
function requestData(value) {
	return new Promise(res => 
		setTimeout(()=>{ 
			console.log('requestData:', value);
			resolve(value);
		}, 1000),
	); 
}
async function printData() {
	const data1 = await requestData(10);
	const data2 = await requestData(20);
	console.log(data1, data2);
}
printData();
```



```javascript
async function getData() {
	console.log('getData1');
	await Promise.reject();
	console.log('getData2');
	await Promise.resolve();
	console.log('getData3');
}

getData()
	.then(() => console.log('fulfilled'))
	.catch(error => console.log('rejected'));

// getData1
// rejected
```


```javascript
function getData() {
	const data = await requestData(10); // error
	console.log(data); 
```


## Async vs Promise 비교
### 의존성 없을때
```javascript
// promise
function getDataPromise() {
	asyncFunc1()
		.then(data => {
			console.log(data);
				return asyncFunc2();
		})
		.then(data => {
			console.log(data);
		});
}
// async await
async function getDataAsync() {
	const data1 = await asyncFunc1();
	console.log(data1);
	const data2 = await asyncFunc2();
	console.log(data2);
}
```

### 의존성 있을때

```javascript

// promise
function getDataPromise() {
	asyncFunc1()
		.then(data1 => Promise.all([data1, asyncFunc2(data1)]))
		.then(([data1, data2]) => {
			return asyncFunc(data1, data2);
		});
}
// async await
async function getDataAsync() {
	const data1 = await asyncFunc1();
	const data2 = await asyncFunc2(data1);
	return asyncFunc3(data1, data2);
}
```

## 병렬처리
```javascript
function asyncFunc1() {
	return new Promise(resolve => {
		console.log('처리중1');
		setTimeout(()=> {
			resolve(10);
		}, 1000);
	});
}
function asyncFunc2() {
	return new Promise(resolve => {
		console.log('처리중2');
		setTimeout(()=> {
			resolve(10);
		}, 1000);
	});
}

// 병렬처리 X
async function getData() {
	const data1 = await asyncFunc1();
	const data2 = await asyncFunc2();
	console.log({ data1, data2 });
}
getData() 
// 처리중1
// (1초 흐르고)
// 처리중2
// (1초 흐르고)
// { data1: 10, data2: 10}

// 병렬처리 O 
async function getData() {
	const p1 = asyncFunc1();
	const p2 = asyncFunc2();
	const data1 = await p1;
	const data2 = await p2;
	console.log({ data1, data2 });
}
getData();
// 처리중1
// 처리중2
// (1초후)
// { data1: 10, data2: 10} 
```

```javascript
async function getData() {
	const [data1, data2] 
		= await Promise.all([asyncFunc1(), asyncFunc2()]);
```

```javascript
async function getData() {
	try{
		await doAsync();
		return doSync();
	}catch (error ) {
		console.log(error);
		return Promise.reject(error);
```

```javascript

```

```javascript

```

```javascript

```

```javascript

```
#javascript/비동기함수