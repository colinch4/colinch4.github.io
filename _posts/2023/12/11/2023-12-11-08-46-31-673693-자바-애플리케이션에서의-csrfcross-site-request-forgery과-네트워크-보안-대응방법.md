---
layout: post
title: "[java] 자바 애플리케이션에서의 CSRF(Cross-Site Request Forgery)과 네트워크 보안 대응방법"
description: " "
date: 2023-12-11
tags: [java]
comments: true
share: true
---

CSRF(Cross-Site Request Forgery)는 웹 애플리케이션에서 발생하는 보안 취약점 중 하나로, 사용자가 의도하지 않은 요청을 보내는 공격을 말합니다. 이는 악의적인 사이트나 이메일을 통해 해당 요청을 실행하도록 유도함으로써 이루어집니다. CSRF 공격이 성공하면 해당 요청을 보낸 사용자의 계정으로 인증된 요청이 실행되게 됩니다.

## CSRF 공격 대응 방법

CSRF 공격으로부터 안전한 자바 애플리케이션을 설계하기 위해서는 다음과 같은 대응 방법을 고려해야 합니다.

1. **CSRF 토큰 사용**: 사용자의 세션과 연관된 CSRF 토큰을 생성하여, 모든 중요한 요청에 이를 포함시켜야 합니다. 이를 통해 악의적인 사이트에서 요청을 위변조하는 것을 방지할 수 있습니다.

예시:
```java
@RequestMapping(value = "/changePassword", method = RequestMethod.POST)
public String changePassword(@RequestParam("newPassword") String newPassword, HttpSession session) {
    String csrfToken = session.getAttribute("csrfToken");
    // CSRF 토큰을 검증하는 로직 추가
    // ...
}
```

2. **SameSite 쿠키 옵션 사용**: SameSite 쿠키 옵션을 사용하여, 웹 애플리케이션이 타 도메인에서의 요청에 대해 쿠키를 전송하지 않도록 설정할 수 있습니다.

예시:
```java
response.addHeader("Set-Cookie", "sessionid=ABCDEFG; SameSite=Strict");
```

3. **Referrer 검증**: HTTP 요청 헤더의 Referrer 값을 검증하여, 요청이 원래의 출처에서 온 것인지 확인할 수 있습니다.

## 결론

CSRF 공격은 웹 애플리케이션에서 중요한 보안 이슈 중 하나이며, 위에서 언급한 대응 방법들을 통해 안전한 애플리케이션을 설계할 수 있습니다. 개발자는 이러한 보안 이슈에 대한 이해와 대응 방법들에 대해 항상 주의할 필요가 있습니다.

[OWASP CSRF 공격 대응 방법](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)