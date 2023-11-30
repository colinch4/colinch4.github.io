---
layout: post
title: "[java] 아파치 플링크와 Kinesis 데이터 스트림 연동(Integration of Apache Flink with Kinesis Data Streams)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크는 분산 스트리밍 처리를 위한 오픈 소스 플랫폼입니다. 이 플랫폼은 대규모의 실시간 데이터 처리를 지원하며, 다양한 소스와 연동하여 실시간 스트림 처리를 수행할 수 있습니다. 이번 블로그 포스트에서는 아파치 플링크를 Kinesis 데이터 스트림과 연동하는 방법에 대해 알아보겠습니다.

## Kinesis 데이터 스트림 이란?
Kinesis 데이터 스트림은 아마존 웹 서비스 (AWS)에서 제공하는 실시간 스트리밍 데이터 수집 및 처리 서비스입니다. 이 서비스는 매우 큰 용량의 데이터를 실시간으로 처리하고 분석할 수 있으며, 데이터를 안정적으로 스트림화하여 저장할 수 있습니다. Kinesis 데이터 스트림은 다양한 데이터 소스로부터 데이터를 수집하고, 여러 애플리케이션과 연동하여 데이터를 처리하는 데 사용됩니다.

## 아파치 플링크와 Kinesis 데이터 스트림 연동하기
아파치 플링크는 Kinesis 데이터 스트림과의 연결을 위한 플러그인을 제공합니다. 이 플러그인을 사용하면 플링크 애플리케이션을 통해 Kinesis 데이터 스트림으로부터 데이터를 읽고 쓸 수 있습니다.

### 의존성 추가하기
먼저, 플링크 애플리케이션에 Kinesis 데이터 스트림과의 연동을 위한 의존성을 추가해야 합니다. Maven 프로젝트의 경우, `pom.xml` 파일에 다음과 같이 의존성을 추가합니다:

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-connector-kinesis_${scala.binary.version}</artifactId>
        <version>${flink.version}</version>
    </dependency>
</dependencies>
```

### Kinesis 소스 생성하기
플링크 애플리케이션에서 Kinesis 데이터 스트림으로부터 데이터를 읽기 위해 소스를 생성해야 합니다. 다음은 Kinesis 소스를 생성하는 예제 코드입니다:

```java
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.functions.source.SourceFunction;
import org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer;

public class KinesisSourceExample {

    public static void main(String[] args) throws Exception {
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        FlinkKinesisConsumer<String> kinesisConsumer = new FlinkKinesisConsumer<>("my-kinesis-stream", new SimpleStringSchema(), getKinesisConfig());
        DataStream<String> stream = env.addSource(kinesisConsumer);

        stream.print();

        env.execute("Kinesis Source Example");
    }

    private static Properties getKinesisConfig() {
        Properties config = new Properties();
        config.setProperty(AWSConfigConstants.AWS_REGION, "us-west-2");
        config.setProperty(AWSConfigConstants.AWS_ACCESS_KEY_ID, "your-access-key");
        config.setProperty(AWSConfigConstants.AWS_SECRET_ACCESS_KEY, "your-secret-access-key");
        return config;
    }
}
```

위의 예제에서는 `FlinkKinesisConsumer`를 사용하여 Kinesis 데이터 스트림으로부터 데이터를 읽고, `stream.print()`를 통해 읽은 데이터를 콘솔에 출력합니다.

### Kinesis 싱크 생성하기
플링크 애플리케이션에서 Kinesis 데이터 스트림에 데이터를 쓰기 위해 싱크를 생성해야 합니다. 다음은 Kinesis 싱크를 생성하는 예제 코드입니다:

```java
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.connectors.kinesis.FlinkKinesisProducer;
import org.apache.flink.streaming.connectors.kinesis.serialization.SimpleStringSchema;

public class KinesisSinkExample {

    public static void main(String[] args) throws Exception {
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        DataStream<String> stream = ...

        stream.addSink(new FlinkKinesisProducer<>("my-kinesis-stream", new SimpleStringSchema(), getKinesisConfig()));

        env.execute("Kinesis Sink Example");
    }

    private static Properties getKinesisConfig() {
        Properties config = new Properties();
        config.setProperty(AWSConfigConstants.AWS_REGION, "us-west-2");
        config.setProperty(AWSConfigConstants.AWS_ACCESS_KEY_ID, "your-access-key");
        config.setProperty(AWSConfigConstants.AWS_SECRET_ACCESS_KEY, "your-secret-access-key");
        return config;
    }
}
```

위의 예제에서는 `FlinkKinesisProducer`를 사용하여 플링크 애플리케이션에서 생성된 데이터를 Kinesis 데이터 스트림에 씁니다. `new FlinkKinesisProducer<>("my-kinesis-stream", new SimpleStringSchema(), getKinesisConfig())` 코드에서 `"my-kinesis-stream"`은 데이터를 쓸 Kinesis 데이터 스트림의 이름을 나타냅니다.

## 결론
이번 포스트에서는 아파치 플링크를 Kinesis 데이터 스트림과 연동하는 방법에 대해 알아보았습니다. 플링크를 사용하면 Kinesis 데이터 스트림으로부터 데이터를 읽고, 데이터를 Kinesis 데이터 스트림에 쓰는 실시간 애플리케이션을 개발할 수 있습니다. 이를 통해 대용량의 실시간 데이터를 효율적으로 처리하고 분석할 수 있습니다.

## 참고 자료
- [Apache Flink 공식 문서](https://ci.apache.org/projects/flink/flink-docs-release-1.13/)
- [Amazon Kinesis 공식 문서](https://aws.amazon.com/kinesis/)