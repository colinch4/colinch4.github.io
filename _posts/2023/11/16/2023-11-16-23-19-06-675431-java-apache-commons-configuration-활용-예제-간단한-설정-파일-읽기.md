---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 간단한 설정 파일 읽기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 프로젝트에서 설정 파일을 읽고 관리하기 위한 유용한 라이브러리입니다. 이번 예제에서는 Apache Commons Configuration을 사용하여 간단한 설정 파일을 읽어와서 값을 가져오는 방법을 살펴보겠습니다.

## 1. Apache Commons Configuration 추가하기

먼저, Maven이나 Gradle과 같은 빌드 도구를 사용하여 프로젝트에 Apache Commons Configuration을 추가해야 합니다. 이를 위해 아래와 같은 종속성을 추가합니다.

```java
dependencies {
    // Maven 사용시
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-configuration2</artifactId>
        <version>2.7</version>
    </dependency>

    // Gradle 사용시
    implementation 'org.apache.commons:commons-configuration2:2.7'
}
```

## 2. 설정 파일 작성하기

간단한 설정 파일을 작성해보겠습니다. 설정 파일은 일반적으로 XML, Properties, YAML 등의 형식으로 작성할 수 있습니다. 예제에서는 Properties 형식을 사용하겠습니다.

```properties
# config.properties
database.url=jdbc:mysql://localhost:3306/mydb
database.username=myusername
database.password=mypassword
```

## 3. 설정 파일 읽기

Java 코드에서 Apache Commons Configuration을 사용하여 설정 파일을 읽어오는 방법을 살펴보겠습니다. 아래 코드는 설정 파일을 읽어온 후, `database.url`, `database.username`, `database.password`의 값을 가져오는 예제입니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilderProperties;
import org.apache.commons.configuration2.builder.fluent.Parameters;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class ConfigReader {
    public static void main(String[] args) {
        try {
            Parameters parameters = new Parameters();
            FileBasedConfigurationBuilder<FileBasedConfiguration> builder =
                    new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                            .configure(parameters.fileBased()
                                    .setFile(new File("config.properties")));

            Configuration config = builder.getConfiguration();

            String databaseUrl = config.getString("database.url");
            String username = config.getString("database.username");
            String password = config.getString("database.password");

            System.out.println("Database URL: " + databaseUrl);
            System.out.println("Username: " + username);
            System.out.println("Password: " + password);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드를 실행하면 설정 파일에서 읽어온 값을 출력합니다.

```
Database URL: jdbc:mysql://localhost:3306/mydb
Username: myusername
Password: mypassword
```

위 예제에서는 PropertiesConfiguration 클래스를 사용하여 Properties 형식의 설정 파일을 읽어왔습니다. XML이나 다른 형식의 설정 파일을 읽을 때에는 해당 형식에 맞는 Configuration 클래스를 사용하면 됩니다.

이처럼 Apache Commons Configuration을 사용하면 복잡한 설정 파일을 쉽게 읽을 수 있고, 간단한 코드로 설정 값을 가져올 수 있습니다.

## 참고 자료

- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/userguide/index.html)
- [Apache Commons Configuration GitHub](https://github.com/apache/commons-configuration)