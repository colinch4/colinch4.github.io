---
layout: post
title: "[AWS] services - Analytics"
description: " "
date: 2021-11-18
tags: [AWS]
comments: true
share: true
---


Amazon Kinesis
--

+ Amazon Kinesis Data Streams

 대규모 데이터 레코드 스트림을 실시간으로 수집하고 처리
 > + 가속화된 로그 및 데이터 피드 인테이크 및 처리
 > + 실시간 측정치 및 보고
 > + 실시간 데이터 분석
 > + 복잡한 스트림 처리

+ Amazon Kinesis Video Streams
+ Amazon Kinesis Data Firehose
+ Amazon Kinesis Data Analytics
+ Amazon Kinesis Agent for Microsoft Windows

Amazon Elasticsearch Service
--

> + AWS 클라우드에서 Elasticsearch 클러스터를 쉽게 배포, 운영 및 조정할 수 있는 관리형 서비스입니다.
> + Elasticsearch는 로그 분석, 실시간 애플리케이션 모니터링, 클릭 스트림 분석 같은 사용 사례를 위한 인기 있는 오픈 소스 검색 및 분석 엔진입니다.
> + Amazon ES를 사용하면 Elasticsearch API에 직접 액세스 할 수 있습니다. 기존 코드 및 애플리케이션이 서비스와 원활하게 작동합니다.
>> ### 규모
>>
>> + 인스턴스 유형으로 알려진 다양한 CPU, 메모리 및 스토리지 용량 구성
>>
>> + 최대 3PB의 연결된 스토리지
>> + 읽기 전용 데이터를위한 비용 효율적인 UltraWarm 스토리지
>> ### 보안
>> + AWS Identity and Access Management (IAM) 액세스 제어
>> + Amazon VPC 및 VPC 보안 그룹과의 손쉬운 통합
>> + 미사용 데이터 암호화 및 노드 간 암호화
>> + Kibana에 대한 Amazon Cognito, HTTP 기본 또는 SAML 인증
>> + 인덱스 수준, 문서 수준 및 필드 수준 보안
>> + 감사 로그
>> + Kibana multi-tenancy
>> ### 안정
>> + 리전 및 가용 영역 으로 알려진 리소스의 다양한 지리적 위치
>> + 다중 AZ 라고하는 동일한 AWS 리전에있는 2 개 또는 3 개의 가용 영역에 대한 노드 할당
>> + 클러스터 관리 작업 부담을 덜어주는 전용 마스터 노드
>> + Amazon ES 도메인 백업 및 복원을위한 자동화 된 스냅 샷
>> ### 적응성
>> + 비즈니스 인텔리전스 (BI) 애플리케이션과의 통합을위한 SQL 지원
>> + 검색 결과를 개선하기위한 사용자 정의 패키지
>> ### 인기있는 서비스와 통합
>> + Kibana를 사용한 데이터 시각화
>> + Amazon ES 도메인 지표 모니터링 및 경보 설정을 위해 Amazon CloudWatch와 통합
>> + Amazon ES 도메인에 대한 구성 API 호출을 감사하기 위해 AWS CloudTrail과 통합
>> + Amazon ES로 스트리밍 데이터를로드하기 위해 Amazon S3, Amazon Kinesis 및 Amazon DynamoDB와 통합
>> + 데이터가 특정 임계 값을 초과하면 Amazon SNS에서 알림
>>

Amazon Athena
--
> + Amazon S3에 저장된 비정형, 반정형 및 정형 데이터를 분석
Amazon S3에서 표준 SQL을 사용하여 데이터를 쉽게 바로 분석할 수 있는 대화형 쿼리 서비스입니다. AWS Management Console에서 몇 가지 작업을 수행하면 Amazon S3에 저장된 데이터에서 Athena을(를) 가리키고, 표준 SQL을 사용하여 임시 쿼리를 실행하고, 몇 초 안에 결과를 얻을 수 있습니다.
Athena는 서버리스 서비스이므로 설정하거나 관리할 인프라가 없으며, 실행하는 쿼리에 대해서만 비용을 지불합니다. Athena은(는) 자동으로—쿼리를 병렬로 실행—하게 조정되므로, 많은 데이터 세트와 복잡한 쿼리가 있더라도 결과가 빠릅니다.

Amazon QuickSight
--
>  데이터를 사용하여 시각적 객체를 구축하고, 애드혹 분석을 수행하고, 사업과 관련된 통찰을 빠르게 얻을 수 있는 신속한 비즈니스 분석 서비스입니다. Amazon QuickSight는 강력한 인 메모리 엔진(SPICE)을 사용하여 AWS 데이터 원본을 완벽하게 검색하고, 조직이 수십만 명의 사용자까지 규모를 조정할 수 있도록 하며, 속도와 응답성이 뛰어난 쿼리 성능을 제공합니다.

Amazon EMR
--
> + 대량의 데이터를 쉽고 효율적으로 처리할 수 있게 해주는 웹 서비스입니다. Amazon EMR은 여러 AWS 제품과 함께 하둡 프로세싱을 사용하여 웹 인덱싱, 데이터 마이닝, 로그 파일 분석, 기계 학습, 과학 시뮬레이션 및 데이터 웨어하우징과 같은 작업을 수행
> + Apache Hadoop 및 Apache Spark와 같은 빅 데이터 프레임워크 실행을 간소화하는 관리형 클러스터 플랫폼입니다. 이러한 프레임워크와 함께 Apache Hive 및 Apache Pig와 같은 관련 오픈 소스 프로젝트를 사용하여 분석용 데이터와 비즈니스 인텔리전스 워크로드를 처리할 수 있습니다.
> ### EMR 파일 시스템(EMRFS)
> + 모든 Amazon EMR 클러스터가 Amazon EMR에서 Amazon S3로 직접 일반 파일을 읽고 쓸 수 있도록 하는 HDFS 구현
> + EMRFS는 하둡과 함께 사용하기 위해 Amazon S3에 영구 데이터를 저장하는 편리한 기능을 제공하면서 동시에 일관성 보기 및 데이터 암호화 같은 기능도 제공


Amazon Redshift
--
> 신속하며 완벽하게 관리되는 페타바이트 규모의 데이터 웨어하우스 서비스로, 기존 비즈니스 인텔리전스 도구를 사용하여 비용 효율적으로 간편하게 모든 데이터를 분석할 수 있게 해 줍니다. 몇백 GB부터 페타바이트 규모 이상의 데이터 세트에 최적화되어 있으며 대부분의 기존 데이터 웨어하우징 솔루션의 10분의 1 정도인 연간 TB당 1,000 USD 미만의 비용으로 사용할 수 있습니다.
