---
layout: post
title: "[java] Java Apache Commons Configuration으로 JSON 파일 읽고 쓰기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java 어플리케이션에서 설정 파일을 다루는 데 도움을 주는 라이브러리입니다. 이 라이브러리를 통해 JSON 형식의 파일을 읽고 쓸 수 있습니다. 이번 글에서는 Java Apache Commons Configuration을 사용하여 JSON 파일을 읽고 쓰는 방법을 알아보겠습니다.

## 1. Apache Commons Configuration 라이브러리 추가

먼저, 프로젝트에 Apache Commons Configuration 라이브러리를 추가해야 합니다. Maven 프로젝트인 경우, pom.xml 파일에 다음 의존성을 추가합니다:

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>XXX</version>
</dependency>
```

`XXX` 부분은 사용하는 라이브러리의 버전에 따라 변경해야 합니다.

## 2. JSON 파일 읽기

JSON 파일을 읽기 위해서는 `JSONConfiguration` 객체를 만들어야 합니다. `JSONConfiguration`은 Apache Commons Configuration의 `Configuration`을 구현한 클래스입니다.

다음은 JSON 파일을 읽어와서 값들을 가져오는 예제입니다:

```java
import org.apache.commons.configuration2.JSONConfiguration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class JsonConfigReader {
    public static void main(String[] args) {
        try {
            Configurations configs = new Configurations();
            JSONConfiguration config = configs.json("config.json");

            String value = config.getString("key");
            System.out.println("Value: " + value);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서 `config.json`은 읽어올 JSON 파일의 경로입니다. `getString("key")` 메소드를 사용하여 JSON 파일에서 특정 키에 해당하는 값을 가져올 수 있습니다.

## 3. JSON 파일 쓰기

JSON 파일에 값을 쓰기 위해서는 `JSONConfiguration` 객체를 만들고 값을 설정한 후에 저장해야 합니다.

다음은 JSON 파일에 값을 쓰는 예제입니다:

```java
import org.apache.commons.configuration2.JSONConfiguration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class JsonConfigWriter {
    public static void main(String[] args) {
        try {
            Configurations configs = new Configurations();
            JSONConfiguration config = configs.json("config.json");

            config.setProperty("key", "value");
            configs.save(config, "config.json");
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서 `config.setProperty("key", "value")` 메소드를 사용하여 JSON 파일에 값을 설정할 수 있습니다. 

마지막으로, `configs.save(config, "config.json")` 메소드로 설정한 값을 JSON 파일에 저장합니다.

## 결론

이번 글에서는 Java Apache Commons Configuration을 사용하여 JSON 파일을 읽고 쓰는 방법을 알아보았습니다. 이 라이브러리를 사용하면 간편하게 JSON 파일을 다룰 수 있으며, 설정 파일 관리에 유용합니다.

더 자세한 사용법은 Apache Commons Configuration의 [공식 문서](https://commons.apache.org/proper/commons-configuration/userguide/howto_properties.html)를 참고하시기 바랍니다.