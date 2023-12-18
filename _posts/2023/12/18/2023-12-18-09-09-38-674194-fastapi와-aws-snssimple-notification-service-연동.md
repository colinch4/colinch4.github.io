---
layout: post
title: "[python] FastAPI와 AWS SNS(Simple Notification Service) 연동"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

이번 포스트에서는 **FastAPI** 웹 프레임워크와 **AWS SNS(Simple Notification Service)** 를 연동하여 푸시 알림을 보내는 방법을 살펴보겠습니다. 

## FastAPI란 무엇인가?

**FastAPI** 는 Python 3.7 이상을 지원하는 **웹 API 프레임워크** 로, 고성능 및 기능성을 갖추고 있습니다. **FastAPI** 는 빠른 속도, 현대적인 자동 문서화, 강력한 데이터 유효성 확인을 특징으로 하며, 비동기 및 병렬 코드 지원으로 대규모 시스템에도 적합합니다.

## AWS SNS란 무엇인가?

**AWS SNS(Simple Notification Service)** 는 **클라우드 기반의 메시징 서비스** 로, 푸시 알림이나 SMS 등을 통해 애플리케이션, 서비스 또는 사용자에게 알림을 보낼 수 있도록 지원합니다. 

## FastAPI와 AWS SNS 연동 방법

### 1. AWS 계정 및 SNS 토픽 생성

먼저 AWS 콘솔에서 SNS 서비스로 이동하여, 알림을 보낼 **토픽(Topic)** 을 생성합니다.

### 2. FastAPI로 SNS 알림 발송

다음은 FastAPI에서 AWS SDK를 사용하여 SNS로 알림을 보내는 예제 코드입니다.

```python
import boto3
from fastapi import FastAPI

app = FastAPI()

# AWS 인증 정보 설정
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'
region_name = 'your_aws_region'

# SNS 클라이언트 생성
client = boto3.client('sns', 
                      aws_access_key_id=aws_access_key_id, 
                      aws_secret_access_key=aws_secret_access_key, 
                      region_name=region_name)

# FastAPI 엔드포인트 정의
@app.post("/send-notification")
async def send_notification(message: str):
    response = client.publish(
        TopicArn='your_topic_arn',
        Message=message
    )
    return {"status": response['ResponseMetadata']['HTTPStatusCode']}
```

이 코드는 FastAPI 앱을 만들고, POST 메소드 `/send-notification` 를 정의하여, `message` 파라미터를 받아 SNS에 메시지를 전송합니다.

### 3. FastAPI 실행 및 테스트

작성한 FastAPI 앱을 실행하고, HTTP POST 요청을 사용하여 `/send-notification` 엔드포인트에 메시지를 보내 테스트합니다. 이제 AWS SNS 콘솔에서 해당 토픽으로 알림이 전달되는 것을 확인할 수 있습니다.

이처럼 **FastAPI** 와 **AWS SNS** 를 연동하여, 웹 애플리케이션에서 **푸시 알림 서비스** 를 쉽게 구현할 수 있습니다.

더 많은 자세한 정보는 [FastAPI 공식 문서](https://fastapi.tiangolo.com/)와 [AWS SNS 개발 가이드](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)를 참고할 수 있습니다.