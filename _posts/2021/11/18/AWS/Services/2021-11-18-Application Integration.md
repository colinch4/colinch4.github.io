---
layout: post
title: "[AWS] services - Amazon Simple Queue Service(SQS)"
description: " "
date: 2021-11-18
tags: [AWS]
comments: true
share: true
---


### Amazon Simple Queue Service(SQS)

 마이크로 서비스, 분산 시스템 및 서버리스 애플리케이션을 쉽게 분리하고 확장할 수 있게 해주는 완전관리형 메시지 대기열 서비스

 > + 보안 - Amazon SQS 대기열로 메시지 수신을 제어
>>서버 측 암호화(SSE) 는 AWS Key Management Service(AWS KMS)로 관리되는 키를 사용하여 대기열의 메시지 내용을 보호함으로써 중요한 데이터를 전송
 >
 > + 내구성 – 메시지의 안전을 보장하기 위해 Amazon SQS는 여러 서버에 메시지를 저장
 >>표준 대기열은 최소 1회의 메시지 전송을 지원하고 FIFO 대기열은 정확히 1회 메시지 처리를 지원합니다.
 > + 가용성 – Amazon SQS는 중복 인프라를 사용하여 메시지에 대한 고도의 동시 액세스와 메시지 생성 및 소비에 대한 고가용성을 제공
 >
 > + 확장성 – Amazon SQS는 버퍼링된 각 요청을 독립적으로 처리하여 프로비저닝 지침 없이도 로드 증가 또는 급증을 처리하기 위해 투명하게 확장 가능
 >
 > + 안정성 – Amazon SQS는 처리 중에 메시지를 잠그므로 여러 생산자와 소비자가 동시에 메시지를 전송 및 수신 가능
 >
 > + 사용자 지정 – 대기열을 지정 가능.
 >> 예를 들어 대기열에서 기본 지연 시간을 설정할 수 있습니다. Amazon S3 객체에 대한 포인터가 포함된 Amazon SQS의 경우에는 Amazon Simple Storage Service(Amazon S3) 또는 Amazon DynamoDB을 사용하여 256KB 이상의 메시지 내용을 저장하거나 대규모 메시지를 더 작은 메시지로 분할가능
