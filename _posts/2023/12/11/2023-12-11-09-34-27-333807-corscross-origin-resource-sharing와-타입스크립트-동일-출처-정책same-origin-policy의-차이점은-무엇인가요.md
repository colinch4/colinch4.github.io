---
layout: post
title: "[typescript] CORS(Cross-Origin Resource Sharing)와 타입스크립트 동일 출처 정책(Same Origin Policy)의 차이점은 무엇인가요?"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

CORS(Cross-Origin Resource Sharing)와 타입스크립트의 동일 출처 정책(Same Origin Policy)은 모두 웹 보안에 관련된 중요한 개념이지만, 각각의 역할과 동작 방식에는 몇 가지 주요한 차이가 있습니다. 이 블로그 포스트에서는 그 차이에 대해 살펴보겠습니다.

## 동일 출처 정책(Same Origin Policy)

먼저, 타입스크립트의 동일 출처 정책에 대해 간단히 알아보겠습니다. 동일 출처 정책은 **같은 출처(origin)에서 로드된 문서나 스크립트의 리소스에만 접근을 허용**하는 보안 방침입니다. 출처란 프로토콜, 호스트, 포트가 모두 동일한 경우를 말합니다. 이 정책은 웹 보안을 유지하기 위한 중요한 원칙 중 하나입니다.

## CORS(Cross-Origin Resource Sharing)

한편, CORS는 **웹 페이지가 다른 출처의 리소스에 접근할 수 있도록 하는 메커니즘**을 가리킵니다. 기본적으로 동일 출처 정책에 의해 차단되는 클라이언트 사이드 스크립트에서 다른 출처의 리소스에 안전하게 접근할 수 있도록 하는 것이 CORS의 주요 목적입니다. 이를 통해 웹 애플리케이션은 다른 도메인에 있는 서비스를 활용할 수 있게 되며, API 호출 등의 작업이 가능해집니다.

## 차이점

주요한 차이점은 다음과 같습니다:

- **대상**: 타입스크립트의 동일 출처 정책은 웹 보안을 유지하기 위해 사용되는 정책이며, CORS는 다른 출처의 리소스에 안전하게 접근할 수 있는 메커니즘입니다.

- **목적**: 동일 출처 정책은 웹 페이지 보안을 강화하는 데 초점을 두고 있으며, CORS는 클라이언트 측 스크립트에서 다른 출처의 리소스에 안전하게 접근할 수 있도록 하는 것이 주요 목적입니다.

이렇게, CORS와 타입스크립트의 동일 출처 정책은 각각의 역할과 목적에 따라 명확한 차이가 있습니다. 이를 이해하고 적절하게 활용함으로써 웹 애플리케이션 개발 및 보안 강화에 도움이 될 것입니다.

더 자세한 내용은 [Mozilla의 CORS 문서](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)와 [MDN Web Docs의 동일 출처 정책](https://developer.mozilla.org/ko/docs/Web/Security/Same-origin_policy)를 참고하시기 바랍니다.