---
layout: post
title: "[java] 아파치 플링크와 데이터베이스 연동(Integration of Apache Flink with databases)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크(Apache Flink)는 대규모 데이터 처리를 위한 분산 처리 시스템이다. 데이터베이스는 기업에서 중요한 데이터를 저장하고 관리하는 데 사용되는 핵심 시스템이다. 이 블로그 포스트에서는 아파치 플링크와 데이터베이스를 연동하는 방법을 알아보도록 하겠다.

## 1. JDBC 연결 설정

아파치 플링크는 Java Database Connectivity(JDBC)를 통해 다양한 데이터베이스와 연결할 수 있다. 따라서 먼저 JDBC 드라이버를 설치하고 연결 설정을 해야 한다. JDBC 드라이버는 사용하는 데이터베이스 종류에 따라 다를 수 있으므로 해당 데이터베이스 공식 문서를 참고하여 설치하도록 한다.

## 2. 데이터 소스 연결

아파치 플링크에서는 데이터를 소스로 연결하는 방법에 따라 다양한 옵션이 있다. 데이터베이스와의 연동을 위해서는 데이터베이스의 특성에 맞게 데이터 소스를 설정해야 한다.

### 2.1. Batch 처리

만약 데이터베이스에서 일괄 처리(batch processing)를 하고 싶다면 아파치 플링크의 `JDBCInputFormat` 클래스를 사용할 수 있다. 이 클래스는 JDBC를 통해 데이터를 읽어오는 기능을 제공한다. `JDBCInputFormat`을 사용하기 위해서는 데이터베이스 연결 정보와 SQL 쿼리를 정의해야 한다.

다음은 데이터베이스의 연결 정보와 SQL 쿼리를 설정하는 예제 코드이다.

```java
DataSource dataSource = // 데이터베이스 연결 정보 설정
String sqlQuery = "SELECT * FROM tableName";

JDBCInputFormat jdbcInputFormat = JDBCInputFormat
    .buildJDBCInputFormat()
    .setDrivername("com.mysql.jdbc.Driver")
    .setDBUrl("jdbc:mysql://localhost:3306/dbName")
    .setUsername("username")
    .setPassword("password")
    .setQuery(sqlQuery)
    .finish();

// 아파치 플링크에서 JDBCInputFormat 사용
DataSet<Row> dataset = env.createInput(jdbcInputFormat);
```

### 2.2. 스트리밍 처리

실시간으로 데이터베이스와 연동하여 스트리밍 처리를 하고 싶다면 아파치 플링크의 `JDBCSource` 클래스를 사용할 수 있다. 이 클래스는 특정 시간 간격으로 데이터베이스를 폴링하여 데이터를 읽어온다.

다음은 데이터베이스의 연결 정보와 폴링 주기를 설정하는 예제 코드이다.

```java
String username = "username";
String password = "password";
String drivername = "com.mysql.jdbc.Driver";
String dbURL = "jdbc:mysql://localhost:3306/dbName";
String tableName = "tableName";
int pollingInterval = 5000; // 5초마다 폴링

JDBCSource jdbcSource = JDBCSource
    .builder()
    .setUsername(username)
    .setPassword(password)
    .setDrivername(drivername)
    .setDBUrl(dbURL)
    .setTableName(tableName)
    .setPollingIntervalMillis(pollingInterval)
    .finish();

// 아파치 플링크에서 JDBCSource 사용
DataStream<Row> dataStream = env.addSource(jdbcSource);
```

## 3. 데이터베이스와 데이터 처리 연동

아파치 플링크는 다양한 데이터 처리 기능을 제공한다. 따라서 데이터베이스에서 읽어온 데이터를 이러한 처리 기능과 연동해야 한다. 예를 들어, 데이터베이스의 특정 테이블에서 읽어온 데이터에 대해 변환, 필터링, 그룹화 등의 처리를 수행할 수 있다.

다음은 아파치 플링크에서 데이터베이스와 데이터 처리를 연동하는 예제 코드이다.

```java
// 데이터베이스와 연결하여 데이터를 읽어옴
DataStream<Row> dataStream = env.addSource(jdbcSource);

// 데이터 처리를 위한 변환, 필터링, 그룹화 등의 작업 수행
DataStream<Row> processedDataStream = dataStream
    .filter(row -> (int) row.getField("age") > 18)
    .map(row -> {
        // 변환 작업 수행
        // ...
        return transformedRow;
    })
    .keyBy(row -> row.getField("category"))
    .reduce((row1, row2) -> {
        // 그룹화 및 집계 작업 수행
        // ...
        return resultRow;
    });

// 결과를 데이터베이스에 저장
processedDataStream.addSink(jdbcSink);
```

위의 코드에서 `jdbcSink`는 아파치 플링크의 `JDBCSink` 클래스를 사용하여 데이터를 데이터베이스에 저장하는 기능을 수행한다.

## 4. 결론

이렇게 아파치 플링크와 데이터베이스를 연동하여 대규모 데이터 처리를 수행할 수 있다. 데이터베이스와의 연동을 통해 실시간 또는 일괄 처리를 쉽게 구현할 수 있으며, 다양한 데이터 처리 기능과 연동하여 원하는 결과를 얻을 수 있다.

더 자세한 내용은 아파치 플링크 공식 문서를 참고하도록 하자. :link: [아파치 플링크 공식 문서](https://flink.apache.org/documentation/)