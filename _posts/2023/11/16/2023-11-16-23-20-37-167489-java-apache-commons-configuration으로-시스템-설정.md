---
layout: post
title: "[java] Java Apache Commons Configuration으로 시스템 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

시스템 설정은 자바 애플리케이션에서 매우 중요합니다. 설정 정보는 데이터베이스 연결 정보, API 키, 로깅 레벨 등과 같은 애플리케이션 동작을 조정하는 데 필요한 매개변수입니다. 이러한 설정 정보를 하드코딩하는 것은 비효율적이고 유지 보수를 어렵게 만듭니다. 그 대신 Apache Commons Configuration을 사용하여 애플리케이션의 시스템 설정을 외부 파일에서 로드하는 것이 좋습니다.

Apache Commons Configuration은 다양한 형식의 설정 파일을 지원하는 간단하고 유연한 라이브러리입니다. 이 라이브러리를 사용하면 XML, 프로퍼티, YAML 등 다양한 형식의 설정 파일에서 설정 값을 읽을 수 있습니다.

먼저 `pom.xml`에 아파치 커먼즈 컨피규레이션 의존성을 추가합니다:

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

그런 다음, 설정 파일(`config.properties` 또는 `config.xml` 등)을 프로젝트의 클래스 패스에 추가합니다.

이제 Java 코드에서 아파치 커먼즈 컨피규레이션을 사용하여 설정 값을 로드해 보겠습니다:

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class SystemConfiguration {
    private static final String CONFIG_FILE = "config.properties";

    public static void main(String[] args) {
        try {
            PropertiesConfiguration config = new PropertiesConfiguration(CONFIG_FILE);

            // 설정 값 읽기
            String databaseHost = config.getString("database.host");
            int databasePort = config.getInt("database.port");

            // 설정 값 출력
            System.out.println("Database Host: " + databaseHost);
            System.out.println("Database Port: " + databasePort);
        } catch (ConfigurationException e) {
            System.err.println("Failed to load configuration");
            e.printStackTrace();
        }
    }
}
```

위의 예제 코드에서는 `config.properties` 파일에서 `database.host`와 `database.port` 설정 값을 읽습니다. 이러한 설정 값은 자유롭게 변경할 수 있으며, 변경 사항은 애플리케이션 재시작 없이 적용됩니다.

이것은 Apache Commons Configuration을 사용한 Java에서의 시스템 설정 로드의 간단한 예입니다. 이를 통해 애플리케이션의 구성을 외부 파일에서 관리할 수 있으므로, 민감한 설정 정보가 포함된 코드를 배포하거나 공유할 때 보다 안전하게 할 수 있습니다.

## 참고 자료
- [Apache Commons Configuration 문서](https://commons.apache.org/proper/commons-configuration/userguide/index.html)