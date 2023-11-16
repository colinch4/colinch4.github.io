---
layout: post
title: "[java] Ehcache와 Spring Framework의 통합"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Ehcache는 자바 기반의 오픈 소스 인메모리 캐싱 라이브러리입니다. 이는 성능 향상을 위해 데이터를 메모리에 캐시하여 자주 액세스되는 데이터에 대한 빠른 액세스를 지원합니다. Spring Framework는 자바 기반의 애플리케이션 개발을 위한 프레임워크로, 다양한 기능과 모듈을 제공하여 개발자가 애플리케이션을 구축하고 실행하는 데 도움을 줍니다.

이 블로그 게시물에서는 Ehcache와 Spring Framework를 통합하는 방법을 알아보겠습니다. 이를 통해 Spring 애플리케이션에서 Ehcache를 사용하여 데이터 캐싱의 이점을 활용할 수 있게 됩니다.

## 1. 의존성 추가

먼저, Maven 또는 Gradle과 같은 빌드 도구에서 Ehcache 및 Spring Framework의 관련 의존성을 추가해야 합니다. 이를 위해 `pom.xml` (또는 `build.gradle`) 파일을 열고 다음 의존성을 추가합니다:

```xml
<dependencies>
    <!-- Ehcache -->
    <dependency>
        <groupId>org.ehcache</groupId>
        <artifactId>ehcache</artifactId>
        <version>3.8.1</version>
    </dependency>

    <!-- Spring Framework -->
    <!-- Spring Boot Starter Cache -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-cache</artifactId>
    </dependency>
</dependencies>
```

## 2. 캐시 구성

Spring Framework에서 Ehcache를 사용하기 위해 캐시 구성 파일을 설정해야 합니다. `ehcache.xml` 파일을 프로젝트의 리소스 디렉토리에 추가하고 다음과 같이 구성합니다:

```xml
<ehcache xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="http://www.ehcache.org/ehcache.xsd"
         updateCheck="false">

    <cache name="myCache"
           maxEntriesLocalHeap="100"
           eternal="false"
           timeToLiveSeconds="300"/>

</ehcache>
```

위의 예시에서는 `myCache`라는 이름의 캐시를 정의합니다. 이 캐시는 최대 100개의 항목을 로컬 힙 메모리에 저장하며, 300초 동안 유효합니다.

## 3. Spring에 Ehcache 통합

다음으로, Spring Framework에서 Ehcache를 사용할 수 있도록 설정해야 합니다. `@EnableCaching` 애너테이션을 사용하여 캐시 기능을 활성화하고, `ehcache.xml` 파일의 경로를 지정합니다. 이를 위해 메인 구성 클래스에 다음과 같이 코드를 추가합니다:

```java
@Configuration
@EnableCaching
public class MyApplicationConfig extends CachingConfigurerSupport {

    @Bean
    @Override
    public CacheManager cacheManager() {
        net.sf.ehcache.CacheManager cacheManager = new net.sf.ehcache.CacheManager();
        EhCacheCacheManager ehCacheCacheManager = new EhCacheCacheManager(cacheManager);
        ehCacheCacheManager.setCacheManager(cacheManager);
        
        return ehCacheCacheManager;
    }

    @Bean
    @Override
    public KeyGenerator keyGenerator() {
        return new SimpleKeyGenerator();
    }
}
```

위의 예시에서는 `net.sf.ehcache.CacheManager`와 `EhCacheCacheManager`를 사용하여 캐시 관리자를 생성합니다. 또한, `keyGenerator()` 메소드를 사용하여 기본적인 키 생성기를 정의합니다.

## 4. 캐시 사용

이제 Spring 애플리케이션에서 Ehcache를 사용하여 캐시를 설정하고 사용할 수 있습니다. 메소드에 `@Cacheable` 애너테이션을 추가하여 결과를 캐시에 저장하고, 같은 매개변수로 다시 호출될 경우 캐시된 결과를 반환하도록 설정할 수 있습니다. 예를 들어:

```java
@Service
public class MyService {

    @Cacheable("myCache")
    public String getData(String key) {
        // 캐시가 존재하지 않는 경우 로직 처리
        return someExpensiveOperation(key);
    }

    private String someExpensiveOperation(String key) {
        // 비용이 많이 드는 연산을 수행하고 결과 반환
    }
}
```

위의 예시에서는 `getData()` 메소드에 `@Cacheable("myCache")` 애너테이션을 사용하여 `myCache` 캐시를 활용합니다. 같은 `key`로 메소드를 호출할 경우, 캐시에 저장된 결과를 반환하므로 응답 시간이 향상될 수 있습니다.

Ehcache와 Spring Framework의 통합을 통해 애플리케이션의 성능을 향상시키고, 데이터 액세스 작업을 효율적으로 관리할 수 있습니다. 이렇게 구성된 애플리케이션은 자주 액세스되는 데이터를 메모리에 캐시하여 데이터베이스 등의 외부 서비스에 더 적은 액세스를 요구하므로 성능과 확장성을 향상시킬 수 있습니다.

참고 문서:
- [Ehcache 공식 사이트](http://www.ehcache.org)
- [Spring Framework 공식 사이트](https://spring.io/)