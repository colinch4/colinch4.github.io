---
layout: post
title: "파이썬 Zappa와 AWS Lambda Edge를 활용한 CDN 배포"
description: " "
date: 2023-09-26
tags: [Zappa, AWSLambda]
comments: true
share: true
---

CDN(Content Delivery Network)은 전 세계에 분산된 서버를 통해 웹 컨텐츠를 더 빠르게 제공하는 기술입니다. AWS Lambda Edge는 서버리스 컴퓨팅 서비스인 AWS Lambda를 기반으로한 CDN 기능을 제공합니다. 이번 글에서는 파이썬 Zappa 프레임워크를 이용하여 AWS Lambda Edge를 활용한 CDN 배포를 간단히 알아보겠습니다.

## Zappa를 이용한 AWS Lambda 배포

먼저, Zappa를 사용하여 AWS Lambda에 파이썬 애플리케이션을 배포하는 방법을 알아보겠습니다. Zappa는 AWS Lambda를 모방하는 장고(Django) 스타일의 프레임워크로, 몇 가지 간단한 설정만으로 AWS Lambda에 애플리케이션을 배포할 수 있습니다.

먼저, Zappa를 설치합니다.

```python
pip install zappa
```

다음으로, 애플리케이션의 `zappa_settings.json` 파일을 생성합니다.

```python
{
    "dev": {
        "django_settings": "your_app.settings",
        "aws_region": "us-west-2",
        "s3_bucket": "your-s3-bucket",
        "slim_handler": true
    }
}
```

`zappa_settings.json` 파일에서 `django_settings`에는 장고(Django) 애플리케이션의 설정 모듈을 지정하고, `aws_region`에는 AWS 리전을 지정합니다. `s3_bucket`은 애플리케이션 코드 및 패키지를 업로드할 S3 버킷을 지정합니다.

마지막으로, Zappa를 사용하여 애플리케이션을 배포합니다.

```python
zappa deploy dev
```

Zappa는 애플리케이션 코드를 AWS Lambda에 업로드하고, 필요한 리소스를 설정하며, API Gateway를 생성합니다. 배포가 완료되면, 생성된 엔드포인트를 통해 애플리케이션에 접근할 수 있습니다.

## AWS Lambda Edge를 통한 CDN 배포

이제, AWS Lambda Edge를 사용하여 CDN 기능을 추가해보겠습니다. AWS Lambda Edge를 활용하면 분산된 엣지 노드에서 실행되는 Lambda 함수를 통해 컨텐츠를 가까운 지역에서 제공할 수 있게 됩니다.

먼저, AWS Management Console에서 Lambda 함수를 생성합니다. Python 3.7 런타임을 선택하고, 필요한 코드를 작성합니다. 해당 코드는 요청된 컨텐츠를 캐싱하기 위한 기능을 구현하거나, 헤더를 추가하는 등의 작업에 사용될 수 있습니다.

다음으로, Lambda 함수의 트리거로서 CloudFront를 설정합니다. 

CDN 배포를 위해 CloudFront를 생성하고, 배포 속성에서 Lambda 함수를 선택하여 트리거로 추가합니다. 이렇게 함으로써 Lambda 함수가 CDN 액세스 요청 때마다 실행되게 됩니다.

Lambda 함수가 CloudFront에서 제공되는 컨텐츠의 처리를 감독하고 조작하게 되므로, CDN 기능을 추가할 수 있습니다.

## 마무리

이번에는 파이썬 Zappa와 AWS Lambda Edge를 활용하여 CDN 배포하는 방법에 대해 알아보았습니다. 이를 통해 웹 컨텐츠의 전송 속도를 개선하고, 사용자 경험을 향상시킬 수 있습니다. AWS Lambda와 Zappa를 적절히 활용하여 CDN을 구축해보세요!

#AWS #CDN #파이썬 #Zappa #AWSLambda #AWSLambdaEdge