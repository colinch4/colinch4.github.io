---
layout: post
title: "[typescript] 타입스크립트와 AWS Lambda Destinations를 사용하여 비동기 호출 오류 처리"
description: " "
date: 2023-12-12
tags: [typescript]
comments: true
share: true
---

AWS Lambda를 사용하여 서버리스 애플리케이션을 개발하는 경우, **비동기 호출**이 많이 발생합니다. 이때 호출 결과를 모니터링하고 오류를 처리하는 것은 매우 중요합니다.

이번 블로그에서는 **타입스크립트** 언어를 사용하여 AWS Lambda Destinations를 활용하여 비동기 호출 오류를 처리하는 방법에 대해 알아보겠습니다.

## 목차
- [AWS Lambda Destinations란?](#AWS-Lambda-Destinations란)
- [타입스크립트와 AWS Lambda Destinations를 이용한 비동기 호출 오류 처리](#타입스크립트와-AWS-Lambda-Destinations를-이용한-비동기-호출-오류-처리)
- [결론](#결론)

## AWS Lambda Destinations란?
AWS Lambda Destinations는 **비동기 Lambda 함수의 실행 결과를 처리**하고 다른 AWS 서비스로 전달할 수 있는 기능입니다. 비동기 호출로 실행되는 Lambda 함수의 결과를 모니터링하고 오류 처리 로직을 추가할 수 있으며, S3, SNS, SQS와 같은 서비스로 결과를 라우팅할 수 있습니다.

## 타입스크립트와 AWS Lambda Destinations를 이용한 비동기 호출 오류 처리
먼저, AWS Lambda 함수를 타입스크립트로 작성합니다. 이때 사용될 Lambda Destinations 설정은 함수의 구성(configuration) 내에 정의됩니다. 타입스크립트를 사용하여 Lambda 함수를 작성하면 풍부한 **타입 정보와 에러 핸들링**을 할 수 있습니다.

아래는 타입스크립트를 사용하여 작성된 AWS Lambda 함수의 예시입니다.

```typescript
import { Handler, Context, Callback, AWSLambdaResult } from 'aws-lambda';

export const myLambdaHandler: Handler = async (event: any, context: Context, callback: Callback) => {
  try {
    // 비동기 작업 수행
    // 결과 반환
    const result: AWSLambdaResult = {
      statusCode: 200,
      body: 'Success',
    };
    return result;
  } catch (error) {
    // 에러 처리 로직
    console.error(error);
    throw error;
  }
};
```

위 코드에서는 `AWSLambdaResult`를 사용하여 Lambda 함수의 실행 결과를 정의하고, 에러 발생 시 적절한 처리를 하고 있습니다.

이제 Lambda 함수 구성(configuration)에 Destinations 설정을 추가해줍니다. 이를 통해 비동기 호출의 실행 결과를 모니터링하고 오류 처리를 수행할 수 있습니다.

```json
{
  "FunctionName": "myLambdaHandler",
  "DestinationConfig": {
    "OnFailure": {
      "Destination": "arn:aws:sns:us-east-1:123456789012:mySnsTopic"
    }
  }
}
```

위 설정에서는 `OnFailure` 항목을 사용하여 오류 발생 시 SNS 토픽으로 결과를 라우팅하도록 설정하였습니다.

## 결론
타입스크립트와 AWS Lambda Destinations를 활용하여 비동기 호출의 오류를 효과적으로 처리할 수 있습니다. 타입스크립트는 **타입 안정성과 에러 핸들링**을 강화하여 안정적인 Lambda 함수를 작성할 수 있도록 도와주며, Destinations를 통해 호출 결과를 쉽게 모니터링하고 오류 처리를 추가할 수 있습니다. 이를 통해 서버리스 애플리케이션 개발 시 안정성과 신뢰성을 높일 수 있습니다.

AWS Lambda Destinations에 관한 자세한 내용은 [공식 AWS 문서](https://aws.amazon.com/ko/blogs/compute/introducing-aws-lambda-destinations/)를 참고하세요.