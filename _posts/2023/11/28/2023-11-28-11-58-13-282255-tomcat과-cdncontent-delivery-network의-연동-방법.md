---
layout: post
title: "[java] Tomcat과 CDN(Content Delivery Network)의 연동 방법"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

CDN(Content Delivery Network)은 웹 콘텐츠를 전 세계 여러 대의 서버에 분산 저장하고 사용자에게 더 빠른 콘텐츠 전송을 제공하는 서비스입니다. 이러한 CDN을 사용하면 웹 애플리케이션의 성능과 로딩 시간을 크게 향상시킬 수 있습니다. 이번 글에서는 Tomcat과 CDN의 연동 방법에 대해 알아보겠습니다.

## 1. CDN 설정

먼저, CDN에서 제공하는 액세스 키를 획득해야 합니다. 이 액세스 키는 CDN에 콘텐츠를 업로드하고 다운로드할 때 사용됩니다. CDN 제공업체의 문서나 관리자 페이지를 참고하여 액세스 키를 발급받아야 합니다.

## 2. 웹 애플리케이션 설정

Tomcat의 `web.xml` 파일을 편집하여 CDN을 사용하도록 설정해야합니다. 아래는 예제 코드입니다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                       http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">

    <filter>
        <filter-name>CDNFilter</filter-name>
        <filter-class>com.example.CDNFilter</filter-class>
    </filter>
    
    <filter-mapping>
        <filter-name>CDNFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>

</web-app>
```

위의 코드에서 `<filter>`와 `<filter-mapping>` 태그를 추가하여 CDNFilter를 등록합니다. CDNFilter는 사용자의 요청을 가로채서 CDN에서 콘텐츠를 가져오도록 설정합니다.

## 3. CDNFilter 구현

이제 CDNFilter를 구현해야합니다. 아래는 예제 코드입니다.

```java
package com.example;

import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class CDNFilter implements Filter {

    private static final String CDN_BASE_URL = "https://cdn.example.com/";
    private static final String[] ALLOWED_EXTENSIONS = {".css", ".js", ".png", ".jpg", ".jpeg"};

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // 필요한 초기화 작업 수행
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        HttpServletRequest httpRequest = (HttpServletRequest) request;
        HttpServletResponse httpResponse = (HttpServletResponse) response;

        String requestUri = httpRequest.getRequestURI();
        boolean isStaticContent = checkIfStaticContent(requestUri);

        if (isStaticContent) {
            // CDN URL로 리다이렉션
            String cdnUrl = CDN_BASE_URL + requestUri;
            httpResponse.sendRedirect(cdnUrl);
        } else {
            // 요청 그대로 처리
            chain.doFilter(httpRequest, httpResponse);
        }
    }

    @Override
    public void destroy() {
        // 필요한 마무리 작업 수행
    }

    private boolean checkIfStaticContent(String requestUri) {
        for (String extension : ALLOWED_EXTENSIONS) {
            if (requestUri.endsWith(extension)) {
                return true;
            }
        }
        return false;
    }
}
```

위의 코드에서 `CDN_BASE_URL`은 CDN의 기본 URL로 변경해야하며, `ALLOWED_EXTENSIONS` 배열에는 CDN으로 업로드할 허용되는 정적 콘텐츠 확장자를 지정해야합니다.

## 결론

위의 설정 및 코드를 통해 Tomcat과 CDN을 연동할 수 있습니다. CDN을 통해 웹 애플리케이션의 성능을 향상시키고, 사용자에게 더 빠른 로딩 속도를 제공할 수 있습니다.

관련 참조:
- [Apache Tomcat 공식 문서](https://tomcat.apache.org/tomcat-9.0-doc/index.html)
- [CDN 제공업체 문서](https://www.example-cdn-provider.com/documentation)
- [CDNFilter 예제 코드](https://github.com/example/cdn-filter)