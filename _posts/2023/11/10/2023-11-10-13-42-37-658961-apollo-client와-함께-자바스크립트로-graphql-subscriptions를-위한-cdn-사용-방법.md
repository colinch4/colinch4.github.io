---
layout: post
title: "Apollo Client와 함께 자바스크립트로 GraphQL Subscriptions를 위한 CDN 사용 방법"
description: " "
date: 2023-11-10
tags: [graphql]
comments: true
share: true
---

## 개요
GraphQL을 사용하여 실시간 데이터 업데이트를 구현하기 위해 Apollo Client를 활용하는 것은 매우 일반적입니다. 그러나, Apollo Server를 사용하지 않는 경우, 서버와 클라이언트 사이의 실시간 통신을 위한 대안이 필요할 수 있습니다. 이 경우, GraphQL Subscriptions를 사용할 수 있습니다. GraphQL Subscriptions는 실시간 이벤트를 구독하고 처리할 수 있도록 하는 메커니즘을 제공합니다.

이번 블로그에서는 Apollo Client를 사용하여 CDN을 통해 GraphQL Subscriptions를 구현하는 방법에 대해 알아보겠습니다.

## 단계별 가이드
### 1. Apollo Client CDN 추가
먼저, HTML 파일의 `<head>` 태그 내에 Apollo Client CDN을 추가해야 합니다. 다음은 CDN 링크입니다:

```html
<script src="https://cdn.jsdelivr.net/npm/apollo-client@2.6.10/dist/apollo.min.js"></script>
```

### 2. WebSocket 연결 설정
Apollo Client를 사용하여 GraphQL Subscriptions를 이용하려면 WebSocket 연결이 필요합니다. `ApolloLink`와 `WebSocketLink`를 사용하여 WebSocket 연결을 설정할 수 있습니다.

```javascript
// Apollo Client 초기화
const { ApolloClient, InMemoryCache, ApolloLink, split } = Apollo;
const { WebSocketLink } = ApolloLink;

// WebSocket 연결 설정
const wsLink = new WebSocketLink({
  uri: 'ws://example.com/graphql',
  options: {
    reconnect: true, // 연결이 끊어졌을 때 다시 연결 시도 여부
  },
});

// Apollo Client 설정
const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: ApolloLink.from([
    wsLink,
    // 이어서 다른 link들도 추가할 수 있음
  ]),
});
```

위 코드에서 `uri`는 GraphQL 서버의 WebSocket 엔드포인트 주소로 변경해야 합니다.

### 3. GraphQL Subscriptions 구독
WebSocket 연결이 설정되면 GraphQL Subscriptions를 구독할 수 있습니다. 다음은 간단한 예시입니다:

```javascript
// GraphQL Subscriptions 구독
client.subscribe({
  query: gql`
    subscription {
      newMessage {
        id
        content
      }
    }
  `
}).subscribe({
  next(data) {
    console.log('새로운 메세지:', data.newMessage);
  }
});
```

위의 코드에서 `newMessage`는 구독하고자 하는 이벤트 이름입니다.

## 결론
Apollo Client를 사용하여 GraphQL Subscriptions를 구현하는 것은 실시간 데이터 업데이트를 위한 강력한 기능을 제공합니다. CDN을 통해 Apollo Client를 사용하여 GraphQL Subscriptions를 구현하는 방법을 소개했습니다. 이를 통해 간편하게 GraphQL Subscriptions를 활용할 수 있습니다.

더 많은 정보는 [Apollo Client 공식 문서](https://www.apollographql.com/docs/react/)를 참조하시기 바랍니다.

#GraphQL #ApolloClient