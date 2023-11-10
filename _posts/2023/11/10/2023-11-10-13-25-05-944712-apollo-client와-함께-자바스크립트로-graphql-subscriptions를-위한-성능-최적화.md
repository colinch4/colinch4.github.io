---
layout: post
title: "Apollo Client와 함께 자바스크립트로 GraphQL Subscriptions를 위한 성능 최적화"
description: " "
date: 2023-11-10
tags: [GraphQL, ApolloClient]
comments: true
share: true
---

GraphQL Subscriptions은 실시간 데이터 업데이트를 위한 강력한 기능이지만, 대규모 애플리케이션에서는 성능 문제가 발생할 수 있습니다. 특히 Apollo Client를 사용하는 경우, GraphQL Subscriptions의 성능을 최적화해야합니다.

여기서는 Apollo Client와 함께 JavaScript를 사용하여 GraphQL Subscriptions를 위한 성능 최적화 방법을 알아보겠습니다.

## 1. 네트워크 부하 최소화

GraphQL Subscriptions를 사용할 때, 불필요한 네트워크 부하를 최소화해야합니다. 이를 위해 다음과 같은 방법을 고려해볼 수 있습니다.

### 데이터 축소화 (Data Compression)
실시간 데이터 업데이트가 자주 발생하는 경우, 데이터를 압축하여 전송하는 것이 성능 향상에 도움이 될 수 있습니다. gzip 등의 압축 알고리즘을 사용하여 데이터를 압축하고, 클라이언트와 서버 모두에서 압축 해제를 처리해야합니다.

### 배치 요청 (Batching Requests)
여러 개의 구독을 동시에 요청하는 대신, 한 번에 여러 개의 구독을 처리하는 "배치 요청"을 사용할 수 있습니다. Apollo Client에서는 `subscribe` 함수에 배열을 전달하여 여러 개의 구독을 한 번에 등록할 수 있습니다.

```javascript
const subscription = gql`
  subscription {
    ...
  }
`;

const subscriptions = [
  subscription,
  subscription,
  subscription,
  ...
];

client.subscribe({ queries: subscriptions }).subscribe({
  next(data) {
    // handle data
  },
});
```

## 2. 웹 소켓 연결 최적화

GraphQL Subscriptions는 웹 소켓(WebSocket)을 사용하여 실시간 데이터 업데이트를 처리합니다. 웹 소켓 연결은 애플리케이션의 성능에 큰 영향을 미치므로, 최적화해야합니다.

### 웹 소켓 풀링 (WebSocket Pooling)
Apollo Client에서는 웹 소켓 연결을 관리하는 WebSocketLink를 사용합니다. 웹 소켓을 풀링하여 재사용하면 연결을 맺고 끊는 데 드는 오버헤드를 줄일 수 있습니다. 이를 위해 Apollo Client에서 제공하는 `WebSocketLink`의 `reconnect` 옵션을 설정할 수 있습니다.

```javascript
import { WebSocketLink } from '@apollo/client/link/ws';

const link = new WebSocketLink({
  uri: 'ws://localhost:4000/graphql',
  options: {
    reconnect: true, // 웹 소켓 풀링을 활성화합니다.
  },
});
```

### 연결 스로틀링 (Connection Throttling)
GraphQL Subscriptions의 업데이트 주기가 너무 빠르면 웹 소켓 연결에 과부하가 걸리게 됩니다. 이를 해결하기 위해 연결 스로틀링을 적용할 수 있습니다. 연결 스로틀링은 일정 시간 동안 동일한 구독으로 연결할 수 있는 횟수를 제한하는 것입니다. Apollo Server에서는 `withFilter` 함수를 사용하여 구독자에 대한 연결 스로틀링을 구현할 수 있습니다.

```javascript
import { withFilter } from 'graphql-subscriptions';

const subscription = {
  ...
  subscribe: withFilter(
    () => pubsub.asyncIterator('SOME_TOPIC'),
    (payload, variables) => {
      // 연결 스로틀링 조건을 설정합니다.
      return true; // 연결 허용
      // or
      return false; // 연결 거부
    }
  ),
};
```

GraphQL Subscriptions를 최적화해서 사용하면 Apollo Client와 함께 실시간 데이터 업데이트를 효율적으로 처리할 수 있습니다.

더 자세한 내용은 [Apollo Client 문서](https://www.apollographql.com/docs/react/data/subscriptions/)를 참고하세요.

#GraphQL #ApolloClient #JavaScript