---
layout: post
title: "[java] Java Apache Commons Configuration으로 알고리즘 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java에서 구성 파일을 읽고 쓰는 데 사용되는 유용한 라이브러리입니다. 이 라이브러리를 사용하면 애플리케이션 설정을 구성 파일에 저장하고 읽어들일 수 있습니다. 이번 블로그 포스트에서는 Apache Commons Configuration을 사용하여 알고리즘 설정을 구성하는 방법을 알아보겠습니다.

## 1. Apache Commons Configuration 라이브러리 추가하기

먼저, Maven을 사용하는 경우 `pom.xml` 파일에 아래의 종속성을 추가합니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

Gradle을 사용하는 경우 `build.gradle` 파일에 아래의 종속성을 추가합니다.

```groovy
implementation 'org.apache.commons:commons-configuration2:2.7'
```

라이브러리를 추가한 후에는 프로젝트를 다시 빌드해야 합니다.

## 2. 알고리즘 설정 구성 파일 작성하기

알고리즘 설정을 저장할 구성 파일을 작성합니다. 일반적으로 `.properties` 확장자를 사용하여 plain text 형식으로 작성됩니다. 예를 들어, `algorithm.properties` 파일을 작성하고 다음과 같은 내용으로 채웁니다.

```properties
algorithm.name=SHA-256
algorithm.keyLength=256
algorithm.iterations=10000
```

위의 예제에서 알고리즘 이름, 키 길이 및 반복 횟수를 설정합니다.

## 3. 알고리즘 설정 가져오기

이제 Java 코드에서 알고리즘 설정을 가져오는 방법을 살펴보겠습니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Configurations;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class AlgorithmConfiguration {

    private static final String CONFIG_FILE = "algorithm.properties";

    public static void main(String[] args) {
        Configurations configurations = new Configurations();
        try {
            FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
                    configurations.propertiesBuilder(CONFIG_FILE);
            Configuration configuration = builder.getConfiguration();

            String algorithmName = configuration.getString("algorithm.name");
            int keyLength = configuration.getInt("algorithm.keyLength");
            int iterations = configuration.getInt("algorithm.iterations");

            System.out.println("Algorithm Name: " + algorithmName);
            System.out.println("Key Length: " + keyLength);
            System.out.println("Iterations: " + iterations);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서는 `algorithm.properties` 파일을 사용하여 `FileBasedConfigurationBuilder`를 만들고 구성 파일에서 필요한 설정 값을 가져와서 출력합니다.

## 4. 실행 결과 확인하기

코드를 실행하면 다음과 같은 결과를 얻을 수 있습니다.

```
Algorithm Name: SHA-256
Key Length: 256
Iterations: 10000
```

알고리즘 설정이 성공적으로 가져와져서 출력되는 것을 확인할 수 있습니다.

## 결론

Apache Commons Configuration을 사용하면 Java에서 알고리즘 설정과 같은 구성 정보를 쉽게 관리할 수 있습니다. 이 편리한 라이브러리를 사용하면 애플리케이션의 환경 설정을 외부 파일로 분리하여 유지 관리하기 쉽게 할 수 있습니다.

참고 자료:
- [Apache Commons Configuration User Guide](https://commons.apache.org/proper/commons-configuration/userguide/index.html)