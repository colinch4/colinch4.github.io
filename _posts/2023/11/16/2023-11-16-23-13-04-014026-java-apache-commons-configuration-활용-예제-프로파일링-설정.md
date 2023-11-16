---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 프로파일링 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 자바 어플리케이션에서 설정 파일을 읽고 구성하는 데 사용되는 유용한 라이브러리입니다. 이 라이브러리를 사용하면 손쉽게 설정을 관리할 수 있으며, 간단한 코드로 프로파일링과 같은 작업을 할 수 있습니다.

이 예제에서는 Apache Commons Configuration을 사용하여 프로파일링 설정을 읽어오고 적용하는 방법을 살펴보겠습니다.

## 1. Apache Commons Configuration 라이브러리 추가하기

Maven을 사용하는 경우 `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>2.7</version>
</dependency>
```

Gradle을 사용하는 경우 `build.gradle` 파일에 다음 의존성을 추가합니다:

```groovy
implementation 'commons-configuration:commons-configuration:2.7'
```

## 2. 설정 파일 작성하기

프로파일링 설정을 관리하기 위해 `profiling.properties`라는 이름의 파일을 작성합니다. 이 파일에는 다음과 같은 설정이 포함될 수 있습니다:

```properties
profiling.enabled=true
profiling.level=debug
profiling.threshold=1000
```

## 3. 설정 파일 읽어오기

아래 코드를 사용하여 설정 파일을 읽어옵니다:

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Parameters;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class ProfilingConfig {

    private static final String CONFIG_FILE = "profiling.properties";

    public static void main(String[] args) {
        Parameters params = new Parameters();
        FileBasedConfigurationBuilder<PropertiesConfiguration> builder = new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                .configure(params.properties()
                        .setFileName(CONFIG_FILE));
        
        try {
            Configuration config = builder.getConfiguration();
            
            boolean enabled = config.getBoolean("profiling.enabled");
            String level = config.getString("profiling.level");
            int threshold = config.getInt("profiling.threshold");
            
            // 프로파일링 설정을 사용하여 작업 수행
            if (enabled) {
                // 프로파일링 활성화되었을 때의 로직
                System.out.println("프로파일링이 활성화되었습니다");
            } else {
                // 프로파일링 비활성화되었을 때의 로직
                System.out.println("프로파일링이 비활성화되었습니다");
            }
            
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서는 파일 기반의 구성 빌더(FileBasedConfigurationBuilder)를 사용하여 `profiling.properties` 파일을 읽어옵니다. 그런 다음, 읽어온 설정을 변수에 할당하여 프로파일링 설정에 따라 작업을 수행합니다.

## 4. 결과 확인하기

위의 예제를 실행하면 설정 파일에 지정된 프로파일링 설정에 따라 적절한 메시지가 출력됩니다.

프로파일링이 활성화되어 있는 경우:

```
프로파일링이 활성화되었습니다
```

프로파일링이 비활성화되어 있는 경우:

```
프로파일링이 비활성화되었습니다
```

## 결론

Apache Commons Configuration을 사용하면 자바 어플리케이션에서 간단하게 설정을 관리할 수 있습니다. 프로파일링 설정과 같은 작업을 쉽게 구현할 수 있으며, 유연하고 확장 가능한 어플리케이션을 개발하는 데 도움이 됩니다.

더 많은 정보를 원하는 경우 [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)를 참조하십시오.