---
layout: post
title: "[java] JAX-RS HATEOAS(Hypermedia as the Engine of Application State) 이해하기"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

## 개요
JAX-RS는 RESTful 웹 서비스를 구현하기 위한 Java API입니다. HATEOAS는 웹 서비스의 상태 전이를 위해 하이퍼미디어를 사용하는 개념입니다. 이번 블로그에서는 JAX-RS HATEOAS의 개념과 활용 방법을 살펴보겠습니다.

## HATEOAS란?
HATEOAS는 웹 서비스의 상태 전이를 위해 하이퍼미디어를 활용하는 아키텍처 스타일입니다. 이는 RESTful 웹 서비스에서 리소스 간의 연결을 가능하게 하는 링크 정보를 리소스의 표현에 포함하는 개념입니다. HATEOAS를 사용하면 클라이언트 애플리케이션은 리소스와 관련된 가능한 동작을 런타임 시에 확인할 수 있습니다.

## JAX-RS HATEOAS 적용하기
JAX-RS에서 HATEOAS를 구현하기 위해서는 다음과 같은 단계를 따릅니다.

### 1. 응답에 하이퍼미디어 링크 추가하기
```java
@GET
@Path("/users/{id}")
public Response getUserById(@PathParam("id") int id) {
    User user = userService.getUserById(id);
    
    Link selfLink = Link.fromUri("/users/" + user.getId()).rel("self").build();
    Link ordersLink = Link.fromUri("/users/" + user.getId() + "/orders").rel("orders").build();
    
    return Response.ok(user)
                   .links(selfLink, ordersLink)
                   .build();
}
```
위의 예시에서는 `getUserById` 메서드가 `/users/{id}` 경로로 GET 요청을 받고, 해당하는 사용자 정보를 반환합니다. 이 때 `Response` 객체에 `links` 메서드를 이용하여 하이퍼미디어 링크를 추가할 수 있습니다.

### 2. 클라이언트에서 링크 활용하기
클라이언트 애플리케이션은 서버 응답에서 전달되는 링크 정보를 활용하여 다음 동작을 수행할 수 있습니다. 예를 들어, 위의 예시에서 반환된 응답에서 `orders` 링크 정보를 추출하여 주문 목록을 요청하는 등의 동작을 수행할 수 있습니다.

## 결론
JAX-RS HATEOAS는 RESTful 웹 서비스에서 하이퍼미디어를 활용한 상태 전이를 구현하기 위한 방법입니다. 이를 통해 클라이언트 애플리케이션은 동적으로 리소스간의 연결을 탐색하고 상호작용할 수 있습니다.

더 자세한 내용은 아래의 참고자료를 참고하시기 바랍니다.

## 참고자료
- [JAX-RS Specification](https://javaee.github.io/jax-rs-spec/)
- [HATEOAS - Wikipedia](https://en.wikipedia.org/wiki/HATEOAS)