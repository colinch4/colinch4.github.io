---
layout: post
title: "[java] Java Apache Commons Configuration을 사용한 동적 설정 로딩"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java에서 설정 파일을 로드하고 관리하기 위한 유용한 라이브러리입니다. 이 라이브러리를 사용하면 프로그램이 실행 중에 설정 파일을 동적으로 로드하고 업데이트할 수 있습니다. 이 글에서는 Java Apache Commons Configuration을 사용하여 동적으로 설정 파일을 로딩하는 방법을 알아보겠습니다.

## 설정 파일 준비하기

먼저, 설정 파일을 준비해야합니다. 예를 들어, `config.properties`라는 이름의 설정 파일을 생성하고 다음과 같은 내용을 추가합니다:

```text
name=John Doe
age=30
```

## Maven 종속성 추가하기

Apache Commons Configuration을 사용하기 위해서는 Maven 파일에 다음 종속성을 추가해야합니다:

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

## 설정 파일 로딩하기

이제 Java 코드에서 Apache Commons Configuration을 사용하여 설정 파일을 로딩해보겠습니다. 다음은 예제 코드입니다:

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class ConfigLoader {
    private static final String CONFIG_FILE_PATH = "config.properties";
    private static Configuration config;

    public static void loadConfig() throws ConfigurationException {
        config = new PropertiesConfiguration(CONFIG_FILE_PATH);
    }

    public static String getProperty(String key) {
        return config.getString(key);
    }

    public static void main(String[] args) {
        try {
            loadConfig();
            String name = getProperty("name");
            int age = Integer.parseInt(getProperty("age"));

            System.out.println("Name: " + name);
            System.out.println("Age: " + age);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서는 `ConfigLoader` 클래스에서 설정 파일을 로드하고, `getProperty` 메소드를 통해 설정 값을 가져옵니다. `main` 메소드에서는 설정 파일에서 가져온 값을 출력합니다.

## 코드 실행하기

그리고 코드를 실행하면 다음과 같은 결과가 출력됩니다:

```
Name: John Doe
Age: 30
```

## 결론

Java Apache Commons Configuration을 사용하면 프로그램이 실행 중에 설정 파일을 동적으로 로드하고 업데이트하는 것이 간단해집니다. 이를 통해 설정 파일의 내용을 수정하지 않고도 프로그램의 동작을 변경할 수 있습니다. Apache Commons Configuration은 강력하고 유연한 설정 관리 도구로 사용될 수 있으며, 프로젝트에서 활용해 볼 만한 가치가 있습니다.

더 자세한 내용은 [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)를 참조하십시오.