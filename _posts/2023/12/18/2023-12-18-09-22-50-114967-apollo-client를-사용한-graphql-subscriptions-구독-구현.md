---
layout: post
title: "[nodejs] Apollo Client를 사용한 GraphQL Subscriptions 구독 구현"
description: " "
date: 2023-12-18
tags: [nodejs]
comments: true
share: true
---

GraphQL은 실시간으로 업데이트를 수신할 수 있는 **Subscriptions** 메커니즘을 제공합니다. **Apollo Client**는 GraphQL Subscriptions을 구독하여 실시간으로 데이터를 수신할 수 있는 기능을 제공합니다. 이 포스트에서는 Apollo Client를 사용하여 GraphQL Subscriptions을 구독하고 데이터를 처리하는 방법에 대해 알아보겠습니다.

## 1. Apollo Client 설정

먼저, Apollo Client를 프로젝트에 설정해야 합니다. 아래와 같이 Apollo Client를 설치하고 설정 파일에 Apollo Client를 초기화합니다.

```javascript
// package 설치
npm install @apollo/client graphql

// client 초기화
import { ApolloClient, InMemoryCache } from '@apollo/client';

const client = new ApolloClient({
  uri: 'http://localhost:4000/graphql',
  cache: new InMemoryCache()
});
```

## 2. GraphQL Subscriptions 구독

Apollo Client를 사용하여 GraphQL Subscriptions을 구독할 때에는 `subscribeToMore` 함수를 사용합니다. 아래 예제는 `NEW_POST`라는 Subscription을 구독하고, 새로운 데이터가 도착할 때마다 처리하는 방법을 보여줍니다.

```javascript
import { gql } from '@apollo/client';

const GET_POSTS = gql`
  query GetPosts {
    posts {
      id
      title
    }
  }
`;

const NEW_POST = gql`
  subscription {
    newPost {
      id
      title
    }
  }
`;

client.query({ query: GET_POSTS }).then(result => {
  // 기존 데이터 처리

  client.subscribeToMore({
    document: NEW_POST,
    updateQuery: (prev, { subscriptionData }) => {
      if (!subscriptionData.data) return prev;
      const newPost = subscriptionData.data.newPost;

      return {
        posts: [...prev.posts, newPost]
      };
    }
  });
});
```

## 3. 데이터 처리

데이터를 수신하고 나면, 해당 데이터를 UI나 다른 로직에서 활용할 수 있습니다. 데이터를 수신할 때마다 UI를 업데이트하거나 특정 동작을 수행하는 등의 작업을 수행할 수 있습니다.

이렇게 Apollo Client를 사용하여 GraphQL Subscriptions을 구독하고 데이터를 처리할 수 있습니다. GraphQL Subscriptions를 통해 실시간으로 데이터를 수신하고 업데이트하는 기능을 구현할 수 있으므로, 실시간 데이터 업데이트가 필요한 프로젝트에 유용하게 활용할 수 있을 것입니다.

## 참고 자료

- [Apollo Client 공식 문서](https://www.apollographql.com/docs/react/)
- [GraphQL Subscriptions 공식 문서](https://www.apollographql.com/docs/graphql-subscriptions/)