---
layout: post
title: "[java] Java Apache Commons Configuration으로 테스트 데이터 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java로 작성된 라이브러리로, 설정 파일을 읽고 쓰는 기능을 제공합니다. 이 라이브러리를 사용하면 프로그램에서 테스트에 필요한 데이터를 간단하게 설정할 수 있습니다. 이번 포스트에서는 Java Apache Commons Configuration을 사용하여 테스트 데이터를 설정하는 방법을 알아보겠습니다.

## 1. Apache Commons Configuration 라이브러리 추가하기

먼저, Apache Commons Configuration 라이브러리를 프로젝트에 추가해야 합니다. 이를 위해 Maven을 사용할 경우, `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

Gradle을 사용하는 경우, `build.gradle` 파일에 다음 의존성을 추가합니다:

```
dependencies {
    implementation 'org.apache.commons:commons-configuration2:2.7'
}
```

의존성을 추가한 후, 프로젝트를 빌드하여 라이브러리를 다운로드합니다.

## 2. 테스트 데이터 설정하기

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.builder.fluent.Configurations;

public class TestConfigurator {
    private static final String TEST_PROPERTIES_FILE = "test.properties";

    public static void main(String[] args) {
        Configurations configs = new Configurations();
        try {
            Configuration config = configs.properties(TEST_PROPERTIES_FILE);
            
            // 테스트 데이터 읽기
            String username = config.getString("username");
            String password = config.getString("password");
            
            // 테스트 데이터 설정
            config.setProperty("url", "http://example.com");
            config.setProperty("maxConnections", 10);
            
            // 테스트 데이터 저장
            configs.properties(TEST_PROPERTIES_FILE).write(config);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서는 `test.properties` 파일을 읽어와서 테스트 데이터를 설정하고 저장하는 간단한 예제를 보여줍니다. `Configurations` 객체를 사용하여 설정 파일을 읽어온 후, `Configuration` 객체를 통해 테스트 데이터를 읽고 수정합니다. 마지막으로, `write()` 메소드를 사용하여 변경된 데이터를 저장합니다.

## 3. 실행 결과

위의 코드를 실행하면, `test.properties` 파일에 테스트 데이터가 설정되고 저장되는 것을 확인할 수 있습니다. 아래는 `test.properties` 파일의 예시입니다:

```properties
username=admin
password=admin123
url=http://example.com
maxConnections=10
```

## 마무리

Java Apache Commons Configuration 라이브러리를 사용하면 테스트 데이터 설정이 간단하고 효율적으로 가능합니다. 이를 통해 테스트를 위한 설정 데이터를 쉽게 관리할 수 있습니다. 자세한 내용은 [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)를 참조하세요.