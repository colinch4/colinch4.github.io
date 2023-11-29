---
layout: post
title: "[java] Thymeleaf에서 로그인 인증(authentication) 처리를 어떻게 수행하나요?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

Thymeleaf에서 로그인 인증 처리를 수행하는 방법은 다양합니다. 여기서는 Spring Security를 사용하여 Thymeleaf에서 로그인 인증 처리를 수행하는 방법에 대해 알아보겠습니다.

## 1. Spring Security 설정

먼저, Spring Security를 사용하기 위해 `pom.xml`에 아래 의존성을 추가해주세요.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

그리고, `application.properties` (또는 `application.yml`) 파일에 로그인 관련 설정을 추가해야합니다.

```properties
# 로그인 인증을 사용할 URL을 설정합니다.
spring.security.loginUrl=/login

# 인증 성공 후 리다이렉트할 URL을 설정합니다.
spring.security.successUrl=/

# 로그아웃 후 리다이렉트할 URL을 설정합니다.
spring.security.logoutSuccessUrl=/login
```

## 2. Thymeleaf 템플릿에서 로그인 폼 생성

Thymeleaf 템플릿에서 로그인 폼을 생성할 수 있습니다. 예를 들어, `login.html` 템플릿 파일을 생성하고 아래와 같이 작성해주세요.

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    
    <form th:action="@{/login}" method="post">
        <div>
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <div>
            <button type="submit">Login</button>
        </div>
    </form>
</body>
</html>
```

위의 예시는 간단한 로그인 폼을 생성하는 코드입니다. 필요에 따라 스타일이나 추가적인 요소를 추가할 수 있습니다.

## 3. 컨트롤러에서 로그인 처리

마지막으로, 컨트롤러에서 로그인 처리를 수행해야합니다. 아래는 로그인을 처리하는 컨트롤러 메소드의 예시입니다.

```java
@Controller
public class LoginController {
    @GetMapping("/login")
    public String login() {
        return "login";
    }
}
```

위의 예시에서는 GET 요청으로 `/login` 경로로 접속하면 `login.html` 템플릿을 반환합니다.

### 참고 자료

- [Spring Security Reference](https://docs.spring.io/spring-security/site/docs/current/reference/html5/)