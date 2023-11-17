---
layout: post
title: "[java] Jasypt와 Spring Framework를 함께 사용하는 방법"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

Spring Framework는 자바 기반의 웹 어플리케이션 개발에 매우 유용하다. 그리고 Jasypt는 데이터베이스 연결 정보나 비밀번호와 같은 민감한 정보를 암호화하는 기능을 제공한다. 이 두 가지를 함께 사용하여 암호화된 데이터를 안전하게 저장하고 사용할 수 있다. 이번 블로그 포스트에서는 Jasypt를 Spring Framework와 함께 사용하는 방법에 대해 알아보겠다.

## 1. Jasypt 라이브러리 추가하기

먼저 프로젝트에 Jasypt 라이브러리를 추가해야 한다. 이를 위해 Maven 또는 Gradle을 사용할 수 있다. 라이브러리를 프로젝트에 추가한 후에는 암호화와 해독 기능을 사용할 수 있다.

### Maven을 사용하는 경우

```xml
<dependency>
    <groupId>org.jasypt</groupId>
    <artifactId>jasypt</artifactId>
    <version>1.9.4</version>
</dependency>
```

### Gradle을 사용하는 경우

```
implementation 'org.jasypt:jasypt:1.9.4'
```

## 2. 환경 설정

Spring Framework에서 Jasypt를 사용하기 위해서는 몇 가지 환경 설정을 해주어야 한다. 이를 위해서는 다음과 같은 단계를 따라야 한다.

### 2.1. 암호화 설정 추가하기

먼저 `application.properties` 파일에 암호화에 필요한 설정을 추가해주어야 한다.

```properties
jasypt.encryptor.password=your_password
```

위의 예시에서는 `jasypt.encryptor.password`로 암호화에 사용할 패스워드를 설정한 것이다. 본인이 원하는 패스워드로 변경해주어야 한다.

### 2.2. 환경 변수 설정하기

Spring Framework에서 Jasypt를 사용하기 위해서는 다음과 같은 환경 변수를 설정해주어야 한다.

```java
@Configuration
public class JasyptConfiguration {

    @Value("${jasypt.encryptor.password}")
    private String encryptorPassword;

    @Bean("jasyptStringEncryptor")
    public StringEncryptor stringEncryptor() {
        PBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword(encryptorPassword);
        return encryptor;
    }
}
```

위의 예시에서 `jasypt.encryptor.password`를 `encryptorPassword`에 주입하여 필요한 곳에서 사용할 수 있도록 설정하였다. 여기서는 `StringEncryptor`를 사용하는 예시이다.

## 3. 암호화와 해독 사용하기

이제 설정을 마쳤으므로 Jasypt를 사용하여 암호화와 해독 기능을 사용할 수 있다. 아래의 예시 코드를 참고해보자.

```java
@Service
public class MyService {

    @Autowired
    private StringEncryptor encryptor;

    public String encrypt(String value) {
        return encryptor.encrypt(value);
    }

    public String decrypt(String encryptedValue) {
        return encryptor.decrypt(encryptedValue);
    }
}
```

위의 예시에서는 `StringEncryptor`를 사용하여 메서드를 호출하는 방식으로 암호화와 해독을 수행하였다. `encrypt` 메서드는 주어진 값의 암호화를 수행하고, `decrypt` 메서드는 암호화된 값을 해독한다.

이제 Jasypt와 Spring Framework를 함께 사용하여 데이터를 안전하게 암호화하고 해독할 수 있다.

## 참고 자료

- [Jasypt 공식 홈페이지](http://www.jasypt.org/)
- [Spring Framework 공식 홈페이지](https://spring.io/)