---
layout: post
title: "[java] Java Apache Commons Configuration으로 특정 버전 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java로 구현된 설정 관리 라이브러리입니다. 이 라이브러리를 사용하면 XML, Properties, YAML 등 다양한 형식의 설정 파일을 읽고 쓸 수 있습니다.

이번에는 Apache Commons Configuration을 사용하여 특정 버전의 설정을 처리하는 방법에 대해 알아보겠습니다.

## 1. Apache Commons Configuration 추가하기

먼저, 프로젝트에 Apache Commons Configuration을 추가해야 합니다. Maven을 사용한다면 `pom.xml` 파일에 다음 의존성을 추가해주세요.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.8.0</version>
</dependency>
```

Gradle을 사용한다면 `build.gradle` 파일에 다음 의존성을 추가해주세요.

```groovy
implementation 'org.apache.commons:commons-configuration2:2.8.0'
```

## 2. 특정 버전 설정 가져오기

Apache Commons Configuration을 사용하여 특정 버전의 설정을 가져오려면 `HierarchicalConfiguration` 인터페이스를 사용해야 합니다. 이 인터페이스를 구현한 구체적인 클래스는 XML, Properties 등 다양한 형식의 설정 파일을 다룰 수 있습니다.

아래는 XML 형식의 설정 파일에서 특정 버전 설정을 가져오는 예제입니다.

```java
import org.apache.commons.configuration2.HierarchicalConfiguration;
import org.apache.commons.configuration2.XMLConfiguration;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class VersionConfiguration {

    public static void main(String[] args) {
        try {
            XMLConfiguration config = new XMLConfiguration("config.xml");
            HierarchicalConfiguration versionConfig = config.configurationAt("version(0)");

            String version = versionConfig.getString("value");
            System.out.println("Version: " + version);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 예제에서 `config.xml`은 다음과 같은 XML 형식의 설정 파일입니다.

```xml
<config>
    <version>
        <value>1.0.0</value>
    </version>
    <version>
        <value>2.0.0</value>
    </version>
</config>
```

위의 코드는 `config.xml` 파일에서 첫 번째 `<version>` 요소의 `<value>` 값을 가져와서 출력합니다.

## 3. 버전 설정 변경하기

특정 버전의 설정을 가져왔다면 이를 변경하는 것도 가능합니다. `HierarchicalConfiguration` 인터페이스에는 설정 값을 변경하기 위한 다양한 메서드가 제공됩니다.

예를 들어, 위의 예제에서 가져온 첫 번째 버전의 값을 변경해보겠습니다.

```java
import org.apache.commons.configuration2.HierarchicalConfiguration;
import org.apache.commons.configuration2.XMLConfiguration;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class VersionConfiguration {

    public static void main(String[] args) {
        try {
            XMLConfiguration config = new XMLConfiguration("config.xml");
            HierarchicalConfiguration versionConfig = config.configurationAt("version(0)");

            // 기존 값 출력
            String version = versionConfig.getString("value");
            System.out.println("Old Version: " + version);

            // 값 변경
            versionConfig.setProperty("value", "3.0.0");

            // 변경된 값 출력
            String newVersion = versionConfig.getString("value");
            System.out.println("New Version: " + newVersion);

            // 변경된 설정 파일 저장
            config.save();
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드는 `config.xml` 파일의 첫 번째 `<version>` 요소의 `<value>` 값을 변경하고, 변경된 값을 출력합니다. 마지막으로 변경된 설정 파일은 `save()` 메서드를 호출하여 저장됩니다.

## 결론

Apache Commons Configuration을 사용하면 Java에서 특정 버전의 설정을 다루는 것이 간단해집니다. XML, Properties, YAML 등 다양한 형식의 설정 파일을 손쉽게 읽고 쓸 수 있으며, 특정 버전의 설정도 쉽게 가져와서 변경할 수 있습니다.