---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 연결 풀 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이번 예제에서는 Apache Commons Configuration 라이브러리를 사용하여 Java 애플리케이션에서 데이터베이스 연결 풀을 설정하는 방법을 알아보겠습니다.

## Apache Commons Configuration

Apache Commons Configuration은 다양한 형식의 설정 파일을 읽고 관리하기 위한 Java 라이브러리입니다. 이 라이브러리를 사용하면 애플리케이션의 설정 파일을 쉽게 로드하고 값을 읽을 수 있습니다.

## 연결 풀 설정

데이터베이스 연결 풀은 애플리케이션에서 데이터베이스와의 연결을 관리하는 데 사용되는 기술입니다. 연결 풀을 사용하면 매번 데이터베이스에 연결하는 데 필요한 비용을 줄일 수 있습니다.

아래는 Apache Commons Configuration을 사용하여 연결 풀을 설정하는 예제 코드입니다.

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;
import org.apache.commons.dbcp2.BasicDataSource;

import javax.sql.DataSource;

public class ConnectionPoolExample {

    public static DataSource createDataSource() throws ConfigurationException {
        PropertiesConfiguration config = new PropertiesConfiguration("db.properties");

        BasicDataSource dataSource = new BasicDataSource();
        dataSource.setDriverClassName(config.getString("db.driver"));
        dataSource.setUrl(config.getString("db.url"));
        dataSource.setUsername(config.getString("db.username"));
        dataSource.setPassword(config.getString("db.password"));

        dataSource.setInitialSize(config.getInt("db.pool.initialSize"));
        dataSource.setMaxTotal(config.getInt("db.pool.maxTotal"));
        dataSource.setMaxIdle(config.getInt("db.pool.maxIdle"));
        dataSource.setMinIdle(config.getInt("db.pool.minIdle"));
        dataSource.setMaxWaitMillis(config.getLong("db.pool.maxWaitMillis"));

        return dataSource;
    }

    public static void main(String[] args) {
        DataSource dataSource;
        try {
            dataSource = createDataSource();

            // 데이터베이스 연결 풀을 사용하여 작업 수행
            // ...

            // 연결 풀 반환
            ((BasicDataSource) dataSource).close();
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 예제 코드에서는 `db.properties` 파일에서 데이터베이스 연결 정보와 연결 풀 설정을 읽어옵니다. 그 후 `BasicDataSource` 객체를 생성하고 필요한 설정 값들을 지정합니다. 마지막으로 애플리케이션에서 데이터베이스 작업을 수행한 후에는 연결 풀을 반환합니다.

## 결론

Apache Commons Configuration을 사용하여 Java 애플리케이션에서 데이터베이스 연결 풀을 설정하는 방법에 대해 알아보았습니다. 연결 풀을 사용하면 데이터베이스 연결 비용을 최소화하고 효율적인 데이터베이스 액세스를 할 수 있습니다. 이 예제를 참고하여 실제 애플리케이션에서 연결 풀을 구성해 보세요.

## 참고 자료

- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)
- [Apache Commons DBCP 공식 문서](https://commons.apache.org/proper/commons-dbcp/)