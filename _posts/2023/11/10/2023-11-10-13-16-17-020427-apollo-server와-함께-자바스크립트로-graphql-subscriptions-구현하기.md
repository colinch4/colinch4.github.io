---
layout: post
title: "Apollo Server와 함께 자바스크립트로 GraphQL Subscriptions 구현하기"
description: " "
date: 2023-11-10
tags: [GraphQL]
comments: true
share: true
---

GraphQL Subscriptions는 클라이언트와 실시간으로 상호작용할 수 있는 기능을 제공하는 GraphQL의 한 부분입니다. 이를 이용하면 실시간 데이터 업데이트, 채팅 애플리케이션, 실시간 스트리밍 등 다양한 기능을 구현할 수 있습니다. 이번 글에서는 Apollo Server와 자바스크립트를 사용하여 GraphQL Subscriptions를 구현하는 방법에 대해 알아보겠습니다.

## Apollo Server와 GraphQL Subscriptions

[Apollo Server](https://www.apollographql.com/docs/apollo-server/)는 GraphQL을 위한 완전한 서버 배포 플랫폼입니다. Apollo Server를 사용하여 GraphQL Subscriptions를 설정하려면 다음과 같이 진행할 수 있습니다.

1. Apollo Server를 설치합니다.

```shell
npm install apollo-server
```

2. 필요한 모듈을 가져옵니다. 이 예시에서는 `graphql`, `subscriptions-transport-ws`, `apollo-server-express` 모듈을 사용합니다.

```javascript
const { ApolloServer } = require('apollo-server');
const { execute, subscribe } = require('graphql');
const { SubscriptionServer } = require('subscriptions-transport-ws');
const express = require('express');
const http = require('http');
```

3. Apollo Server 및 GraphQL Subscriptions를 설정합니다.

```javascript
const typeDefs = `
  type Query {
    hello: String
  }

  type Subscription {
    greetings: String
  }
`;

const resolvers = {
  Query: {
    hello: () => 'Hello world!',
  },
  Subscription: {
    greetings: {
      subscribe: () => pubsub.asyncIterator('GREETINGS'),
    },
  },
};

const pubsub = new PubSub();
```

4. Express 서버를 생성하고 Apollo Server를 마운트합니다.

```javascript
const app = express();
const server = new ApolloServer({
  typeDefs,
  resolvers,
});

server.applyMiddleware({ app });
```

5. HTTP 서버를 생성하고 웹소켓을 통해 GraphQL Subscriptions를 활성화합니다.

```javascript
const httpServer = http.createServer(app);
server.installSubscriptionHandlers(httpServer);

httpServer.listen(4000, () => {
  console.log(`Server ready at http://localhost:4000${server.graphqlPath}`);
  console.log(`Subscriptions ready at ws://localhost:4000${server.subscriptionsPath}`);
});
```

## GraphQL Subscriptions 사용 예시

Subscription을 사용하는 클라이언트는 `subscribe` 함수를 호출하여 실시간 변경 사항을 구독할 수 있습니다.

```javascript
const client = new ApolloClient({
  uri: 'http://localhost:4000/graphql',
  cache: new InMemoryCache(),
});

client.subscribe({
  query: gql`
    subscription {
      greetings
    }
  `,
}).subscribe({
  next(data) {
    console.log('New greeting:', data);
  },
});
```

위의 예시에서는 `greetings` Subscription을 구독하고 있습니다. 서버에서 `pubsub.publish('GREETINGS', { greetings: 'Hello' })`와 같은 코드로 새로운 인사말을 발행하면 클라이언트에서 해당 데이터를 받아올 수 있습니다.

## 마치며

Apollo Server와 자바스크립트를 사용하여 GraphQL Subscriptions를 구현하는 방법을 알아보았습니다. 이를 통해 실시간으로 상호작용할 수 있는 애플리케이션을 개발할 수 있습니다. Apollo Server와 GraphQL의 다양한 기능을 참고하여 원하는 기능을 구현해보세요!

#GraphQL #ApolloServer