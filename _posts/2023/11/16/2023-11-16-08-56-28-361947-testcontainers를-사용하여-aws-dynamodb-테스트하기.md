---
layout: post
title: "[java] TestContainers를 사용하여 AWS DynamoDB 테스트하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

AWS DynamoDB는 클라우드 기반의 관리형 NoSQL 데이터베이스로 많은 개발자들이 사용하고 있습니다. DynamoDB를 사용하는 애플리케이션을 개발할 때, 로컬 환경에서 테스트하는 것은 중요한 요소입니다. 이를 도와주는 도구 중 하나인 TestContainers를 사용하여 AWS DynamoDB를 테스트하는 방법에 대해 알아보겠습니다.

## TestContainers란?

TestContainers는 자바 기반 테스트용 컨테이너 라이브러리입니다. 테스트 실행 중에 필요한 컨테이너를 동적으로 생성하고 관리할 수 있습니다. Docker를 기반으로 동작하며, 다양한 데이터베이스, 웹 서버, 메시지 큐 등의 컨테이너를 지원합니다.

## TestContainers를 이용한 AWS DynamoDB 테스트

AWS DynamoDB를 테스트하기 위해서는 우선 TestContainers의 의존성을 추가해야 합니다. Maven 프로젝트의 경우 `pom.xml` 파일에 다음의 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>dynamodb-local</artifactId>
    <version>1.15.2</version>
    <scope>test</scope>
</dependency>
```

이제 테스트 클래스에서 `GenericContainer` 클래스를 사용하여 DynamoDB 컨테이너를 생성하고 관리할 수 있습니다. 아래의 예제 코드를 참고해보세요.

```java
import org.junit.jupiter.api.Test;
import org.testcontainers.containers.GenericContainer;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;

public class DynamoDBTest {

    private static final GenericContainer dynamoDBContainer = new GenericContainer("amazon/dynamodb-local")
            .withExposedPorts(8000);

    @Test
    public void testDynamoDB() {
        dynamoDBContainer.start();
        String endpoint = "http://" + dynamoDBContainer.getContainerIpAddress() + ":" +
                dynamoDBContainer.getMappedPort(8000);

        DynamoDbClient dynamoDbClient = DynamoDbClient.builder()
                .endpointOverride(URI.create(endpoint))
                .build();

        // DynamoDB 테스트 코드 작성

        dynamoDbClient.close();
        dynamoDBContainer.stop();
    }
}
```

위의 예제 코드에서는 `GenericContainer`를 사용하여 DynamoDB Docker 이미지를 실행하고, `DynamoDbClient`를 사용하여 DynamoDB에 접속합니다. 이후에는 필요한 테스트 코드를 작성하면 됩니다.

테스트를 실행하면 로컬 환경에서 AWS DynamoDB를 사용하는 애플리케이션을 테스트할 수 있습니다.

## 마무리

TestContainers를 사용하여 AWS DynamoDB를 테스트하는 방법에 대해 알아보았습니다. 이를 통해 개발자들은 로컬 환경에서 안정적으로 DynamoDB를 테스트할 수 있습니다. TestContainers는 다양한 컨테이너를 제공하므로, 다른 데이터베이스나 서비스도 동일한 방식으로 테스트할 수 있다는 장점이 있습니다.

더 자세한 내용은 [TestContainers 공식 문서](https://www.testcontainers.org/)를 참고하시기 바랍니다.