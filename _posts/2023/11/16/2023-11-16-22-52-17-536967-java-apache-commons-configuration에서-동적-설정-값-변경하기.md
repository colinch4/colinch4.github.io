---
layout: post
title: "[java] Java Apache Commons Configuration에서 동적 설정 값 변경하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java Apache Commons Configuration은 Java 프로젝트에서 설정 파일을 읽고 관리하는데 도움을 줍니다. 이 라이브러리를 사용하면 설정 파일의 값을 손쉽게 가져오고 변경할 수 있습니다. 이번 포스트에서는 Java Apache Commons Configuration을 사용하여 동적으로 설정 값을 변경하는 방법을 알아보겠습니다.

## 1. Apache Commons Configuration 추가하기

먼저, 프로젝트에서 Apache Commons Configuration 라이브러리를 사용할 수 있도록 추가해야합니다. 이를 위해 Maven이나 Gradle과 같은 의존성 관리 도구를 사용할 수 있습니다. 다음은 Maven을 사용하는 경우 pom.xml 파일에 추가하는 방법입니다.

```xml
<dependency>
  <groupId>commons-configuration</groupId>
  <artifactId>commons-configuration</artifactId>
  <version>2.7</version>
</dependency>
```

## 2. 설정 파일 로드하기

Apache Commons Configuration을 사용하여 설정 파일을 로드해야합니다. 설정 파일은 properties, xml, yaml 등 다양한 형식으로 작성할 수 있습니다. 예를 들어, `config.properties` 파일을 다음과 같이 작성해보겠습니다.

```
database.url=jdbc:mysql://localhost:3306/mydb
database.username=admin
database.password=123456
```

Java 코드에서 다음과 같이 설정 파일을 로드할 수 있습니다.

```java
PropertiesConfiguration config = new PropertiesConfiguration("config.properties");
```

## 3. 설정 값 변경하기

Apache Commons Configuration을 사용하여 설정 값을 변경하려면, `setProperty()` 메서드를 사용하면 됩니다. 예를 들어, `database.password` 값을 변경해보겠습니다.

```java
config.setProperty("database.password", "newPassword");
```

## 4. 변경된 설정 값 저장하기

변경된 설정 값을 설정 파일에 저장하려면, `save()` 메서드를 사용합니다.

```java
config.save();
```

## 5. 변경된 설정 값 확인하기

변경된 설정 값을 다시 읽어오려면, `getString()` 메서드를 사용합니다. 예를 들어, 변경된 `database.password` 값을 확인하려면 다음과 같이 코드를 작성할 수 있습니다.

```java
String newPassword = config.getString("database.password");
System.out.println("New password: " + newPassword);
```

## 6. 전체 코드

아래는 전체 코드 예시입니다:

```java
import org.apache.commons.configuration2.PropertiesConfiguration;

public class ConfigExample {

    public static void main(String[] args) {
        try {
            PropertiesConfiguration config = new PropertiesConfiguration("config.properties");

            // 설정 값 변경
            config.setProperty("database.password", "newPassword");

            // 변경된 설정 값 저장
            config.save();

            // 변경된 설정 값 확인
            String newPassword = config.getString("database.password");
            System.out.println("New password: " + newPassword);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드를 실행하면 `config.properties` 파일에서 `database.password` 값을 변경한 후, 변경된 값과 함께 출력됩니다.

이제 Java Apache Commons Configuration을 사용하여 동적으로 설정 값을 변경하는 방법을 알게 되었습니다. 이를 통해 프로젝트에서 설정 파일을 효과적으로 관리할 수 있습니다.

## 참고 자료
- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)