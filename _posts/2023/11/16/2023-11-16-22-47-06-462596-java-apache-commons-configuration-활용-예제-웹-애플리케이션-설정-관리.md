---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 웹 애플리케이션 설정 관리"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

웹 애플리케이션을 개발하다보면 설정 값들을 효율적으로 관리해야하는 경우가 많습니다. Java에서는 Apache Commons Configuration 라이브러리를 활용하여 웹 애플리케이션의 설정 값을 관리할 수 있습니다. 이번 글에서는 Apache Commons Configuration 라이브러리를 사용한 Java 웹 애플리케이션의 설정 관리 예제를 다루어보겠습니다.

## Apache Commons Configuration 라이브러리란?

Apache Commons Configuration은 Java에서 설정 파일을 쉽게 읽고 쓰는 기능을 제공하는 라이브러리입니다. 다양한 설정 파일 형식을 지원하며, 설정 값들을 쉽게 조회하고 수정할 수 있습니다.

## 예제 설명

이 예제에서는 웹 애플리케이션의 DB 연결 설정 값을 관리하는 예제를 다루겠습니다. 설정 파일은 XML 형식으로 작성되어 있으며, DB 연결 관련 설정 값들을 포함하고 있습니다.

### 1. 설정 파일 작성

먼저, 아래와 같이 `config.xml` 파일을 작성합니다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property name="db.url">jdbc:mysql://localhost:3306/mydb</property>
    <property name="db.username">admin</property>
    <property name="db.password">password</property>
</configuration>
```

### 2. 설정 값 조회하기

다음으로, 아래와 같이 설정 값을 조회하는 코드를 작성합니다.

```java
import org.apache.commons.configuration2.XMLConfiguration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class AppConfig {
    private static final String CONFIG_FILE = "config.xml";
   
    public static void main(String[] args) {
        try {
            Configurations configs = new Configurations();
            XMLConfiguration xmlConfig = configs.xml(CONFIG_FILE);
            
            String dbUrl = xmlConfig.getString("db.url");
            String dbUsername = xmlConfig.getString("db.username");
            String dbPassword = xmlConfig.getString("db.password");
            
            System.out.println("DB URL: " + dbUrl);
            System.out.println("DB Username: " + dbUsername);
            System.out.println("DB Password: " + dbPassword);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

### 3. 설정 값 수정하기

아래는 설정 값을 수정하는 코드입니다.

```java
import org.apache.commons.configuration2.XMLConfiguration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class AppConfig {
    private static final String CONFIG_FILE = "config.xml";
   
    public static void main(String[] args) {
        try {
            Configurations configs = new Configurations();
            XMLConfiguration xmlConfig = configs.xml(CONFIG_FILE);
            
            xmlConfig.setProperty("db.url", "jdbc:mysql://localhost:3306/newdb");
            
            xmlConfig.save();
            System.out.println("Configuration saved successfully.");
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

## 실행 결과

위 예제를 실행하면 다음과 같은 결과를 얻을 수 있습니다.

```
DB URL: jdbc:mysql://localhost:3306/mydb
DB Username: admin
DB Password: password
```

## 결론

Apache Commons Configuration 라이브러리를 사용하면 Java 웹 애플리케이션의 설정 값을 효율적으로 관리할 수 있습니다. 이를 통해 설정 값들의 변경 및 조회가 용이해지며, 코드의 가독성과 유지 보수성을 향상시킬 수 있습니다.

더 자세한 내용은 [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)를 확인하십시오.