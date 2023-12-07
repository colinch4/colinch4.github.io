---
layout: post
title: "[spring] mybatis-DB설정"
description: " "
date: 2021-06-09
tags: [springboot]
comments: true
share: true
---

## mybatis-DB설정

> root-context.xml 안에 설정

### dataSource

* DB설정 정보

### sqlSessionFactory 

* session을 만들어 내는 것 
* 데이터 소스를 향해서 가는 것
*  db에도 세션 생김

### dataSource와 mapper 경로 

```java
//mybatis가 알아서 설정해줌
<mybatis-spring:scan base-package="<Mapper package경로>" />
```





## Query문 넣을 때 (JDBC에서)

### #{} 

> PreparedStatement (Statement의 자식)

* ?로 바뀜
* 쿼리를 db에 보내면 한번만 컴파일하는데 메모리에 올려놈 (재사용가능) 
* 더유리함(Statement보다)

### ${}

> Statement

* String 연산자로 '+'로 이어 붙임
* 그때 그때 마다 컴파일을 한다.
