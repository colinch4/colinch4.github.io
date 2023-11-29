---
layout: post
title: "[javascript] Marionette.js에서 사용되는 서버리스(Serverless) 아키텍처와 관련된 기술과 도구는 어떤 것들이 있는가?"
description: " "
date: 2023-11-29
tags: [javascript]
comments: true
share: true
---

마리오넷(Marionette) 프레임워크는 JavaScript로 구축된 클라이언트 측 애플리케이션을 개발하기 위해 사용되는 강력한 프레임워크입니다. 서버리스 아키텍처는 클라이언트와 서버 간의 통신을 효율적이고 확장 가능하게 만드는데 도움이 됩니다. Marionette.js와 함께 사용할 수 있는 여러 가지 서버리스 관련 기술과 도구를 알아보겠습니다.

### AWS Lambda
AWS Lambda는 실행되는 동안 백그라운드에서 코드를 실행할 수 있는 서버리스 컴퓨팅 서비스입니다. Lambda를 사용하면 애플리케이션의 일부기능을 분리하여 실행할 수 있습니다. 이를 통해 애플리케이션의 확장성과 유연성을 향상시킬 수 있습니다.

### Azure Functions
Azure Functions는 마이크로소프트의 클라우드 컴퓨팅 플랫폼인 Azure에서 실행되는 서버리스 컴퓨팅 서비스입니다. Azure Functions를 사용하면 마이크로서비스 아키텍처를 구축하고 각 기능을 개별적으로 구성 및 관리할 수 있습니다.

### Google Cloud Functions
Google Cloud Functions는 Google Cloud Platform에서 실행되는 서버리스 컴퓨팅 서비스입니다. Cloud Functions를 사용하면 이벤트 기반의 백엔드 서비스를 간단하게 작성할 수 있습니다. 이 서비스는 확장가능하며, 사용한 만큼만 요금을 지불하게 됩니다.

### Serverless Framework
Serverless Framework는 서버리스 애플리케이션을 빌드, 배포 및 관리하기 위한 오픈 소스 프레임워크입니다. 이 프레임워크를 사용하면 다양한 서버리스 플랫폼에서 일관된 방식으로 앱을 관리 할 수 있습니다. Marionette.js 애플리케이션을 배포하고 관리하는 데 사용할 수 있습니다.

### Serverless Database
서버리스 애플리케이션을 위한 서버리스 데이터베이스도 있습니다. 예를 들어, DynamoDB는 AWS에서 제공되는 서버리스 NoSQL 데이터베이스입니다. 이렇게 서버리스 데이터베이스를 사용하면 관리가 더욱 간편해지고 확장성을 높일 수 있습니다.

### 그 외의 기술과 도구
서버리스 아키텍처를 구축하기 위해 다른 기술과 도구를 사용할 수도 있습니다. 예를 들어, API Gateway, 웹 소켓, 메시징 시스템 등을 사용하여 클라이언트와 서버 간의 통신을 관리할 수 있습니다.

서버리스 아키텍처는 클라이언트 측 애플리케이션을 구축하는 데 있어서 많은 이점을 제공합니다. Marionette.js와 함께 사용할 수 있는 다양한 서버리스 기술과 도구를 활용하여 효율적이고 확장 가능한 애플리케이션을 개발할 수 있습니다.

> [AWS Lambda](https://aws.amazon.com/lambda/)
> [Azure Functions](https://azure.microsoft.com/en-us/services/functions/)
> [Google Cloud Functions](https://cloud.google.com/functions/)
> [Serverless Framework](https://serverless.com/)
> [DynamoDB](https://aws.amazon.com/dynamodb/)
> [API Gateway](https://aws.amazon.com/api-gateway/)
> [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
> [Messaging Systems](https://en.wikipedia.org/wiki/Message_broker)