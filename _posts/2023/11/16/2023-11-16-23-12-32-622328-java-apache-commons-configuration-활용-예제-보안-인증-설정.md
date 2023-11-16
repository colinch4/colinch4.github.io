---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 보안 인증 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

보안 인증은 웹 응용 프로그램에서 중요한 부분입니다. Apache Commons Configuration 라이브러리를 사용하면 Java에서 간단하게 보안 인증 설정을 구현할 수 있습니다.

## Apache Commons Configuration 라이브러리 추가하기

먼저, 프로젝트에 Apache Commons Configuration 라이브러리를 추가해야 합니다. Maven을 사용한다면, `pom.xml` 파일에 다음 코드를 추가합니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-configuration2</artifactId>
        <version>2.7</version>
    </dependency>
</dependencies>
```

Gradle을 사용한다면, `build.gradle` 파일에 다음 코드를 추가합니다.

```groovy
dependencies {
    implementation 'org.apache.commons:commons-configuration2:2.7'
}
```

## 보안 인증 설정 파일 작성하기

다음으로, 보안 인증 설정을 저장할 파일을 작성해야 합니다. 예를 들어, `security.properties` 파일을 생성하고 다음과 같은 내용을 작성합니다.

```properties
# 보안 인증 설정
security.enabled = true
security.username = admin
security.password = password123
```

## 보안 인증 설정 로드하기

이제 Java 코드에서 보안 인증 설정을 로드할 수 있습니다. 다음은 `SecurityConfig.java` 파일의 예제 코드입니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.ConfigurationBuilderEvent;
import org.apache.commons.configuration2.builder.ConfigurationBuilderListener;
import org.apache.commons.configuration2.builder.fluent.Parameters;

public class SecurityConfig {

    private Configuration config;

    public SecurityConfig(String filePath) {
        Parameters params = new Parameters();
        FileBasedConfigurationBuilder<Configuration> builder = 
            new FileBasedConfigurationBuilder<Configuration>(PropertiesConfiguration.class)
            .configure(params.properties().setFileName(filePath));
        
        builder.addEventListener(ConfigurationBuilderEvent.RESET, 
            new ConfigurationBuilderListener() {
                @Override
                public void configurationReset(ConfigurationBuilderEvent event) {
                    config = event.getConfiguration();
                }
            });
        
        try {
            config = builder.getConfiguration();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public boolean isSecurityEnabled() {
        return config.getBoolean("security.enabled");
    }

    public String getUsername() {
        return config.getString("security.username");
    }

    public String getPassword() {
        return config.getString("security.password");
    }
}
```

위의 예제 코드에서는 `SecurityConfig` 클래스를 사용하여 `security.properties` 파일에서 보안 인증 설정을 로드합니다. `isSecurityEnabled`, `getUsername`, `getPassword` 메소드를 통해 해당 설정 값을 가져올 수 있습니다.

## 보안 인증 설정 사용하기

보안 인증 설정을 사용하는 예제 코드입니다.

```java
public class Main {
    public static void main(String[] args) {
        SecurityConfig securityConfig = new SecurityConfig("security.properties");
        
        if (securityConfig.isSecurityEnabled()) {
            String username = securityConfig.getUsername();
            String password = securityConfig.getPassword();
            
            System.out.println("Username: " + username);
            System.out.println("Password: " + password);
            
            // 인증 로직 구현
        } else {
            System.out.println("보안 인증이 비활성화되었습니다.");
        }
    }
}
```

위의 코드에서는 `SecurityConfig` 클래스를 사용하여 `security.properties` 파일에서 보안 인증 설정을 로드한 후, 해당 설정 값을 사용하여 원하는 작업을 수행합니다.

## 결론

Apache Commons Configuration 라이브러리를 사용하면 Java에서 보안 인증 설정을 간편하게 구현할 수 있습니다. 이 예제를 활용하여 웹 응용 프로그램에서 보안 인증 기능을 구현해보세요.

참고: [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)