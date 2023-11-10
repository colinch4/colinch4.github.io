---
layout: post
title: "Apollo Client와 함께 자바스크립트로 GraphQL Subscriptions를 위한 메모리 관리 방법"
description: " "
date: 2023-11-10
tags: [ApolloClient, GraphQLSubscriptions]
comments: true
share: true
---

GraphQL Subscriptions는 실시간 데이터 업데이트를 위해 웹소켓을 사용하는 기능입니다. Apollo Client는 GraphQL Subscriptions를 지원하며, 이를 사용하여 자바스크립트 애플리케이션에서 실시간 데이터를 구독하고 처리할 수 있습니다. 그러나 GraphQL Subscriptions을 사용하는 경우 메모리 관리를 적절히 처리해야 합니다.

여기에는 Apollo Client와 자바스크립트를 사용하여 GraphQL Subscriptions를 구현하는 방법과 메모리 관리에 대한 몇 가지 팁이 있습니다.

## Apollo Client와 GraphQL Subscriptions 설정

먼저, Apollo Client를 설정해야 합니다. Apollo Client의 `SubscriptionClient`를 사용하여 웹소켓을 초기화하고, `split` 함수를 사용하여 GraphQL Subscription 요청을 웹소켓으로 라우팅합니다.

```javascript
import { ApolloClient } from 'apollo-client';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { HttpLink } from 'apollo-link-http';
import { WebSocketLink } from 'apollo-link-ws';
import { split } from 'apollo-link';
import { getMainDefinition } from 'apollo-utilities';

// HTTP 연결을 위한 링크
const httpLink = new HttpLink({
  uri: 'http://localhost:4000/graphql',
});

// 웹소켓 연결을 위한 링크
const wsLink = new WebSocketLink({
  uri: 'ws://localhost:4000/graphql',
  options: {
    reconnect: true,
  },
});

// GraphQL Subscription에서 웹소켓으로 요청을 라우팅하기 위한 링크
const link = split(
  // 요청이 Subscription일 경우
  ({ query }) => {
    const { kind, operation } = getMainDefinition(query);
    return kind === 'OperationDefinition' && operation === 'subscription';
  },
  wsLink, // 웹소켓 링크
  httpLink // HTTP 링크
);

// Apollo Client 생성
const client = new ApolloClient({
  link,
  cache: new InMemoryCache(),
});
```

## GraphQL Subscription 구독 관리

GraphQL Subscriptions은 메모리 관리 측면에서 추가적인 주의가 필요합니다. 애플리케이션에서 구독을 생성하고 해제함에 따라 메모리 누수가 발생할 수 있습니다.

올바른 메모리 관리를 위해 구독을 생성한 후에는 해제해야 합니다. 예를 들어, React 컴포넌트의 생명주기 메서드인 `componentWillUnmount`에서 구독을 해제하는 것이 좋습니다.

```javascript
import React, { useEffect } from 'react';
import { useSubscription } from '@apollo/react-hooks';
import { SUBSCRIPTION_QUERY } from './constants';

const MyComponent = () => {
  useEffect(() => {
    // 구독 생성
    const subscribe = subscribeToData();

    return () => {
      // 구독 해제
      subscribe.unsubscribe();
    };
  }, []);

  const { data } = useSubscription(SUBSCRIPTION_QUERY);

  // ...
};
```

## 메모리 누수 방지를 위한 GC 설정

메모리 누수를 최소화하기 위해 브라우저의 가비지 컬렉터(GC)를 적절히 설정하는 것도 좋은 아이디어입니다. GC는 더 이상 사용되지 않는 메모리를 해제하여 누수를 방지하는 역할을 합니다.

대부분의 최신 브라우저는 기본적으로 GC를 자동으로 수행합니다. 그러나 몇 가지 추가적인 설정을 통해 GC의 동작을 조절할 수도 있습니다. 예를 들어, `window.requestAnimationFrame`을 사용하여 애니메이션과 같은 높은 프레임 레이트로 실행되는 작업의 메모리를 해제할 수 있습니다.

```javascript
// GC를 트리거하는 콜백 함수
const triggerGC = () => {
  // GC를 수행할 작업
};

// 프레임 레이트에 맞춰 GC를 호출
const raf = window.requestAnimationFrame ||
  window.webkitRequestAnimationFrame ||
  window.mozRequestAnimationFrame ||
  window.msRequestAnimationFrame;

raf(triggerGC);
```

## 결론

이제 Apollo Client와 함께 자바스크립트로 GraphQL Subscriptions를 구현하는 방법과 메모리 관리에 대한 몇 가지 팁을 알아보았습니다. 이를 통해 애플리케이션에서 GraphQL Subscriptions를 안전하게 사용할 수 있고 메모리 누수를 최소화할 수 있습니다.

#ApolloClient #GraphQLSubscriptions