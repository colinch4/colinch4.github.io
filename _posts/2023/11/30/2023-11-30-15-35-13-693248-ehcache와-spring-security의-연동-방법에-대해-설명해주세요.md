---
layout: post
title: "[java] Ehcache와 Spring Security의 연동 방법에 대해 설명해주세요."
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

## 1. Ehcache란?
Ehcache는 Java 어플리케이션에서 메모리 기반의 캐시를 사용하기 위한 라이브러리입니다. Ehcache를 사용하면 자주 사용되는 데이터를 메모리에 저장하여 응답 시간을 크게 개선할 수 있습니다.

## 2. Spring Security란?
Spring Security는 Spring 기반의 어플리케이션에서 보안을 관리하기 위한 프레임워크입니다. Spring Security를 사용하면 사용자 인증, 권한 관리, 보안 설정 등을 간편하게 처리할 수 있습니다.

## 3. Ehcache와 Spring Security의 연동 방법
Ehcache와 Spring Security를 연동하기 위해서는 다음 단계를 따라야 합니다.

### 단계 1: Ehcache 설정하기
먼저 Ehcache를 설정해야 합니다. Ehcache 설정 파일을 작성하고, 캐시할 데이터의 이름과 최대 크기, TTL(Time-to-Live) 등을 설정합니다.

```java
// ehcache.xml 파일 예시

<ehcache>
  <cache name="userCache"
         maxEntriesLocalHeap="100"
         eternal="false"
         timeToLiveSeconds="300"/>
</ehcache>
```

### 단계 2: Spring Security 설정하기
Spring Security를 설정해야 합니다. `ResourceServerConfigurerAdapter` 클래스를 상속받은 클래스를 작성하고, `configure(HttpSecurity http)` 메소드에서 보안 설정을 정의합니다.

```java
@Configuration
@EnableResourceServer
public class SecurityConfig extends ResourceServerConfigurerAdapter {

    @Override
    public void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
            .antMatchers("/api/**").authenticated()
            .anyRequest().permitAll();
    }
}
```

### 단계 3: Ehcache와 Spring Security 연동하기
Ehcache와 Spring Security를 연동하기 위해서는 아래의 작업을 수행해야 합니다.

#### 3.1. EhcacheManager 설정하기
Ehcache를 Spring에 등록하기 위해 `EhCacheManagerFactoryBean` 클래스를 사용합니다. `ehcache.xml` 파일의 경로를 설정해야 합니다.

```java
@Configuration
@EnableCaching
public class CacheConfig {

    @Bean
    public EhCacheManagerFactoryBean ehCacheManagerFactoryBean() {
        EhCacheManagerFactoryBean factoryBean = new EhCacheManagerFactoryBean();
        factoryBean.setConfigLocation(new ClassPathResource("ehcache.xml"));
        factoryBean.setShared(true);
        return factoryBean;
    }

    //...
}
```

#### 3.2. CachingConfigurer 설정하기
Spring Cache를 사용하기 위해서 `CachingConfigurer` 인터페이스를 구현한 클래스를 작성합니다. `CachingConfigurer` 인터페이스의 메소드를 오버라이드하여 Ehcache를 사용하도록 설정합니다.

```java
@Configuration
@EnableCaching
public class CacheConfig implements CachingConfigurer {

    @Autowired
    private EhcacheManagerFactoryBean ehCacheManagerFactoryBean;

    @Override
    public CacheManager cacheManager() {
        EhCacheCacheManager cacheManager = new EhCacheCacheManager(ehCacheManagerFactoryBean.getObject());
        return cacheManager;
    }

    //...
}
```

### 단계 4: 캐시 사용하기
Ehcache와 Spring Security가 연동되면, 아래와 같이 `@Cacheable` 어노테이션을 사용하여 메소드의 결과를 캐시할 수 있습니다.

```java
@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    @Cacheable(value = "userCache")
    public User getUserById(Long userId) {
        return userRepository.findById(userId);
    }

    //...
}
```

위의 예시에서는 `User` 클래스를 `userCache`라는 이름의 캐시에 저장하도록 설정하였습니다. 이렇게 설정된 메소드는 첫 번째 호출 시에는 데이터베이스에서 값을 가져와 캐시에 저장하지만, 이후에는 캐시에서 값을 가져와서 사용하므로 데이터베이스 접근이 최소화됩니다.

이렇게 Ehcache와 Spring Security를 연동하여 어플리케이션의 응답 시간을 개선할 수 있습니다.

## 참고 자료
- [Ehcache 공식 홈페이지](https://www.ehcache.org/)
- [Spring Security 공식 문서](https://spring.io/projects/spring-security)
- [Spring Framework 공식 문서](https://docs.spring.io/spring-framework/docs/current/reference/html/index.html)