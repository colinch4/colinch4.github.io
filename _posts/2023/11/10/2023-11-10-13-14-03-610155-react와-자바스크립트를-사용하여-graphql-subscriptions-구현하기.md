---
layout: post
title: "React와 자바스크립트를 사용하여 GraphQL Subscriptions 구현하기"
description: " "
date: 2023-11-10
tags: [GraphQL, React]
comments: true
share: true
---

GraphQL은 클라이언트와 서버 간의 효율적인 데이터 통신을 위한 쿼리 언어입니다. GraphQL Subscriptions는 실시간으로 업데이트되는 데이터를 서버에서 클라이언트로 전송하는 기능을 제공합니다. 이 기능은 실시간 채팅앱, 실시간 알림 등 다양한 응용프로그램에 유용하게 사용될 수 있습니다.

이번 글에서는 React와 JavaScript를 사용하여 GraphQL Subscriptions을 구현하는 방법을 알아보겠습니다.

## 1. 필요한 패키지 설치하기

먼저, 프로젝트 폴더에서 다음 명령어를 사용하여 필요한 패키지들을 설치합니다.

```shell
npm install graphql apollo-client apollo-link-ws subscriptions-transport-ws
```

## 2. Apollo Client 설정하기

GraphQL Subscriptions을 사용하기 위해서는 Apollo Client를 설정해야합니다. 프로젝트의 진입점 파일에서 다음과 같이 Apollo Client를 설정합니다.

```javascript
import { ApolloClient, ApolloLink, HttpLink, InMemoryCache, split } from 'apollo-client';
import { WebSocketLink } from 'apollo-link-ws';
import { getMainDefinition } from 'apollo-utilities';
import { SubscriptionClient } from 'subscriptions-transport-ws';

const httpLink = new HttpLink({ uri: 'http://localhost:4000/graphql' });

const wsLink = new WebSocketLink(
  new SubscriptionClient('ws://localhost:4000/graphql', {
    reconnect: true,
  })
);

const link = split(
  ({ query }) => {
    const definition = getMainDefinition(query);
    return definition.kind === 'OperationDefinition' && definition.operation === 'subscription';
  },
  wsLink,
  httpLink
);

const client = new ApolloClient({
  link: ApolloLink.from([link]),
  cache: new InMemoryCache(),
});
```

Apollo Client 설정에는 HTTP 연결(`HttpLink`)과 웹소켓 연결(`WebSocketLink`)이 함께 사용됩니다. HTTP 연결은 일반적인 GraphQL 쿼리와 뮤테이션에 사용되고, 웹소켓 연결은 구독(Subscriptions)에 사용됩니다. 위의 코드에서는 `split` 함수를 사용하여 쿼리 타입에 따라 적절한 연결을 선택하도록 설정하였습니다.

## 3. 구독 선언하기

GraphQL Subscriptions를 사용하기 위해서는 서버에서 해당 구독을 정의해야 합니다. 서버의 GraphQL 스키마에서 구독을 선언하고, 적절한 리졸버를 작성합니다. 예를 들어, 실시간으로 업데이트되는 채팅 메시지를 구독하는 경우 다음과 같이 스키마와 리졸버를 작성할 수 있습니다.

```graphql
type Subscription {
  newMessage: Message
}

type Message {
  id: ID!
  text: String!
  sender: String!
}
```

```javascript
const resolvers = {
  Subscription: {
    newMessage: {
      subscribe: (_, __, { pubsub }) => pubsub.asyncIterator("NEW_MESSAGE"),
    },
  },
};
```

위의 예시에서는 `newMessage`라는 구독을 선언하고, 해당 구독을 통해 새로운 메시지가 전달됩니다. `pubsub` 객체는 해당 메시지를 발행하고, 구독자에게 전송하는 역할을 담당합니다.

## 4. 구독 사용하기

이제 구독을 사용하여 실시간으로 업데이트되는 데이터를 받아올 수 있습니다. React 컴포넌트에서 `useSubscription` 훅을 사용하여 구독을 수행하고, 데이터를 처리할 수 있습니다. 예를 들어, 실시간으로 업데이트되는 메시지를 화면에 표시하는 컴포넌트는 다음과 같이 작성할 수 있습니다.

```javascript
import React from 'react';
import { useSubscription } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';

const NEW_MESSAGE_SUBSCRIPTION = gql`
  subscription {
    newMessage {
      id
      text
      sender
    }
  }
`;

const ChatComponent = () => {
  const { data, loading } = useSubscription(NEW_MESSAGE_SUBSCRIPTION);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      {data.newMessage.sender}: {data.newMessage.text}
    </div>
  );
}

export default ChatComponent;
```

위의 예시에서는 `NEW_MESSAGE_SUBSCRIPTION` 쿼리를 사용하여 `useSubscription` 훅을 호출하고, 반환된 `data` 객체를 통해 실시간으로 업데이트되는 메시지를 화면에 표시합니다. 데이터가 로딩 중인 동안 "Loading..." 텍스트가 표시되며, 데이터 로딩이 완료된 후에는 메시지 내용이 화면에 표시됩니다.

## 마치며

React와 JavaScript를 사용하여 GraphQL Subscriptions을 구현하는 방법을 알아보았습니다. GraphQL Subscriptions은 실시간으로 업데이트되는 데이터를 클라이언트로 전송하기 위한 강력한 기능이며, 실시간 채팅앱 또는 실시간 알림 기능 등을 구현하는 데 유용하게 사용될 수 있습니다.

더 자세한 내용은 [Apollo 공식 문서](https://www.apollographql.com/docs/react/data/subscriptions/)를 참조하시기 바랍니다.

#GraphQL #React