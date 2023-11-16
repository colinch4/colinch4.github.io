---
layout: post
title: "[java] Java Apache Commons Configuration과 캐시 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 개발자들이 구성 설정 파일을 쉽게 사용할 수 있도록 도와주는 라이브러리입니다. 이 라이브러리를 사용하면 XML, 프로퍼티, YAML 등 다양한 유형의 구성 파일을 읽고 쓸 수 있습니다.

## Apache Commons Configuration 설치

Apache Commons Configuration을 사용하기 위해 먼저 의존성을 추가해야 합니다. Maven을 사용하는 경우 `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependencies>
    <dependency>
        <groupId>commons-configuration</groupId>
        <artifactId>commons-configuration</artifactId>
        <version>1.10</version>
    </dependency>
</dependencies>
```

## 기본 사용법

Apache Commons Configuration을 사용하여 구성 설정 파일을 로드하고 값을 가져올 수 있습니다. 예를 들어, `config.xml` 파일에 다음과 같은 내용이 있다고 가정해보겠습니다:

```xml
<configuration>
    <app>
        <name>My App</name>
        <version>1.0</version>
    </app>
    <database>
        <url>jdbc:mysql://localhost:3306/mydb</url>
        <username>admin</username>
        <password>password</password>
    </database>
</configuration>
```

Java 코드에서 아래와 같이 구성 파일을 로드하고 값을 가져올 수 있습니다:

```java
import org.apache.commons.configuration2.XMLConfiguration;
import org.apache.commons.configuration2.builder.fluent.Configurations;

public class AppConfig {
    private static final String CONFIG_FILE = "config.xml";
    
    public static void main(String[] args) {
        try {
            Configurations configs = new Configurations();
            XMLConfiguration config = configs.xml(CONFIG_FILE);
            
            String appName = config.getString("app.name");
            String dbUrl = config.getString("database.url");
            String dbUsername = config.getString("database.username");
            String dbPassword = config.getString("database.password");
            
            System.out.println("App Name: " + appName);
            System.out.println("DB URL: " + dbUrl);
            System.out.println("DB Username: " + dbUsername);
            System.out.println("DB Password: " + dbPassword);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

실행 결과는 다음과 같을 것입니다:

```
App Name: My App
DB URL: jdbc:mysql://localhost:3306/mydb
DB Username: admin
DB Password: password
```

## 캐시 설정

Apache Commons Configuration에서 캐시를 사용하여 구성 설정 파일의 성능을 향상시킬 수도 있습니다. 기본적으로 캐시는 비활성화되어 있지만, 필요한 경우 캐시를 설정하여 다시 로드할 필요 없이 값을 가져올 수 있습니다.

```java
import org.apache.commons.configuration2.ConfigurationUtils;
import org.apache.commons.configuration2.XMLConfiguration;
import org.apache.commons.configuration2.builder.fluent.Configurations;

public class AppConfig {
    private static final String CONFIG_FILE = "config.xml";
    
    public static void main(String[] args) {
        try {
            Configurations configs = new Configurations();
            
            // 캐시를 사용하여 구성 파일 로드
            XMLConfiguration config = configs.xml(CONFIG_FILE);
            ConfigurationUtils.dump(config, System.out);
            
            // 캐시된 값 가져오기
            String appName = config.getString("app.name");
            String dbUrl = config.getString("database.url");
            String dbUsername = config.getString("database.username");
            String dbPassword = config.getString("database.password");
            
            System.out.println("App Name: " + appName);
            System.out.println("DB URL: " + dbUrl);
            System.out.println("DB Username: " + dbUsername);
            System.out.println("DB Password: " + dbPassword);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

이제 구성 파일은 처음에만 로드되고, 이후에는 메모리에 저장된 캐시 값을 사용합니다.

## 결론

Apache Commons Configuration은 구성 설정 파일을 사용할 때 편리한 기능을 제공하는 유용한 라이브러리입니다. 캐시 설정을 통해 성능을 향상시킬 수 있으므로, 애플리케이션의 구성 파일을 처리할 때 이 라이브러리를 고려해보세요.

---

참고: 
- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/userguide/howto_xml.html)
- [Maven Central Repository](https://search.maven.org/artifact/commons-configuration/commons-configuration/1.10/jar)