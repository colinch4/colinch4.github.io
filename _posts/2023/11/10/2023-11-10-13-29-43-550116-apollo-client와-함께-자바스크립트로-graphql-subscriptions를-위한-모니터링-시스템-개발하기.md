---
layout: post
title: "Apollo Client와 함께 자바스크립트로 GraphQL Subscriptions를 위한 모니터링 시스템 개발하기"
description: " "
date: 2023-11-10
tags: [GraphQL, ApolloClient]
comments: true
share: true
---

GraphQL은 API를 위한 쿼리 언어로서, 클라이언트와 서버 간의 효율적인 데이터 교환을 가능하게 합니다. Apollo Client는 GraphQL을 위한 클라이언트 라이브러리로서, 데이터를 관리하고 캐싱하여 웹 애플리케이션에서 GraphQL을 효율적으로 사용할 수 있게 해줍니다. 이번 포스팅에서는 Apollo Client를 이용하여 GraphQL Subscriptions를 모니터링하는 시스템을 개발하는 방법에 대해 알아보겠습니다.

## 1. Apollo Client 설정하기

먼저, 프로젝트에 Apollo Client를 설치하고 설정해야 합니다. 이를 위해 우선 아래의 명령어를 사용하여 Apollo Client를 설치합니다.

```bash
npm install apollo-client apollo-link apollo-link-ws apollo-link-http subscriptions-transport-ws graphql graphql-tag
```

설치가 완료되면, Apollo Client를 초기화하기 위한 코드를 작성합니다.

```jsx
import ApolloClient from 'apollo-client';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { WebSocketLink } from 'apollo-link-ws';
import { HttpLink } from 'apollo-link-http';

// GraphQL 서버의 엔드포인트 URL
const httpLink = new HttpLink({
  uri: 'http://localhost:4000/graphql'
});

// WebSocket 연결을 위한 엔드포인트 URL
const wsLink = new WebSocketLink({
  uri: 'ws://localhost:4000/graphql',
  options: {
    reconnect: true
  }
});

// Apollo Client 초기화
const client = new ApolloClient({
  link: wsLink,
  cache: new InMemoryCache()
});
```

위의 코드에서 `httpLink`는 GraphQL 서버와의 HTTP 연결을 위한 것이고, `wsLink`는 WebSocket 연결을 위한 것입니다. 두 개의 링크를 `ApolloLink.from()` 함수를 사용하여 하나의 링크로 만들고, 이를 `ApolloClient`의 `link` 옵션에 전달합니다. 또한, `ApolloClient`의 `cache` 옵션으로는 `InMemoryCache`를 사용하도록 설정합니다.

## 2. GraphQL Subscription 구독하기

Apollo Client를 이용하여 GraphQL Subscriptions를 구독하기 위해서는 `subscribeToMore` 함수를 사용해야 합니다. 이 함수는 Apollo Client의 쿼리나 구독 연결에 대한 결과를 구독하고, 업데이트할 수 있는 기능을 제공합니다.

아래의 예시는 `messages`라는 쿼리를 구독하고, 새로운 메시지가 도착할 때마다 화면에 업데이트하는 코드입니다.

```jsx
import React from 'react';
import { gql } from 'apollo-boost';
import { Subscription } from 'react-apollo';

const MESSAGES_SUBSCRIPTION = gql`
  subscription MessagesSubscription {
    messages {
      id
      content
    }
  }
`;

class MessageContainer extends React.Component {
  handleNewMessage = (prev, { subscriptionData }) => {
    const newMessage = subscriptionData.data.messages;
    this.props.updateMessage(newMessage);
  }

  render() {
    return (
      <Subscription subscription={MESSAGES_SUBSCRIPTION}>
        {({ data }) => {
          // 새로운 메시지가 도착할 때마다 화면 업데이트
          if (data) {
            this.handleNewMessage(null, { subscriptionData: { data } });
          }

          return (
            <div>
              {this.props.messages.map(message => (
                <div key={message.id}>{message.content}</div>
              ))}
            </div>
          );
        }}
      </Subscription>
    );
  }
}
```

위의 코드에서 `MESSAGES_SUBSCRIPTION`은 GraphQL 서버에서 정의한 구독 쿼리입니다. `Subscription` 컴포넌트를 사용하여 해당 구독을 구독하고, `data`를 받아와 화면에 렌더링합니다. `componentDidUpdate` 메소드에서 새로운 메시지가 도착할 때마다 `updateMessage` 함수를 호출하여 상태를 업데이트합니다.


## 결론

이제 Apollo Client를 사용하여 GraphQL Subscriptions를 모니터링하는 시스템을 개발하는 방법에 대해 알아보았습니다. Apollo Client를 사용하면 GraphQL Subscriptions를 간편하게 구독하고 업데이트할 수 있으며, 실시간으로 데이터를 모니터링하는 웹 애플리케이션을 개발할 수 있습니다.

더 많은 정보를 알고 싶다면 [Apollo Client 공식 문서](https://www.apollographql.com/docs/react/)를 참고하십시오.

#GraphQL #ApolloClient