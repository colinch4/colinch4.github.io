---
layout: post
title: "자바스크립트를 사용하여 GraphQL Subscriptions를 위한 Pub-Sub 시스템 개발하기"
description: " "
date: 2023-11-10
tags: [GraphQL]
comments: true
share: true
---

GraphQL Subscriptions은 클라이언트와 서버 간 양방향 실시간 통신을 제공하는 기능입니다. 이를 구현하기 위해서는 Pub-Sub 시스템을 사용해야 합니다. Pub-Sub 시스템은 Publisher가 메시지를 발행하고 Subscriber가 해당 메시지를 구독하는 형태로 동작합니다. 이번 블로그 포스트에서는 자바스크립트를 사용하여 GraphQL Subscriptions를 위한 Pub-Sub 시스템을 개발하는 방법을 알아보겠습니다.

## Pub-Sub 패턴 라이브러리 선택

Pub-Sub 패턴을 쉽게 구현할 수 있는 많은 라이브러리들이 있습니다. 이 중에서 우리는 `graphql-subscriptions` 라이브러리를 사용하여 Pub-Sub 시스템을 개발할 것입니다. 이 라이브러리는 GraphQL Subscriptions에 특화되어 있으며, 간단한 API를 제공하여 사용하기 쉽습니다.

## Pub-Sub 시스템 개발하기

먼저, `graphql-subscriptions` 라이브러리를 프로젝트에 설치합니다.

```shell
npm install graphql-subscriptions
```

그런 다음, PubSub 객체를 생성하고 메시지를 발행하고 구독하는 기능을 구현합니다. 아래는 예시 코드입니다.

```javascript
const { PubSub } = require('graphql-subscriptions');

// Pub-Sub 객체 생성
const pubsub = new PubSub();

// 메시지 발행
pubsub.publish('TOPIC_NAME', { message: 'Hello, World!' });

// 메시지 구독
pubsub.subscribe('TOPIC_NAME', (payload) => {
  console.log(payload.message);
});
```

위의 코드에서 `TOPIC_NAME`은 원하는 이름으로 대체할 수 있습니다. 메시지를 발행하기 위해서는 `publish` 함수를 호출하고, 메시지를 구독하기 위해서는 `subscribe` 함수를 호출합니다. 메시지를 발행하면 해당 토픽에 대해 구독 중인 모든 Subscriber들에게 메시지가 전달됩니다.

## GraphQL Subscriptions에 Pub-Sub 시스템 적용하기

GraphQL Subscriptions를 위해 Pub-Sub 시스템을 적용하려면 먼저 `graphql-subscriptions` 라이브러리를 사용하는 것과 함께 `subscriptions-transport-ws` 라이브러리를 설치해야 합니다. 이 라이브러리는 WebSocket 연결을 통해 클라이언트와 서버 간의 실시간 통신을 가능하게 합니다.

먼저, 서버측에서 PubSub 객체를 생성하고 GraphQL 서버에 적용합니다. 아래는 예시 코드입니다.

```javascript
const { PubSub } = require('graphql-subscriptions');
const { SubscriptionServer } = require('subscriptions-transport-ws');
const { execute, subscribe } = require('graphql');

const pubsub = new PubSub();

SubscriptionServer.create({
  schema,
  execute,
  subscribe,
  // context 등을 설정할 수 있음
  // ...
}, {
  server,
  path: '/graphql',
});
```

클라이언트측에서는 `subscriptions-transport-ws` 라이브러리를 사용하여 WebSocket 연결을 설정하고, GraphQL Subscriptions를 사용할 수 있습니다.

```javascript
import { ApolloClient } from 'apollo-client';
import { createHttpLink } from 'apollo-link-http';
import { WebSocketLink } from 'apollo-link-ws';
import { getMainDefinition } from 'apollo-utilities';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { split } from 'apollo-link';

const httpLink = createHttpLink({
  uri: '/graphql',
});

const wsLink = new WebSocketLink({
  uri: `ws://${window.location.host}/graphql`,
  options: {
    reconnect: true,
  },
});

const link = split(
  ({ query }) => {
    const { kind, operation } = getMainDefinition(query);
    return kind === 'OperationDefinition' && operation === 'subscription';
  },
  wsLink,
  httpLink,
);

const client = new ApolloClient({
  link,
  cache: new InMemoryCache(),
});
```

위의 코드에서 서버의 GraphQL 엔드포인트를 설정하기 위해 `httpLink`를 생성하고, WebSocket 연결을 설정하기 위해 `wsLink`를 생성합니다. `split` 함수를 사용하여 GraphQL Subscriptions를 위한 WebSocket 연결과 나머지 GraphQL 요청을 위한 HTTP 연결을 분리합니다. 마지막으로 Apollo Client를 생성할 때 위에서 생성한 `link`와 `cache`를 설정합니다.

## 결론

이번 블로그 포스트에서는 자바스크립트를 사용하여 GraphQL Subscriptions를 위한 Pub-Sub 시스템을 개발하는 방법에 대해 알아보았습니다. `graphql-subscriptions` 라이브러리를 사용하여 Pub-Sub 시스템을 구현하고, `subscriptions-transport-ws` 라이브러리를 사용하여 GraphQL Subscriptions에 WebSocket 연결을 적용하는 방법을 살펴보았습니다. 이를 통해 클라이언트와 서버 간 실시간 통신을 구현할 수 있으며, 효율적인 웹 어플리케이션을 개발할 수 있습니다.

#GraphQL #Javascript