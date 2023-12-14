---
layout: post
title: "Apollo Client와 함께 자바스크립트로 GraphQL Subscriptions 구축하기"
description: " "
date: 2023-11-10
tags: [graphql]
comments: true
share: true
---

GraphQL은 데이터를 효율적으로 조회하고 업데이트할 수 있는 쿼리 언어입니다. Apollo Client는 프론트엔드 개발자들이 GraphQL을 사용하여 데이터를 관리하는 데 도움을 주는 강력한 도구입니다. 이번 포스트에서는 Apollo Client와 함께 자바스크립트로 GraphQL Subscriptions를 구축하는 방법에 대해 알아보겠습니다.

## GraphQL Subscriptions란 무엇인가요?

GraphQL Subscriptions는 서버에서 클라이언트로 실시간으로 데이터 업데이트를 전송할 수 있게 해주는 기능입니다. 이는 WebSocket을 사용하여 실시간 통신을 지원하며, 클라이언트 애플리케이션은 구독(subscription)을 통해 서버로부터 실시간 업데이트를 수신할 수 있습니다. GraphQL Subscriptions는 실시간 채팅 애플리케이션, 실시간 알림, 주식 시세 업데이트 등 다양한 용도로 활용될 수 있습니다.

## Apollo Client를 사용해 GraphQL Subscriptions 구축하기

1. Apollo Client 설치하기

   우선, Apollo Client를 설치해야 합니다. npm을 사용한다면 다음 명령어를 통해 설치할 수 있습니다:

    ```shell
    npm install @apollo/client graphql subscriptions-transport-ws
    ```

   yarn을 사용한다면 다음 명령어를 사용할 수 있습니다:

    ```shell
    yarn add @apollo/client graphql subscriptions-transport-ws
    ```

2. WebSocket 프로토콜을 지원하는 Apollo Client 만들기

   Apollo Client는 기본적으로 HTTP를 통해 GraphQL 쿼리를 전송하는 방식을 제공합니다. 하지만 우리는 WebSocket 프로토콜을 사용하여 실시간 업데이트를 전송하기 위해 Apollo Link WebSocket을 사용할 것입니다. 다음과 같이 Apollo Client를 설정할 수 있습니다:

    ```javascript
    import { ApolloClient, InMemoryCache } from '@apollo/client';
    import { WebSocketLink } from '@apollo/client/link/ws';

    const link = new WebSocketLink({
      uri: 'ws://localhost:4000/graphql',
      options: {
        reconnect: true
      }
    });

    const client = new ApolloClient({
      link,
      cache: new InMemoryCache()
    });
    ```

   위 코드에서는 `uri`에 서버의 GraphQL 엔드포인트 WebSocket 주소를 입력합니다.

3. Subscription 구독하기

   이제 Apollo Client를 사용하여 GraphQL Subscriptions를 구독할 수 있습니다. 다음은 예시입니다:

    ```javascript
    import { gql } from '@apollo/client';

    const SUBSCRIPTION_QUERY = gql`
        subscription {
            newMessage {
                id
                content
                createdAt
            }
        }
    `;

    const subscription = client.subscribe({ query: SUBSCRIPTION_QUERY }).subscribe({
      next(response) {
        console.log('Received new message:', response.data.newMessage);
      }
    });
    ```

   위 코드에서는 `SUBSCRIPTION_QUERY` 변수에 실시간으로 업데이트를 받을 필드와 값들을 작성합니다. `client.subscribe` 메서드를 사용하여 서버에 구독을 요청하고, `subscribe` 메서드를 사용하여 실시간 업데이트를 받습니다.

## 결론

이제 Apollo Client와 자바스크립트를 사용하여 GraphQL Subscriptions를 구축하는 방법에 대해 알아보았습니다. Apollo Client의 강력한 도구를 활용하면 데이터를 효율적으로 관리하고 실시간 업데이트를 제공할 수 있습니다. GraphQL Subscriptions는 다양한 실시간 기능을 구현하는 데 유용하게 활용될 수 있으므로, 꼭 한 번 써보시기 바랍니다!

참고 링크: [Apollo Client Documentation](https://www.apollographql.com/docs/react/)