---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 캐싱 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

## 소개

Apache Commons Configuration은 Java에서 구성 파일을 읽고 쓰기 위한 유용한 라이브러리입니다. 이 라이브러리를 사용하면 프로그램에서 구성 파일을 쉽게 로드하고, 설정의 값을 읽거나 수정할 수 있습니다.

이 예제에서는 Apache Commons Configuration을 사용하여 캐싱 설정을 구성하는 방법을 보여줄 것입니다.

## Apache Commons Configuration 설치

Apache Commons Configuration을 사용하기 위해서는 Maven 또는 Gradle과 같은 의존성 관리 도구를 사용하여 라이브러리를 추가해야 합니다. 아래는 Maven을 사용한 예제입니다.

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

## 구성 파일 생성

먼저, 캐싱 관련 설정을 포함하는 구성 파일을 생성해야 합니다. 예를 들어, `config.properties`라는 파일을 생성하고 아래와 같이 구성합니다.

```properties
cache.enabled=true
cache.maxSize=100
cache.evictionPolicy=LRU
```

## 캐싱 설정 코드

이제 Java 코드에서 Apache Commons Configuration을 사용하여 구성 파일을 로드하고, 캐싱 설정 값을 읽을 수 있습니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class CachingExample {
    public static void main(String[] args) {
        Configurations configs = new Configurations();
        try {
            Configuration config = configs.properties("config.properties");

            boolean cacheEnabled = config.getBoolean("cache.enabled");
            int cacheMaxSize = config.getInt("cache.maxSize");
            String evictionPolicy = config.getString("cache.evictionPolicy");

            // 캐싱 설정 값 출력
            System.out.println("Cache Enabled: " + cacheEnabled);
            System.out.println("Cache Max Size: " + cacheMaxSize);
            System.out.println("Cache Eviction Policy: " + evictionPolicy);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서는 `Configurations` 객체를 생성하고, `properties()` 메서드를 사용하여 구성 파일을 로드합니다. 그리고 `getBoolean()`, `getInt()`, `getString()` 메서드를 사용하여 각각의 설정 값을 읽어옵니다.

## 실행 결과

위의 코드를 실행하면 아래와 같은 실행 결과가 출력됩니다.

```
Cache Enabled: true
Cache Max Size: 100
Cache Eviction Policy: LRU
```

## 결론

Apache Commons Configuration을 사용하면 Java에서 쉽게 구성 파일을 읽고 쓸 수 있습니다. 이 예제에서는 캐싱 설정을 구성하는 방법을 보여주었지만, 더 복잡한 설정도 Apache Commons Configuration을 활용하여 처리할 수 있습니다.

더 많은 사용 예제와 자세한 내용은 [Apache Commons Configuration 문서](https://commons.apache.org/proper/commons-configuration/userguide/index.html)를 참조하세요.