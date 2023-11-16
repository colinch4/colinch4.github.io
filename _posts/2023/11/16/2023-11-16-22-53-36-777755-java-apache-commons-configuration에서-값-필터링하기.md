---
layout: post
title: "[java] Java Apache Commons Configuration에서 값 필터링하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java에서 환경 설정 파일을 읽고 관리하기 위한 유용한 라이브러리입니다. 이 라이브러리는 다양한 유형의 환경 설정 파일을 지원하며, 프로퍼티 값들을 손쉽게 가져올 수 있습니다. 이번 포스트에서는 Java Apache Commons Configuration에서 값 필터링하는 방법에 대해 알아보겠습니다.

## 필터 생성하기

값을 필터링하기 위해서는 `org.apache.commons.configuration2.AbstractConfiguration` 클래스를 확장한 프로퍼티 필터 클래스를 생성해야 합니다. 필터 클래스는 `org.apache.commons.configuration2.builder.fluent.Configurations` 클래스의 인스턴스를 사용하여 환경 설정 파일을 로드합니다. 아래는 필터 클래스의 예시입니다.

```java
import org.apache.commons.configuration2.AbstractConfiguration;
import org.apache.commons.configuration2.builder.BasicConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;
import org.apache.commons.configuration2.io.FileHandler;
import org.apache.commons.configuration2.PropertiesConfiguration;

public class PropertyFilterConfiguration extends AbstractConfiguration {

    private PropertiesConfiguration config;

    public PropertyFilterConfiguration(String filePath) throws ConfigurationException {
        config = new Configurations().properties(filePath);
    }

    @Override
    public Object getProperty(String key) {
        // 값 필터링 로직 구현
        // 예를 들어, 특정 값을 제외하고 반환하거나, 특정 값을 수정한 후 반환하는 등의 작업을 할 수 있음
        return config.getProperty(key);
    }
}
```

위에서 생성한 `PropertyFilterConfiguration` 클래스는 `AbstractConfiguration`를 확장하며, 특정 환경 설정 파일을 로드하여 프로퍼티 값을 필터링하는 역할을 합니다.

## 값 필터링하기

값을 필터링하려는 환경 설정 파일의 경로를 지정하여 `PropertyFilterConfiguration` 클래스를 생성한 후, `getProperty` 메서드를 오버라이드하여 필터링 로직을 구현합니다.

```java
try {
    PropertyFilterConfiguration config = new PropertyFilterConfiguration("config.properties");
    String value = (String) config.getProperty("key");
    System.out.println("Filtered Value: " + value);
} catch (ConfigurationException e) {
    e.printStackTrace();
}
```

위의 코드에서는 "config.properties" 환경 설정 파일에서 "key"라는 키에 해당하는 프로퍼티 값을 가져옵니다. 필터링 로직에서 값을 필터링하거나 수정하는 작업을 수행한 후, 최종적으로 필터링된 값만 반환하게 됩니다.

## 결론

Java Apache Commons Configuration을 사용하면 환경 설정 파일에서 필요한 값을 가져오고 필터링하는 작업을 효율적으로 수행할 수 있습니다. 필터링된 값을 사용하여 애플리케이션을 유연하게 구성하고 관리할 수 있습니다.

참고 문서:
- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)
- [Apache Commons Configuration GitHub 저장소](https://github.com/apache/commons-configuration)