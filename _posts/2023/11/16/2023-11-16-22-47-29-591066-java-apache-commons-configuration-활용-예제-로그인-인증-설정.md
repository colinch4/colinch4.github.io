---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 로그인 인증 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이 예제에서는 Java Apache Commons Configuration 라이브러리를 사용하여 로그인 인증 설정을 관리하는 방법에 대해 알아보겠습니다.

## Apache Commons Configuration

Apache Commons Configuration은 Java에서 설정 파일을 관리하기 위한 라이브러리입니다. 이 라이브러리를 사용하면 XML, 프로퍼티, YAML 등 다양한 형식의 설정 파일을 쉽게 읽고 쓸 수 있습니다.

## 의존성 추가

먼저, Apache Commons Configuration을 프로젝트에 추가해야 합니다. Maven을 사용한다면 `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependencies>
    <dependency>
        <groupId>commons-configuration</groupId>
        <artifactId>commons-configuration</artifactId>
        <version>1.10</version>
    </dependency>
</dependencies>
```

Gradle을 사용한다면 `build.gradle` 파일에 다음 의존성을 추가합니다:

```groovy
dependencies {
    implementation 'commons-configuration:commons-configuration:1.10'
}
```

## 설정 파일 생성

먼저, `config.properties`라는 이름의 설정 파일을 생성합니다. 이 파일은 사용자 인증에 필요한 정보를 저장할 것입니다. 다음은 설정 파일에 들어갈 예시입니다:

```properties
# 사용자 정보
user.username=admin
user.password=1234
```

## 설정 파일 로드

이제 Java 코드에서 설정 파일을 로드하는 부분을 작성해보겠습니다. 다음은 `Configuration` 객체를 생성하고 설정 파일을 로드하는 예제입니다:

```java
import org.apache.commons.configuration.Configuration;
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class LoginConfig {
    private static final String CONFIG_FILE = "config.properties";
    
    private Configuration config;
    
    public LoginConfig() {
        try {
            config = new PropertiesConfiguration(CONFIG_FILE);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
    
    public String getUsername() {
        return config.getString("user.username");
    }
    
    public String getPassword() {
        return config.getString("user.password");
    }
}
```

위 코드에서 `LoginConfig` 클래스는 `Configuration` 객체를 생성하고 설정 파일을 로드하는 역할을 합니다. `getUsername`과 `getPassword` 메소드는 설정 파일에서 사용자 이름과 패스워드를 가져오는 역할을 합니다.

## 사용 예제

이제 설정 파일을 사용하여 로그인 인증을 수행하는 예제를 작성해보겠습니다. 다음은 간단한 예제 코드입니다:

```java
public class LoginAuthenticator {
    private LoginConfig config;
    
    public LoginAuthenticator() {
        config = new LoginConfig();
    }
    
    public boolean authenticate(String username, String password) {
        String storedUsername = config.getUsername();
        String storedPassword = config.getPassword();
        
        return storedUsername.equals(username) && storedPassword.equals(password);
    }
}
```

위 코드에서 `LoginAuthenticator` 클래스는 `LoginConfig` 객체를 사용하여 설정 파일에서 저장된 사용자 이름과 패스워드를 가져와 사용자가 입력한 정보와 비교합니다.

## 결론

Java Apache Commons Configuration을 사용하여 로그인 인증 설정을 관리하는 방법에 대해 알아보았습니다. 이를 통해 설정 파일에서 사용자 정보를 쉽게 로드할 수 있으며, 인증 로직에서 사용할 수 있습니다.

더 자세한 내용은 [Apache Commons Configuration documentation](https://commons.apache.org/proper/commons-configuration/)을 참고하시기 바랍니다.