---
layout: post
title: "[java] Hibernate에서 두 번째 레벨 캐시(Second Level Cache) 사용하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

Hibernate는 객체-관계 매핑(ORM) 프레임워크로서, 쿼리 결과나 데이터베이스에서 가져온 엔티티를 캐시에 저장하여 성능을 향상시킬 수 있습니다. 이때 사용되는 캐시의 종류에는 첫 번째 레벨 캐시(First Level Cache)와 두 번째 레벨 캐시(Second Level Cache)가 있습니다. 

첫 번째 레벨 캐시는 Hibernate의 세션(Session) 객체에 의해 관리되며, 세션 범위에서 동작합니다. 반면 두 번째 레벨 캐시는 여러 세션 간에 공유되어 사용되며, 쿼리 결과와 엔티티를 저장하는 전역적인 캐시입니다.

## 1. 의존성 추가

먼저 Hibernate의 두 번째 레벨 캐시를 사용하기 위해서는 해당 기능에 대한 의존성을 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음과 같이 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.hibernate</groupId>
    <artifactId>hibernate-core</artifactId>
    <version>{Hibernate 버전}</version>
</dependency>
<dependency>
    <groupId>org.hibernate</groupId>
    <artifactId>hibernate-ehcache</artifactId>
    <version>{Hibernate 버전}</version>
</dependency>
```

Hibernate 버전은 프로젝트에 맞는 버전을 선택하여 사용하시면 됩니다.

## 2. 캐시 설정

Hibernate의 두 번째 레벨 캐시를 사용하기 위해서는 Hibernate 설정 파일(`hibernate.cfg.xml` 또는 `hibernate.properties`)에 다음과 같이 캐시 관련 설정을 추가해야 합니다:

```xml
<!-- 하이버네이트 설정 파일 -->
<!-- ... -->

<property name="hibernate.cache.use_second_level_cache">true</property>
<!-- 사용할 캐시 구현체를 선택 -->
<property name="hibernate.cache.region.factory_class">org.hibernate.cache.ehcache.EhCacheRegionFactory</property>

<!-- ... -->
```

위 설정에서 `hibernate.cache.use_second_level_cache`를 `true`로 설정하여 두 번째 레벨 캐시를 사용하도록 합니다. 또한 `hibernate.cache.region.factory_class`에서는 캐시 구현체를 선택합니다. 위 예제에서는 Ehcache를 사용하도록 설정하였습니다. 다른 구현체를 사용하려면 해당 구현체에 대한 의존성을 추가한 후, `hibernate.cache.region.factory_class` 설정을 변경하시면 됩니다.

## 3. 엔티티에 캐시 설정 추가

두 번째 레벨 캐시를 사용할 엔티티에는 캐시 설정을 추가해야 합니다. 엔티티 클래스에는 `@Cacheable` 애노테이션을 추가하여 캐시를 사용하도록 지정할 수 있습니다:

```java
@Entity
@Table(name = "example_entity")
@Cacheable // 캐시 사용
@Cache(usage = CacheConcurrencyStrategy.READ_WRITE) // 캐시 전략 설정
public class ExampleEntity {
    // ...
}
```

위 예제에서는 `@Cacheable` 애노테이션을 통해 캐시를 사용하도록 하였으며, `@Cache` 애노테이션을 통해 캐시 전략을 설정하였습니다. `CacheConcurrencyStrategy.READ_WRITE`는 읽기와 쓰기 모두 지원하는 캐시 전략으로 가장 일반적으로 사용됩니다. 다른 전략을 사용하려면 해당 전략에 맞게 설정하시면 됩니다.

## 4. 캐시 사용 확인

Hibernate의 두 번째 레벨 캐시가 제대로 동작하는지 확인하기 위해서는 세션 범위를 넘어서 연속적으로 발생하는 쿼리에 대해 캐시가 적용되는지 확인해야 합니다. 이를 위해 다음과 같은 테스트 코드를 작성해 보겠습니다:

```java
Session session = sessionFactory.openSession();
Transaction tx = session.beginTransaction();

ExampleEntity entity1 = session.get(ExampleEntity.class, 1L);
ExampleEntity entity2 = session.get(ExampleEntity.class, 1L);
ExampleEntity entity3 = session.get(ExampleEntity.class, 1L);

tx.commit();
session.close();
```

위 예제에서는 같은 ID를 가진 `ExampleEntity`를 세 번씩 로드합니다. 첫 번째 로드할 때만 데이터베이스에서 엔티티를 가져오고, 이후의 로드에서는 두 번째 레벨 캐시에서 엔티티를 반환받아 성능이 향상되는지 확인할 수 있습니다.

이렇게 Hibernate에서 두 번째 레벨 캐시를 사용하는 방법에 대해 알아보았습니다. 캐시를 사용하면 데이터베이스 액세스를 줄이고 응답 시간을 단축시킬 수 있으므로, 성능 향상을 위해 적절히 활용해 보시기 바랍니다.

## 참고 자료
- Hibernate Documentation: [Caching](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#caching)
- Hibernate Ehcache: [http://www.ehcache.org/](http://www.ehcache.org/)