---
layout: post
title: "[java] 인증(Authentication)과 인가(Authorization)"
description: " "
date: 2023-12-07
tags: [java]
comments: true
share: true
---

웹 애플리케이션에서 보안은 핵심 요소입니다. 인증(Authentication)과 인가(Authorization)는 웹 애플리케이션의 보안을 제공하기 위한 중요한 개념입니다. 이 두 용어는 종종 혼동되기도 하지만, 각각 다른 개념을 의미합니다.

## 인증(Authentication)

인증은 사용자가 자신의 신원을 증명하는 과정을 말합니다. 예를 들어, 로그인 시스템을 사용하여 사용자가 제공한 아이디와 비밀번호가 일치하는지 확인하는 것입니다. 인증 과정을 통해 사용자는 자신의 신원을 증명하고 일련의 권한을 부여받을 수 있게 됩니다.

Java에서는 기본적으로 `java.security` 패키지를 통해 인증 기능을 제공합니다. 예를 들어, `UsernamePasswordAuthenticationToken` 클래스를 사용하여 사용자 이름과 비밀번호를 인증하는 로직을 구현할 수 있습니다.

```java
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;

public class AuthenticationExample {
    public static void main(String[] args) {
        // 사용자 이름과 비밀번호를 입력받음
        String username = "user123";
        String password = "password123";

        // 사용자 이름과 비밀번호로 인증 토큰 생성
        Authentication authentication = new UsernamePasswordAuthenticationToken(username, password);

        // Spring Security의 SecurityContext에 인증 객체 설정
        SecurityContextHolder.getContext().setAuthentication(authentication);
        
        // 인증된 사용자 정보 가져오기
        String authenticatedUsername = SecurityContextHolder.getContext().getAuthentication().getName();
        
        System.out.println("Authenticated username: " + authenticatedUsername);
    }
}
```

## 인가(Authorization)

인가는 인증된 사용자에게 특정한 작업을 수행할 수 있는 권한을 부여하는 과정입니다. 즉, 인증된 사용자에게 허용된 리소스나 기능에만 접근할 수 있도록 제한을 두는 것입니다. 

일반적으로 인가는 롤(Role) 기반으로 이루어집니다. 사용자는 특정한 롤에 할당되며, 롤에 따라 접근 가능한 리소스와 기능이 달라집니다. 

Java에서는 Spring Security 프레임워크를 통해 인가 기능을 구현할 수 있습니다. Spring Security는 보다 세부적인 권한 제어를 위한 애너테이션 기반의 접근 제어 기능을 제공합니다.

```java
import org.springframework.security.access.annotation.Secured;

public class AuthorizationExample {
    @Secured("ROLE_ADMIN")
    public void performAdminAction() {
        // 관리자 권한으로 수행할 작업
        System.out.println("Admin action performed");
    }

    @Secured({"ROLE_USER", "ROLE_ADMIN"})
    public void performUserAction() {
        // 사용자 혹은 관리자 권한으로 수행할 작업
        System.out.println("User action performed");
    }

    public void performPublicAction() {
        // 인증 없이 접근 가능한 작업
        System.out.println("Public action performed");
    }
}
```

위의 예제에서 `@Secured` 애너테이션은 메소드가 특정한 롤에 할당된 사용자만 호출 가능하도록 제한합니다.

## 결론

인증과 인가는 웹 애플리케이션 보안을 구축하는 데 필수적인 요소입니다. 인증은 사용자의 신원을 확인하는 과정이고, 인가는 사용자에게 부여된 권한에 따라 액세스를 제한하는 과정입니다. Java에서는 Spring Security 프레임워크를 사용하여 간편하게 인증과 인가 기능을 구현할 수 있습니다.

참고 자료:
- [Spring Security Documentation](https://docs.spring.io/spring-security)
- [Java SE Security Documentation](https://docs.oracle.com/en/java/javase/11/security/index.html)
- [OWASP - 인증(Authentication)과 인가(Authorization)](https://owasp.org/kr/www-project-application-security-verification-standard/other-security-requirements/identification-and-authentication)