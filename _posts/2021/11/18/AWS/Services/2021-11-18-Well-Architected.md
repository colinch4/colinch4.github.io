---
layout: post
title: "[AWS] services - Well Architected"
description: " "
date: 2021-11-18
tags: [AWS]
comments: true
share: true
---

Loose Coupling (느슨한 결합)
---
[Ref](https://d36cz9buwru1tt.cloudfront.net/ko/WP/AWS_Cloud_Best_Practices_05252010.pdf)
> + 클라우드는 시스템 구성 요소들을 더 느슨하게 결합할 수록, 이들 요소의 확장성이 더 향상된다는 SOA(Service-Oriented Architecture)설계 원칙을 재확인시켜 줍니다.
>
> + 본질적으로 결합이 느슨하면 애플리케이션의 다양한 계층과 구성 요소들을 상호 격리하여 각 구성 요소가 서로 비동기적으로 동작하며, 상대요소들을 "블랙 박스"로 취급합니다.
>
> + 예를 들어, 웹 애플리케이션 아키텍처에서는 앱 서버를 웹 서버 및 데이터베이스에서 격리시킬 수 있습니다. 이 앱 서버와 웹 서버가 서로에 대해 인식하지 못하므로, 이들 계층 간 결합이 해체되며, 코드 및 기능면에서 연관성이 사라집니다.
>
> + 일괄 처리형(batch-processing) 아키텍처에서는 상호
독립적인 비동기 구성 요소들을 만들 수 있습니다.
>
