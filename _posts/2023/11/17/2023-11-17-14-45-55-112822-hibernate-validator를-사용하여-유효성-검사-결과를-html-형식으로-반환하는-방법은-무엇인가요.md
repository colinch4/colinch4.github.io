---
layout: post
title: "[java] Hibernate Validator를 사용하여 유효성 검사 결과를 HTML 형식으로 반환하는 방법은 무엇인가요?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

Hibernate Validator는 자바 객체의 유효성을 검사하기 위한 강력한 도구입니다. 이를 사용하여 유효성 검사 결과를 HTML 형식으로 반환하는 방법을 알아보겠습니다.

1. 의존성 추가
먼저, 프로젝트의 의존성에 Hibernate Validator를 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.hibernate.validator</groupId>
    <artifactId>hibernate-validator</artifactId>
    <version>6.2.0.Final</version>
</dependency>
```

2. 유효성 검사 수행
검사를 수행할 자바 객체에 `@Valid` 어노테이션을 추가합니다. 예를 들어, 다음과 같은 사용자 객체가 있다고 가정해봅시다:

```java
public class User {

    @NotEmpty(message = "이름을 입력해주세요.")
    private String name;

    @Email(message = "유효한 이메일 주소를 입력해주세요.")
    private String email;

    // Getters and Setters
    // ...
}
```

3. 검사 결과 반환
검사 결과를 HTML 형식으로 반환하기 위해 `ConstraintViolationException`을 처리하는 `ExceptionHandler` 클래스를 만들어야 합니다. 아래 예제 코드는 검사 결과를 리스트로 반환하는 예제입니다:

```java
@RestControllerAdvice
public class RestExceptionHandler extends ResponseEntityExceptionHandler {

    @ExceptionHandler(ConstraintViolationException.class)
    public ResponseEntity<List<String>> handleValidationException(ConstraintViolationException ex) {
        List<String> errors = ex.getConstraintViolations()
                .stream()
                .map(violation -> violation.getMessage())
                .collect(Collectors.toList());

        return ResponseEntity.badRequest().body(errors);
    }
}
```

4. 결과 확인
이제 유효성 검사를 수행하고 유효하지 않은 내용을 HTML 형식으로 반환하는 예제가 준비되었습니다. 테스트를 위해 다음과 같은 컨트롤러를 작성해보세요:

```java
@RestController
public class UserController {

    @PostMapping("/users")
    public String createUser(@RequestBody @Valid User user) {
        // User 객체 저장 등의 비즈니스 로직 수행
        return "사용자가 생성되었습니다.";
    }
}
```

위 컨트롤러에서 `@Valid` 어노테이션은 사용자 객체의 유효성을 검사합니다. 유효성 검사에 실패하면, `RestExceptionHandler`에서 작성한 `handleValidationException` 메서드가 호출되어 유효성 검사 결과를 HTML 형식으로 반환합니다.

이제 위의 예제를 실행하면, 유효성 검사에 실패한 경우에는 HTML 형식의 오류 메시지가 반환되는 것을 확인할 수 있습니다.

참고 자료:
- Hibernate Validator 공식 문서: [https://docs.jboss.org/hibernate/validator/6.2/reference/en-US/html_single/](https://docs.jboss.org/hibernate/validator/6.2/reference/en-US/html_single/)
- Spring Framework 공식 문서: [https://spring.io/projects/spring-framework](https://spring.io/projects/spring-framework)