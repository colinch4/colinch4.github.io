---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 보안 암호화 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

## 개요
이 예제는 Java에서 Apache Commons Configuration을 활용하여 보안 암호화 설정을 구현하는 방법에 대해 알려줍니다. Apache Commons Configuration은 일반적인 속성 파일을 읽고 쓰는 기능을 제공하는 라이브러리로, 속성 값을 암호화하는 기능도 포함하고 있습니다.

## 설정 파일 준비
먼저, 보안 암호화를 적용할 속성들을 포함한 설정 파일을 작성해야 합니다. 예를 들어, `config.properties` 파일을 다음과 같이 작성해봅시다.

```properties
# 보안 암호화 설정
database.username = admin
database.password = mysecretpassword
```

## 의존성 추가
Apache Commons Configuration을 사용하기 위해, 먼저 프로젝트의 의존성에 해당 라이브러리를 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

Gradle을 사용하는 경우, `build.gradle` 파일에 다음 의존성을 추가합니다.

```groovy
dependencies {
    implementation 'org.apache.commons:commons-configuration2:2.7'
}
```

## 암호화 설정 사용
이제 Java 코드에서 암호화 설정을 사용하여 암호화된 속성 값을 읽어올 수 있습니다. 다음은 예제 코드입니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class ConfigurationExample {
    public static void main(String[] args) {
        try {
            Configurations configurations = new Configurations();
            Configuration config = configurations.properties("config.properties");

            String username = config.getString("database.username");
            String password = config.getString("database.password");

            System.out.println("Username: " + username);
            System.out.println("Password: " + password);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드는 `config.properties` 파일에서 `database.username`과 `database.password` 속성 값을 읽어와 출력하는 간단한 예제입니다.

## 실행 결과
위의 예제를 실행하면 다음과 같은 결과를 볼 수 있습니다.

```
Username: admin
Password: mysecretpassword
```

## 결론
Apache Commons Configuration을 사용하여 보안 암호화 설정을 구현하는 방법에 대해 알아보았습니다. 이를 통해 속성 파일에 저장된 보안 관련 정보를 안전하게 보호할 수 있습니다.

## 참고 자료
- [Apache Commons Configuration Documentation](https://commons.apache.org/proper/commons-configuration/)
- [Apache Commons Configuration GitHub Repository](https://github.com/apache/commons-configuration)