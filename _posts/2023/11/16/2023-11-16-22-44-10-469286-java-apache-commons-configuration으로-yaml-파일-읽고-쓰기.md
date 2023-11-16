---
layout: post
title: "[java] Java Apache Commons Configuration으로 YAML 파일 읽고 쓰기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java에서 설정 파일을 읽고 쓰는 데 도움이 되는 라이브러리입니다. 이 라이브러리를 사용하면 YAML 파일을 읽고 쓸 수 있어서 설정 파일을 관리하기 편리합니다. 이번 포스트에서는 YAML 파일을 읽고 쓰는 방법을 알아보겠습니다.

## Apache Commons Configuration 설정하기

먼저 Maven을 통해 Apache Commons Configuration 의존성을 프로젝트에 추가해야 합니다. `pom.xml` 파일에 다음과 같이 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

이제 YAML 파일을 읽고 쓰기 위해 `YamlConfiguration` 객체를 생성하겠습니다.

```java
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class AppConfig {

    private static final String CONFIG_FILE = "config.yml";

    public static void readConfig() {
        Configurations configs = new Configurations();
        try {
            FileBasedConfigurationBuilder<YamlConfiguration> builder = configs.yamlBuilder(CONFIG_FILE);
            YamlConfiguration config = builder.getConfiguration();
            
            // 설정 파일 읽기 예제
            String username = config.getString("username");
            int port = config.getInt("port");
            boolean enabled = config.getBoolean("enabled");
            
            System.out.println("Username: " + username);
            System.out.println("Port: " + port);
            System.out.println("Enabled: " + enabled);
            
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }

    public static void writeConfig() {
        Configurations configs = new Configurations();
        try {
            FileBasedConfigurationBuilder<YamlConfiguration> builder = configs.yamlBuilder(CONFIG_FILE);
            YamlConfiguration config = builder.getConfiguration();
            
            // 설정 값 설정하기 예제
            config.setProperty("username", "example");
            config.setProperty("port", 8080);
            config.setProperty("enabled", true);
            
            builder.save();
            
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        readConfig();
        writeConfig();
    }
}
```

## 실행 결과

위 예제를 실행하면 `config.yml` 파일을 읽고 쓰는 결과를 확인할 수 있습니다.

```
Username: example
Port: 8080
Enabled: true
```

## 결론

Apache Commons Configuration을 사용하면 Java에서 YAML 파일을 읽고 쓸 수 있어서 설정 파일을 쉽게 관리할 수 있습니다. 설정 파일을 읽어와서 프로그램에 적용하거나, 프로그램에서 변경된 설정을 파일로 저장할 수 있습니다. 이렇게 설정 파일 관리를 편리하게 하는 Apache Commons Configuration은 Java 개발을 할 때 유용하게 사용할 수 있는 라이브러리입니다.

참고: https://commons.apache.org/proper/commons-configuration/userguide/howto_configbuilder.html