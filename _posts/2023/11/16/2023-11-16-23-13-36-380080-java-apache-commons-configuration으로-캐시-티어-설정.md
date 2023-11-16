---
layout: post
title: "[java] Java Apache Commons Configuration으로 캐시 티어 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

캐시는 많은 애플리케이션에서 성능 향상을 위해 사용됩니다. Apache Commons Configuration 라이브러리는 다양한 타입의 설정 데이터를 로드하고 관리하는데 도움을 주는 유용한 도구입니다. 이 블로그 포스트에서는 Java Apache Commons Configuration을 사용하여 캐시 티어 설정을 구현하는 방법을 알아보겠습니다.

## 1. Apache Commons Configuration 의존성 추가하기

Apache Commons Configuration을 사용하기 위해서는 Maven 또는 Gradle과 같은 빌드 도구를 사용하여 의존성을 추가해야 합니다. 먼저 Maven 프로젝트의 경우, `pom.xml` 파일에 다음과 같이 의존성을 추가합니다:

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

Gradle 프로젝트의 경우, `build.gradle` 파일에 다음과 같은 의존성을 추가합니다:

```groovy
dependencies {
    implementation 'commons-configuration:commons-configuration:1.10'
}
```

의존성을 추가한 후에는 프로젝트를 업데이트하여 라이브러리를 가져올 수 있습니다.

## 2. 캐시 티어 설정 파일 작성하기

캐시 티어 설정은 프로퍼티 파일 형식으로 작성됩니다. 예를 들어, `cache.properties` 파일에 다음과 같이 세 가지 캐시 티어를 정의할 수 있습니다:

```properties
cache.tier1.url=http://localhost:8081
cache.tier1.timeout=1000

cache.tier2.url=http://localhost:8082
cache.tier2.timeout=2000

cache.tier3.url=http://localhost:8083
cache.tier3.timeout=3000
```

각 티어마다 `url`과 `timeout` 프로퍼티를 정의하였습니다.

## 3. 캐시 티어 설정 읽기

Java에서 Apache Commons Configuration을 사용하여 캐시 티어 설정을 읽으려면 다음과 같은 코드를 작성합니다:

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class CacheConfigReader {
    public static void main(String[] args) {
        Configurations configs = new Configurations();
        try {
            Configuration config = configs.properties("cache.properties");

            String tier1Url = config.getString("cache.tier1.url");
            int tier1Timeout = config.getInt("cache.tier1.timeout");

            String tier2Url = config.getString("cache.tier2.url");
            int tier2Timeout = config.getInt("cache.tier2.timeout");

            String tier3Url = config.getString("cache.tier3.url");
            int tier3Timeout = config.getInt("cache.tier3.timeout");

            System.out.println("Tier 1 URL: " + tier1Url);
            System.out.println("Tier 1 Timeout: " + tier1Timeout);

            System.out.println("Tier 2 URL: " + tier2Url);
            System.out.println("Tier 2 Timeout: " + tier2Timeout);

            System.out.println("Tier 3 URL: " + tier3Url);
            System.out.println("Tier 3 Timeout: " + tier3Timeout);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드는 `cache.properties` 파일에서 각 캐시 티어의 URL과 Timeout 값을 읽고 출력하는 간단한 예제입니다.

## 4. 실행 결과

위의 예제를 실행하면 다음과 같은 결과를 얻을 수 있습니다:

```
Tier 1 URL: http://localhost:8081
Tier 1 Timeout: 1000
Tier 2 URL: http://localhost:8082
Tier 2 Timeout: 2000
Tier 3 URL: http://localhost:8083
Tier 3 Timeout: 3000
```

## 결론

이 블로그 포스트에서는 Apache Commons Configuration 라이브러리를 사용하여 Java 애플리케이션에서 캐시 티어 설정을 구현하는 방법을 살펴보았습니다. 이를 통해 캐시 티어의 URL과 Timeout 값을 관리할 수 있으며, 필요한 경우 설정 파일을 수정하여 세부적인 설정을 변경할 수 있습니다.

`commons-configuration`: [https://commons.apache.org/proper/commons-configuration/](https://commons.apache.org/proper/commons-configuration/)