---
layout: post
title: "[nodejs] Apollo Federation을 사용한 분산 GraphQL 서비스 구축"
description: " "
date: 2023-12-18
tags: [nodejs]
comments: true
share: true
---

분산 시스템은 많은 이점을 가지고 있지만, 분산 그래프 시스템을 구축하는 것은 복잡하고 어려운 작업일 수 있습니다. 이 글에서는 **Apollo Federation**을 사용하여 서비스 간의 데이터 그래프를 구축하는 방법에 대해 알아보겠습니다. Apollo Federation은 단일 **GraphQL Gateway**로 여러 서비스를 조합하여 하나의 완전한 그래프 API를 생성할 수 있도록 해줍니다.

## 1. Apollo Federation 소개

**Apollo Federation**은 여러 개별 GraphQL 서비스를 구성 요소로 사용하여 하나의 통합된 GraphQL API를 생성할 수 있는 도구입니다. 각 서비스는 독립적으로 개발하고 배포할 수 있으며, Gateway를 통해 조합됩니다.

### 1.1 Federation의 핵심 기능

- **타입의 확장성:** 서비스 간에 타입을 공유하고 확장하여 중복을 제거할 수 있습니다.
- **단일 진입점:** 하나의 진입점으로 여러 서비스에 분산된 데이터에 접근할 수 있습니다.
- **조건적 쿼리:** 하위 서비스만 필요한 경우 해당 서비스에만 쿼리를 보낼 수 있습니다.

## 2. Apollo Federation의 구성 요소

아래는 Apollo Federation을 구현하기 위해 필요한 구성 요소입니다.

- **Gateway**: 모든 서비스를 조합하고 클라이언트 요청을 분배하는 역할을 합니다.
- **Subgraphs**: 독립적인 GraphQL 서비스로, 고유한 스키마와 리졸버를 갖습니다.

## 3. Apollo Federation 사용하기

### 3.1 Gateway 설정

```javascript
const { ApolloGateway } = require("@apollo/gateway");
const { ApolloServer } = require("apollo-server");

const gateway = new ApolloGateway({
  serviceList: [
    { name: "accounts", url: "http://localhost:4001" },
    { name: "reviews", url: "http://localhost:4002" },
  ],
});

const server = new ApolloServer({
  gateway,
  subscriptions: false,
});

server.listen().then(({ url }) => {
  console.log(`Server ready at ${url}`);
});
```

### 3.2 Subgraph 설정

```javascript
const { ApolloServer, gql } = require("apollo-server");
const { buildFederatedSchema } = require("@apollo/federation");

const typeDefs = gql`
  type Review @key(fields: "id") {
    id: ID
    body: String
    author: User
  }

  extend type User @key(fields: "id") {
    id: ID @external
    reviews: [Review]
  }
`;

const resolvers = {
  Review: {
    author(review) {
      return { __typename: "User", id: review.authorId };
    },
  },
};

const server = new ApolloServer({
  schema: buildFederatedSchema([{ typeDefs, resolvers }]),
});

server.listen({ port: 4002 }).then(({ url }) => {
  console.log(`Server ready at ${url}`);
});
```

## 4. 결론

Apollo Federation을 사용하면 분산된 GraphQL 서비스를 통합하여 효율적으로 데이터 그래프를 구축할 수 있습니다. 이를 통해 각각의 서비스를 독립적으로 확장하고 유지보수할 수 있으면서도, 클라이언트에게 단일 진입점을 제공할 수 있습니다.

더 많은 정보를 원하시면 [Apollo Federation 공식 문서](https://www.apollographql.com/docs/apollo-server/federation/introduction/)를 참고하세요.

**참고문헌**:
- https://www.apollographql.com/docs/apollo-server/federation/introduction/
- https://www.apollographql.com/docs/apollo-server/api/apollo-gateway/
- https://www.apollographql.com/docs/apollo-server/api/apollo-server/