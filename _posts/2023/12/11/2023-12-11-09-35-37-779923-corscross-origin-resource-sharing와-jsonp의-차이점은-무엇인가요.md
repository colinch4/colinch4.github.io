---
layout: post
title: "[typescript] CORS(Cross-Origin Resource Sharing)와 JSONP의 차이점은 무엇인가요?"
description: " "
date: 2023-12-11
tags: [typescript]
comments: true
share: true
---

### CORS (Cross-Origin Resource Sharing)
CORS는 웹 애플리케이션에서 다른 출처로부터의 리소스 요청을 보안적으로 안전하게 허용하기 위한 W3C 표준 기술입니다. 이를 통해 웹 브라우저는 서버로부터의 리소스 요청이 안전한지 사전 요청(preflight request)하여 확인하고, 안전한 경우에만 실제 요청을 보내게 됩니다. 이를 통해 권한 없이 다른 출처의 리소스에 접근하는 것을 방지합니다.

#### 장점
- 브라우저와 서버 간의 안전한 교차 출처 요청을 가능하게 함
- 표준 기술로써 널리 지원되고 있음

#### 단점
- 복잡한 설정과 이해가 필요함
- 구현이 잘못된 경우 보안에 취약해질 수 있음

### JSONP (JSON with Padding)
JSONP는 JSON 데이터를 다른 출처로부터 가져오는 방법 중 하나로, script 태그를 이용하여 다른 도메인의 자원을 요청하는 간단한 방법입니다. 요청하는 URL 뒤에 콜백 함수명을 지정하여 응답을 받게 되는데, 이 콜백 함수를 이용하여 데이터를 처리합니다.

#### 장점
- 간단하고 브라우저에서 교차 출처 요청을 우회할 수 있음
- 구현이 간단함

#### 단점
- 보안상의 취약점이 존재함
- JSONP 요청을 위해 서버 측에서 콜백 함수를 지원해야 함

### 결론
CORS는 브라우저와 서버 간의 안전한 교차 출처 요청을 가능케 해주는 표준 기술이며, JSONP는 간단하고 빠르게 교차 출처 요청을 처리할 수 있는 방법입니다. CORS는 보안 측면에서 더 안전하고, JSONP는 낮은 호환성을 지원하는 서버 환경에서 유용할 수 있습니다.

더 자세한 내용은 [Mozilla 개발자 네트워크](https://developer.mozilla.org/ko/docs/Web/HTTP/CORS)에서 확인할 수 있습니다.