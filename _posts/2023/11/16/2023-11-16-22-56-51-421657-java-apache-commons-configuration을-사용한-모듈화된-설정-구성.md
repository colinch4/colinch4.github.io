---
layout: post
title: "[java] Java Apache Commons Configuration을 사용한 모듈화된 설정 구성"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 프로젝트에서 설정 파일을 읽고 구성하는 데 사용되는 라이브러리입니다. 이를 사용하여 모듈화된 방식으로 설정을 구성하고 관리하는 방법에 대해 알아보겠습니다.

## 설정 파일 준비

먼저, 설정 파일을 준비해야 합니다. 일반적으로 properties 파일이나 XML 파일을 사용하여 설정을 정의할 수 있습니다. 예를 들어, 다음과 같이 "config.properties" 파일을 만들어서 설정을 정의할 수 있습니다.

```properties
# Database 정보
db.url=localhost
db.port=3306
db.username=myuser
db.password=mypassword

# 로그 레벨
log.level=DEBUG

# 서버 설정
server.host=127.0.0.1
server.port=8080
```

## Maven 종속성 추가

Apache Commons Configuration을 사용하기 위해 Maven 종속성을 추가해야 합니다. `pom.xml` 파일에 다음 종속성을 추가해주세요.

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

## 설정 로드하기

이제 Java 코드에서 설정을 로드해보겠습니다.

```java
import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class AppConfig {

    private PropertiesConfiguration config;

    public AppConfig(String configFile) {
        try {
            config = new PropertiesConfiguration(configFile);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }

    public String getDatabaseUrl() {
        return config.getString("db.url");
    }

    public int getDatabasePort() {
        return config.getInt("db.port");
    }

    public String getDatabaseUsername() {
        return config.getString("db.username");
    }

    public String getDatabasePassword() {
        return config.getString("db.password");
    }

    public String getLogLevel() {
        return config.getString("log.level");
    }

    public String getServerHost() {
        return config.getString("server.host");
    }

    public int getServerPort() {
        return config.getInt("server.port");
    }
}
```

위의 코드에서 `PropertiesConfiguration` 클래스를 사용하여 설정 파일을 로드합니다. `configFile` 인자에 로드할 설정 파일의 경로를 전달하면, 해당 파일의 설정을 읽을 수 있게 됩니다. 설정 값을 가져오기 위해 각각의 `get` 메소드를 정의하였습니다.

## 설정 사용하기

이제 AppConfig 클래스의 인스턴스를 생성하고, 필요한 설정 값을 사용할 수 있습니다.

```java
public class App {
    public static void main(String[] args) {
        AppConfig appConfig = new AppConfig("config.properties");

        // 설정 값 사용하기
        System.out.println("Database URL: " + appConfig.getDatabaseUrl());
        System.out.println("Database Port: " + appConfig.getDatabasePort());
        System.out.println("Database Username: " + appConfig.getDatabaseUsername());
        System.out.println("Database Password: " + appConfig.getDatabasePassword());
        System.out.println("Log Level: " + appConfig.getLogLevel());
        System.out.println("Server Host: " + appConfig.getServerHost());
        System.out.println("Server Port: " + appConfig.getServerPort());
    }
}
```

위의 코드에서는 AppConfig 클래스의 인스턴스를 생성하고, 필요한 설정 값을 가져와서 출력합니다.

## 결론

Apache Commons Configuration을 사용하면 Java 프로젝트의 설정을 모듈화하고 쉽게 관리할 수 있습니다. 이를 통해 설정 파일의 변경에 따라 코드를 수정하지 않고도 설정 값을 업데이트할 수 있습니다.