---
layout: post
title: "[java] Java Play Framework에서의 XSRF 공격 대응 방법은 어떻게 되나요?"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

XSRF(Cross-Site Request Forgery)은 악성 사용자가 인증된 사용자의 권한을 이용하여 의도하지 않은 요청을 보내는 공격입니다. Java Play Framework에서는 이러한 XSRF 공격을 방지하기 위해 기본적으로 보안 기능을 제공합니다.

Play Framework에서 XSRF 공격에 대응하기 위해 다음과 같은 방법을 사용할 수 있습니다.

1. CSRF 필터 적용: Play Framework는 CSRF 필터를 제공하여 XSRF 공격을 방지할 수 있습니다. 이 필터를 적용하면 모든 POST 요청에 대해 CSRF 토큰을 확인하고 검증하게 됩니다. CSRF 필터를 적용하려면 `play.filters.csrf.CSRFFilter`를 `application.conf` 파일에 추가해야 합니다.

   ```
   play.filters.enabled += "play.filters.csrf.CSRFFilter"
   ```

2. CSRF 토큰 사용: Play Framework에서는 CSRF 토큰을 사용하여 보안을 강화할 수 있습니다. CSRF 토큰은 모든 POST 요청에 대해 생성되고 요청과 함께 전송됩니다. 요청이 서버로 도착할 때, 서버에서는 CSRF 토큰을 검증하여 요청이 유효한지 확인합니다. Play Framework에서는 CSRF 토큰을 생성하기 위해 `@CSRF` 어노테이션을 사용할 수 있습니다.

   ```java
   public Result submitForm() {
       // CSRF 토큰 생성
       String token = CSRF.getToken(request).map(CSRF.Token::value).orElse("");
       
       // 템플릿에 CSRF 토큰 전달
       return ok(form.render(token));
   }
   ```

   ```html
   <!-- 템플릿에서 CSRF 토큰 사용 -->
   <form action="/submit" method="post">
       <input type="hidden" name="csrfToken" value="@token">
       <!-- 입력 필드 등 -->
       <input type="submit" value="Submit">
   </form>
   ```

이 외에도 Play Framework에서는 HTTPS를 사용하여 통신을 암호화하거나, HTTP Only 속성을 사용하여 쿠키의 접근을 제한하는 등 다양한 방법을 사용하여 보안을 강화할 수 있습니다. 

참고문서:
- [Play Framework 공식 문서 - CSRF 보안](https://www.playframework.com/documentation/2.8.x/JavaCsrf)
- [Play Framework 공식 문서 - CSRF 토큰 생성](https://www.playframework.com/documentation/2.8.x/JavaCsrf#Creating-a-CSRF-Token)