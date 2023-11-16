---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 메일 발송 서버 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Configuration은 자바에서 손쉽게 설정 파일을 읽고 쓸 수 있는 유용한 라이브러리입니다. 이번에는 Apache Commons Configuration을 사용하여 메일 발송 서버의 설정을 관리하는 예제를 살펴보겠습니다.

## Apache Commons Configuration 라이브러리 추가하기
먼저, Maven을 사용하여 Apache Commons Configuration 라이브러리를 프로젝트에 추가해야 합니다. 아래와 같이 `pom.xml` 파일에 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

의존성을 추가한 후 Maven 빌드를 실행하여 라이브러리를 다운로드 받습니다.

## 설정 파일 작성하기
메일 발송 서버의 설정을 저장하기 위해 환경설정 파일을 작성해야 합니다. 예를 들어, `mail.properties`라는 파일을 생성하고 아래와 같이 설정 값을 작성합니다.

```properties
mail.server.host = smtp.example.com
mail.server.port = 587
mail.server.ssl.enabled = true
mail.server.username = your-email@example.com
mail.server.password = your-password
```

## 설정 파일 읽기
이제 Java 코드에서 Apache Commons Configuration을 사용하여 설정 파일을 읽어올 수 있습니다. 아래는 예제 코드입니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Parameters;

public class MailServerConfig {
    private static final String FILE_PATH = "mail.properties";

    private Configuration configuration;

    public MailServerConfig() {
        try {
            Parameters params = new Parameters();
            FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
                    new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                            .configure(params.fileBased()
                                    .setFileName(FILE_PATH));

            configuration = builder.getConfiguration();
        } catch (ConfigurationException e) {
            // 예외 처리
            e.printStackTrace();
        }
    }

    public String getHost() {
        return configuration.getString("mail.server.host");
    }

    public int getPort() {
        return configuration.getInt("mail.server.port");
    }

    public boolean isSslEnabled() {
        return configuration.getBoolean("mail.server.ssl.enabled");
    }

    public String getUsername() {
        return configuration.getString("mail.server.username");
    }

    public String getPassword() {
        return configuration.getString("mail.server.password");
    }
}
```

위의 예제 코드에서는 `mail.properties` 파일을 `PropertiesConfiguration`을 사용하여 읽어옵니다. 필요한 설정 값은 `Configuration` 객체를 통해 접근할 수 있습니다.

## 설정 값 사용하기
이제 `MailServerConfig` 클래스에서 읽어온 설정 값을 사용하여 메일 발송 서버를 설정할 수 있습니다. 예를 들어, Spring Framework를 사용하는 경우 아래와 같이 `JavaMailSender`를 설정할 수 있습니다.

```java
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.JavaMailSenderImpl;

public class MailService {
    private MailServerConfig config;

    public MailService(MailServerConfig config) {
        this.config = config;
    }

    public JavaMailSender getMailSender() {
        JavaMailSenderImpl mailSender = new JavaMailSenderImpl();
        mailSender.setHost(config.getHost());
        mailSender.setPort(config.getPort());
        mailSender.setUsername(config.getUsername());
        mailSender.setPassword(config.getPassword());

        Properties properties = new Properties();
        properties.setProperty("mail.smtp.auth", "true");
        properties.setProperty("mail.smtp.starttls.enable", String.valueOf(config.isSslEnabled()));

        mailSender.setJavaMailProperties(properties);

        return mailSender;
    }
}
```

위의 예제 코드에서는 `MailServerConfig` 클래스를 생성자 매개변수로 받아온 후에 읽어온 설정 값을 사용하여 `JavaMailSender`를 설정합니다.

## 결론
Apache Commons Configuration을 사용하면 설정 파일을 간편하게 읽고 쓸 수 있습니다. 이를 활용하면 메일 발송 서버 설정과 같은 환경설정을 관리하는 작업을 간편하게 처리할 수 있습니다.

## 참고 자료
- [Apache Commons Configuration](https://commons.apache.org/proper/commons-configuration/)
- [JavaMailSender Documentation](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/mail/javamail/JavaMailSender.html)