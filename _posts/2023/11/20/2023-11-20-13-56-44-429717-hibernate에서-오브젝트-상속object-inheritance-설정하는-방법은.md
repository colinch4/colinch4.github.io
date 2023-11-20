---
layout: post
title: "[java] Hibernate에서 오브젝트 상속(Object inheritance) 설정하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

오브젝트 상속은 Hibernate에서 매우 유용한 기능 중 하나입니다. 이 기능을 사용하면 상속 구조를 갖는 객체를 데이터베이스에 매핑할 수 있으며, 객체 지향 프로그래밍의 특성을 데이터베이스에도 반영할 수 있습니다.

Hibernate에서 오브젝트 상속을 설정하는 방법은 다음과 같습니다:

1. 상속 관계를 갖는 클래스들을 정의합니다:

```java
@Entity
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
@DiscriminatorColumn(name = "discriminator", discriminatorType = DiscriminatorType.STRING)
public abstract class Vehicle {
    // 공통 필드와 메서드 정의
}

@Entity
@DiscriminatorValue("car")
public class Car extends Vehicle {
    // Car 클래스에 특정 필드와 메서드 정의
}

@Entity
@DiscriminatorValue("bike")
public class Bike extends Vehicle {
    // Bike 클래스에 특정 필드와 메서드 정의
}
```

2. `@Inheritance` 어노테이션을 사용하여 상속 전략을 설정합니다. 일반적으로 `InheritanceType.SINGLE_TABLE`을 사용하여 단일 테이블에 모든 클래스를 저장하는 방식을 선택합니다. 다른 전략으로는 `InheritanceType.JOINED`와 `InheritanceType.TABLE_PER_CLASS`가 있습니다.

3. `@DiscriminatorColumn` 어노테이션을 사용하여 하위 클래스를 식별하는 컬럼을 생성합니다. `name` 속성으로 컬럼 이름을 정하고, `discriminatorType` 속성으로 컬럼의 데이터 타입을 지정합니다.

4. `@DiscriminatorValue` 어노테이션을 사용하여 하위 클래스마다 다른 식별자 값을 설정합니다. 이 값은 `@DiscriminatorColumn`에서 지정한 컬럼의 값과 일치해야 합니다.

위의 예제에서 `Vehicle` 클래스는 추상 클래스로 정의되어 있으며, `Car`와 `Bike`는 `Vehicle`를 상속받아 특정 필드와 메서드를 정의한 클래스입니다. `@DiscriminatorValue` 어노테이션을 사용하여 `Car`와 `Bike`를 식별할 수 있습니다.

이제 Hibernate가 상속 구조를 인식하도록 설정했습니다. 이제 `Vehicle`, `Car`, `Bike` 클래스에 대한 테이블이 생성되고, 해당 테이블들은 상속 구조를 올바르게 유지할 것입니다.

더 자세한 내용은 Hibernate 공식 문서를 참조하시기 바랍니다. [Hibernate 공식 문서](https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html#entity-inheritance)