---
layout: post
title: "[nodejs] GraphQL API를 위한 Rate Limiting 구현"
description: " "
date: 2023-12-18
tags: [nodejs]
comments: true
share: true
---

GraphQL API를 운영할 때, 과도한 요청으로 인한 서버 부하를 방지하기 위해 Rate Limiting이 필요합니다. Rate Limiting은 클라이언트로부터 들어오는 요청의 양을 제한하여 서버의 안정성을 보장하는 역할을 합니다. 이번 포스트에서는 Node.js 기반의 GraphQL API를 보호하기 위한 Rate Limiting을 구현하는 방법을 살펴보겠습니다.

## Rate Limiting 라이브러리 선택

Node.js에서는 Rate Limiting을 구현하기 위한 다양한 라이브러리가 제공됩니다. 그 중에서 [express-rate-limit](https://www.npmjs.com/package/express-rate-limit) 라이브러리를 선택하여 GraphQL API에 Rate Limiting을 적용해보겠습니다.

### express-rate-limit 설치

먼저, npm을 사용하여 express-rate-limit 라이브러리를 설치합니다.

```bash
npm install express-rate-limit
```

## GraphQL API에 Rate Limiting 적용

GraphQL API의 엔드포인트에 Rate Limiting을 적용하기 위해 다음과 같은 단계를 따릅니다.

1. **express-rate-limit 미들웨어 설정**

   ```javascript
   const rateLimit = require("express-rate-limit");

   const limiter = rateLimit({
     windowMs: 15 * 60 * 1000, // 15분
     max: 100 // 15분 동안 최대 100개의 요청 허용
   });

   app.use('/graphql', limiter);
   ```

   위 코드에서 `windowMs`는 요청을 제한할 시간 범위를, `max`는 해당 시간 동안 허용할 최대 요청 수를 의미합니다.

2. **GraphQL 엔드포인트에 미들웨어 적용**

   기존의 GraphQL 엔드포인트에 express-rate-limit 미들웨어를 적용합니다.

   ```javascript
   const express = require('express');
   const { graphqlHTTP } = require('express-graphql');
   const schema = require('./schema');

   const app = express();

   app.use('/graphql', limiter); // Rate Limiting 미들웨어 적용
   app.use('/graphql', graphqlHTTP({
     schema: schema,
     graphiql: true
   }));
   ```

이렇게하면 Rate Limiting이 적용된 GraphQL API가 완성됩니다. 클라이언트로부터 오는 과도한 요청을 제한하고, API 서버의 안정성을 높일 수 있습니다.

## 결론

Node.js 기반의 GraphQL API에 Rate Limiting을 적용하여 과도한 요청으로 인한 서버의 안정성 문제를 해결하는 방법을 살펴보았습니다. 이를 통해 보안 강화를 위한 기초적인 조치를 취할 수 있으며, 더 나아가 API 보안을 강화하는데 기여할 수 있습니다.