---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 콘텐츠 압축 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이 예제에서는 Java 프로젝트에서 [Apache Commons Configuration](https://commons.apache.org/proper/commons-configuration/) 라이브러리를 사용하여 콘텐츠 압축 설정을 구현하는 방법을 알아보겠습니다.

## 1. 의존성 추가

먼저, Maven 프로젝트를 사용하는 경우 `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

Gradle을 사용한다면, `build.gradle` 파일에 다음을 추가합니다:

```groovy
dependencies {
    implementation 'commons-configuration:commons-configuration:1.10'
}
```

## 2. 설정 파일 작성

Apache Commons Configuration은 다양한 유형의 설정 파일을 지원합니다. 우리는 XML 형식의 파일을 사용하여 콘텐츠 압축 설정을 정의하겠습니다. `config.xml` 파일을 생성하고 다음과 같이 작성합니다:

```xml
<configuration>
    <compress>
        <enable>true</enable>
        <level>9</level>
    </compress>
</configuration>
```

위의 설정 파일은 콘텐츠 압축을 활성화하고 압축 수준을 9로 설정합니다.

## 3. Java 코드 작성

이제 Java 코드에서 Apache Commons Configuration을 사용하여 설정 파일을 로드하고 콘텐츠 압축 설정을 가져오는 방법을 보여줄 것입니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Parameters;

public class AppConfig {

    private static final String CONFIG_FILE = "config.xml";

    public static void main(String[] args) {
        Parameters params = new Parameters();
        FileBasedConfigurationBuilder<XMLConfiguration> builder =
                new FileBasedConfigurationBuilder<>(XMLConfiguration.class)
                        .configure(params.xml()
                                .setFileName(CONFIG_FILE));

        try {
            Configuration config = builder.getConfiguration();
            boolean enableCompression = config.getBoolean("compress.enable");
            int compressionLevel = config.getInt("compress.level");

            // 콘텐츠 압축 설정을 사용하여 작업 수행
            if (enableCompression) {
                System.out.println("콘텐츠 압축이 활성화되었습니다.");
                System.out.println("압축 수준: " + compressionLevel);
                // 콘텐츠 압축 로직 구현
            } else {
                System.out.println("콘텐츠 압축이 비활성화되었습니다.");
                // 압축 비활성화 로직 구현
            }
        } catch (Exception e) {
            // 예외 처리
            e.printStackTrace();
        }
    }
}
```

위의 코드는 `config.xml` 파일에서 콘텐츠 압축 설정을 로드하고, 가져온 설정 값을 기반으로 작업을 수행하는 예제입니다.

## 4. 실행 결과

위의 Java 코드를 실행하면 다음과 같은 결과가 출력됩니다:

```
콘텐츠 압축이 활성화되었습니다.
압축 수준: 9
```

콘텐츠 압축이 활성화되고 압축 수준이 9인 것을 알 수 있습니다.

이제 Java 프로젝트에서 Apache Commons Configuration을 사용하여 콘텐츠 압축 설정을 구현하는 방법을 알게 되었습니다. 이 라이브러리를 사용하면 다양한 유형의 설정 파일을 손쉽게 로드하고 사용할 수 있으며, 설정 값을 사용하여 원하는 작업을 수행할 수 있습니다.