---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 오류 로깅 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 자바 애플리케이션에서 설정 파일을 쉽게 읽고 관리할 수 있는 라이브러리입니다. 이번 예제에서는 Apache Commons Configuration을 사용하여 오류 로깅 설정을 구현하는 방법을 알아보겠습니다.

## Apache Commons Configuration 라이브러리 추가

먼저, Maven을 이용하여 프로젝트에 Apache Commons Configuration을 추가합니다. `pom.xml` 파일의 `<dependencies>` 섹션에 다음 코드를 추가합니다.

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>2.7</version>
</dependency>
```

이제 Maven을 통해 의존성을 추가했으니, Apache Commons Configuration을 사용할 준비가 되었습니다.

## 설정 파일 작성

다음으로, 오류 로깅에 대한 설정을 담은 `config.properties` 파일을 작성합니다. 예를 들어, 다음과 같은 설정을 포함할 수 있습니다.

```
# 오류 로깅 설정
error.logging.enabled=true
error.logging.level=debug
error.logging.file=/var/log/myapp/error.log
```

위 설정 파일에서 `error.logging.enabled`는 오류 로깅을 활성화할지 여부를 나타내며, `error.logging.level`은 오류 로그의 레벨을 나타냅니다. `error.logging.file`은 오류 로그가 저장될 파일 경로를 지정합니다.

## Java 코드 작성

이제 Apache Commons Configuration을 사용하여 설정 파일을 읽고 오류 로깅 설정을 가져오는 Java 코드를 작성해보겠습니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class ErrorLoggingConfig {
    private static final String CONFIG_FILE = "config.properties";

    public static void main(String[] args) {
        Configurations configs = new Configurations();
        try {
            Configuration config = configs.properties(CONFIG_FILE);
            
            // 오류 로깅 설정 가져오기
            boolean enabled = config.getBoolean("error.logging.enabled");
            String level = config.getString("error.logging.level");
            String file = config.getString("error.logging.file");
            
            // 설정 값 출력
            System.out.println("Error Logging Enabled: " + enabled);
            System.out.println("Error Logging Level: " + level);
            System.out.println("Error Logging File: " + file);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드는 `config.properties` 파일을 로드하고, Apache Commons Configuration을 통해 설정 값을 가져오는 예제입니다. 코드에서는 `Configuration` 객체를 사용하여 설정 값을 가져온 후, 값을 출력하는 부분이 포함되어 있습니다.

## 실행 결과

위 예제 코드를 실행하면, `config.properties` 파일에 기재된 오류 로깅 설정 값들이 콘솔에 출력됩니다.

```
Error Logging Enabled: true
Error Logging Level: debug
Error Logging File: /var/log/myapp/error.log
```

이와 같이 Apache Commons Configuration을 활용하면 별도의 설정 파일에서 오류 로깅과 같은 설정 값을 가져올 수 있습니다.

## 결론

이번 예제에서는 Apache Commons Configuration 라이브러리를 사용하여 자바 애플리케이션에서 설정 값을 관리하는 방법을 살펴보았습니다. Apache Commons Configuration은 설정 파일의 로드와 값을 가져오는 작업을 간편하게 처리할 수 있도록 도와줍니다. 설정을 자주 변경해야하는 경우나 별도의 설정 파일을 사용해야 하는 경우에는 Apache Commons Configuration을 활용하면 유연하고 효율적인 설정 관리를 할 수 있습니다.

## 참고 자료

- [Apache Commons Configuration - User Guide](https://commons.apache.org/proper/commons-configuration/userguide/index.html)