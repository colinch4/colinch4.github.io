---
layout: post
title: "[java] Java Apache Commons Configuration과 멀티 프로파일 설정 관리"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 어플리케이션에서 설정 파일을 쉽게 로드하고 관리할 수 있는 라이브러리입니다. 이 라이브러리를 사용하여 멀티 프로파일 설정을 관리하는 방법을 살펴보겠습니다.

## Apache Commons Configuration 설정 파일 구성

Apache Commons Configuration을 사용하려면 먼저 설정 파일의 구성을 알아야 합니다. 일반적으로 `.properties`, `.xml`, `.json`과 같은 형식의 파일을 사용할 수 있습니다. 각 파일 형식에 맞는 설정 파일을 작성해야 합니다.

## 설정 파일 로드

Apache Commons Configuration을 사용하여 설정 파일을 로드하는 방법을 살펴보겠습니다. 

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.combined.CombinedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Parameters;

public class ConfigurationLoader {

    public Configuration loadConfiguration(String configFile) throws Exception {
        Parameters params = new Parameters();
        CombinedConfigurationBuilder builder = new CombinedConfigurationBuilder()
                .configure(params.properties().setFileName(configFile));

        return builder.getConfiguration();
    }
}
```

위의 코드는 `ConfigurationLoader`라는 클래스에서 설정 파일을 로드하는 메서드를 보여줍니다. `configFile`는 설정 파일의 경로 및 파일 이름을 나타냅니다. 

## 멀티 프로파일 설정 관리

멀티 프로파일 설정을 관리하기 위해 Apache Commons Configuration을 사용할 수 있습니다. 다음은 프로파일을 바탕으로 설정을 가져오는 예제입니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.PropertiesConfiguration;

public class MultiProfileConfigurationManager {

    private Configuration configuration;

    public MultiProfileConfigurationManager(Configuration configuration) {
        this.configuration = configuration;
    }

    public String getProperty(String key) {
        return configuration.getString(key);
    }

    public String getProperty(String key, String defaultValue) {
        return configuration.getString(key, defaultValue);
    }

    public Integer getIntProperty(String key) {
        return configuration.getInt(key);
    }

    public Integer getIntProperty(String key, Integer defaultValue) {
        return configuration.getInteger(key, defaultValue);
    }
}
```

위의 코드는 `MultiProfileConfigurationManager`라는 클래스에서 프로파일에 따라 설정 값을 가져오는 예입니다. `getProperty`이나 `getIntProperty` 메서드를 사용하여 설정 값을 가져올 수 있습니다.

## 사용 예제

```java
public class Application {

    public static void main(String[] args) {
        try {
            ConfigurationLoader configLoader = new ConfigurationLoader();
            Configuration configuration = configLoader.loadConfiguration("config.properties");
            
            MultiProfileConfigurationManager configManager = new MultiProfileConfigurationManager(configuration);
            
            String userName = configManager.getProperty("user.name");
            Integer age = configManager.getIntProperty("user.age");

            System.out.println("User Name: " + userName);
            System.out.println("User Age: " + age);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위의 예제는 `config.properties` 파일에서 `user.name`과 `user.age` 설정 값을 가져오는 예제입니다. `ConfigurationLoader`를 사용하여 설정 파일을 로드하고, `MultiProfileConfigurationManager`를 사용하여 설정 값을 가져옵니다.

## 결론

Apache Commons Configuration은 Java 어플리케이션에서 설정 파일을 쉽게 로드하고 관리하기 위한 강력한 도구입니다. 멀티 프로파일 설정을 관리하는 경우에도 유용하게 사용할 수 있습니다. 앞서 소개한 예제를 참고하여 자신의 Java 프로젝트에서 설정 파일 관리에 Apache Commons Configuration을 적용해 보세요!

## 참고 자료

- [Apache Commons Configuration](https://commons.apache.org/proper/commons-configuration/)
- [Apache Commons Configuration User Guide](https://commons.apache.org/proper/commons-configuration/userguide/index.html)