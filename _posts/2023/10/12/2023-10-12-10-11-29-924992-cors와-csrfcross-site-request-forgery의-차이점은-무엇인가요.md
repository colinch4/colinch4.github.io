---
layout: post
title: "CORS와 CSRF(Cross-Site Request Forgery)의 차이점은 무엇인가요?"
description: " "
date: 2023-10-12
tags: []
comments: true
share: true
---

CORS(Cross-Origin Resource Sharing)는 웹 브라우저에서 발생하는 Cross-Origin 요청을 제어하기 위한 보안 메커니즘입니다. Cross-Origin 요청은 동일한 출처가 아닌 서로 다른 도메인, 포트, 프로토콜에서 리소스를 요청하는 것을 말합니다. 이는 보안 상의 이유로 기본적으로 제한되어 있습니다. CORS는 서버에서 설정되는 헤더를 사용하여 Cross-Origin 요청을 허용하기 위한 정책을 정의합니다. 즉, 서버에서 명시적으로 허용하는 도메인에서만 Cross-Origin 요청이 가능하도록 제어하는 것입니다.

반면에 CSRF(Cross-Site Request Forgery)는 인증된 사용자가 자신의 의지와 무관하게 공격자의 의도에 따라 악의적인 요청을 보내는 공격입니다. 이는 사용자가 악성 웹사이트를 방문하여 악용될 수 있습니다. 예를 들어, 공격자가 피해자의 계정으로 자금 이체 요청을 보내는 것입니다. 이를 방지하기 위해 CSRF 토큰을 사용하여 요청의 유효성을 검증하거나, Referer 헤더를 검증하는 등의 추가적인 보안 메커니즘이 필요합니다.

따라서, CORS는 서로 다른 도메인간의 통신을 안전하게 제어하기 위한 메커니즘입니다. CSRF는 인증된 사용자의 요청을 방지하기 위한 메커니즘입니다. 이 두 가지 개념은 각각 다른 취약점을 방지하기 위해 사용됩니다.