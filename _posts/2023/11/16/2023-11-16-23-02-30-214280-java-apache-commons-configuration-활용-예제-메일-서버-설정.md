---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 메일 서버 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java Apache Commons Configuration은 설정 파일을 쉽게 읽어들이고 처리할 수 있는 라이브러리입니다. 이번 예제에서는 이 라이브러리를 사용하여 메일 서버의 설정을 처리하는 방법을 알아보겠습니다.

## 설정 파일 작성하기

먼저, 메일 서버의 설정 정보를 담은 `mail.properties`라는 설정 파일을 작성합니다. 해당 파일은 아래와 같은 내용을 포함해야 합니다.

```
# mail.properties

# 메일 서버 호스트
mail.host=smtp.example.com

# 메일 서버 포트
mail.port=587

# 사용자명
mail.username=admin@example.com

# 패스워드
mail.password=secretpassword
```

## 설정 파일 읽어오기

이제 Java 코드에서 해당 설정 파일을 읽어와서 값을 사용할 수 있도록 작성해보겠습니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.PropertiesConfiguration;
import org.apache.commons.configuration2.ex.ConfigurationException;

public class MailServerConfig {

    private static final String CONFIG_FILE = "mail.properties";

    public static void main(String[] args) {
        try {
            // 설정 파일 로드
            Configuration config = new PropertiesConfiguration(CONFIG_FILE);

            // 값 가져오기
            String host = config.getString("mail.host");
            int port = config.getInt("mail.port");
            String username = config.getString("mail.username");
            String password = config.getString("mail.password");

            // 설정 값 출력
            System.out.println("Host: " + host);
            System.out.println("Port: " + port);
            System.out.println("Username: " + username);
            System.out.println("Password: " + password);
        } catch (ConfigurationException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드에서는 `PropertiesConfiguration` 클래스를 사용하여 설정 파일을 로드하고, 필요한 값들을 가져와서 출력하고 있습니다.

## 실행 결과 확인하기

위의 Java 코드를 실행하면, 설정 파일에서 읽어온 메일 서버의 설정 정보가 콘솔에 출력됩니다. 아래는 예상되는 출력 결과입니다.

```
Host: smtp.example.com
Port: 587
Username: admin@example.com
Password: secretpassword
```

## 결론

Java Apache Commons Configuration을 활용하면 설정 파일을 손쉽게 읽어와서 처리할 수 있습니다. 이를 통해 코드의 유연성과 재사용성을 높일 수 있으며, 설정 파일을 통해 애플리케이션의 동작을 쉽게 변경할 수 있습니다.

더 자세한 내용은 [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/javadocs/v2.7/apidocs/index.html)를 참고하시기 바랍니다.