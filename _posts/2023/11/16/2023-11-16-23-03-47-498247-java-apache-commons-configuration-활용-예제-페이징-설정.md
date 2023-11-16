---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 페이징 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java에서 설정 파일을 읽고 파싱하기 위한 유용한 라이브러리입니다. 이 예제에서는 Apache Commons Configuration을 사용하여 페이징 설정을 구현하는 방법에 대해 알아보겠습니다.

## Apache Commons Configuration 설정

먼저, Maven 또는 Gradle과 같은 의존성 관리 도구를 사용하여 Apache Commons Configuration을 프로젝트에 추가해야 합니다. 아래는 Maven을 사용하는 경우의 의존성 설정입니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

## 페이징 설정 파일 작성

`paging.properties`라는 설정 파일을 생성하고 아래와 같은 내용을 작성합니다.

```properties
paging.page-size = 10
paging.default-page = 1
```

위의 예제에서는 `page-size`와 `default-page`라는 두 개의 프로퍼티를 정의하고 있습니다.

## Java 코드 작성

다음으로, Java 코드에서 Apache Commons Configuration을 사용하여 설정 파일을 읽고 페이징 설정을 사용하는 방법을 알아보겠습니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Parameters;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class PagingExample {

    public static void main(String[] args) {
        // 설정 파일 빌더 생성
        FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
                new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                        .configure(new Parameters().properties()
                                .setFileName("paging.properties"));

        try {
            // 설정 파일 로딩
            Configuration config = builder.getConfiguration();

            // 페이징 설정 사용
            int pageSize = config.getInt("paging.page-size");
            int defaultPage = config.getInt("paging.default-page");

            System.out.println("페이지 크기: " + pageSize);
            System.out.println("기본 페이지: " + defaultPage);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서는 `paging.properties` 파일을 로딩하고 `paging.page-size` 및 `paging.default-page` 프로퍼티 값을 사용하여 페이징 설정을 가져옵니다.

## 실행 결과

위의 Java 코드를 실행하면 다음과 같은 결과를 얻을 수 있습니다.

```
페이지 크기: 10
기본 페이지: 1
```

이렇게 Apache Commons Configuration을 사용하여 페이징 설정을 구현할 수 있습니다. 추가적으로 설정 파일에 더 많은 프로퍼티를 추가하고 필요에 따라 사용할 수 있습니다.

## 참고 자료

- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)
- [Apache Commons Configuration GitHub 저장소](https://github.com/apache/commons-configuration)