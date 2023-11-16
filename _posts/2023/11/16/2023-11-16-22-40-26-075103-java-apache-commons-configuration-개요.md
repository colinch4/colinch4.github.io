---
layout: post
title: "[java] Java Apache Commons Configuration 개요"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java Apache Commons Configuration은 Java 애플리케이션에서 설정 파일을 처리하기 위한 유용한 라이브러리입니다. 이 라이브러리는 Apache Commons 프로젝트의 일부로 개발되었으며, 다양한 포맷의 설정 파일을 읽고 쓸 수 있는 강력한 기능을 제공합니다.

## 기능

Java Apache Commons Configuration은 다음과 같은 기능을 제공합니다:

1. 설정 파일 파싱: 다양한 포맷의 설정 파일(XML, Properties 등)을 파싱하여 Java 객체로 변환합니다.
2. 설정 값 읽기: 설정 파일에서 값을 읽어올 때 편리한 API를 제공합니다.
3. 설정 값 저장: 변경된 설정 값을 저장할 때 유용한 메소드를 제공합니다.
4. 파일 감시: 설정 파일의 변경을 감지하고, 변경이 발생할 경우 이벤트를 발생시킵니다.
5. 설정 파일 병합: 여러 개의 설정 파일을 병합하여 하나의 설정 파일로 처리할 수 있습니다.
6. 프로퍼티 서버 연동: 프로퍼티 서버와 연동하여 동적으로 설정 값을 가져올 수 있습니다.

## 예제 코드

다음은 Java Apache Commons Configuration을 사용하여 설정 파일을 읽고 처리하는 간단한 예제 코드입니다:

```java
// 1. 설정 파일 인스턴스 생성
Configuration configuration = new PropertiesConfiguration("config.properties");

// 2. 설정 값 읽기
String name = configuration.getString("name");
int age = configuration.getInt("age");

// 3. 설정 값 저장
configuration.setProperty("email", "example@example.com");
configuration.save();

// 4. 파일 감시
FileChangedReloadingStrategy strategy = new FileChangedReloadingStrategy();
configuration.setReloadingStrategy(strategy);

// 5. 설정 파일 병합
CompositeConfiguration compositeConfig = new CompositeConfiguration();
compositeConfig.addConfiguration(new PropertiesConfiguration("config1.properties"));
compositeConfig.addConfiguration(new XMLConfiguration("config2.xml"));

// 6. 프로퍼티 서버 연동
PropertiesConfiguration propertyConfig = new PropertiesConfiguration();
propertyConfig.addProperty("name", new JndiConfiguration("java:comp/env/name"));
```

위의 예제 코드는 각각 설정 파일의 인스턴스를 생성하고, 설정 값을 읽고 저장하며, 파일 감시 및 설정 파일 병합, 프로퍼티 서버 연동을 수행하는 기본적인 사용법을 보여줍니다.

## 참고 자료

- Apache Commons Configuration 공식 문서: [https://commons.apache.org/proper/commons-configuration/](https://commons.apache.org/proper/commons-configuration/)
- Apache Commons Configuration GitHub 저장소: [https://github.com/apache/commons-configuration](https://github.com/apache/commons-configuration)

Java Apache Commons Configuration은 강력한 설정 파일 처리 라이브러리로써, Java 애플리케이션에서 설정 파일을 쉽게 다룰 수 있도록 도와줍니다. 이 라이브러리를 사용하면 설정 파일의 파싱, 수정, 저장 등을 간편하게 처리할 수 있으며, 유연하고 확장 가능한 설정 관리 기능을 제공합니다.