---
layout: post
title: "[java] Hibernate Validator와 Spring MVC의 통합은 어떻게 이루어지나요?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

Hibernate Validator는 자바 기반의 어플리케이션에서 데이터 검증을 쉽게 할 수 있는 기능을 제공하는 라이브러리입니다. Spring MVC는 자바 기반의 웹 어플리케이션 개발을 위한 프레임워크로, 컨트롤러와 뷰 등의 웹 구성 요소를 제공합니다.

Hibernate Validator와 Spring MVC를 통합하기 위해서는 다음과 같은 단계를 따를 수 있습니다:

1. 의존성 추가: Maven이나 Gradle을 사용하여 Hibernate Validator와 Spring MVC의 의존성을 추가해야 합니다. 이를 위해 `pom.xml` 파일이나 `build.gradle` 파일에 아래의 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

2. Validator 설정: Spring MVC의 Validator를 사용하기 위해 `WebMvcConfigurer` 인터페이스를 구현한 설정 클래스를 생성합니다. 이 클래스에서 `addValidators()` 메서드를 오버라이딩하여 Hibernate Validator를 등록합니다.

```java
@Configuration
public class ValidatorConfig implements WebMvcConfigurer {

    @Override
    public void addValidators(ValidatorRegistry validatorRegistry) {
        validatorRegistry.addValidator("hibernateValidator", new HibernateValidator());
    }
}
```

3. 컨트롤러에서 검증 설정: Spring MVC의 컨트롤러 메서드에 `@Validated` 어노테이션을 사용하여 검증을 수행하도록 지정할 수 있습니다. 검증 오류가 발생한 경우, `BindingResult` 객체를 통해 오류 정보에 접근할 수 있습니다.

```java
@PostMapping("/users")
public String createUser(@Validated @RequestBody User user, BindingResult result) {
    if (result.hasErrors()) {
        // 검증 오류 처리
    }

    // 검증 통과한 경우, 로직 처리
}
```

위의 단계를 따라 Hibernate Validator와 Spring MVC를 통합하면, 컨트롤러에서 사용되는 모델 객체의 데이터 검증을 손쉽게 처리할 수 있게 됩니다.

더 자세한 정보는 다음의 문서를 참고하시기 바랍니다:
- Hibernate Validator 공식 문서: https://docs.jboss.org/hibernate/stable/validator/reference/en-US/html_single/
- Spring MVC 공식 문서: https://docs.spring.io/spring-framework/docs/current/reference/html/web.html#mvc