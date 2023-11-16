---
layout: post
title: "[java] Java Apache Commons Configuration으로 서버 클라이언트 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java 어플리케이션에서 서버와 클라이언트 간의 설정을 관리하는 것은 중요한 과제입니다. Apache Commons Configuration 라이브러리는 다양한 설정 형식을 지원하며, 이를 사용하여 간단하고 효율적으로 설정을 관리할 수 있습니다.

## Apache Commons Configuration 소개

Apache Commons Configuration은 Java 어플리케이션의 설정 파일을 읽고 작성하는 데 사용되는 라이브러리입니다. 이 라이브러리는 다양한 형식의 설정 파일을 처리할 수 있으며, XML, Properties, YAML 등과 같은 형식을 지원합니다. 또한, 설정 값을 동적으로 변경하고 저장할 수 있는 기능도 제공합니다.

## Maven을 통한 Apache Commons Configuration 라이브러리 추가

먼저, Maven 프로젝트에서 Apache Commons Configuration 라이브러리를 사용하기 위해 의존성을 추가해야 합니다. `pom.xml` 파일에 다음 의존성을 추가해주세요:

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

Maven을 통해 라이브러리를 추가한 후, 프로젝트의 클래스패스에 라이브러리가 포함되어 있어야 합니다.

## 설정 파일 작성과 읽기

Apache Commons Configuration의 주요 기능 중 하나는 설정 파일을 작성하고 읽는 것입니다. 아래는 간단한 예제입니다:

```java
import org.apache.commons.configuration2.XMLConfiguration;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class ConfigManager {

    private XMLConfiguration config;

    public ConfigManager(String configFile) {
        try {
            config = new XMLConfiguration(configFile);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }

    public String getProperty(String key) {
        return config.getString(key);
    }

    public void setProperty(String key, String value) {
        config.setProperty(key, value);
    }

    public void save() {
        try {
            config.save();
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위 예제는 XML 형식의 설정 파일을 읽고 작성하는 ConfigManager 클래스를 보여줍니다. 생성자에서는 설정 파일의 경로를 전달받고, getProperty 메서드를 통해 특정 키의 값을 가져올 수 있습니다. 또한, setProperty 메서드를 사용하여 설정 값을 변경하고, save 메서드를 호출하여 변경 사항을 저장할 수 있습니다.

## 설정 파일 예시

다음은 XML 형식의 설정 파일의 예시입니다:

```xml
<configuration>
    <server>
        <ip>127.0.0.1</ip>
        <port>8080</port>
    </server>
    <client>
        <timeout>5000</timeout>
    </client>
</configuration>
```

XML 설정 파일은 계층 구조로 구성되며, `<configuration>` 요소에 모든 설정 정보가 포함됩니다. 위 예시에서는 `<server>`와 `<client>` 하위 요소를 정의하고, 해당 요소의 속성 값으로 설정 값을 지정합니다.

## 설정 값 사용하기

아래는 ConfigManager 클래스를 사용하여 설정 값을 읽고 변경하는 간단한 예시입니다:

```java
public class Main {

    public static void main(String[] args) {
        ConfigManager configManager = new ConfigManager("config.xml");

        // 서버 IP 주소 가져오기
        String serverIP = configManager.getProperty("server.ip");
        System.out.println("Server IP: " + serverIP);

        // 클라이언트 타임아웃 설정
        configManager.setProperty("client.timeout", "10000");
        configManager.save();
        System.out.println("Client timeout updated.");

    }
}
```

위 예시는 ConfigManager를 생성하고, getProperty 메서드를 사용하여 서버 IP 주소를 가져옵니다. 또한, setProperty 메서드를 사용하여 클라이언트 타임아웃 값을 변경하고, save 메서드를 호출하여 변경 사항을 저장합니다.

## 결론

Apache Commons Configuration 라이브러리는 Java 어플리케이션에서 서버와 클라이언트 설정을 관리하는 데 유용한 도구입니다. 이 라이브러리를 사용하면 다양한 형식의 설정 파일을 쉽게 읽고 쓸 수 있으며, 설정 값을 동적으로 변경할 수 있습니다. 따라서, Apache Commons Configuration은 자바 어플리케이션의 설정 관리에 필수적인 라이브러리입니다.

## 참고 자료

- [Apache Commons Configuration 공식 사이트](https://commons.apache.org/proper/commons-configuration/)