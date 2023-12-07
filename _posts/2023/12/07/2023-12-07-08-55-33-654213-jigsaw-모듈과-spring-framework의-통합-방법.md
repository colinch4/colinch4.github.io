---
layout: post
title: "[java] Jigsaw 모듈과 Spring Framework의 통합 방법"
description: " "
date: 2023-12-07
tags: [java]
comments: true
share: true
---

Java 9에서 소개된 Jigsaw 모듈 시스템은 프로젝트의 구조를 모듈화하여 더욱 견고하고 유지보수가 용이한 애플리케이션을 개발할 수 있게 해준다. Spring Framework는 대표적인 Java 프레임워크로, 다양한 기능과 유연성을 제공하여 개발자들이 빠르게 애플리케이션을 개발할 수 있도록 도와준다.

이번 글에서는 Jigsaw 모듈 시스템과 Spring Framework의 통합 방법에 대해 알아보겠다.

## Jigsaw 모듈 시스템과 Spring Framework

Jigsaw 모듈 시스템은 Java 9부터 제공되며, 애플리케이션을 여러 모듈로 분리하여 개발 및 배포할 수 있도록 한다. Spring Framework는 여러 모듈로 구성된 큰 프레임워크이기 때문에, Jigsaw의 모듈 시스템과의 통합에는 몇 가지 접근 방법이 필요하다.

### 1. Automatic Module

Spring Framework는 현재 Java 9의 모듈 시스템을 완전히 지원하지는 않지만, JDK 9 이전의 라이브러리를 Automatic Module로 사용하는 방법을 제공한다. Automatic Module은 기존의 JAR 파일을 모듈로 사용할 수 있도록 해준다.

Spring Framework를 사용하려면, 해당 라이브러리를 Automatic Module로 변환해야 한다. 이를 위해 `module-info.java` 파일을 작성하고, `requires` 구문으로 Spring Framework에 필요한 모듈들을 추가해주어야 한다.

```java
module com.example.myapp {
    requires spring.core;
    requires spring.web;
    requires spring.context;
    // other requires statements
}
```

### 2. Custom Module

Spring Framework를 완전히 모듈화하기 위해서는 Custom Module을 생성해야 한다. Custom Module은 Spring Framework의 각 모듈을 직접 모듈로 만들어 사용하는 방법이다.

Custom Module을 만들기 위해서는 해당 모듈의 의존성을 모두 해결해야 한다. 예를 들어, Spring MVC를 사용하는 경우 다음과 같이 모듈의 의존성을 해결할 수 있다.

```java
module com.example.myapp {
    requires spring.core;
    requires spring.beans;
    requires spring.context;
    requires spring.web;
    requires spring.webmvc;
    requires spring.tx;
    // other requires statements
}
```

이렇게 Custom Module을 만들면, Spring Framework의 모듈들 간의 의존성을 명확하게 나타낼 수 있고, 각각의 모듈을 개별적으로 사용할 수 있다.

### 3. Maven 모듈

Maven은 Java 개발자들이 프로젝트를 관리하고 라이브러리를 관리하기 위해 널리 사용되는 빌드 도구이다. Maven을 사용하여 Spring Framework와 Jigsaw 모듈 시스템을 함께 사용할 수 있다.

Maven을 사용하면 각 모듈에 대한 의존성을 관리할 수 있으며, 필요한 라이브러리를 자동으로 가져올 수 있다. Maven의 pom.xml 파일에 해당 의존성을 추가하고, Maven을 통해 빌드하면 자동으로 해당 모듈들의 JAR 파일을 가져올 수 있다.

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-web</artifactId>
        <version>5.3.8</version>
    </dependency>
    <!-- other dependencies -->
</dependencies>
```

## 결론

Jigsaw 모듈 시스템과 Spring Framework를 통합하여 애플리케이션을 개발하는 방법에 대해 알아보았다. Jigsaw의 Automatic Module과 Custom Module, 그리고 Maven을 통한 모듈 관리 방법을 사용하여 Spring Framework를 자유롭게 사용할 수 있다.

Spring Framework와 Jigsaw 모듈 시스템을 함께 사용하면, 애플리케이션의 구조를 더욱 체계적으로 관리할 수 있고, 필요한 모듈들의 의존성을 명확하게 나타낼 수 있다. 이는 유지보수성과 확장성을 높이는데 도움을 줄 것이다.

**참고 자료:**
- [Oracle Documentation - Project Jigsaw](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/module/ModuleDescriptor.html)
- [Spring Framework Reference Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/)