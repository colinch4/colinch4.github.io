---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 사용자 프로필 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

자바 개발 프로젝트에서 자주 사용되는 설정 파일을 관리하기 위해 Apache Commons Configuration 라이브러리를 사용할 수 있습니다. 이 라이브러리는 다양한 형식의 설정 파일을 읽고 쓰는 기능을 제공하여 편리하게 설정 관리를 할 수 있습니다.

이 예제에서는 사용자 프로필 설정을 위한 간단한 예제를 소개하겠습니다. 사용자 프로필은 이름, 나이, 이메일 주소 등의 정보를 보유하고 있습니다.

## Apache Commons Configuration 라이브러리 추가

먼저, Maven 또는 Gradle과 같은 의존성 관리 도구를 사용하여 Apache Commons Configuration 라이브러리를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음과 같은 의존성을 추가합니다:

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

Gradle을 사용하는 경우, `build.gradle` 파일의 `dependencies` 섹션에 다음과 같이 의존성을 추가합니다:

```groovy
compile 'commons-configuration:commons-configuration:1.10'
```

## 사용자 프로필 설정 파일 생성

먼저, 사용자 프로필 설정을 저장할 `user-profile.properties` 파일을 프로젝트의 리소스 디렉터리에 생성합니다. 이 파일에는 다음과 같이 사용자 정보를 설정합니다:

```properties
user.name=John
user.age=30
user.email=john@example.com
```

## 사용자 프로필 읽기

다음으로, 위에서 생성한 설정 파일에서 사용자 프로필을 읽어오는 Java 코드를 작성해보겠습니다:

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class UserProfileReader {
    
    public static void main(String[] args) {
        try {
            PropertiesConfiguration config = new PropertiesConfiguration("user-profile.properties");
            
            String name = config.getString("user.name");
            int age = config.getInt("user.age");
            String email = config.getString("user.email");
            
            System.out.println("Name: " + name);
            System.out.println("Age: " + age);
            System.out.println("Email: " + email);
        } catch (ConfigurationException e) {
            System.err.println("Error reading user profile configuration");
            e.printStackTrace();
        }
    }
}
```

위의 예제 코드에서는 `PropertiesConfiguration` 클래스를 사용하여 `user-profile.properties` 파일을 읽어옵니다. `getString` 또는 `getInt` 메소드를 사용하여 각각 문자열과 정수 값으로 설정값을 가져올 수 있습니다. 이후, 설정 값을 출력합니다.

## 사용자 프로필 수정

사용자 프로필을 수정하려면 `PropertiesConfiguration` 객체에서 설정 값을 변경한 후, `save` 메소드를 호출하여 변경 사항을 설정 파일에 저장해야 합니다. 아래는 사용자 이메일을 수정하는 예제입니다:

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class UserProfileModifier {
    
    public static void main(String[] args) {
        try {
            PropertiesConfiguration config = new PropertiesConfiguration("user-profile.properties");
            
            config.setProperty("user.email", "newemail@example.com");
            config.save();
            
            System.out.println("User profile updated successfully");
        } catch (ConfigurationException e) {
            System.err.println("Error modifying user profile configuration");
            e.printStackTrace();
        }
    }
}
```

위의 예제 코드에서는 `setProperty` 메소드를 사용하여 `user.email` 설정 값을 변경하고, `save` 메소드를 호출하여 변경 사항을 저장합니다.

## 결론

Apache Commons Configuration 라이브러리는 자바 프로젝트에서 설정 파일을 관리하는 데 유용한 도구입니다. 이 예제에서는 사용자 프로필 설정에 대한 기본적인 읽기와 수정하는 방법을 소개했습니다. 이를 활용하여 프로젝트에서 설정 파일을 효율적으로 관리할 수 있습니다.

---

참고 문서:
- [Apache Commons Configuration 공식 사이트](https://commons.apache.org/proper/commons-configuration/)
- [Apache Commons Configuration API 문서](https://commons.apache.org/proper/commons-configuration/javadocs/v1.10/apidocs/)