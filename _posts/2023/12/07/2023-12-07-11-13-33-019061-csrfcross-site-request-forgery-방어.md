---
layout: post
title: "[java] CSRF(Cross-site Request Forgery) 방어"
description: " "
date: 2023-12-07
tags: [java]
comments: true
share: true
---

웹 애플리케이션에서 CSRF(Cross-site Request Forgery)는 악성 사용자가 인증된 사용자의 권한을 이용하여 원치 않은 요청을 보내는 공격 형태입니다. 이를 방어하기 위해 몇 가지 기법들이 있습니다.

## 1. CSRF 토큰 사용

CSRF 공격을 방어하기 위한 가장 일반적인 방법은 CSRF 토큰을 사용하는 것입니다. 서버는 로그인 또는 세션에 관련된 CSRF 토큰을 생성하여 클라이언트에게 전달합니다. 클라이언트는 이 토큰을 폼 데이터나 AJAX 호출 등의 요청에 포함시켜야만 서버로 요청을 보낼 수 있습니다. 이렇게 함으로써 악성 사용자는 CSRF 토큰을 알지 못하기 때문에 요청을 위조할 수 없습니다.

```java
@RequestMapping(value = "/processForm", method = RequestMethod.POST)
public String processForm(@RequestParam("csrfToken") String csrfToken, Model model) {
    // CSRF 토큰 검증 로직
    if (isValid(csrfToken)) {
        // 요청 처리 로직
        return "success";
    } else {
        // 유효하지 않은 CSRF 토큰 처리 로직
        return "error";
    }
}
```

## 2. SameSite 쿠키 설정

SameSite 쿠키 설정을 통해 CSRF 공격의 위험을 줄일 수 있습니다. SameSite 쿠키의 설정값을 Strict 또는 Lax로 설정하면, 해당 도메인에서만 쿠키를 전송하고 타 도메인에서는 쿠키를 참조할 수 없게 됩니다. 이렇게 함으로써 CSRF 공격을 실행하는데 필요한 쿠키를 타 도메인에서 가져갈 수 없게 됩니다.

```java
HttpCookie cookie = new HttpCookie("session", "xxxx");
cookie.setSameSite("Strict");
response.addCookie(cookie);
```

## 3. Referrer 검증

Referrer 검증은 CSRF 공격을 방어하기 위한 추가적인 보안 기법입니다. Referrer 헤더를 검증하여 요청이 원래의 도메인에서 발생한 것인지 확인할 수 있습니다. 하지만 Referrer 헤더는 때때로 정상적인 요청에서도 값을 포함하지 않을 수 있기 때문에 완벽한 보안을 제공하지는 않습니다. 그래서 Referrer 검증은 CSRF 토큰과 같이 사용하는 것이 좋습니다.

```java
String referrer = request.getHeader("Referer");
if (isValidReferrer(referrer)) {
    // 요청 처리 로직
} else {
    // 유효하지 않은 Referrer 처리 로직
}
```

## 결론

CSRF(Cross-site Request Forgery)는 웹 애플리케이션에서 중요한 보안 취약점이므로 이를 방어하기 위한 조치가 필요합니다. CSRF 토큰 사용, SameSite 쿠키 설정, Referrer 검증 등의 기법을 적절히 사용하여 애플리케이션의 보안성을 향상시킬 수 있습니다.

참고 문헌:
- OWASP CSRF Cheat Sheet: [https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- Spring Security Documentation: [https://docs.spring.io/spring-security/site/docs/3.2.x/reference/html/csrf.html](https://docs.spring.io/spring-security/site/docs/3.2.x/reference/html/csrf.html)