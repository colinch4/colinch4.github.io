---
layout: post
title: "[java] Hibernate에서 양방향 연관 관계(Bidirectional relationship) 설정하는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

Hibernate는 자바 개발자들이 객체와 관계형 데이터베이스 간의 매핑을 쉽게 구현할 수 있도록 도와주는 ORM(Object-Relational Mapping) 프레임워크입니다. 양방향 연관 관계는 특정 엔티티 간의 서로 참조하는 관계를 의미합니다. 이를 설정하려면 다음과 같은 단계를 따를 수 있습니다.

## 1. 엔티티 클래스 작성하기

먼저 양방향 연관 관계를 설정할 엔티티 클래스를 작성해야 합니다. 예를 들어, `Order`와 `Product` 클래스 간의 연관 관계를 설정하려고 한다면 다음과 같은 코드를 작성할 수 있습니다.

```java
@Entity
public class Order {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    // 다른 필드들...
    
    @ManyToMany
    @JoinTable(name = "order_product",
            joinColumns = @JoinColumn(name = "order_id"),
            inverseJoinColumns = @JoinColumn(name = "product_id"))
    private List<Product> products;
    
    // getter와 setter, 생성자 등
}
```

```java
@Entity
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    // 다른 필드들...
    
    @ManyToMany(mappedBy = "products")
    private List<Order> orders;
    
    // getter와 setter, 생성자 등
}
```

위 코드에서 `Order` 엔티티 클래스는 `products` 필드를 통해 `Product` 엔티티 클래스와 연관되어 있습니다. `Product` 엔티티 클래스는 `orders` 필드를 통해 `Order` 엔티티 클래스와 연관되어 있습니다.

## 2. 연관 관계 메서드 작성하기

이제 연관 관계를 설정한 엔티티 클래스에 대해 양방향 연관 관계를 맺을 수 있는 메서드를 작성해야 합니다. 보통 이러한 메서드는 cascade 등의 연관성 설정을 하기 위해 사용됩니다. 예를 들어, `Order` 클래스에 `addProduct`와 `removeProduct` 메서드를 다음과 같이 작성할 수 있습니다.

```java
@Entity
public class Order {

    // 이전의 코드...
    
    public void addProduct(Product product) {
        products.add(product);
        product.getOrders().add(this);
    }

    public void removeProduct(Product product) {
        products.remove(product);
        product.getOrders().remove(this);
    }
    
    // getter와 setter, 생성자 등
}
```

위 코드에서는 `addProduct` 메서드를 호출하여 `Order`와 `Product` 간의 연관 관계를 설정하고, `removeProduct` 메서드를 호출하여 연관 관계를 해제할 수 있습니다.

## 3. 연관 관계를 활용하기

이제 양방향 연관 관계가 설정된 엔티티 클래스를 활용할 수 있습니다. 예를 들어, 다음과 같이 `Order`와 `Product`를 연관지을 수 있습니다.

```java
Order order = new Order();
Product product1 = new Product();
Product product2 = new Product();

order.addProduct(product1);
order.addProduct(product2);
```

위 코드에서는 `Order` 객체에 `Product` 객체들을 추가하고 양방향 연관 관계를 설정하였습니다.

## 결론

위의 단계를 따라하면 Hibernate에서 양방향 연관 관계를 쉽게 설정할 수 있습니다. 양방향 연관 관계를 설정하면 객체 간의 관계를 더욱 직관적으로 표현하고 다양한 연산을 수행할 수 있습니다. Hibernate 문서나 공식 튜토리얼 등을 참고하여 더 자세한 내용을 찾아보세요. 

참고 자료:
- Hibernate 공식 문서: [https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html](https://docs.jboss.org/hibernate/orm/5.5/userguide/html_single/Hibernate_User_Guide.html)