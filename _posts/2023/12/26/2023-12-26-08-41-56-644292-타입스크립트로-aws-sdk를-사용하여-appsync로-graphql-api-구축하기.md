---
layout: post
title: "[typescript] 타입스크립트로 AWS SDK를 사용하여 AppSync로 GraphQL API 구축하기"
description: " "
date: 2023-12-26
tags: [typescript]
comments: true
share: true
---

AWS AppSync는 GraphQL을 사용하여 애플리케이션을 위한 실시간 데이터 쿼리 및 동기화 기능을 제공하는 관리형 서비스입니다. 타입스크립트를 사용하여 AWS SDK를 통해 AppSync로 GraphQL API를 구축하는 방법을 알아보겠습니다.

## 1. AWS SDK 설치

먼저 타입스크립트 프로젝트에 AWS SDK를 설치합니다.

```bash
npm install aws-sdk
```

## 2. AWS 자격 증명 구성

AWS SDK를 사용하기 위해서는 적절한 AWS 자격 증명이 필요합니다. AWS 자격 증명을 구성하여 SDK에 제공해야 합니다.

```typescript
import AWS from 'aws-sdk';

AWS.config.update({
  region: 'your-region',
  credentials: {
    accessKeyId: 'your-access-key',
    secretAccessKey: 'your-secret-access-key'
  }
});
```

## 3. AppSync API 생성

AppSync 콘솔에서 GraphQL API를 생성하여 스키마와 리졸버를 구성합니다.

## 4. GraphQL API에 쿼리 수행

타입스크립트에서 AWS SDK를 사용하여 AppSync의 GraphQL API에 쿼리를 수행하는 예제 코드는 다음과 같습니다.

```typescript
import AWS from 'aws-sdk';

const appsync = new AWS.AppSync();

const params = {
  apiId: 'your-api-id',
  query: 'Your GraphQL query',
};

appsync
  .startQueryExecution(params)
  .promise()
  .then((data) => {
    // 쿼리 실행 결과 처리
    console.log(data);
  })
  .catch((err) => {
    // 오류 처리
    console.error(err);
  });
```

위의 예제 코드에서 `apiId`는 생성한 AppSync API의 ID이며, `query`에는 실행할 GraphQL 쿼리를 입력합니다.

위와 같이 타입스크립트로 AWS SDK를 사용하여 AppSync로 GraphQL API를 구축할 수 있습니다.

## 참고 자료
- [AWS SDK for JavaScript 문서](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/AppSync.html)
- [AWS AppSync 문서](https://docs.aws.amazon.com/appsync/index.html)

이제 타입스크립트로 AWS SDK를 사용하여 AppSync로 GraphQL API를 구축하는 방법에 대해 살펴보았습니다. 해당 기술을 사용하여 자신의 애플리케이션에 GraphQL API를 연동하고 싶을 때 참고할 수 있을 것입니다.