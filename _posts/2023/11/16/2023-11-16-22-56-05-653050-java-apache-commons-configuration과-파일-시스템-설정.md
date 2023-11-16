---
layout: post
title: "[java] Java Apache Commons Configuration과 파일 시스템 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java로 구현된 설정 관리 라이브러리로, 간단하고 효과적인 방법으로 설정 파일을 관리하고 로드하는 데 도움을 줍니다. 이 라이브러리는 파일, XML, 프로퍼티 등 다양한 형식의 설정 파일을 지원하며, 파일 시스템에서 설정 파일을 로드하는 기능도 제공합니다. 이번 글에서는 Java Apache Commons Configuration을 사용하여 파일 시스템에서 설정 파일을 로드하는 방법을 알아보겠습니다.

## Apache Commons Configuration 설치

Apache Commons Configuration을 사용하기 위해서는 먼저 해당 라이브러리를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음 종속성을 추가합니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

Gradle을 사용하는 경우, `build.gradle` 파일에 다음 종속성을 추가합니다.

```groovy
dependencies {
    implementation 'org.apache.commons:commons-configuration2:2.7'
}
```

위의 설정을 추가한 후에는 Maven이나 Gradle을 통해 종속성을 다운로드하고 프로젝트를 빌드해야 합니다.

## 파일 시스템에서 설정 파일 로드하기

아래 예제는 파일 시스템에서 설정 파일을 로드하는 간단한 Java 코드입니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.fluent.Configurations;

public class FileSystemConfigLoader {

    public static void main(String[] args) {
        // Configurations 객체 생성
        Configurations configurations = new Configurations();

        try {
            // 설정 파일 로드
            Configuration config = configurations.properties(new File("config.properties"));

            // 로드한 설정 값 읽기
            String host = config.getString("host");
            int port = config.getInt("port");

            // 로드한 설정 값 출력
            System.out.println("Host: " + host);
            System.out.println("Port: " + port);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위 코드에서는 `Configurations` 객체를 생성하여 설정 파일을 로드합니다. `properties()` 메서드를 사용하여 `config.properties` 파일을 로드하고, `getString()` 및 `getInt()` 메서드를 사용하여 설정 값을 읽을 수 있습니다.

위의 예제에서는 `config.properties` 파일을 로드하도록 되어 있으므로, 해당 파일이 프로젝트의 루트 디렉토리에 존재해야 합니다. 읽어야 할 설정 값이 다른 파일에 저장되어 있다면, 파일의 경로 및 이름을 올바르게 수정해야 합니다.

## 결론

Java Apache Commons Configuration을 사용하면 파일 시스템에서 설정 파일을 간단하게 로드할 수 있습니다. 설정 값의 변경이 필요한 경우에도 코드의 수정 없이 설정 파일을 업데이트하는 것만으로 변경된 값을 로드할 수 있습니다. 따라서 Apache Commons Configuration을 활용하여 설정 관리를 효율적으로 수행할 수 있습니다.

## 참고 자료

- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)