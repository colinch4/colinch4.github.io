---
layout: post
title: "Apollo Server와 Prisma를 활용한 GraphQL Subscriptions 개발하기"
description: " "
date: 2023-11-10
tags: [tech, graphql]
comments: true
share: true
---

GraphQL은 API를 개발할 때 자주 사용되는 기술 중 하나입니다. GraphQL은 클라이언트가 필요한 데이터만 요청할 수 있도록 하여, 불필요한 데이터를 네트워크를 통해 전송하는 비효율을 줄여줍니다. 이러한 GraphQL의 장점 중 하나는 실시간으로 데이터를 업데이트할 수 있는 GraphQL Subscriptions 기능입니다.

이번 포스트에서는 Apollo Server와 Prisma를 활용하여 GraphQL Subscriptions를 개발하는 방법을 알아보겠습니다.

## Apollo Server란?

[Apollo Server](https://www.apollographql.com/docs/apollo-server/)는 GraphQL API를 개발할 수 있는 오픈 소스 프레임워크입니다. Apollo Server는 다양한 언어와 프레임워크에서 사용될 수 있으며, GraphQL의 일관된 스키마 정의, 데이터 요청 및 응답 처리, 에러 핸들링 등을 지원합니다.

## Prisma란?

[Prisma](https://www.prisma.io/)는 데이터베이스 도구로, GraphQL을 위한 ORM(Object-Relational Mapping)을 제공합니다. Prisma는 간단한 스키마 정의와 데이터 모델링을 통해 데이터베이스를 다루는 작업을 쉽게 해줍니다. Prisma를 사용하면 데이터베이스에 대한 CRUD(Create, Read, Update, Delete) 작업을 간편하게 수행할 수 있습니다.

## GraphQL Subscriptions란?

GraphQL Subscriptions는 실시간으로 데이터를 업데이트할 수 있는 기능입니다. 이 기능을 사용하면 서버에서 클라이언트로 데이터의 변경사항을 실시간으로 푸시할 수 있습니다. 대부분의 실시간 웹 애플리케이션에서는 채팅, 실시간 알림, 실시간 주식 시세 등과 같은 기능을 구현할 때 GraphQL Subscriptions를 사용합니다.

## 개발 환경 설정

```bash
# 프로젝트 초기화
$ mkdir graphql-subscriptions
$ cd graphql-subscriptions
$ npm init -y

# Apollo Server 및 Prisma 설치
$ npm install apollo-server graphql prisma
```

## 데이터 모델 정의하기

먼저 Prisma를 사용하여 데이터 모델을 정의해야 합니다. 예시로 블로그 글을 저장하기 위한 `Post` 데이터 모델을 사용하도록 하겠습니다.

```prisma
model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String
  createdAt DateTime @default(now())
}
```

위의 코드에서는 `Post`라는 데이터 모델을 정의하였습니다. `Post`는 `id`, `title`, `content`, `createdAt` 필드를 가지고 있습니다. `id` 필드는 자동으로 생성되는 고유 식별자이며, `createdAt` 필드는 현재 날짜와 시간을 기본값으로 갖습니다.

## Apollo Server 설정하기

Apollo Server를 설정하기 위해 `index.js` 파일을 생성하고 다음과 같이 작성합니다.

```javascript
const { ApolloServer, gql } = require('apollo-server');
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();

const typeDefs = gql`
  type Post {
    id: Int!
    title: String!
    content: String!
    createdAt: String!
  }

  type Query {
    posts: [Post!]!
  }

  type Mutation {
    createPost(title: String!, content: String!): Post!
  }

  type Subscription {
    postAdded: Post!
  }
`;

const resolvers = {
  Query: {
    posts: async () => {
      return prisma.post.findMany();
    },
  },
  Mutation: {
    createPost: async (_, { title, content }) => {
      const post = await prisma.post.create({
        data: {
          title,
          content,
        },
      });

      return post;
    },
  },
  Subscription: {
    postAdded: {
      subscribe: () => prisma.post.findMany(),
      resolve: (payload) => payload,
    },
  },
};

const server = new ApolloServer({
  typeDefs,
  resolvers,
});

server.listen().then(({ url }) => {
  console.log(`Server running at ${url}`);
});
```

위의 코드에서는 Apollo Server를 생성하고, Prisma를 초기화하여 Apollo Server와 연결합니다. 또한, GraphQL 스키마를 정의하고, 각 필드의 타입과 쿼리, 뮤테이션, 서브스크립션을 처리하는 리졸버를 작성합니다.

## GraphQL Subscriptions 테스트하기

서버를 실행한 후 [GraphQL Playground](https://www.apollographql.com/docs/apollo-server/testing/graphql-playground/)를 통해 GraphQL Subscriptions를 테스트할 수 있습니다.

1. Post 추가 구독하기
```graphql
subscription {
  postAdded {
    id
    title
    content
    createdAt
  }
}
```

`postAdded` 구독을 실행하면 새로운 Post가 추가되었을 때 해당 데이터를 실시간으로 받아볼 수 있습니다.

2. Post 추가하기
```graphql
mutation {
  createPost(title: "제목", content: "내용") {
    id
    title
    content
    createdAt
  }
}
```

`createPost` 뮤테이션을 실행하여 새로운 Post를 추가할 수 있습니다.

이처럼 Apollo Server와 Prisma를 활용하여 GraphQL Subscriptions를 개발할 수 있습니다. GraphQL Subscriptions를 사용하면 실시간으로 데이터를 업데이트하고 클라이언트에게 푸시할 수 있어, 실시간 기능이 필요한 애플리케이션 개발에 유용합니다.

#tech #graphql #subscriptions