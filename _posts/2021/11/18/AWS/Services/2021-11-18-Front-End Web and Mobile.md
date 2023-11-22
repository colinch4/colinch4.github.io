---
layout: post
title: "[AWS] services - Front-End Web 과 Mobile"
description: " "
date: 2021-11-18
tags: [aws]
comments: true
share: true
---

Amazon SNS (Simple Notification Service)
---
 게시자가 구독자(생산자 및 소비자라고도 함)에게 메시지를 전송하는 관리형 서비스
 > 논리적 액세스 포인트 및 통신 채널인 주제에 메시지를 전송하여 구독자와 비동기적으로 통신합니다.
 클라이언트는 Amazon SQS, AWS Lambda, HTTP, 이메일, 모바일 푸시 알림 및 모바일 텍스트 메시지(SMS)와 같은 지원되는 프로토콜을 사용하여
 SNS 주제를 구독하고 게시된 메시지를 수신 가능
 > ![](https://docs.aws.amazon.com/ko_kr/sns/latest/dg/images/sns-overview-1.png)
> # 일반적인 Amazon SNS 시나리오
> + 애플리케이션 통합
>> Fanout 시나리오는 SNS 주제에 게시된 메시지가 복제되어 대기열, HTTP(S) 엔드포인트, Amazon SQS 함수 등 여러 엔드포인트로 푸시되는 경우입니다.Lambda 따라서 평행한 비동시적 처리가 가능
> + 애플리케이션 알림
>> 애플리케이션 및 시스템 알림은 사전 정의된 임계값에 의해 트리거되는 알림
> + 사용자 알림
>> Amazon SNS는 푸시 이메일 메시지 및 문자 메시지(SMS 메시지)를 개인 또는 그룹에 전송할 수 있다.
>> Ex. 전자 상거래 주문 확인을 사용자 알림으로 전송
> + 모바일 푸시 알림
>> 모바일 푸시 알림을 통해 메시지를 모바일 앱으로 바로 전송할 수 있습니다. 예를 들어, Amazon SNS를 사용하여 앱에 업데이트 알림을 보낼 수 있다.
