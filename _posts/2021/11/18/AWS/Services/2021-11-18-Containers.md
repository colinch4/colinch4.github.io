---
layout: post
title: "[AWS] services - Amazon Elastic Container Service(ECS)"
description: " "
date: 2021-11-18
tags: [aws]
comments: true
share: true
---


### Amazon Elastic Container Service(ECS)

> + 확장성이 뛰어나고 빠른 컨테이너 관리 서비스로 클러스터에서 컨테이너를 실행, 중지 및 관리용이    
>    
> ![ECS](https://docs.aws.amazon.com/ko_kr/AmazonECS/latest/developerguide/images/overview-fargate.png)
>
> ### AWS Fargate
> + 컨테이너에 적합한 서버리스 컴퓨팅 엔진으로, Amazon Elastic Container Service(ECS) 및 Amazon Elastic Kubernetes Service(EKS)에서 모두 작동
> + Fargate에서는 서버를 프로비저닝하고 관리할 필요가 없어 애플리케이션별로 리소스를 지정하고 관련 비용을 지불할 수 있으며, 계획적으로 애플리케이션을 격리함으로써 보안 성능을 향상 가능
> #### 이점
> + 인프라가 아닌 애플리케이션을 배포/관리
> + 요금 옵션이 유연한 적정 규모의 리소스
> + 계획적으로 안전하게 격리
> + 높은 수준의 애플리케이션 가시성
>
>![fargate](https://d1.awsstatic.com/re19/FargateonEKS/Product-Page-Diagram_Fargate@2x.a20fb2b15c2aebeda3a44dbbb0b10b82fb89aa6a.png)
