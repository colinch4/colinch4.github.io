---
layout: post
title: "[java] XSRF(Cross-Site Request Forgery) 방어"
description: " "
date: 2023-12-07
tags: [java]
comments: true
share: true
---

XSRF(Cross-Site Request Forgery)는 웹 애플리케이션에서 발생할 수 있는 보안 취약점 중 하나입니다. XSRF 공격은 사용자가 의도하지 않은 요청을 악의적인 공격자가 해당 사용자의 권한으로 보내는 것을 의미합니다. 이는 해당 사용자의 신뢰성 있는 액션을 동반하는 악성 요청을 사용하는 공격입니다.

## XSRF 방어 기법

XSRF 공격으로부터 웹 애플리케이션을 보호하기 위해 몇 가지 기본적인 방어 기법을 적용할 수 있습니다.

### 1. 동일 출처 정책(Same-Origin Policy)

동일 출처 정책은 웹 브라우저가 웹 페이지에서 불러온 리소스가 동일한 출처에서 로딩되었는지 확인하는 보안 메커니즘입니다. 따라서, 서로 다른 출처에서 실행되는 스크립트나 리소스는 상호 간에 직접적인 접근이 불가능합니다. 이는 XSRF와 같은 공격으로부터 웹 애플리케이션을 보호하는데 중요한 역할을 합니다.

### 2. CSRF 토큰 사용

CSRF 토큰은 사용자의 세션에 생성되는 일회성 토큰입니다. 웹 애플리케이션은 이 토큰을 포함한 폼을 제공하고, 사용자의 모든 POST 요청에 이 토큰을 첨부합니다. 서버는 요청을 받을 때마다 토큰의 유효성을 확인하고, 유효하지 않은 요청은 처리하지 않습니다. 이를 통해 XSRF 공격을 탐지하고 예방할 수 있습니다.

### 3. SameSite 쿠키 속성 사용

SameSite 쿠키 속성은 브라우저가 쿠키를 언제 전송할지 제어하는 기능입니다. SameSite 속성을 "Strict"으로 설정하면, 쿠키는 동일한 사이트에서만 요청에 함께 전송됩니다. 따라서 외부 사이트에서의 XSS 공격 등으로부터 보호될 수 있습니다.

## 결론

XSRF(Cross-Site Request Forgery)는 웹 애플리케이션에서 중요한 보안 취약점 중 하나입니다. 이를 방어하기 위해 동일 출처 정책, CSRF 토큰 사용, SameSite 쿠키 속성 등의 방어 기법을 적용할 수 있습니다. 웹 애플리케이션의 보안을 강화하기 위해서는 XSRF 방어를 고려해야 합니다.

참고 자료:
- OWASP: [Cross-Site Request Forgery](https://owasp.org/www-community/attacks/csrf)
- MDN Web Docs: [Same-Origin Policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)
- OWASP Cheat Sheet: [CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- OWASP Cheat Sheet: [SameSite Attribute](https://cheatsheetseries.owasp.org/cheatsheets/SameSite_Cheat_Sheet.html)