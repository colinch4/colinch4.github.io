---
layout: post
title: "[java] Hibernate에서 복합키(Composite key) 설정하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---
1. [소개](#소개)
2. [복합키(Composite key)란?](#복합키란)
3. [Hibernate에서 복합키 설정하기](#Hibernate에서-복합키-설정하기)
4. [예제 코드](#예제-코드)
5. [참고 자료](#참고-자료)

## 소개 {#소개}
Hibernate는 자바를 기반으로 하는 ORM(Object-Relational Mapping) 프레임워크로써, 관계형 데이터베이스와 자바 객체 사이의 매핑을 쉽게 할 수 있게 도와줍니다. 복합키(Composite key)는 한 개 이상의 속성으로 이루어진 키로, 데이터베이스에서 해당 레코드를 고유하게 식별할 때 사용됩니다.

이 글에서는 Hibernate를 사용하여 복합키를 설정하는 방법에 대해 알아보겠습니다.

## 복합키(Composite key)란? {#복합키란}
복합키(Composite key)는 두 개 이상의 속성으로 이루어진 키입니다. 이를 통해 복수의 속성을 결합하여 레코드를 고유하게 식별할 수 있습니다. 예를 들어, 주문 테이블에서 주문번호와 주문일자를 복합키로 지정한다면 같은 주문번호와 주문일자를 가진 주문을 중복해서 저장할 수 없게 됩니다.

## Hibernate에서 복합키 설정하기 {#Hibernate에서-복합키-설정하기}
Hibernate에서 복합키를 설정하기 위해서는 다음의 단계를 따라야 합니다:

1. `@Embeddable` 어노테이션을 사용하여 복합키 클래스를 정의합니다. 복합키 클래스는 해당 엔티티 클래스에 포함될 속성들을 가지고 있습니다.
2. `@EmbeddedId` 어노테이션을 사용하여 해당 엔티티 클래스에 복합키를 설정합니다. `@EmbeddedId` 어노테이션은 복합키 클래스를 참조합니다.

이렇게 복합키를 설정하면 Hibernate는 복합키를 기반으로 데이터베이스 테이블을 생성하고, 복합키를 사용하여 레코드를 식별합니다.

## 예제 코드 {#예제-코드}
다음은 Hibernate에서 복합키를 설정하는 예제 코드입니다. 예제 코드에서는 `Order`라는 엔티티 클래스를 만들고, `OrderId`라는 복합키 클래스를 정의합니다.

```java
@Entity
@Table(name = "orders")
public class Order {
    @EmbeddedId
    private OrderId id;
    
    // 필요한 다른 속성들...
    
    // getter와 setter 메소드...
}

@Embeddable
public class OrderId implements Serializable {
    private Long orderNumber;
    private Date orderDate;
    
    // getter와 setter 메소드, equals()와 hashCode() 메소드...
}
```

위의 예제 코드에서 `Order` 클래스는 `OrderId` 클래스를 복합키로 사용하고 있습니다. `Order` 클래스의 `id` 속성에는 `@EmbeddedId` 어노테이션을 사용하여 복합키를 설정하였습니다. `OrderId` 클래스는 `@Embeddable` 어노테이션을 사용하여 복합키 클래스임을 표시하고, `orderNumber`와 `orderDate` 속성을 가지고 있습니다.

## 참고 자료 {#참고-자료}
- Hibernate 공식 문서: [https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html](https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html)
- Baeldung의 "A Guide to Composite Keys in Hibernate": [https://www.baeldung.com/hibernate-composite-keys](https://www.baeldung.com/hibernate-composite-keys)