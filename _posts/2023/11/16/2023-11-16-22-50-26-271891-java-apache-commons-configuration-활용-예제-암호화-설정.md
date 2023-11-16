---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 암호화 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java에서 속성 파일을 읽고 쓰는 데 사용되는 라이브러리입니다. 이 라이브러리를 사용하면 속성 파일을 관리하고 설정을 로드하는 것이 매우 간편해집니다. 이번 예제에서는 Apache Commons Configuration을 사용하여 속성 파일의 암호화 설정을 관리하는 방법을 알아보겠습니다.

## 1. 의존성 추가하기

Apache Commons Configuration을 사용하기 위해서는 먼저 Maven 또는 Gradle 프로젝트에 의존성을 추가해야 합니다. 아래는 Maven을 사용하는 경우 `pom.xml` 파일에 의존성을 추가하는 방법입니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-configuration2</artifactId>
        <version>2.7</version>
    </dependency>
</dependencies>
```

## 2. 속성 파일 작성하기

먼저, 암호화된 값을 저장할 속성 파일을 작성해야 합니다. 예를 들어 `config.properties`라는 파일을 생성하고 아래와 같이 작성합니다.

```properties
# 설정 파일
db.username=encrypted_value
db.password=encrypted_value
```

여기서 `encrypted_value`는 암호화된 값이 되어야 합니다. 이 값은 저희 예제에서는 단순히 암호화된 값으로 가정하겠습니다.

## 3. 속성 파일 읽기

이제 Java 코드에서 Apache Commons Configuration을 사용하여 속성 파일을 읽어오는 작업을 해보겠습니다. 아래는 간단한 예제 코드입니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.PropertiesConfiguration;

public class AppConfig {

    private static final String CONFIG_FILE = "config.properties";

    public static void main(String[] args) {
        try {
            Configuration config = new PropertiesConfiguration(CONFIG_FILE);
            
            String username = config.getString("db.username");
            String password = config.getString("db.password");
            
            System.out.println("Username: " + username);
            System.out.println("Password: " + password);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

이 코드에서는 `PropertiesConfiguration` 클래스를 사용하여 `config.properties` 파일을 읽어옵니다. 이후 `getString` 메서드를 사용하여 각 속성의 값을 가져옵니다. 위 예제에서는 `db.username`과 `db.password`의 값을 가져와 출력하고 있습니다.

## 4. 속성 파일 암호화 설정하기

위 예제에서는 간단한 암호화 예제를 위해 단순히 암호화된 값을 가정했습니다. 하지만 실제로는 암호화된 값들을 사용해야 하며, 이를 위해 추가적인 설정이 필요합니다. 암호화된 값을 속성 파일에서 읽기 위해서는 별도의 복호화 작업이 필요하며, 이를 위해 Apache Commons Configuration에서 제공하는 암호화 설정을 사용할 수 있습니다.

암호화 설정을 사용하려면 `config.properties` 파일에 암호화 알고리즘과 복호화에 사용할 키를 추가해야 합니다. 예를 들어, AES 알고리즘과 16바이트 길이의 키를 사용하려면 아래와 같이 설정합니다.

```properties
# 설정 파일
db.username=encrypted_value
db.password=encrypted_value

# 암호화 설정
config.encryption.algorithm=AES
config.encryption.key=1234567890123456
```

위 설정대로 속성 파일에 암호화 설정을 추가한 후 암호화된 값을 읽을 때, Apache Commons Configuration은 이 설정을 기반으로 복호화 작업을 수행하여 암호화된 값을 제공합니다.

위 예제 코드에서는 암호화 설정을 사용하지 않고 단순히 암호화된 값으로 가정하고 있기 때문에 별도의 복호화 작업은 수행하지 않습니다.

## 결론

이번 예제에서는 Apache Commons Configuration을 사용하여 Java에서 속성 파일의 암호화 설정을 관리하는 방법을 알아보았습니다. 이를 통해 속성 파일에 암호화된 값을 저장하고, 암호화 설정을 사용하여 값을 읽어올 수 있습니다. 이러한 방법을 활용하면 암호화 설정을 쉽게 관리할 수 있으며, 보안에도 더 큰 안정성을 제공할 수 있습니다.

참고 자료:
- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/userguide/index.html)