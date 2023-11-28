---
layout: post
title: "[java] Tomcat의 CSRF(Cross-Site Request Forgery) 방어 기법"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

CSRF(Cross-Site Request Forgery)는 웹 응용 프로그램에서 발생할 수 있는 보안 취약점 중 하나입니다. 이 공격은 인증된 사용자의 동의 없이 악의적인 웹 사이트에서 해당 사용자의 자원에 접근하는 것을 가능하게 합니다. 이러한 공격으로부터 Tomcat 서버를 보호하기 위해 CSRF 방어 기법을 적용할 수 있습니다. 

## CSRF 방어 기법

1. CSRF 토큰 사용: 모든 웹 요청에 대한 유효성 검사를 위해 CSRF 토큰을 사용합니다. 이 토큰은 사용자의 세션과 연결됩니다. 클라이언트로부터의 요청마다 CSRF 토큰을 제공해야 합니다. 

2. SameSite 속성 설정: SameSite 속성을 설정하여 다른 도메인에서의 요청을 제한할 수 있습니다. 이렇게 하면 악의적인 웹 사이트가 사용자의 자격 증명을 가로채지 못하게 할 수 있습니다.

3. Origin 검증: 모든 웹 요청에 대해 원래 요청이 작성된 origin과 현재 origin을 비교하여 검증하는 방법입니다. 이를 통해 악의적인 사이트로부터의 요청을 거부할 수 있습니다.

## Tomcat에서 CSRF 방어 기법 활성화하기

Tomcat에서 CSRF 방어 기능을 활성화하려면 다음 설정을 수행해야 합니다.

1. `web.xml` 파일에서 보안 제한을 위해 CSRF 필터를 추가합니다.

```xml
<filter>
    <filter-name>CSRF</filter-name>
    <filter-class>org.apache.catalina.filters.CsrfPreventionFilter</filter-class>
    <init-param>
        <param-name>entryPoints</param-name>
        <param-value>/example1/*,/example2/*</param-value>
    </init-param>
</filter>
<filter-mapping>
    <filter-name>CSRF</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

2. `context.xml` 파일에 CSRF 필터의 정의를 추가합니다.

```xml
<Context>
    <Valve className="org.apache.catalina.valves.RemoteAddrValve" />
    <Valve className="org.apache.catalina.valves.CsrfPreventionValve"
           denyStatus="403"
           maxTokens="20"
           methodGet="true"
           methodHead="true"
           methodPost="true"
           methodPut="true"
           methodDelete="true"
           methodOptions="true"
           methodTrace="true"
           parameter="csrf_token"
           headerName="X-Csrf-Token"
           nonceCacheSize="20"
           paranoid="true"/>
</Context>
```

이 설정을 통해 Tomcat 서버는 CSRF 공격으로부터 보호됩니다.

## 참고 자료

- [Tomcat Documentation](https://tomcat.apache.org/tomcat-8.5-doc/config/filter.html#CSRF_Prevention_Filter)
- [OWASP CSRF](https://owasp.org/www-community/attacks/csrf)