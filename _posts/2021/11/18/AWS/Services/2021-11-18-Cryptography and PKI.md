---
layout: post
title: "[AWS] services - Cryptography 와 PKI"
description: " "
date: 2021-11-18
tags: [aws]
comments: true
share: true
---


AWS CloudHSM
---
>  AWS 클라우드에 하드웨어 보안 모듈을 제공합니다. 하드웨어 보안 모듈(HSM)은 암호화 작업을 처리하고 암호화 키에 보안 스토리지를 제공하는 컴퓨팅 장치입니다.
> + 대칭적 키 및 비대칭적 키 페어를 포함하여 암호화 키를 생성, 저장, 가져오기, 내보내기 및 관리합니다.
> + 대칭 및 비대칭 알고리즘을 사용하여 데이터를 암호화하고 해독합니다.
> + 암호화 해시 함수를 사용하여 컴퓨팅 메시지 다이제스트 및 해시 기반 메시지 인증 코드(HMAC)를 계산합니다.
> + 암호로 데이터에 서명(코드 서명 포함)하고 서명을 확인합니다.
> + 암호로 임의 보안 데이터를 생성합니다.

AWS Key Management Service(KMS)
---

> [KMS](https://docs.aws.amazon.com/ko_kr/kms/latest/developerguide/concepts.html)
> + 고객 마스터 키 (CMKs)
> + 데이터 키
> + 데이터 키 페어
> + Aliases
> + 암호화 작업
> + 키 식별자(KeyId)
> + 키 구성 요소 오리진
> + 키 사양
> + 키 사용
> + 봉투 암호화
> + 암호화 컨텍스트
> + 키 정책
> + Grants
> + 권한 부여 토큰
> + 사용 감사CMK
> + 키 관리 인프라



AWS Glue
---
>  완전 관리형 추출, 변환 및 로드(ETL) 서비스로, 효율적인 비용으로 간단하게 여러 데이터 스토어 및 데이터 스트림 간에 원하는 데이터를 분류, 정리, 보강, 이동합니다. AWS Glue는 AWS Glue 데이터 카탈로그로 알려진 중앙 메타데이터 리포지토리, 자동으로 Python 및 Scala 코드를 생성하는 ETL 엔진, 그리고 종속성 확인, 작업 모니터링 및 재시도를 관리하는 유연한 스케줄러로 구성됩니다. AWS Glue는 서버리스이므로 설정하거나 관리할 인프라가 없습니다.
