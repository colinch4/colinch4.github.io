---
layout: post
title: "[java] Ehcache와 Spring Framework의 연동 방법에 대해 설명해주세요."
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

## 소개

Ehcache는 자바 기반의 오픈 소스 캐시 라이브러리로, 메모리에 캐시된 데이터를 사용하여 애플리케이션의 성능을 향상시킬 수 있습니다. Spring Framework는 자바 기반의 애플리케이션 개발을 위한 프레임워크로, 여러 기능과 모듈을 제공하여 개발 과정을 간소화합니다. 이번 글에서는 Ehcache와 Spring Framework를 함께 사용하는 방법에 대해 알아보겠습니다.

## 의존성 설정

먼저, 프로젝트에 Ehcache와 Spring Framework의 의존성을 추가해야 합니다. Maven을 사용하는 경우 `pom.xml` 파일에 다음과 같이 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-cache</artifactId>
</dependency>

<dependency>
    <groupId>org.ehcache</groupId>
    <artifactId>ehcache</artifactId>
</dependency>
```

## 캐시 설정

Ehcache와 Spring Framework를 연동하기 위해, `ehcache.xml` 파일에 캐시 설정을 추가해야 합니다. 다음은 예제로 사용할 `ehcache.xml` 파일의 내용입니다:

```xml
<config xmlns="http://www.ehcache.org/v3"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.ehcache.org/v3 http://www.ehcache.org/schema/ehcache-core-3.0.xsd">

    <cache alias="productCache">
        <resources>
            <heap unit="entries">100</heap>
        </resources>
    </cache>
</config>
```

위의 설정은 `productCache`라는 이름의 캐시를 생성하고, 메모리에 최대 100개의 엔트리를 저장할 수 있도록 설정합니다.

## Spring Framework 설정

Spring Framework에서 Ehcache를 사용하기 위해서는 몇 가지 추가적인 설정이 필요합니다. `@EnableCaching` 어노테이션을 사용하여 캐싱을 활성화하고, `CacheManager`를 구성해야 합니다. 이를 위해 다음과 같이 클래스를 작성합니다:

```java
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.context.annotation.Configuration;
import org.springframework.cache.ehcache.EhCacheCacheManager;
import org.springframework.cache.CacheManager;
import org.springframework.context.annotation.Bean;

@Configuration
@EnableCaching
public class CachingConfig {

    @Bean
    public CacheManager cacheManager() {
        return new EhCacheCacheManager(ehCacheCacheManager().getObject());
    }

    @Bean
    public EhCacheManagerFactoryBean ehCacheCacheManager() {
        EhCacheManagerFactoryBean factory = new EhCacheManagerFactoryBean();
        factory.setConfigLocation(new ClassPathResource("ehcache.xml"));
        factory.setShared(true);
        return factory;
    }
}
```

위의 설정은 `EhCacheCacheManager`를 이용하여 `CacheManager`를 구성하고, `ehcache.xml` 설정 파일을 사용하여 Ehcache를 초기화합니다.

## 캐시 사용

이제 캐시를 사용할 때에는 `@Cacheable`, `@CachePut`, `@CacheEvict` 등의 어노테이션을 이용하여 캐시를 조작할 수 있습니다. 다음은 예제 코드입니다:

```java
import org.springframework.cache.annotation.Cacheable;

@Service
public class ProductService {

    @Cacheable("productCache")
    public Product getProductById(String id) {
        // 캐시가 존재하지 않을 경우 해당 메소드가 실행되어 데이터를 캐시에 저장하고 반환합니다.
        return productRepository.findById(id).orElse(null);
    }

    @CachePut("productCache")
    public Product updateProduct(Product product) {
        // 캐시를 갱신하고 Product를 반환합니다.
        return productRepository.save(product);
    }

    @CacheEvict("productCache")
    public void deleteProduct(String id) {
        // 캐시를 삭제합니다.
        productRepository.deleteById(id);
    }
}
```

위의 예제에서는 `@Cacheable` 어노테이션을 사용하여 `getProductById` 메소드의 결과를 `productCache`라는 이름의 캐시에 저장합니다. 만약 캐시에 데이터가 존재하지 않을 경우에만 해당 메소드가 실행돼 데이터를 캐시에 저장하고 반환합니다. `@CachePut` 어노테이션은 항상 메소드를 실행하고 캐시를 갱신합니다. `@CacheEvict` 어노테이션은 지정된 캐시를 삭제합니다.

## 결론

이렇게 Ehcache와 Spring Framework를 연동하여 캐싱을 구현하는 방법을 알아보았습니다. Ehcache와 Spring Framework의 연동을 통해 애플리케이션의 성능을 향상시킬 수 있고, 자주 사용되는 데이터를 메모리에 캐싱하여 I/O 비용을 줄일 수 있습니다. 관련 문서를 참조하여 더 자세한 내용을 살펴볼 수 있습니다.

## 참고자료

- [Ehcache Documentation](https://www.ehcache.org/documentation/)
- [Spring Framework Caching](https://docs.spring.io/spring-framework/docs/current/reference/html/integration.html#cache)