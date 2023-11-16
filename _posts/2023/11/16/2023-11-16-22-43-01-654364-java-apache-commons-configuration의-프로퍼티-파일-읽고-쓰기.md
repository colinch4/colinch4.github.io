---
layout: post
title: "[java] Java Apache Commons Configuration의 프로퍼티 파일 읽고 쓰기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java에서 설정 파일을 읽고 쓰는데 사용할 수 있는 유용한 라이브러리입니다. 이 라이브러리를 사용하면 손쉽게 프로퍼티 파일을 읽고 쓸 수 있으며, 설정 값의 변경에 따라 애플리케이션의 동작을 조정할 수 있습니다.

## 의존성 추가하기

먼저 Apache Commons Configuration을 사용하기 위해 의존성을 추가해야 합니다. Maven을 사용한다면 `pom.xml` 파일에 아래의 의존성을 추가하세요:

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

Gradle을 사용한다면 `build.gradle` 파일에 아래의 의존성을 추가하세요:

```groovy
dependencies {
    implementation 'commons-configuration:commons-configuration:1.10'
}
```

## 프로퍼티 파일 읽기

Apache Commons Configuration을 사용하여 프로퍼티 파일을 읽는 방법은 매우 간단합니다. 다음과 같은 코드를 사용하면 됩니다:

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class ConfigurationApp {
    public static void main(String[] args) {
        try {
            PropertiesConfiguration config = new PropertiesConfiguration("config.properties");
            
            // 특정 키의 값을 가져옵니다.
            String value = config.getString("key");
            
            System.out.println("Value: " + value);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드는 `config.properties` 파일에서 "key"라는 키의 값(value)을 읽어와 출력합니다. 별도의 예외 처리가 필요하므로, `ConfigurationException`을 처리하는 `try-catch` 구문을 사용합니다.

## 프로퍼티 파일 쓰기

프로퍼티 파일을 쓰기 위해서는 `PropertiesConfiguration` 객체를 사용하여 키-값 쌍을 추가하면 됩니다. 다음은 예제 코드입니다:

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class ConfigurationApp {
    public static void main(String[] args) {
        try {
            PropertiesConfiguration config = new PropertiesConfiguration("config.properties");
            
            // 키-값 쌍 추가하기
            config.addProperty("newKey", "newValue");
            
            // 변경사항 저장하기
            config.save();
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드는 `config.properties` 파일에 "newKey"라는 키와 "newValue"라는 값을 추가하고, 변경 사항을 저장합니다. `save()` 메소드를 호출하여 변경사항이 파일에 적용되도록 합니다.

## 결론

이제 Java Apache Commons Configuration을 사용하여 프로퍼티 파일을 읽고 쓰는 방법을 알게 되었습니다. 이를 활용하여 설정 파일에서 필요한 값들을 쉽게 읽어와서 Java 애플리케이션의 동작을 조정할 수 있습니다.

더 자세한 내용은 [Apache Commons Configuration](https://commons.apache.org/proper/commons-configuration/) 공식 문서를 참조하세요.