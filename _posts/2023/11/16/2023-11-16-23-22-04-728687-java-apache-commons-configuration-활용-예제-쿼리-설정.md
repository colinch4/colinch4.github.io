---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 쿼리 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 프로젝트에서 설정 파일을 읽고 조작하기 위한 라이브러리입니다. 이 라이브러리를 사용하면 쉽게 프로퍼티 파일, XML 파일 또는 다른 형식의 설정 파일을 읽고 해당 설정을 사용할 수 있습니다.

이 예제에서는 Apache Commons Configuration을 사용하여 데이터베이스 쿼리를 설정하는 방법을 알아보겠습니다. 데이터베이스 쿼리는 프로젝트에서 자주 사용되는 중요한 구성 요소이기 때문에 설정 파일에서 동적으로 읽을 수 있는 것이 유용합니다.

## 1. Maven 종속성 추가

Apache Commons Configuration 라이브러리를 프로젝트에 추가하기 위해 `pom.xml` 파일에 다음 종속성을 추가합니다:

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-configuration2</artifactId>
        <version>2.7</version>
    </dependency>
</dependencies>
```

Maven을 사용하지 않는 경우, 다운로드 링크(https://commons.apache.org/proper/commons-configuration/download_configuration.cgi)에서 JAR 파일을 수동으로 다운로드하고 프로젝트에 추가해야 합니다.

## 2. 설정 파일 준비

데이터베이스 쿼리를 설정하기 위해 `queries.properties`라는 이름의 프로퍼티 파일을 생성해야 합니다. 이 파일은 다음과 같은 내용을 가지고 있습니다:

```properties
user.select.all=SELECT * FROM users
user.select.one=SELECT * FROM users WHERE id = :id
user.insert=INSERT INTO users (name, email) VALUES (:name, :email)
user.update=UPDATE users SET name = :name, email = :email WHERE id = :id
user.delete=DELETE FROM users WHERE id = :id
```

위의 예제에서 `:id`, `:name`, `:email`와 같은 플레이스홀더를 사용하여 동적인 값으로 쿼리를 조작할 수 있습니다.

## 3. 코드 구현

Apache Commons Configuration을 사용하여 `queries.properties` 파일을 로드하고, 쿼리 값을 동적으로 읽어와서 사용하는 코드를 작성해보겠습니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class QueryConfigExample {
    public static void main(String[] args) {
        try {
            Configurations configs = new Configurations();
            Configuration config = configs.properties("queries.properties");

            String selectAllUsersQuery = config.getString("user.select.all");
            String selectUserByIdQuery = config.getString("user.select.one");
            String insertUserQuery = config.getString("user.insert");
            String updateUserQuery = config.getString("user.update");
            String deleteUserQuery = config.getString("user.delete");

            System.out.println("selectAllUsersQuery: " + selectAllUsersQuery);
            System.out.println("selectUserByIdQuery: " + selectUserByIdQuery);
            System.out.println("insertUserQuery: " + insertUserQuery);
            System.out.println("updateUserQuery: " + updateUserQuery);
            System.out.println("deleteUserQuery: " + deleteUserQuery);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서 `queries.properties` 파일은 Configurations 객체를 사용하여 로드됩니다. 그런 다음 Configuration 객체에서 `getString()` 메소드를 사용하여 특정 쿼리 값을 읽어올 수 있습니다. 해당 쿼리 값은 변수에 저장되고 출력됩니다.

## 결론

Apache Commons Configuration을 사용하면 Java 프로젝트에서 설정 파일을 쉽게 읽고 조작할 수 있습니다. 이 예제에서는 데이터베이스 쿼리를 설정 파일에서 동적으로 읽어오는 방법을 살펴보았습니다. 이를 통해 쿼리를 손쉽게 조작하고 변경할 수 있어 프로젝트 유지 보수에 큰 도움이 될 것입니다.

## 참고 자료

- [Apache Commons Configuration 다운로드 페이지](https://commons.apache.org/proper/commons-configuration/download_configuration.cgi)
- [Apache Commons Configuration 소개 문서](https://commons.apache.org/proper/commons-configuration/userguide/user_guide.html)