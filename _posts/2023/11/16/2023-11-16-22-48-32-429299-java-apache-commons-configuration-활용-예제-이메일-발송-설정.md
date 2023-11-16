---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 이메일 발송 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이메일을 발송하기 위해선 SMTP 서버의 설정이 필요합니다. 이 예제에서는 Java Apache Commons Configuration 라이브러리를 사용하여 이메일 발송 설정을 외부 설정 파일에서 가져오는 방법을 알아보겠습니다.

## 1. Apache Commons Configuration 추가

먼저, Maven 프로젝트의 `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependency>
    <groupId>commons-configuration</groupId>
    <artifactId>commons-configuration</artifactId>
    <version>1.10</version>
</dependency>
```

## 2. 설정 파일 작성

이메일 발송과 관련된 설정을 저장할 `email.properties` 파일을 작성합니다. 설정 파일은 다음과 같은 형식으로 작성됩니다:

```properties
# SMTP 서버 설정
smtp.server=smtp.gmail.com
smtp.port=587

# 발송자 계정 정보
email.sender=sender@example.com
email.password=secret_password

# 수신자 계정
email.recipient=recipient@example.com
```

## 3. 설정 파일 로드

Java 코드에서 `email.properties` 파일을 로드하여 이메일 발송 설정을 가져옵니다. 다음은 설정 파일을 로드하는 예제입니다:

```java
import org.apache.commons.configuration.ConfigurationException;
import org.apache.commons.configuration.PropertiesConfiguration;

public class EmailConfig {

    private static final String CONFIG_FILE = "email.properties";

    private String smtpServer;
    private int smtpPort;
    private String emailSender;
    private String emailPassword;
    private String emailRecipient;

    public EmailConfig() {
        loadConfig();
    }

    private void loadConfig() {
        try {
            PropertiesConfiguration config = new PropertiesConfiguration(CONFIG_FILE);
            smtpServer = config.getString("smtp.server");
            smtpPort = config.getInt("smtp.port");
            emailSender = config.getString("email.sender");
            emailPassword = config.getString("email.password");
            emailRecipient = config.getString("email.recipient");
        } catch (ConfigurationException e) {
            // 예외 처리
        }
    }

    // 설정 값에 접근하는 메소드들...

}
```

위 예제에서는 `PropertiesConfiguration` 클래스를 사용하여 설정 파일을 로드하고, 설정 값을 필드에 저장합니다.

## 4. 설정 값 사용

이제 `EmailConfig` 클래스에서 로드된 설정 값을 이메일 발송에 사용할 수 있습니다. 예를 들어, 다음과 같이 JavaMail 라이브러리를 사용하여 이메일을 보낼 수 있습니다:

```java
import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class EmailSender {

    private EmailConfig config;

    public EmailSender(EmailConfig config) {
        this.config = config;
    }

    public void sendEmail(String subject, String body) {
        Properties properties = new Properties();
        properties.put("mail.smtp.host", config.getSmtpServer());
        properties.put("mail.smtp.port", config.getSmtpPort());
        properties.put("mail.smtp.auth", "true");
        properties.put("mail.smtp.starttls.enable", "true");

        Session session = Session.getDefaultInstance(properties, new javax.mail.Authenticator(){
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(config.getEmailSender(), config.getEmailPassword());
            }
        });

        try {
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress(config.getEmailSender()));
            message.setRecipients(Message.RecipientType.TO, InternetAddress.parse(config.getEmailRecipient()));
            message.setSubject(subject);
            message.setText(body);
            Transport.send(message);
        } catch (MessagingException e) {
            // 예외 처리
        }
    }

    // 이메일 발송 메소드들...

}
```

위 예제에서는 `EmailConfig` 인스턴스를 생성자로 받아와서 설정 값을 사용합니다. `sendEmail` 메소드는 주어진 제목과 본문을 가지고 이메일을 발송하는 기능을 제공합니다.

## 결론

Java Apache Commons Configuration 라이브러리를 사용하면 외부 설정 파일에서 설정 값을 가져올 수 있어서 이메일 발송과 같이 환경에 따라 다른 설정이 필요한 기능을 유연하게 구현할 수 있습니다.