---
layout: post
title: "[java] TestContainers로 DynamoDB 컨테이너를 시작하는 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

DynamoDB는 Amazon Web Services(AWS)에서 제공하는 NoSQL 데이터베이스 서비스입니다. TestContainers는 자동으로 Docker 컨테이너를 시작하여 통합 테스트를 수행할 수 있는 도구입니다. 이번 블로그 포스트에서는 TestContainers를 사용하여 DynamoDB 컨테이너를 시작하는 방법에 대해 알아보겠습니다.

## TestContainers란?

TestContainers는 통합 테스트를 위해 도커 컨테이너를 자동으로 시작하고 관리하는 자바 라이브러리입니다. 이를 통해 테스트 환경을 쉽게 구성하고 다양한 컨테이너들을 사용하여 테스트를 수행할 수 있습니다. TestContainers는 JUnit, TestNG 등의 테스트 프레임워크와 함께 사용할 수 있습니다.

## DynamoDB 컨테이너를 시작하기 위한 의존성 추가

TestContainers를 사용하여 DynamoDB 컨테이너를 시작하기 위해서는 다음과 같은 의존성을 프로젝트에 추가해야 합니다.

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>dynamodb</artifactId>
    <version>REPLACE_WITH_LATEST_VERSION</version>
    <scope>test</scope>
</dependency>
```

의존성을 추가한 후에는 Maven 또는 Gradle을 사용하여 프로젝트를 다시 빌드해야 합니다.

## DynamoDB 컨테이너 시작하기

DynamoDB 컨테이너를 시작하기 위해서는 TestContainers의 `GenericContainer` 클래스를 사용해야 합니다. 다음은 DynamoDB 컨테이너를 시작하는 간단한 예제 코드입니다.

```java
import org.testcontainers.containers.GenericContainer;

public class DynamoDBContainerTest {

    private static final int DYNAMODB_PORT = 8000;
    private static final String DYNAMODB_IMAGE = "amazon/dynamodb-local";

    @Test
    public void startDynamoDBContainer() {
        try (GenericContainer dynamodbContainer = new GenericContainer(DYNAMODB_IMAGE)
                .withExposedPorts(DYNAMODB_PORT)) {

            dynamodbContainer.start();

            // DynamoDB 컨테이너가 시작되었을 때 수행할 작업을 작성합니다.

        }
    }
}
```

위의 코드에서 `DYNAMODB_PORT`는 DynamoDB 컨테이너가 바인딩하는 로컬 포트를 나타냅니다. `DYNAMODB_IMAGE`는 사용할 DynamoDB 이미지를 지정합니다.

테스트 메서드가 실행될 때, TestContainers는 DynamoDB 컨테이너를 시작하고 `dynamodbContainer` 객체를 생성합니다. `withExposedPorts` 메서드를 사용하여 컨테이너의 포트를 로컬 포트에 바인딩합니다. 그 후, `dynamodbContainer.start()`를 호출하여 컨테이너를 시작할 수 있습니다.

컨테이너가 시작된 후, 필요한 작업을 수행하는 코드를 작성할 수 있습니다.

## 마치며

이번 포스트에서는 TestContainers를 사용하여 DynamoDB 컨테이너를 시작하는 방법에 대해 알아보았습니다. TestContainers를 통해 테스트 환경을 더욱 편리하게 구축하고 도커 컨테이너를 활용하여 통합 테스트를 수행할 수 있습니다.

더 자세한 내용은 [TestContainers의 공식 문서](https://www.testcontainers.org/)를 참고하시기 바랍니다.

Happy testing!