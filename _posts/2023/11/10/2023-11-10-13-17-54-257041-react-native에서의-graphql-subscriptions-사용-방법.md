---
layout: post
title: "React Native에서의 GraphQL Subscriptions 사용 방법"
description: " "
date: 2023-11-10
tags: [GraphQL]
comments: true
share: true
---

React Native는 웹과 모바일 앱을 개발하기 위한 인기있는 프레임워크입니다. GraphQL은 클라이언트-서버 간 데이터 통신을 위한 쿼리 언어와 Runtime입니다. 이 두 가지 기술을 함께 사용하면 React Native 앱에서 실시간 데이터 업데이트를 쉽게 처리할 수 있습니다. 

## GraphQL Subscriptions란?

GraphQL Subscriptions는 GraphQL에서 제공하는 기능 중 하나로, 실시간으로 데이터를 구독할 수 있는 기능입니다. 이를 통해 서버에서 데이터 변경 시 클라이언트에 자동으로 업데이트를 전송할 수 있습니다. 실시간 채팅, 실시간 주문 추적, 실시간 알림 등과 같은 기능을 구현할 때 유용하게 사용됩니다.

## React Native에서의 GraphQL Subscriptions 사용하기

React Native에서 GraphQL Subscriptions를 사용하려면 몇 가지 단계를 거쳐야 합니다.

### 1. Apollo Client 설치하기

React Native에서는 Apollo Client를 사용하여 GraphQL Subscriptions를 처리할 수 있습니다. 먼저 프로젝트에 Apollo Client를 설치해야 합니다. 

```shell
npm install apollo-client apollo-cache-inmemory apollo-link apollo-link-http apollo-link-ws subscriptions-transport-ws graphql-tag graphql
```

### 2. WebSocket 연결 설정하기

GraphQL Subscriptions는 WebSocket 프로토콜을 사용하여 실시간 데이터를 전송합니다. 이를 위해 Apollo Link를 사용하여 WebSocket 연결을 설정해야 합니다. 

```javascript
import { WebSocketLink } from 'apollo-link-ws';

const wsLink = new WebSocketLink({
  uri: 'ws://example.com/graphql', // GraphQL 서버의 WebSocket 엔드포인트
  options: {
    reconnect: true
  }
});
```

### 3. Apollo Client에 WebSocketLink 적용하기

Apollo Client에 WebSocketLink를 적용하여 WebSocket 연결을 사용할 수 있도록 설정해야 합니다. Apollo Client를 생성할 때 link 속성에 WebSocketLink를 추가합니다.

```javascript
import ApolloClient from 'apollo-client';
import { InMemoryCache } from 'apollo-cache-inmemory';

const client = new ApolloClient({
  link: wsLink, // WebSocketLink를 link에 적용
  cache: new InMemoryCache()
});
```

### 4. Subscription 구독하기

GraphQL Subscriptions를 사용하여 실시간 데이터를 구독하려면 Apollo Client의 subscribe 함수를 사용해야 합니다. 이를 통해 서버에 구독 쿼리를 전송하고 실시간 업데이트를 수신할 수 있습니다.

```javascript
import { gql } from 'apollo-boost';

const SUBSCRIPTION_QUERY = gql`
  subscription MySubscription {
    // 구독할 쿼리 내용
  }
`;

const subscription = client.subscribe({ query: SUBSCRIPTION_QUERY });

subscription.subscribe(({ data }) => {
  // 데이터 업데이트 처리
});
```

## 마무리

이제 React Native에서 GraphQL Subscriptions를 사용하여 실시간 데이터 업데이트를 구현할 수 있습니다. Apollo Client를 사용하여 WebSocket 연결을 설정하고, subscribe 함수를 사용하여 데이터를 구독하면 됩니다. GraphQL Subscriptions는 효율적이고 강력한 실시간 기능을 제공하여 앱의 사용자 경험을 더욱 향상시킬 수 있습니다.

[#ReactNative](link1) [#GraphQL](link2)

[link1]: https://reactnative.dev/
[link2]: https://graphql.org/