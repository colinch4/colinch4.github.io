---
layout: post
title: "[typescript] CORS(Cross-Origin Resource Sharing)에서의 출처(Origin)란 무엇인가요?"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

CORS는 웹 브라우저에서 실행 중인 스크립트가 다른 출처(origin)에 있는 리소스에 접근할 수 있는 권한을 부여하는 메커니즘입니다. 출처는 프로토콜 (예: https), 호스트(예: www.example.com), 포트(예: 443)의 조합으로 정의됩니다.

출처는 리소스에 접근하는 도메인을 식별하고, 웹 브라우저가 보안 상의 이유로 이 출처와의 상호작용을 제어할 수 있도록 합니다. 출처가 서로 다를 경우, CORS 정책에 따라 추가 HTTP 헤더가 필요하며, 이를 통해 다른 출처의 리소스에 안전하게 접근할 수 있습니다.

이러한 CORS 정책은 보안을 유지하면서도 다른 출처 간의 상호작용을 가능하게 합니다. 이를 통해 웹 애플리케이션은 다른 도메인에 있는 리소스를 활용하여 보다 다양하고 풍부한 사용자 경험을 제공할 수 있습니다.