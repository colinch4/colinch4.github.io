---
layout: post
title: "[java] Java Apache Commons Configuration으로 네트워크 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 자바 프로그램에서 설정 파일을 읽고 쓰는 데 도움이 되는 유용한 라이브러리입니다. 이를 사용하면 네트워크 설정과 관련된 정보를 손쉽게 처리할 수 있습니다. 이번 블로그 게시물에서는 Java Apache Commons Configuration을 사용하여 네트워크 설정을 다루는 방법에 대해 알아보겠습니다.

## 1. Apache Commons Configuration 추가

처음으로 해야 할 일은 Maven 또는 Gradle 등의 의존성 관리 도구를 이용하여 Apache Commons Configuration을 프로젝트에 추가하는 것입니다. Maven을 사용한다면 `pom.xml` 파일에 다음과 같이 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

Gradle을 사용한다면 `build.gradle` 파일에 다음과 같이 의존성을 추가합니다.

```groovy
implementation 'org.apache.commons:commons-configuration2:2.7'
```

의존성을 추가한 후, 프로젝트를 빌드하여 Apache Commons Configuration을 사용할 준비를 마칩니다.

## 2. 설정 파일 작성

Apache Commons Configuration을 사용하려면 설정 파일을 작성해야 합니다. 예를 들어, `network.properties`라는 파일을 생성하고 다음과 같이 설정을 추가합니다.

```
network.host=127.0.0.1
network.port=8080
```

이 파일은 네트워크 호스트와 포트 번호에 대한 설정을 담고 있습니다.

## 3. 설정 파일 로드하기

이제 Java 코드에서 설정 파일을 로드해보겠습니다. 아래의 예제 코드를 참고하세요.

```java
import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Parameters;

public class NetworkConfiguration {

    public static void main(String[] args) {
        // 설정 파일을 로드하기 위한 FileBasedConfigurationBuilder 객체 생성
        FileBasedConfigurationBuilder<PropertiesConfiguration> builder = new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                .configure(new Parameters().properties()
                        .setFileName("network.properties"));

        try {
            // 설정 파일 로드
            PropertiesConfiguration config = builder.getConfiguration();

            // 설정 값 가져오기
            String host = config.getString("network.host");
            int port = config.getInt("network.port");

            // 설정 값 출력
            System.out.println("Host: " + host);
            System.out.println("Port: " + port);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위 코드에서는 Apache Commons Configuration을 사용하여 `network.properties` 파일을 로드하고, 설정 값들을 가져와서 출력합니다. `getString` 메서드를 사용하여 문자열 값을, `getInt` 메서드를 사용하여 정수 값을 가져올 수 있습니다.

## 4. 실행 결과

위 예제 코드를 실행하면 다음과 같은 출력 결과를 얻을 수 있습니다.

```
Host: 127.0.0.1
Port: 8080
```

이렇게 Apache Commons Configuration을 사용하여 네트워크 설정을 처리할 수 있습니다. 설정 파일의 내용을 변경하면 프로그램을 다시 실행하여 새로운 설정 값을 가져올 수 있습니다.

더 많은 기능과 설정 옵션을 사용하려면 Apache Commons Configuration 문서를 참고하세요.

## 참고 자료

- [Apache Commons Configuration 문서](https://commons.apache.org/proper/commons-configuration/)
- [Maven 공식 웹사이트](https://maven.apache.org/)
- [Gradle 공식 웹사이트](https://gradle.org/)