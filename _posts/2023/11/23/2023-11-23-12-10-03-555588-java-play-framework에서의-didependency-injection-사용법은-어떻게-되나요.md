---
layout: post
title: "[java] Java Play Framework에서의 DI(Dependency Injection) 사용법은 어떻게 되나요?"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Java Play Framework은 의존성 주입(Dependency Injection)을 지원하기 위해 Guice를 사용합니다. 이를 통해 객체의 의존성을 자동으로 해결하고 유지보수 가능한 코드를 작성할 수 있습니다. Java Play Framework에서 DI를 사용하는 방법에 대해 알아보겠습니다.

1. 의존성 주입 설정하기
   Java Play Framework에서 DI를 사용하려면 의존성 주입을 설정해야 합니다. 이를 위해 `Module` 클래스를 만들고 필요한 의존성을 바인딩해야 하는 메서드를 정의합니다. 아래는 예시입니다:

   ```java
   // app/Module.java

   import com.google.inject.AbstractModule;
   import services.MyService;
   import services.MyServiceImpl;

   public class Module extends AbstractModule {
       @Override
       protected void configure() {
           bind(MyService.class).to(MyServiceImpl.class);
       }
   }
   ```

   위 예시에서는 `MyService` 인터페이스를 `MyServiceImpl` 클래스에 바인딩하고 있습니다.

2. 의존성 주입된 객체 사용하기
   의존성 주입된 객체를 사용하기 위해서는 해당 객체가 필요한 클래스에서 생성자나 필드 주석을 통해 의존성을 주입받아야 합니다. 아래는 예시입니다:

   ```java
   // app/controllers/MyController.java

   import services.MyService;
   import javax.inject.Inject;

   public class MyController {
       private MyService myService;

       @Inject
       public MyController(MyService myService) {
           this.myService = myService;
       }

       public void doSomething() {
           // myService 사용
       }
   }
   ```

   위 예시에서는 `MyService` 인터페이스를 생성자 주석을 통해 의존성을 주입받고 있습니다.

3. 의존성 주입된 객체 사용하기
   생성자나 필드 주석을 통해 의존성이 주입되면 Play Framework이 해당 객체를 자동으로 생성하고 주입합니다. 따라서 개발자는 의존성 주입된 객체를 사용하기 위해 객체를 직접 생성하거나 주입할 필요가 없습니다. 필요한 객체에 의존성이 자동으로 주입되기 때문에 객체를 바로 사용할 수 있습니다.

이것으로 Java Play Framework에서의 DI(Dependency Injection) 사용법을 알아보았습니다. 의존성을 주입하기 위해 Guice를 사용하는 방법을 확인하였으며, 이를 통해 유지보수 가능하고 테스트 용이한 코드를 작성할 수 있습니다. Java Play Framework 공식 문서에 더 자세한 내용을 참조할 수 있습니다.

[Play Framework Documentation](https://www.playframework.com/documentation/latest/JavaDependencyInjection)