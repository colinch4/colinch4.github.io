---
layout: post
title: "Apollo Client와 Prisma를 이용한 GraphQL Subscriptions 개발하기"
description: " "
date: 2023-11-10
tags: [GraphQL, ApolloClient]
comments: true
share: true
---

## 소개
GraphQL은 데이터를 효율적으로 가져오고 업데이트하기 위한 강력한 쿼리 언어입니다. GraphQL Subscriptions은 실시간으로 데이터 변경 사항을 알려주는 기능을 제공합니다. 이번 글에서는 Apollo Client와 Prisma를 이용하여 GraphQL Subscriptions을 개발하는 방법에 대해 알아보겠습니다.

## Apollo Client란?
[Apollo Client](https://www.apollographql.com/docs/react/)는 GraphQL 클라이언트 라이브러리로, 프론트엔드 애플리케이션과 GraphQL 서버 간의 데이터 통신을 쉽게 처리할 수 있도록 도와줍니다. Apollo Client는 React, Vue, Angular와 같은 프론트엔드 프레임워크와 함께 사용될 수 있습니다.

## Prisma란?
[Prisma](https://www.prisma.io/)는 데이터베이스 간략화 도구로, ORM(Object-Relational Mapping)을 제공하여 데이터베이스 스키마와 연결하여 쉽게 데이터를 조작할 수 있도록 도와줍니다. Prisma는 GraphQL 서버에서 데이터 액세스를 처리하는데 매우 유용합니다.

## GraphQL Subscriptions 개발하기
이제 Apollo Client와 Prisma를 이용하여 GraphQL Subscriptions을 개발해 보겠습니다.

### 1. 프로젝트 초기화
먼저 새로운 프로젝트를 초기화합니다. 아래의 명령을 실행하여 필요한 패키지들을 설치합니다.

```shell
$ mkdir my-project
$ cd my-project
$ npm init -y
$ npm install apollo-client graphql graphql-tag apollo-link apollo-link-http apollo-link-ws subscriptions-transport-ws
```

### 2. 서버 설정
GraphQL 서버를 설정합니다. Prisma와 연동할 수 있도록 Prisma Client도 설치합니다.

```shell
$ npm install graphql-yoga prisma prisma-binding
```

### 3. Subscription 제공하기
GraphQL 서버에서 Subscription을 제공하기 위해 다음과 같은 단계를 따릅니다.

- GraphQL 스키마에 Subscription 타입을 정의합니다.
- resolvers에 Subscription을 처리할 함수를 작성합니다.
- 해당 함수에서 변경 사항을 클라이언트에게 전달합니다.

```javascript
// schema.graphql
type Subscription {
  newPost: Post
}

// resolvers.js
const resolvers = {
  Subscription: {
    newPost: {
      subscribe: () => pubsub.asyncIterator('NEW_POST'),
    },
  },
};

// index.js
const { ApolloServer, PubSub } = require('apollo-server');
const pubsub = new PubSub();
const server = new ApolloServer({
  typeDefs: fs.readFileSync('./schema.graphql', 'utf8'),
  resolvers,
  context: ({ req }) => {
    // Prisma client initialization
  },
});
```

### 4. 클라이언트 설정
클라이언트에서는 Apollo Client를 사용하여 Subscription을 구독합니다. 아래는 React를 사용한 예시입니다.

```javascript
import React from 'react';
import { ApolloClient, ApolloProvider, InMemoryCache, gql, useSubscription } from '@apollo/client';
import { WebSocketLink } from '@apollo/link-ws';

const wsLink = new WebSocketLink({
  uri: `ws://localhost:4000/graphql`,
  options: {
    reconnect: true,
  },
});

const client = new ApolloClient({
  link: wsLink,
  cache: new InMemoryCache(),
});

const NEW_POST_SUBSCRIPTION = gql`
  subscription {
    newPost {
      id
      title
      content
    }
  }
`;

const NewPostSubscription = () => {
  const { data } = useSubscription(NEW_POST_SUBSCRIPTION);
  
  return (
    <div>
      <p>New post:</p>
      <p>Title: {data?.newPost?.title}</p>
      <p>Content: {data?.newPost?.content}</p>
    </div>
  );
};

const App = () => (
  <ApolloProvider client={client}>
    <NewPostSubscription />
  </ApolloProvider>
);

export default App;
```

## 결론
이제 Apollo Client와 Prisma를 이용하여 GraphQL Subscriptions을 개발하는 방법을 알아보았습니다. GraphQL Subscriptions을 활용하면 실시간으로 데이터 변경을 감지하고 알림을 받을 수 있어 유저 경험을 더욱 향상시킬 수 있습니다. Apollo Client와 Prisma는 매우 강력한 도구이므로 개발에 적극적으로 활용해 보시기 바랍니다.

[#GraphQL](https://www.hashtags.org/top-hashtags/graphql) [#ApolloClient](https://www.hashtags.org/top-hashtags/apolloclient)