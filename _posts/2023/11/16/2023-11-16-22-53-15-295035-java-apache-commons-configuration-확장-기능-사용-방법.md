---
layout: post
title: "[java] Java Apache Commons Configuration 확장 기능 사용 방법"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java에서 애플리케이션 구성을 관리할 때 Apache Commons Configuration을 사용하는 것은 매우 일반적입니다. 그러나 기본 기능 이외에도 Commons Configuration은 확장 기능을 제공합니다. 이 기능을 사용하면 더욱 편리하게 구성을 관리할 수 있습니다.

이 포스트에서는 Apache Commons Configuration을 사용하여 애플리케이션 구성을 확장하는 방법을 알아보겠습니다.

## 1. 의존성 추가

먼저 Maven 또는 Gradle과 같은 빌드 도구를 사용하여 프로젝트에 Apache Commons Configuration 라이브러리를 추가해야 합니다. 아래는 Maven을 사용하는 경우의 의존성 추가 방법입니다.

```xml
<dependencies>
    <dependency>
        <groupId>commons-configuration</groupId>
        <artifactId>commons-configuration</artifactId>
        <version>2.7</version>
    </dependency>
</dependencies>
```

Gradle을 사용하는 경우 다음과 같이 의존성을 추가할 수 있습니다.

```groovy
dependencies {
    implementation 'commons-configuration:commons-configuration:2.7'
}
```

## 2. PropertiesConfiguration 사용하기

Apache Commons Configuration의 기본 구성 요소 중 하나인 `PropertiesConfiguration`을 사용하여 구성 파일을 읽고 수정할 수 있습니다. `PropertiesConfiguration`은 Java의 `Properties` 파일과 같은 형식으로 구성을 저장합니다.

```java
import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class AppConfig {
    private static final String CONFIG_FILE = "app.config";
    private PropertiesConfiguration config;

    public AppConfig() {
        try {
            config = new PropertiesConfiguration(CONFIG_FILE);
            config.load();
        } catch (ConfigurationException e) {
            // 예외 처리
        }
    }

    public String getConfigValue(String key) {
        return config.getString(key);
    }

    public void setConfigValue(String key, String value) {
        config.setProperty(key, value);
        // 변경 사항 저장
        try {
            config.save();
        } catch (ConfigurationException e) {
            // 예외 처리
        }
    }
}
```

위의 예제에서 `PropertiesConfiguration` 클래스의 인스턴스를 생성하고, `load()` 메서드로 구성 파일을 읽어옵니다. `getConfigValue()` 메서드로 특정 키에 해당하는 구성 값을 가져올 수 있으며, `setConfigValue()` 메서드로 구성값을 설정할 수 있습니다.

## 3. XMLConfiguration 사용하기

만약 XML 형식의 구성 파일을 사용해야 한다면, `XMLConfiguration` 클래스를 사용할 수 있습니다. `XMLConfiguration`은 XML 형식의 구성을 저장하고 관리합니다.

```java
import org.apache.commons.configuration2.XMLConfiguration;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class AppConfig {
    private static final String CONFIG_FILE = "app.config";
    private XMLConfiguration config;

    public AppConfig() {
        try {
            config = new XMLConfiguration(CONFIG_FILE);
            config.load();
        } catch (ConfigurationException e) {
            // 예외 처리
        }
    }

    public String getConfigValue(String key) {
        return config.getString(key);
    }

    public void setConfigValue(String key, String value) {
        config.setProperty(key, value);
        // 변경 사항 저장
        try {
            config.save();
        } catch (ConfigurationException e) {
            // 예외 처리
        }
    }
}
```

위의 예제에서 `XMLConfiguration` 클래스를 사용하여 XML 구성 파일을 읽고 수정합니다. 사용법은 `PropertiesConfiguration`과 동일합니다.

## 4. 다른 구성 포맷 사용하기

Apache Commons Configuration은 `PropertiesConfiguration`와 `XMLConfiguration` 외에도 다양한 구성 포맷을 지원합니다. CSV, JSON, YAML 등 다양한 포맷으로 구성 파일을 읽고 쓸 수 있습니다. 필요한 구성 포맷에 맞춰 `XXXConfiguration`을 사용하면 됩니다.

## 결론

Java에서 Apache Commons Configuration을 사용하여 구성 파일을 관리하는 방법을 살펴보았습니다. `PropertiesConfiguration`과 `XMLConfiguration`을 사용하여 간단하게 구성 값을 읽고 수정할 수 있습니다. 또한 다양한 구성 포맷을 지원하므로 필요에 따라 적절한 `XXXConfiguration` 클래스를 사용하면 됩니다.

Apache Commons Configuration의 확장 기능을 효과적으로 활용하여 애플리케이션의 구성 관리를 더욱 편리하게 할 수 있습니다.

참고:
- [Apache Commons Configuration User Guide](https://commons.apache.org/proper/commons-configuration/userguide/index.html)