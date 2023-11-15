---
layout: post
title: "Package.json 설정을 활용한 GraphQL API 서버 설정하기"
description: " "
date: 2023-11-06
tags: [javascript]
comments: true
share: true
---

GraphQL은 현대적이고 강력한 API 쿼리 언어이며, 이를 이용하여 웹 애플리케이션과 서버 간 효율적인 데이터 통신이 가능합니다. GraphQL API 서버를 설정하기 위해 우리는 `package.json` 파일을 활용할 수 있습니다.

## package.json 파일 생성하기

먼저, 프로젝트의 루트 디렉토리에서 터미널을 열고 다음 명령어를 실행하여 `package.json` 파일을 생성합니다.

```bash
npm init -y
```

위 명령어를 실행하면 `package.json` 파일이 생성됩니다.

## 필요한 패키지 설치하기

GraphQL API 서버를 설정하기 위해 우리는 몇 가지 패키지를 설치해야 합니다. `express`는 서버 프레임워크로 사용되며, `apollo-server-express`는 GraphQL 서버를 설정하는 데 사용됩니다.

```bash
npm install express apollo-server-express
```

위 명령어를 실행하여 필요한 패키지를 설치합니다.

## GraphQL API 서버 설정하기

이제 `index.js` 파일을 생성하고 다음 코드를 추가합니다.

```javascript
const express = require('express');
const { ApolloServer, gql } = require('apollo-server-express');

const PORT = 3000;
const app = express();

// GraphQL 스키마 정의
const typeDefs = gql`
  type Query {
    hello: String
  }
`;

// Resolver 함수
const resolvers = {
  Query: {
    hello: () => 'Hello, GraphQL!'
  }
};

// Apollo Server 생성
const server = new ApolloServer({
  typeDefs,
  resolvers
});

// Express에 Apollo Server 미들웨어 추가
server.applyMiddleware({ app });

// 서버 시작
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}/graphql`);
});
```

위 코드에서는 `express`, `apollo-server-express` 패키지를 불러와서 서버를 설정하고 실행하는 것을 볼 수 있습니다. `typeDefs` 변수는 GraphQL 스키마를 정의하고, `resolvers` 변수는 쿼리에 대한 처리 함수를 정의합니다. `server` 변수는 `ApolloServer` 인스턴스를 생성하며, `applyMiddleware` 메서드를 통해 Express에 미들웨어로 등록합니다.

## 서버 실행하기

터미널에서 다음 명렁어를 실행하여 서버를 실행합니다.

```bash
node index.js
```

위 명렁어를 실행하면 서버가 실행되며, `http://localhost:3000/graphql` 에서 GraphQL Playground를 통해 API에 접근할 수 있습니다.

## 결론

이렇게 하면 `package.json` 파일을 활용하여 GraphQL API 서버를 설정할 수 있습니다. `express`와 `apollo-server-express`를 활용하여 GraphQL 스키마를 정의하고 서버를 실행하는 방법을 배웠습니다. GraphQL은 강력한 API 통신 방법이므로, 이를 활용하여 효율적이고 유연한 데이터 통신을 구현할 수 있습니다.

- tags: #GraphQL #API #서버 #package.json