---
layout: post
title: "[java] Tomcat의 CORS(Cross-Origin Resource Sharing) 설정 방법"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

CORS는 웹 애플리케이션이 다른 도메인에서 리소스를 요청하는 것을 허용하는 보안 메커니즘입니다. 자바로 작성된 웹 애플리케이션인 Tomcat에서 CORS를 설정하는 방법에 대해 알아보겠습니다.

## 1. web.xml을 사용하는 방법

web.xml 파일을 사용하여 Tomcat에서 CORS를 설정할 수 있습니다. 아래 예시를 참고하여 설정해보세요.

```xml
<web-app>
  <filter>
    <filter-name>CorsFilter</filter-name>
    <filter-class>org.apache.catalina.filters.CorsFilter</filter-class>
    <init-param>
      <param-name>cors.allowed.origins</param-name>
      <param-value>*</param-value>
    </init-param>
  </filter>
  
  <filter-mapping>
    <filter-name>CorsFilter</filter-name>
    <url-pattern>/*</url-pattern>
  </filter-mapping>
</web-app>
```

위의 예시에서 `cors.allowed.origins`의 값을 원하는 도메인으로 설정할 수 있습니다. `*`를 사용하면 모든 도메인에서 요청이 허용됩니다. `url-pattern`은 CORS 필터를 적용할 URL 패턴을 지정하는데, 위의 예시는 모든 URL에서 CORS 필터를 적용합니다.

## 2. Filter 클래스를 사용하는 방법

Filter 클래스를 직접 작성하여 Tomcat에서 CORS를 설정할 수도 있습니다. 아래 예시를 참고하여 필터 클래스를 작성해보세요.

```java
import javax.servlet.*;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class CorsFilter implements Filter {

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        HttpServletResponse httpServletResponse = (HttpServletResponse) response;
        httpServletResponse.setHeader("Access-Control-Allow-Origin", "*");
        httpServletResponse.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
        httpServletResponse.setHeader("Access-Control-Allow-Headers", "Content-Type");
        chain.doFilter(request, response);
    }
    
    // init() 메서드와 destroy() 메서드는 비워둬도 됩니다.

}
```

위의 예시에서는 `doFilter` 메서드에서 CORS 관련 헤더를 설정해줍니다. `Access-Control-Allow-Origin`은 허용할 도메인, `Access-Control-Allow-Methods`은 허용할 HTTP 메서드, `Access-Control-Allow-Headers`는 허용할 헤더 정보를 설정합니다.

## 참고자료

- [Apache Tomcat - CORS Filter](https://tomcat.apache.org/tomcat-9.0-doc/config/filter.html#CORS_Filter)
- [MDN Web Docs - HTTP access control (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)