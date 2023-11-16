---
layout: post
title: "[java] TestContainers로 Kafka Streams 애플리케이션 테스트하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

효과적인 테스트는 신뢰할 수 있는 애플리케이션을 구축하는 데 필수적입니다. Kafka Streams 애플리케이션을 테스트하기 위해 TestContainers를 사용하는 방법에 대해 알아보겠습니다.

[Kafka Streams](https://kafka.apache.org/documentation/streams/)는 Apache Kafka를 통해 스트리밍 데이터를 처리하는 라이브러리입니다. TestContainers는 테스트 환경을 자동으로 구성해주는 Java 라이브러리로, 애플리케이션의 통합 테스트를 단순화시켜줍니다. 이 두 가지 라이브러리를 함께 사용하여 Kafka Streams 애플리케이션을 테스트해 봅시다.

### 1. Maven/Gradle에 TestContainers 의존성 추가하기

먼저, 프로젝트의 Maven 또는 Gradle 파일에 TestContainers 의존성을 추가해야 합니다.

Maven:

```xml
<dependency>
  <groupId>org.testcontainers</groupId>
  <artifactId>kafka</artifactId>
  <version>1.15.3</version>
  <scope>test</scope>
</dependency>
```

Gradle:

```groovy
testImplementation 'org.testcontainers:kafka:1.15.3'
```

### 2. KafkaContainer 설정하기

다음으로, KafkaContainer를 설정해야 합니다. KafkaContainer는 테스트에서 사용할 Kafka 브로커를 시작하고 관리해 줍니다.

```java
import org.testcontainers.containers.KafkaContainer;
import org.testcontainers.utility.DockerImageName;

public class KafkaStreamsTest {

  private static final String TOPIC_NAME = "test-topic";

  @Container
  private KafkaContainer kafkaContainer = new KafkaContainer(DockerImageName.parse("confluentinc/cp-kafka:<kafka-version>"))
    .withStartupTimeout(Duration.ofMinutes(1));

  @Test
  void testKafkaStreams() {
    // Kafka 브로커가 준비될 때까지 대기
    kafkaContainer.start();
    kafkaContainer.waitingFor(Wait.forListeningPort());

    // Kafka 브로커의 주소 가져오기
    String bootstrapServers = kafkaContainer.getBootstrapServers();

    // Kafka Streams 애플리케이션 테스트 코드 작성

    // 테스트 완료 후 Kafka 브로커 종료
    kafkaContainer.stop();
  }
}
```

위의 코드에서 `<kafka-version>`에는 사용할 Kafka 버전을 지정해야 합니다.

### 3. Kafka Streams 애플리케이션 테스트하기

KafkaContainer를 사용하여 Kafka 브로커를 시작했다면, 이제 Kafka Streams 애플리케이션을 테스트할 수 있습니다. Kafka 브로커의 주소를 얻어와서 애플리케이션을 설정하고 실행하는 코드를 작성하면 됩니다.

```java
Properties properties = new Properties();
properties.put(StreamsConfig.APPLICATION_ID_CONFIG, "my-kafka-streams-app");
properties.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
// Kafka Streams 설정 추가

KStreamsApp app = new KStreamsApp(properties);
app.start();

// 테스트 코드 작성

app.stop();
```

테스트 코드에서는 테스트 데이터를 생성하고 Kafka Streams 프로세서의 결과를 검증하는 등 원하는 작업을 수행할 수 있습니다.

### 결론

TestContainers를 사용하여 Kafka Streams 애플리케이션을 효과적으로 테스트할 수 있습니다. KafkaContainer를 설정하고 Kafka 브로커를 시작한 후, 애플리케이션을 구성하고 실행하는 코드를 작성하여 테스트할 수 있습니다. 이러한 테스트는 애플리케이션의 신뢰성을 높이고 버그를 줄이는 데 도움이 됩니다.

더 많은 정보를 원하신다면 [TestContainers 공식 문서](https://www.testcontainers.org/modules/kafka/)를 참고하세요.