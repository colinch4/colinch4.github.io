---
layout: post
title: "[java] Axis2와 CORS(Cross-Origin Resource Sharing)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

## 소개
Axis2는 Apache Software Foundation에서 개발한 웹 서비스 프레임워크입니다. 이 프레임워크를 사용하여 웹 서비스를 개발하고 배포할 수 있으며, 다양한 클라이언트 애플리케이션과 통신할 수 있는 기능을 제공합니다.

하지만, 일반적으로 웹 애플리케이션은 동일 출처 정책(Same-Origin Policy)에 따라 동일한 출처에서만 리소스를 요청할 수 있습니다. 이는 웹 애플리케이션의 보안을 위해 도입된 정책으로, 다른 출처에서 리소스를 요청할 경우 보안상의 이유로 차단됩니다.

이러한 문제를 해결하기 위해 등장한 것이 CORS(Cross-Origin Resource Sharing)입니다. CORS는 웹 애플리케이션에게 서로 다른 출처에서 리소스 요청을 허용하는 방법을 제공합니다. 이는 웹 애플리케이션 간의 상호 작용을 가능하게 해주는 중요한 기술입니다.

## Axis2에서 CORS 사용하기
Axis2는 기본적으로 CORS를 지원하지 않습니다. 하지만, 서버 측에서 몇 가지 설정을 통해 CORS를 적용할 수 있습니다.

먼저, Axis2 서버의 `axis2.xml` 파일을 엽니다. 이 파일은 Axis2의 구성 정보를 담고 있습니다.

다음으로, `axis2.xml` 파일에서 `<transportReceiver>` 요소 안에 `<parameter>` 요소를 추가합니다. 이 요소는 CORS 관련 설정을 포함할 수 있습니다. 예를 들어, 다음과 같이 설정할 수 있습니다.

```xml
<transportReceiver name="http" class="org.apache.axis2.transport.http.AxisServletListener">
    <parameter name="cors.allowOrigin">http://example.com</parameter>
    <parameter name="cors.allowMethods">GET, POST, OPTIONS</parameter>
    <parameter name="cors.allowHeaders">Content-Type</parameter>
    <parameter name="cors.allowCredentials">false</parameter>
</transportReceiver>
```

위 설정에서 `cors.allowOrigin`은 CORS 요청을 허용할 출처를 설정하는 것이고, `cors.allowMethods`는 허용할 HTTP 메소드를 설정하는 것입니다. `cors.allowHeaders`는 허용할 HTTP 헤더를 설정하며, `cors.allowCredentials`는 자격 증명을 포함할 것인지 여부를 설정합니다.

이렇게 Axis2 서버에 CORS 설정을 추가하면, 웹 애플리케이션이 다른 출처에서 해당 리소스를 요청할 수 있게 됩니다.

## 결론
Axis2는 CORS를 기본적으로 지원하지 않지만, 서버 측에서 몇 가지 설정을 통해 CORS를 적용할 수 있습니다. CORS를 사용하면 웹 애플리케이션이 다른 출처에서 리소스를 요청할 수 있으므로, 서로 다른 애플리케이션 간의 협업을 효과적으로 구현할 수 있습니다.

## 참고 자료
- [Apache Axis2 공식 사이트](https://axis.apache.org/axis2/java/core/docs/index.html)
- [Cross-Origin Resource Sharing (CORS) - Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)