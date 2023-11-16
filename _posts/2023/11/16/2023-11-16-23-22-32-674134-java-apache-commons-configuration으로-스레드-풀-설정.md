---
layout: post
title: "[java] Java Apache Commons Configuration으로 스레드 풀 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

스레드 풀은 Java 애플리케이션에서 동시에 실행되는 작업을 제어하는 데 사용되는 중요한 요소입니다. 스레드 풀을 사용하면 작업을 효율적으로 관리하고 성능을 향상시킬 수 있습니다. 이번에는 Java Apache Commons Configuration 라이브러리를 사용하여 스레드 풀을 설정하는 방법에 대해 알아보겠습니다.

## Apache Commons Configuration 라이브러리 추가

먼저, Apache Commons Configuration 라이브러리를 프로젝트에 추가해야 합니다. 이 라이브러리를 사용하면 XML, 속성 파일 등 다양한 형식의 설정 파일을 쉽게 읽고 사용할 수 있습니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음 종속성을 추가하여 라이브러리를 가져올 수 있습니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-configuration2</artifactId>
        <version>2.7</version>
    </dependency>
</dependencies>
```

## 스레드 풀 설정 파일 생성하기

스레드 풀을 설정하기 위해선, 먼저 설정 값을 포함한 파일을 생성해야 합니다. 예를 들어, `thread-pool.properties`라는 파일을 생성하고 다음과 같이 내용을 작성합니다.

```properties
core.pool.size=10
max.pool.size=50
keep.alive.time=60
```

이 파일은 스레드 풀의 핵심 크기, 최대 크기, 유지 시간 등의 값을 설정하기 위해 사용됩니다.

## 스레드 풀 설정하기

이제 Java 코드에서 Apache Commons Configuration을 사용하여 스레드 풀을 설정해보겠습니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadPoolDemo {

    public static void main(String[] args) {
        // 설정 파일 로드
        Configuration config = loadConfiguration();

        // 스레드 풀 생성 및 설정
        ExecutorService threadPool = createThreadPool(config);

        // 스레드 풀 사용 예시
        for (int i = 0; i < 100; i++) {
            threadPool.execute(() -> {
                // 스레드 풀이 실행할 작업
                System.out.println("Task executed by thread: " + Thread.currentThread().getName());
            });
        }

        // 스레드 풀 종료
        threadPool.shutdown();
    }

    private static Configuration loadConfiguration() {
        try {
            Configurations configs = new Configurations();
            return configs.properties("thread-pool.properties");
        } catch (ConfigurationException e) {
            e.printStackTrace();
            return null;
        }
    }

    private static ExecutorService createThreadPool(Configuration config) {
        int corePoolSize = config.getInt("core.pool.size");
        int maxPoolSize = config.getInt("max.pool.size");
        long keepAliveTime = config.getLong("keep.alive.time");

        return Executors.newFixedThreadPool(corePoolSize);
    }
}
```

위의 코드에서는 `loadConfiguration()` 메소드를 사용하여 설정 파일을 로드하고, `createThreadPool()` 메소드를 사용하여 스레드 풀을 생성하고 설정합니다. 생성된 스레드 풀을 사용하여 작업을 실행할 수 있으며, 마지막으로 스레드 풀을 종료합니다.

이제 Apache Commons Configuration을 사용하여 Java 애플리케이션에서 스레드 풀을 설정하는 방법에 대해 알게 되었습니다. 이를 통해 스레드 풀을 효율적으로 관리하고 우수한 성능을 달성할 수 있습니다.

참고: [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)