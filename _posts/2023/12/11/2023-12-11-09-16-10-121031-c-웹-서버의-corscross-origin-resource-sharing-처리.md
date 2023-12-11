---
layout: post
title: "[c++] C++ 웹 서버의 CORS(Cross-Origin Resource Sharing) 처리"
description: " "
date: 2023-12-11
tags: [c++]
comments: true
share: true
---

CORS (Cross-Origin Resource Sharing)는 웹 애플리케이션의 보안을 강화하기 위해 도입된 웹 표준 메커니즘입니다. 이 표준은 브라우저와 서버 간의 통신을 제어하여 **한 출처에서 실행 중인 웹 페이지가 다른 출처의 리소스에 접근할 수 있도록 허용**합니다.

## CORS를 구현하는 방법

### 1. HTTP 헤더 설정

CORS를 구현하기 위해 먼저 HTTP 응답 헤더에 다음과 같은 헤더를 추가해야 합니다:

```cpp
Access-Control-Allow-Origin: <origin>
Access-Control-Allow-Methods: <methods>
Access-Control-Allow-Headers: <headers>
```

- `<origin>`: 접근을 허용하는 출처
- `<methods>`: 허용된 HTTP 메소드
- `<headers>`: 허용된 요청 헤더

### 2. 예시 코드

```cpp
response.set_header("Access-Control-Allow-Origin", "*");
response.set_header("Access-Control-Allow-Methods", "GET, POST,PUT, OPTIONS");
response.set_header("Access-Control-Allow-Headers", "Content-Type");
```

## C++ 웹 서버에서의 CORS 구현

C++ 웹 서버에서 **CORS를 구현**하려면 웹 서버 라이브러리, 예를 들어 **libmicrohttpd**나 **Cpp-Netlib**를 사용하거나 직접 **HTTP 응답 헤더를 설정**해야 합니다.

C++ 웹 서버에서 CORS를 설정함으로써 **웹 애플리케이션의 보안을 강화**하고 다른 출처의 리소스에 접근할 수 있는 기능을 제어할 수 있습니다.

## 결론

CORS는 다른 출처의 리소스에 접근할 수 있는 보안 메커니즘을 제공하며, C++ 웹 서버에서도 이 기능을 쉽게 구현할 수 있습니다. **HTTP 응답 헤더를 설정**하거나 **라이브러리를 활용**하여 CORS를 적절히 처리함으로써 웹 애플리케이션의 보안을 강화할 수 있습니다.

## 참고 자료

- [MDN Web Docs: HTTP access control (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)