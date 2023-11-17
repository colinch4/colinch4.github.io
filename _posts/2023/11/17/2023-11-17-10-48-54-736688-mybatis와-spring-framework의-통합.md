---
layout: post
title: "[java] MyBatis와 Spring Framework의 통합"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

이번 글에서는 MyBatis와 Spring Framework를 함께 사용하는 방법에 대해 알아보겠습니다. MyBatis는 SQL 매퍼 프레임워크로서 데이터베이스와의 상호 작용을 단순화하고 개발자에게 유연성을 제공합니다. Spring Framework는 자바 기반의 애플리케이션을 개발하기 위한 다양한 기능과 라이브러리를 제공하는 프레임워크입니다.

## MyBatis와 Spring 연동 설정

MyBatis와 Spring을 함께 사용하기 위해서는 몇 가지 설정이 필요합니다. 

### 1. Maven 의존성 추가

먼저, Maven 프로젝트를 사용하는 경우, `pom.xml` 파일에 MyBatis 및 Spring Framework의 의존성을 추가해야 합니다. 아래 코드는 MyBatis와 Spring Framework의 최신 버전을 사용하는 예시입니다.

```xml
<!-- MyBatis -->
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.5.6</version>
</dependency>

<!-- Spring Framework -->
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>5.3.4</version>
</dependency>
```

### 2. 데이터베이스 연결 설정

MyBatis의 데이터베이스 연결 설정을 위해 `mybatis-config.xml` 파일을 작성해야 합니다. 이 파일은 MyBatis의 설정 정보를 담고 있으며 데이터베이스 연결 및 매퍼 파일의 위치를 지정할 수 있습니다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="com.mysql.jdbc.Driver"/>
                <property name="url" value="jdbc:mysql://localhost:3306/mydatabase"/>
                <property name="username" value="myuser"/>
                <property name="password" value="mypassword"/>
            </dataSource>
        </environment>
    </environments>
    <mappers>
        <mapper resource="mybatis/mapper.xml"/>
    </mappers>
</configuration>
```

### 3. Spring 설정 파일 작성

Spring Framework와 MyBatis를 통합하기 위해 `applicationContext.xml` 파일에 다음 설정을 추가해야 합니다.

```xml
<!-- MyBatis 설정 -->
<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
    <property name="dataSource" ref="dataSource"/>
    <property name="configLocation" value="classpath:mybatis-config.xml"/>
</bean>

<bean id="sqlSession" class="org.mybatis.spring.SqlSessionTemplate">
    <constructor-arg index="0" ref="sqlSessionFactory"/>
</bean>

<!-- MyBatis 매퍼 등록 -->
<bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
    <property name="basePackage" value="com.example.mybatis.mappers"/>
</bean>
```

## MyBatis와 Spring의 연동 예제

이제 MyBatis와 Spring Framework의 연동이 완료되었습니다. 아래는 MyBatis의 매퍼 인터페이스와 Spring의 서비스 계층을 함께 사용하는 간단한 예제 코드입니다.

```java
package com.example.mapper;

import com.example.model.User;

public interface UserMapper {
    User getUserById(int id);
    void insertUser(User user);
    void updateUser(User user);
    void deleteUser(int id);
}
```

```java
package com.example.service;

import com.example.mapper.UserMapper;
import com.example.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    private UserMapper userMapper;

    @Autowired
    public UserService(UserMapper userMapper) {
        this.userMapper = userMapper;
    }

    public User getUserById(int id) {
        return userMapper.getUserById(id);
    }

    public void insertUser(User user) {
        userMapper.insertUser(user);
    }
    
    public void updateUser(User user) {
        userMapper.updateUser(user);
    }

    public void deleteUser(int id) {
        userMapper.deleteUser(id);
    }
}
```

위의 예제에서는 MyBatis의 매퍼 인터페이스를 정의하고, Spring의 서비스 계층에서 해당 인터페이스를 주입받아 사용하는 방식으로 MyBatis와 Spring을 함께 사용합니다.

## 결론

이번에는 MyBatis와 Spring Framework를 함께 사용하는 방법에 대해 알아보았습니다. MyBatis와 Spring을 함께 사용하면 데이터베이스와의 상호 작용을 쉽게 처리할 수 있으며, 개발자에게 유연성과 편의성을 제공합니다. 이를 통해 더욱 효율적이고 생산적인 개발이 가능해집니다.