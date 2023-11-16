---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 인증서 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java에서 구성 파일을 쉽게 읽고 쓸 수 있는 라이브러리입니다. 이 라이브러리를 사용하여 인증서 설정을 쉽게 관리하는 방법에 대해 알아보겠습니다.

## Apache Commons Configuration 라이브러리 추가

먼저, Maven을 사용하여 Apache Commons Configuration 라이브러리를 프로젝트에 추가해야 합니다. 프로젝트의 pom.xml 파일에 다음 의존성을 추가합니다.

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

의존성을 추가한 뒤 Maven을 업데이트하면 Apache Commons Configuration 라이브러리가 프로젝트에 추가됩니다.

## 인증서 설정 파일 생성

인증서 설정을 관리하기 위해 `cert.properties`라는 구성 파일을 생성합니다. 이 파일은 `keystoreFile`과 `keystorePassword`라는 두 가지 속성을 포함해야 합니다.

```properties
keystoreFile=/path/to/keystore
keystorePassword=your_keystore_password
```

## 인증서 설정 읽기

아래 코드는 Apache Commons Configuration을 사용하여 인증서 설정 파일을 읽는 예제입니다.

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class CertConfigExample {

    public static void main(String[] args) {
        try {
            PropertiesConfiguration config = new PropertiesConfiguration("cert.properties");

            String keystoreFile = config.getString("keystoreFile");
            String keystorePassword = config.getString("keystorePassword");

            System.out.println("Keystore File: " + keystoreFile);
            System.out.println("Keystore Password: " + keystorePassword);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위 코드에서 `cert.properties` 파일을 읽고, `keystoreFile`과 `keystorePassword` 속성을 가져와서 출력합니다.

## 인증서 설정 쓰기

아래 코드는 Apache Commons Configuration을 사용하여 인증서 설정 파일을 쓰는 예제입니다.

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class CertConfigExample {

    public static void main(String[] args) {
        try {
            PropertiesConfiguration config = new PropertiesConfiguration("cert.properties");

            String keystoreFile = "/new/path/to/keystore";
            String keystorePassword = "new_keystore_password";

            config.setProperty("keystoreFile", keystoreFile);
            config.setProperty("keystorePassword", keystorePassword);
            
            config.save();
            
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위 코드에서 `cert.properties` 파일을 열고, `keystoreFile`과 `keystorePassword` 속성을 변경한 뒤, 변경 내용을 저장합니다.

## 결론

Apache Commons Configuration을 사용하면 Java에서 인증서 설정을 쉽게 관리할 수 있습니다. 이 라이브러리를 사용해 구성 파일을 읽고 쓰는 방법을 알아보았습니다.