---
layout: post
title: "[java] TestContainers로 MongoDB 컨테이너를 시작하는 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

TestContainers는 테스트 환경에서 구동되는 컨테이너를 사용하여 애플리케이션을 테스트할 수 있도록 도와주는 자바 라이브러리입니다. 이 라이브러리는 여러 종류의 컨테이너를 제공하며, 이 중에서도 MongoDB 컨테이너를 시작해 보겠습니다.

## MongoDB 컨테이너 시작하기

먼저, TestContainers를 사용하기 위해 Maven 또는 Gradle에 의존성을 추가해야 합니다. Maven의 경우 다음과 같이 `pom.xml` 파일에 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>testcontainers</artifactId>
    <version>1.15.3</version>
    <scope>test</scope>
</dependency>
```

Gradle의 경우 `build.gradle` 파일에 다음 의존성을 추가합니다:

```groovy
testImplementation 'org.testcontainers:testcontainers:1.15.3'
```

MongoDB 컨테이너를 시작하기 위해 `@Testcontainers` 어노테이션을 사용하여 테스트 클래스를 작성합니다. `@Container` 어노테이션을 사용하여 MongoDB 컨테이너를 정의하고 시작할 수 있습니다.

```java
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.testcontainers.containers.MongoDBContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

@Testcontainers
public class MongoDBContainerTest {

    @Container
    private static final MongoDBContainer mongoDBContainer = new MongoDBContainer();

    @Test
    public void testMongoDB() {
        // MongoDB 컨테이너 사용하여 테스트 코드 작성
        MongoClientURI uri = new MongoClientURI(mongoDBContainer.getReplicaSetUrl());
        MongoClient client = new MongoClient(uri);
        MongoDatabase database = client.getDatabase("test");
        MongoCollection<Document> collection = database.getCollection("users");

        // ...

        client.close();
    }
}
```

위의 예제에서는 `MongoDBContainer`를 사용하여 MongoDB 컨테이너를 시작하고 테스트 코드에서 이 컨테이너를 사용하여 MongoDB에 연결합니다.

또는 JUnit 4를 사용하는 경우 `@Rule` 어노테이션과 `ExternalResource`를 사용하여 MongoDB 컨테이너를 시작할 수도 있습니다. 

```java
import org.junit.Rule;
import org.junit.Test;
import org.testcontainers.containers.MongoDBContainer;
import org.testcontainers.utility.DockerImageName;

public class MongoDBContainerTest {

    @Rule
    public MongoDBContainer mongoDBContainer = new MongoDBContainer(DockerImageName.parse("mongo:4.0.10"));

    @Test
    public void testMongoDB() {
        // MongoDB 컨테이너 사용하여 테스트 코드 작성
        MongoClientURI uri = new MongoClientURI(mongoDBContainer.getReplicaSetUrl());
        MongoClient client = new MongoClient(uri);
        MongoDatabase database = client.getDatabase("test");
        MongoCollection<Document> collection = database.getCollection("users");

        // ...

        client.close();
    }
}
```

위의 예제에서는 `MongoDBContainer`를 사용하여 도커 이미지 버전을 지정하여 컨테이너를 시작합니다.

이제 MongoDB 컨테이너를 시작하는 방법을 알게 되었습니다. TestContainers를 사용하여 애플리케이션을 테스트하면 실제 환경과 유사한 테스트 환경을 구축할 수 있으며, 테스트 시에 외부 리소스에 의존하지 않고 안정적으로 테스트할 수 있습니다.

더 자세한 내용은 [TestContainers 공식 사이트](https://www.testcontainers.org/ko/)를 참조하시기 바랍니다.