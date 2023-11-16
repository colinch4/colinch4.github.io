---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 테마 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java에서 환경 설정 정보를 읽고 관리하기 위한 유용한 라이브러리입니다. 이 예제에서는 Apache Commons Configuration을 사용하여 Java 애플리케이션에서 사용할 테마를 동적으로 설정하는 방법을 알아보겠습니다.

## 1. 의존성 추가

먼저, 프로젝트의 Maven 또는 Gradle 구성 파일에 Apache Commons Configuration의 의존성을 추가해야 합니다. Maven을 사용하는 경우 `pom.xml` 파일에 다음 의존성을 추가합니다.

```xml
<dependencies>
  <dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
  </dependency>
</dependencies>
```

Gradle을 사용하는 경우 `build.gradle` 파일에 다음 의존성을 추가합니다.

```groovy
dependencies {
    implementation 'org.apache.commons:commons-configuration2:2.7'
}
```

## 2. 테마 설정 파일 생성

테마 설정을 위해 별도의 XML 파일을 작성해야 합니다. 테마 설정 파일은 다음과 같은 형식을 갖습니다.

```xml
<themes>
  <theme>
    <name>theme1</name>
    <background>#ffffff</background>
    <textColor>#000000</textColor>
  </theme>
  <theme>
    <name>theme2</name>
    <background>#000000</background>
    <textColor>#ffffff</textColor>
  </theme>
</themes>
```

XML 파일에서는 여러 개의 테마를 정의하고, 각 테마에 대한 이름, 배경색 및 텍스트 색상을 설정합니다.

## 3. 테마 설정 로직 구현

다음으로, 테마 설정 로직을 구현해 보겠습니다.

```java
import org.apache.commons.configuration2.XMLConfiguration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class ThemeManager {

    private static final String CONFIG_FILE_PATH = "themes.xml";

    private static final String THEME_PREFIX = "theme.";

    private XMLConfiguration configuration;

    public ThemeManager() throws ConfigurationException {
        Configurations configurations = new Configurations();
        FileBasedConfigurationBuilder<XMLConfiguration> builder = configurations.xmlBuilder(CONFIG_FILE_PATH);
        configuration = builder.getConfiguration();
    }

    public void setTheme(String themeName) {
        String themeKey = THEME_PREFIX + themeName;
        String background = configuration.getString(themeKey + ".background", "#ffffff");
        String textColor = configuration.getString(themeKey + ".textColor", "#000000");

        // 테마 설정 로직을 구현한다
        // 배경색과 텍스트 색상을 적용한다
    }

}
```

위의 예제에서 `ThemeManager` 클래스는 `themes.xml` 파일로부터 테마 정보를 읽어와서 테마를 설정하는 역할을 합니다. `setTheme` 메소드를 통해 테마를 적용할 수 있습니다.

## 4. 테마 설정 사용 예제

테마 설정을 사용하는 예제를 살펴보겠습니다.

```java
public class MyApp {
    
    public static void main(String[] args) {
        try {
            ThemeManager themeManager = new ThemeManager();
            themeManager.setTheme("theme1");
            
            // 애플리케이션 로직을 구현한다
            // 테마 설정에 따른 UI 또는 렌더링을 수행한다
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
    
}
```

위의 예제에서 `MyApp` 클래스에서는 `ThemeManager`를 사용하여 "theme1" 테마를 설정하고, 이에 따른 애플리케이션 로직을 구현하고 실행합니다.

위의 예제를 실행하면 `themes.xml` 파일에서 설정된 테마 정보를 읽어와 테마를 동적으로 설정할 수 있습니다.

## 결론

이 예제에서는 Apache Commons Configuration을 사용하여 Java 애플리케이션에서 테마 설정을 동적으로 관리하는 방법을 알아보았습니다. Apache Commons Configuration은 편리한 기능을 제공하므로 복잡한 설정 정보를 간편하게 관리할 수 있습니다. 자세한 내용은 [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)를 참조하시기 바랍니다.