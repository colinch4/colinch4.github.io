---
layout: post
title: "[react] React Query"
description: " "
date: 2021-05-14
tags: [react]
comments: true
share: true
---

# React Query - intro

## Reudx?
일반적으로 Redux를 사용하는 것은 클라이언트의 상태를 관리하는데에 적합하다.

왜냐하면, 실질적으로 Redux를 통해서 서버의 데이터를 주고 받는 경우에는 Single Source of Truth가 지켜지지 않기 때문이다. 서버 내부의 데이터는 계속해서 변하지만, 리덕스 내부의 스토어는 이와 다를 수 있기 때문이다.

그렇다고 해서 페이지를 넘나들때마다, 데이터 fetching을 해준다면, 리덕스를 사용하는 이유가 없지 않을까..?

그렇기 때문에 간단한 API 요청과 같은 데이터들은 Redux가 아닌 다른 기술로 받을 수 있다면 좋지 않을까?

* 캐싱
  기본적인 설정으로 hook을 등록해놨을때, 캐싱이된다. 그리고 일정 시간이 흐른 후에는 백그라운드에서 데이터를 받아오는 작업을 해준다. 그렇다고 무조건 오래된 영역의 데이터를 가져오는 것은 아니다.
  이 작업의 경우 여러가지 조건에 따라서 발동(?) 된다. 캐시 데이터가 오래되었다고 판단고 + 아래의 조건 중 하나가 성립할때.
1. 새로운 쿼리 인스턴스가 마운트 되었을때
2. 네트워크가 다시 연결되었을때
3. 쿼리가 refetch interval이 별도로 설정되어 있을때.


## React Query


### 간단한 예시

설정하는 방법

```js
import { QueryClient } from 'react-query';

const queryClient = new QueryClient()
 
function App() {
  return (
    // Provide the client to your App
    <QueryClientProvider client={queryClient}>
      <Todos />
    </QueryClientProvider>
  )
}

render(<App />, document.getElementById('root'))
```

사용방법
```js
function Todos() {
  // Access the client
  const queryClient = useQueryClient()

  // Queries
  const query = useQuery('todos', getTodos)

  // Mutations
  const mutation = useMutation(postTodo, {
    onSuccess: () => {
      // Invalidate and refetch
      queryClient.invalidateQueries('todos')
    },
  })

  return (
    <div>
      <ul>
        {query.data.map(todo => (
          <li key={todo.id}>{todo.title}</li>
        ))}
      </ul>

      <button
        onClick={() => {
          mutation.mutate({
            id: Date.now(),
            title: 'Do Laundry',
          })
        }}
      >
        Add Todo
      </button>
    </div>
  )
}

```

### Query

일반적인 경우에는
`const {isLoading, isError, data, error} = useQuery()` 만 사용해도 충분하다. 그 외에도 여러 옵션이 있음.

- 첫번째 인자

key의 경우에는 serialize가 가능한 데이터이면 된다.
`useQuery('key', function);`

그렇기 때문에 key는 꼭 string일 필요는 없고, 배열과 객체도 들어갈 수 있는데, 이 경우 여러가지 데이터들을 담을 수 있다.


key의 경우 해시처리가 되어서, 키들의 순서는 중요하지 않다.
```js
useQuery(['todos', {status, page}]) === useQuery(['todos', {page, status}])
```

- 2번째 인자

2번째 인자로는 function이 들어가게 되는데, 이 함수는 promise를 반환하는 함수이면 된다.

```js
useQuery(['todos', todoId], async () => {
  const data = await fetchTodoById(todoId)
  return data
})
```

React Query가 에러를 감지 하기 위해서는 async await 함수가 에러 처리 루틴을 가지고 있어야한다.

```js
// 내부에 들어가는 함수는 아래와 같아야한다. 
async () => {
	try{ 
		const { data } = await fetchData();
	}catch(err){
		console.error(err);
	}
}
```

만약 인자를 전달해야하는 함수라면? 예를 들어서, 특정 아이디값을 가지는 사람의 데이터를 가져오는 경우에는 어떻게 해야하는가.

아래와 같이 Query의 key 값을 받을 수 있다.
```js
function Todos({ status, page }) {
  const result = useQuery(['user', { id }], fetchTodoList)
}

// Access the key, status and page variables in your query function!
function fetchTodoList({ queryKey }) {
  const [_key, { id }] = queryKey
  return axios.get(`user/${id}`);
}
```

그 외에도 Query Object를 통해서 넘겨 받을 수도 있다. [링크](https://react-query.tanstack.com/guides/query-functions)


```js
function Todos() {
  const { isLoading, isError, data, error } = useQuery('todos', fetchTodoList)

  if (isLoading) {
    return <span>Loading...</span>
  }

  if (isError) {
    return <span>Error: {error.message}</span>
   }
// We can assume by this point that `isSuccess === true`
  return (
     <ul>
       {data.map(todo => (
        <li key={todo.id}>{todo.title}</li>
      ))}
    </ul>
  )
}

```


### Mutation

###  




#React/React-Query/intro




# React Query - query
- key : 특정 쿼리에 대한 unique key
- function : Promise를 반환하는 함수
- result : 쿼리의 반환 값
```javascript
useQuery('unique key', function);
```

```javascript
import { useQuery } from 'react-query'
 
function App() {
  const result = useQuery('todos', fetchTodoList)
}
```


## unique key

unique key는 app 전반에서 해당 쿼리에 대한 식별자가 된다. 따라서, app 전반에서  refetching, caching, sharing 된다.

key의 경우에는 serializable 하다면, 사용 가능. eg. string, array etc..

```javascript
useQuery('todos', ...); // todos 
useQuery(['todo', 5], ...); // 특정 todo에 대한..
```

아래의 경우에는, query function에 인자를 넘겨주는 방법이다.

인자를 넘겨줄 때는, 특정 item에 대한 부가적인 정보(idx, id), 포맷(type) 등이 필요로할 때, 사용하면 좋다.

아이템과 관련없는 옵션을 key를 통해 전달해준다면, 각각이 unique key가 되어 caching과 같은 기능을 활용하지 못할 수 도 있으니..

```javascript
function Todos({ status, page }) {
    const result = useQuery(['todos', { status, page }], fetchTodoList)
}

// Access the key, status and page variables in your query function!
function fetchTodoList({ queryKey }) {
    const [_key, { status, page }] = queryKey
    return new Promise()
}

```

위와 같이, 특정 data에 대한 부가적인 옵션이 아니라면,  `() => fn(arg1, arg2)`  방식으로 넘기는게 좋아보임.



## result

반환 값에서는 아래와 같은 다양한 상태에 대한 값을 가진다.

```javascript
"result" : {
	isLoading,
	isError,
	isSuccess,
	isIdle,
	error,
	data,
	isFetching,
}
```


자주쓰는 상태 값
`isLoading`, `isError`, `data`, `error`

```javascript
function Todos() {
    const { isLoading, isError, data, error } = useQuery('todos', fetchTodoList)
    if (isLoading) {
        return <span>Loading...</span>
    }
    if (isError) {
        return <span>Error: {error.message}</span>
    }
    // We can assume by this point that `isSuccess === true`
    return (
        <ul>
            {data.map(todo => (
                <li key={todo.id}>{todo.title}</li>
            ))}
        </ul>
    )
}
```

## function

data를 resolve하거나, error를 던지는 promise를 반환하는 함수.

```javascript
const result = useQuery(['todos', todoId], async () => {
	try {
		const data = await fetchTodoById(todoId)
   	return data
	}catch(error) {
		
	}
 })


```


#React/React-Query/query




















