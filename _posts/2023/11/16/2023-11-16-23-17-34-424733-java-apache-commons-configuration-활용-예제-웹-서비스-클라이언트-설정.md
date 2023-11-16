---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 웹 서비스 클라이언트 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이 예제는 Java Apache Commons Configuration 라이브러리를 사용하여 웹 서비스 클라이언트 설정을 관리하는 방법을 보여줍니다.

## Apache Commons Configuration 소개

Apache Commons Configuration은 설정 데이터를 로드하고 구성하는 데 사용할 수 있는 유연하고 확장 가능한 라이브러리입니다. 이 라이브러리는 다양한 형식의 설정 파일 (프로퍼티, XML, JSON 등)을 지원하며, 설정 데이터를 읽고 쓰고 업데이트하는 기능을 제공합니다.

## 웹 서비스 클라이언트 설정 예제

다음은 웹 서비스 클라이언트 설정 파일을 관리하는 예제입니다.

### 1. Maven 종속성 추가

먼저, Apache Commons Configuration 라이브러리를 Maven 프로젝트의 종속성에 추가해야 합니다. `pom.xml` 파일에 다음 종속성을 추가합니다:

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>2.7</version>
</dependency>
```

### 2. 설정 파일 생성

다음으로, 웹 서비스 클라이언트 설정을 담은 `config.properties` 파일을 생성합니다. 예를 들어, 다음과 같은 설정을 가진 파일을 생성하세요:

```properties
# 웹 서비스 클라이언트 설정
webservice.url=http://example.com
webservice.timeout=5000
webservice.retry.maxAttempts=3
```

### 3. 설정 로드 및 사용

이제 Java 코드에서 설정을 로드하고 사용하는 방법을 살펴봅시다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class WebServiceClient {
    private static final String CONFIG_FILE = "config.properties";

    public static void main(String[] args) {
        // 설정 파일 로드
        Configurations configs = new Configurations();
        Configuration config;
        try {
            config = configs.properties(CONFIG_FILE);
        } catch (ConfigurationException e) {
            e.printStackTrace();
            return;
        }

        // 설정 값 조회
        String url = config.getString("webservice.url");
        int timeout = config.getInt("webservice.timeout");
        int maxAttempts = config.getInt("webservice.retry.maxAttempts");

        // 설정 값 사용
        System.out.println("URL: " + url);
        System.out.println("Timeout: " + timeout);
        System.out.println("Max Attempts: " + maxAttempts);
    }
}
```

위 코드는 `config.properties` 파일을 로드하여 웹 서비스 클라이언트의 URL, 타임아웃 및 최대 재시도 횟수와 같은 설정 값을 읽어옵니다. 이후에는 해당 값들을 사용하여 웹 서비스 클라이언트를 초기화할 수 있습니다.

## 마무리

이 예제에서는 Java Apache Commons Configuration을 사용하여 웹 서비스 클라이언트 설정을 관리하는 방법을 소개했습니다. 이 라이브러리를 통해 설정 파일을 로드하고 설정 값을 사용하여 여러 라이브러리 또는 프레임워크에서 사용하는 설정을 관리할 수 있습니다. 추가적인 기능들에 대해서는 [공식 문서](https://commons.apache.org/proper/commons-configuration/)를 참고하세요.