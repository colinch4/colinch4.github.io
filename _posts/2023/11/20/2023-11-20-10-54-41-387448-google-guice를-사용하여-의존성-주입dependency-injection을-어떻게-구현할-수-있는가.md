---
layout: post
title: "[java] Google Guice를 사용하여 의존성 주입(Dependency Injection)을 어떻게 구현할 수 있는가?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

의존성 주입(Dependency Injection, DI)은 객체 간의 느슨한 결합을 통해 유지 보수 가능한 코드를 작성하는 데 도움이 되는 디자인 패턴입니다. Google Guice는 Java 언어를 위한 경량 DI 프레임워크로, DI를 구현하는 데 도움을 주는 도구입니다. 이제 Google Guice를 사용하여 의존성 주입을 어떻게 구현하는지 살펴보겠습니다.

## Guice의 설치

먼저, Guice를 프로젝트에 추가해야 합니다. Maven을 사용 중이라면 `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependencies>
    <dependency>
        <groupId>com.google.inject</groupId>
        <artifactId>guice</artifactId>
        <version>4.2.3</version>
    </dependency>
</dependencies>
```

Gradle을 사용 중이라면 `build.gradle` 파일에 다음 의존성을 추가합니다:

```groovy
dependencies {
    implementation 'com.google.inject:guice:4.2.3'
}
```

## 의존성 주입 구현하기

1. 인터페이스 및 클래스 정의하기

   의존성 주입을 위해 인터페이스와 해당 인터페이스를 구현하는 클래스를 정의합니다.

   ```java
   public interface MessageService {
       String getMessage();
   }
   ```

   ```java
   public class EmailService implements MessageService {
       @Override
       public String getMessage() {
           return "Email message";
       }
   }
   ```

2. `Module` 클래스 구현하기

   Guice는 바인딩 정보를 포함한 `Module` 클래스를 사용하여 의존성을 관리합니다. 이를 위해 다음과 같이 `Module` 클래스를 구현합니다.

   ```java
   import com.google.inject.AbstractModule;

   public class MessageModule extends AbstractModule {
       @Override
       protected void configure() {
           bind(MessageService.class).to(EmailService.class);
       }
   }
   ```

   위의 코드에서는 `MessageService` 인터페이스를 `EmailService` 클래스에 바인딩하고 있습니다.

3. `Injector` 생성하기

   `Injector`는 Guice에서 의존성 주입을 수행하는 역할을 합니다. `Module` 클래스를 사용하여 `Injector`를 생성합니다.

   ```java
   import com.google.inject.Guice;
   import com.google.inject.Injector;

   public class Main {
       public static void main(String[] args) {
           Injector injector = Guice.createInjector(new MessageModule());
           MessageService messageService = injector.getInstance(MessageService.class);

           String message = messageService.getMessage();
           System.out.println(message);
       }
   }
   ```

   위의 코드에서는 `MessageModule`을 사용하여 `Injector`를 생성하고, `MessageService` 인스턴스를 얻어와 메시지를 출력하고 있습니다.

이제 위의 코드를 실행하여 Guice를 사용한 의존성 주입을 확인할 수 있습니다.

위의 예제에서는 `EmailService`를 사용하고 있지만, 필요에 따라 다른 구현체를 사용할 수도 있습니다. 이를 통해 코드 변경 없이 의존성을 유연하게 관리할 수 있습니다.

구글 Guice에 대한 자세한 내용은 [Guice 홈페이지](https://github.com/google/guice)에서 확인할 수 있습니다.