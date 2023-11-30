---
layout: post
title: "[java] 아파치 플링크의 스트리밍 SQL(Streaming SQL in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크는 대규모 데이터 처리를 위한 오픈 소스 스트리밍 처리 엔진입니다. 플링크는 다양한 데이터 처리 작업을 위한 다양한 API를 제공하며, 그 중 하나가 스트리밍 SQL입니다. 스트리밍 SQL을 사용하면 구조화된 데이터를 처리하기 위해 SQL 쿼리를 작성할 수 있습니다.

## 스트리밍 SQL 사용 예제

아래는 간단한 스트리밍 SQL 쿼리 예제입니다.

```java
TableEnvironment tableEnv = StreamTableEnvironment.create(env);

String sourceDDL = "CREATE TABLE source_table (\n" +
        "  id INT,\n" +
        "  name STRING,\n" +
        "  salary DOUBLE,\n" +
        "  PRIMARY KEY (id) NOT ENFORCED\n" +
        ") WITH (\n" +
        "  'connector.type' = 'kafka',\n" +
        "  'connector.version' = 'universal',\n" +
        "  'connector.startup-mode' = 'earliest-offset',\n" +
        "  'connector.topic' = 'source_topic',\n" +
        "  'connector.properties.bootstrap.servers' = 'localhost:9092',\n" +
        "  'format.type' = 'json',\n" +
        "  'format.derive-schema' = 'true'\n" +
        ")";

String sinkDDL = "CREATE TABLE sink_table (\n" +
        "  id INT,\n" +
        "  name STRING,\n" +
        "  salary DOUBLE\n" +
        ") WITH (\n" +
        "  'connector.type' = 'jdbc',\n" +
        "  'connector.url' = 'jdbc:mysql://localhost:3306/mydb',\n" +
        "  'connector.table' = 'sink_table',\n" +
        "  'connector.username' = 'user',\n" +
        "  'connector.password' = 'password'\n" +
        ")";

String query = "INSERT INTO sink_table\n" +
        "SELECT id, name, salary\n" +
        "FROM source_table\n" +
        "WHERE salary > 50000";

tableEnv.sqlUpdate(sourceDDL);
tableEnv.sqlUpdate(sinkDDL);
tableEnv.sqlUpdate(query);
tableEnv.execute("Streaming SQL Job");
```

위 예제에서는 `source_table`에서 구조화된 데이터를 읽어와서 `salary`가 50000보다 큰 레코드를 `sink_table`로 출력하는 스트리밍 SQL 쿼리를 정의합니다. `source_table`은 Kafka 커넥터를 사용하여 데이터를 읽고, `sink_table`은 JDBC 커넥터를 사용하여 데이터를 저장합니다.

## 스트리밍 SQL 설정

위 예제에서 사용되는 `source_table`과 `sink_table`은 각각 Kafka와 JDBC 커넥터를 사용하여 데이터 처리를 수행합니다. 이를 위해 플링크는 테이블 설정을 제공하는 `WITH` 절을 사용합니다.

`connector.type`을 사용하여 데이터 소스 및 싱크의 유형을 지정할 수 있습니다. 예제에서는 `kafka` 및 `jdbc`를 사용했습니다.

다른 옵션들은 데이터 소스 또는 싱크에 따라 다를 수 있으며, 예제에서는 각 커넥터의 호스트, 포트, 토픽, 데이터 형식 등을 설정합니다.

## 결론

아파치 플링크의 스트리밍 SQL을 사용하면 SQL 기반으로 구조화된 스트리밍 데이터를 처리할 수 있습니다. 이를 통해 개발자는 기존의 SQL 쿼리 작성 경험을 활용하여 대규모 실시간 데이터 처리 작업을 수행할 수 있습니다.

더 많은 정보를 원하신다면 아파치 플링크 공식 문서를 참조해주세요.

- [Apache Flink 공식 웹사이트](https://flink.apache.org/)
- [Apache Flink 스트리밍 SQL 문서](https://ci.apache.org/projects/flink/flink-docs-release-1.13/zh/docs/dev/table/sql/queries/streaming-sql/)