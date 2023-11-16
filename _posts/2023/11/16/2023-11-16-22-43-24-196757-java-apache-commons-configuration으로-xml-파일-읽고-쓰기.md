---
layout: post
title: "[java] Java Apache Commons Configuration으로 XML 파일 읽고 쓰기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java에서 XML 파일을 읽고 쓰는 작업은 Apache Commons Configuration 라이브러리를 사용하여 간단하게 수행할 수 있습니다. 이 라이브러리는 다양한 설정 파일 형식을 다룰 수 있도록 해줍니다.

## Apache Commons Configuration 라이브러리 추가하기

먼저, Maven 프로젝트를 사용하는 경우 pom.xml 파일에 다음 종속성을 추가해야 합니다.

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

Gradle 프로젝트를 사용하는 경우 build.gradle 파일에 다음 종속성을 추가해야 합니다.

```groovy
dependencies {
    implementation 'commons-configuration:commons-configuration:1.10'
}
```

## XML 파일 읽기

아래는 예제 XML 파일(config.xml)의 내용입니다.

```xml
<configuration>
    <database>
        <host>localhost</host>
        <port>3306</port>
        <username>admin</username>
        <password>password123</password>
    </database>
</configuration>
```

다음은 Java 코드에서 XML 파일을 읽는 방법입니다.

```java
import org.apache.commons.configuration2.XMLConfiguration;
import org.apache.commons.configuration2.builder.fluent.Configurations;

public class XmlReaderExample {
    public static void main(String[] args) {
        Configurations configs = new Configurations();
        try {
            XMLConfiguration config = configs.xml("config.xml");
            
            // XML 파일에서 원하는 값을 읽어옵니다.
            String host = config.getString("database.host");
            int port = config.getInt("database.port");
            String username = config.getString("database.username");
            String password = config.getString("database.password");
            
            // 읽어온 값 출력
            System.out.println("Host: " + host);
            System.out.println("Port: " + port);
            System.out.println("Username: " + username);
            System.out.println("Password: " + password);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## XML 파일 쓰기

이제 XML 파일에 새로운 값을 추가하거나 기존 값을 수정하는 방법을 살펴보겠습니다.

```java
import org.apache.commons.configuration2.XMLConfiguration;
import org.apache.commons.configuration2.builder.fluent.Configurations;

public class XmlWriterExample {
    public static void main(String[] args) {
        Configurations configs = new Configurations();
        try {
            XMLConfiguration config = configs.xml("config.xml");
            
            // XML 파일에 새로운 값을 추가합니다.
            config.setProperty("database.host", "newhost.com");
            config.setProperty("database.port", "3307");
            
            // XML 파일에 변경된 값을 저장합니다.
            configs.save(config, "config.xml");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드는 기존 XML 파일의 "database.host"와 "database.port" 값을 변경하여 저장하는 예제입니다.

Apache Commons Configuration을 사용하면 Java에서 XML 파일을 손쉽게 읽고 쓸 수 있습니다. XML 파일을 프로그램의 설정 파일로 사용하는 경우에 유용하게 활용할 수 있습니다.

자세한 내용은 [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)를 참고하시기 바랍니다.