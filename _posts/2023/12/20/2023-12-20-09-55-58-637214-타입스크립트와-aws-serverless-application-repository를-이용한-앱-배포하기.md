---
layout: post
title: "[typescript] 타입스크립트와 AWS Serverless Application Repository를 이용한 앱 배포하기"
description: " "
date: 2023-12-20
tags: [typescript]
comments: true
share: true
---

AWS의 Serverless Application Repository를 사용하면 서버리스 애플리케이션을 생성하고 공유할 수 있습니다. 타입스크립트로 작성된 서버리스 애플리케이션을 AWS SAR를 통해 배포하는 방법에 대해 알아봅시다.

## 목차
- [사전 준비사항](#사전-준비사항)
- [타입스크립트 서버리스 애플리케이션 생성](#타입스크립트-서버리스-애플리케이션-생성)
- [AWS Serverless Application Repository에 애플리케이션 등록](#aws-serverless-application-repository에-애플리케이션-등록)
- [애플리케이션 배포](#애플리케이션-배포)

## 사전 준비사항
1. AWS 계정 생성
2. AWS CLI 설치 및 구성
3. Node.js 및 npm 설치
4. 타입스크립트 및 관련 패키지 설치

## 타입스크립트 서버리스 애플리케이션 생성
타입스크립트로 AWS Lambda 함수를 작성하여 서버리스 애플리케이션을 만들어봅시다. `aws-serverless-express`를 사용하여 Express 애플리케이션을 래핑하고, `typescript`로 코드를 작성합니다.

```typescript
import * as express from 'express';
import * as awsServerlessExpress from 'aws-serverless-express';
import { APIGatewayProxyHandler } from 'aws-lambda';

const app = express();
app.get('/', (req, res) => {
  res.json({ message: 'Hello, AWS SAR with TypeScript!' });
});

const server = awsServerlessExpress.createServer(app);
export const handler: APIGatewayProxyHandler = (event, context) => {
  awsServerlessExpress.proxy(server, event, context);
};
```

## AWS Serverless Application Repository에 애플리케이션 등록
애플리케이션을 AWS Serverless Application Repository에 등록합니다. `serverless.yml` 파일을 생성하고, 애플리케이션의 메타데이터 및 리소스에 대한 정의를 추가합니다.

```yaml
service: aws-sar-with-typescript
provider:
  name: aws
  runtime: nodejs12.x
  stage: dev
  region: us-east-1
functions:
  app:
    handler: dist/app.handler
    events:
      - http: ANY /
```

## 애플리케이션 배포
AWS CLI를 사용하여 애플리케이션을 패키징하고 배포합니다.

```bash
serverless package
serverless deploy
```

이제 AWS Serverless Application Repository에서 타입스크립트로 작성된 서버리스 애플리케이션을 배포할 수 있습니다. 다른 사용자들도 해당 애플리케이션을 사용하고, 필요에 따라 수정하여 다시 배포할 수 있습니다.

위 내용은 타입스크립트와 AWS Serverless Application Repository를 이용한 앱 배포하는 간략한 예시로, 실제 작업환경에 따라 상세한 설정이 필요할 수 있습니다.

## 참고 자료
- [AWS Serverless Application Repository 문서](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/what-is-serverlessrepo.html)
- [타입스크립트 공식 문서](https://www.typescriptlang.org/docs/)