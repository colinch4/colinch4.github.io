---
layout: post
title: "[java] Axis2와 CSRF(Cross-Site Request Forgery)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Axis2는 웹 서비스 클라이언트와 서버 사이에서 소통하기 위한 프레임워크입니다. 그러나, Axis2는 CSRF(Cross-Site Request Forgery) 공격에 취약한 경우가 있습니다. 이러한 공격은 웹 애플리케이션 보안을 위해 고려해야 할 중요한 측면입니다.

## CSRF 공격의 개요

CSRF 공격은 사용자가 악의적인 웹 사이트를 방문했을 때 발생할 수 있습니다. 이 사이트는 정상적으로 작동하는 웹 애플리케이션에 악의적인 요청을 보내는 HTML 또는 JavaScript를 제공합니다. 사용자가 이 사이트에 액세스할 때, 브라우저는 사용자의 인증 정보를 가지고 웹 애플리케이션에 요청을 보내게 됩니다. 이때, 사용자는 이 요청이 악의적인 요청임을 모르고 있는 상태입니다. 결과적으로, 웹 애플리케이션은 사용자의 인증 정보를 사용한 악의적인 동작을 수행하게 됩니다.

## Axis2에서 CSRF 공격 방지하기

Axis2에서 CSRF 공격을 방지하기 위해 다음과 같은 보안 메커니즘을 적용할 수 있습니다.

1. CSRF 토큰 사용: 웹 애플리케이션은 각 사용자 세션에 대해 고유한 CSRF 토큰을 생성합니다. 이 토큰은 웹 페이지에 포함된 숨겨진 필드나 HTTP 헤더를 통해 클라이언트로 전달됩니다. 이후에 발생하는 모든 요청은 이 토큰과 함께 보내져야 합니다. 서버는 이 토큰을 검증하여 요청의 유효성을 확인합니다.

2. SameSite 속성 활성화: SameSite 속성은 쿠키의 전송 방식을 제어하는 데 사용됩니다. SameSite 속성을 'Strict'로 설정하면, 해당 도메인이 아닌 경우에는 쿠키가 전송되지 않습니다. 이를 통해 외부 도메인에서의 CSRF 공격을 방지할 수 있습니다.

3. Referer 헤더 검증: Referer 헤더는 요청을 보낸 이전 웹 페이지의 URL을 포함하고 있습니다. 서버는 Referer 헤더를 검증하여 요청이 유효한 웹 페이지에서 온 것인지 확인할 수 있습니다. Referer 헤더 검증은 일부 상황에서 정상적인 요청을 막을 수 있으므로, 추가적인 조치가 필요할 수 있습니다.

## 결론

Axis2를 사용하는 웹 애플리케이션에서 CSRF 공격을 방지하기 위해서는 위에서 언급한 보안 메커니즘을 적용해야 합니다. CSRF 공격은 심각한 보안 문제로 여겨지므로, 웹 개발자는 이러한 공격을 예방하기 위한 적절한 조치를 취해야 합니다.

---

참고 문서:
- [OWASP CSRF Cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)