---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 회원 등록 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 Java에서 손쉽게 설정 파일을 읽고 쓰는 기능을 제공하는 라이브러리입니다. 이번 예제에서는 Apache Commons Configuration을 사용하여 회원 등록 시스템의 설정을 관리하는 방법을 알아보겠습니다.

## 설정 파일 구성

먼저, 회원 등록 시스템의 설정을 저장하는 설정 파일을 준비해야 합니다. 설정 파일은 일반적으로 XML이나 Properties 형식으로 작성됩니다. 이 예제에서는 Properties 형식으로 작성된 `config.properties` 파일을 사용하도록 하겠습니다. 

```properties
# Database 설정
db.url=jdbc:mysql://localhost:3306/mydb
db.username=myuser
db.password=mypassword

# 회원 관련 설정
member.maxAge=18
member.registrationFee=10000
```

위 설정 파일은 데이터베이스 연결 정보와 회원 관련 설정 값을 포함하고 있습니다.

## 설정 파일 읽기

Apache Commons Configuration을 사용하여 설정 파일을 읽는 방법은 아주 간단합니다. 다음은 해당 예제에서 설정 파일을 읽어오는 방법입니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Parameters;

public class MemberRegistration {
    private static final String CONFIG_FILE = "config.properties";
    private static Configuration config;

    public static void main(String[] args) {
        initializeConfiguration();
        // 설정 값 사용 예시
        String dbUrl = config.getString("db.url");
        String dbUsername = config.getString("db.username");
        String dbPassword = config.getString("db.password");
        int maxAge = config.getInt("member.maxAge", 18);
        int registrationFee = config.getInt("member.registrationFee", 10000);
        // 설정 값 활용하여 회원 등록 로직 구현
        // ...
    }

    private static void initializeConfiguration() {
        Parameters params = new Parameters();
        FileBasedConfigurationBuilder<Configuration> builder =
                new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                        .configure(params.properties().setFileName(CONFIG_FILE));
        try {
            config = builder.getConfiguration();
        } catch (ConfigurationException e) {
            // 설정 파일 로딩 실패 시 예외 처리
            e.printStackTrace();
        }
    }
}
```

위 예제 코드에서 `initializeConfiguration()` 메소드는 설정 파일을 읽어오는 기능을 구현한 것입니다. `FileBasedConfigurationBuilder` 클래스를 사용하여 설정 파일을 읽어올 수 있습니다.

## 설정 값 사용 예시

위 예제에서는 설정 값을 불러와서 변수에 저장한 후 회원 등록 로직에 활용하는 예시를 보여주었습니다. `config.getString()` 메소드를 사용하여 원하는 키(key)에 해당하는 설정 값을 가져올 수 있습니다. 또한, 두 번째 파라미터로 기본값(default)을 지정할 수 있습니다.

위 코드에서는 `config.getString("db.url")`을 통해 데이터베이스 URL 값을 가져왔습니다. 이와 마찬가지로 다른 설정 값도 동일한 방식으로 가져올 수 있습니다.

## 결론

Apache Commons Configuration을 사용하면 손쉽게 설정 파일을 읽고 쓸 수 있습니다. 위 예제에서는 회원 등록 시스템의 설정을 관리하기 위해 Properties 형식의 설정 파일을 사용하도록 구성하였습니다. 이를 통해 설정 값들을 변경하거나 추가하는 경우에도 간단히 설정 파일을 수정하여 관리할 수 있으며, 변경된 설정 값들은 프로그램 실행 중에도 반영될 수 있습니다.

이 외에도 Apache Commons Configuration은 다양한 설정 파일 포맷을 지원하고 있으며, 여러 가지 유용한 기능들을 제공합니다. 자세한 내용은 [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)를 참고하시기 바랍니다.