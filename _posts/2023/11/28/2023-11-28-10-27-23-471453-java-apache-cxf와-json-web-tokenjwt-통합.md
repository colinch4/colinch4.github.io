---
layout: post
title: "[java] Java Apache CXF와 JSON Web Token(JWT) 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

## 개요
이 글은 Java에서 Apache CXF와 JSON Web Token(JWT)을 함께 사용하는 방법에 대해 설명합니다. Apache CXF는 Java에서 웹 서비스를 개발하고 실행하기 위한 오픈 소스 프레임워크입니다. JWT는 웹 애플리케이션에서 인증 및 인가를 처리하기 위해 사용되는 JSON 기반 토큰입니다.

## Apache CXF 설정
1. Apache CXF와 관련된 Maven 의존성을 추가합니다.

```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-rs-security-jose-jwt</artifactId>
        <version>3.4.4</version>
    </dependency>
    ...
</dependencies>
```

2. CXF 설정 파일인 `cxf.xml`을 만듭니다.

```xml
<beans xmlns="http://www.springframework.org/schema/beans">
    <import resource="classpath:META-INF/cxf/cxf.xml" />
    <import resource="classpath:META-INF/cxf/cxf-servlet.xml" />

    <jaxrs:server id="restContainer" address="/">
        <jaxrs:serviceBeans>
            <!-- REST 서비스 빈 등록 -->
        </jaxrs:serviceBeans>
        <jaxrs:providers>
            <bean class="org.apache.cxf.jaxrs.provider.json.JSONProvider" />
        </jaxrs:providers>
    </jaxrs:server>
</beans>
```

3. REST 서비스 클래스를 작성합니다. 다음은 간단한 예시입니다.

```java
@Path("/books")
public class BookService {

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public List<Book> getBooks() {
        List<Book> books = new ArrayList<>();
        // 책 목록 조회 로직
        return books;
    }

    // 추가적인 REST 메서드 작성
}
```

4. JWT 인증 필터를 작성합니다.

```java
public class JwtAuthenticationFilter implements ContainerRequestFilter {

    @Override
    public void filter(ContainerRequestContext requestContext) throws IOException {
        // JWT 인증 로직 작성
    }
}
```

5. `cxf.xml`에 JWT 인증 필터를 등록합니다.

```xml
<jaxrs:server id="restContainer" address="/">
    <jaxrs:serviceBeans>
        <!-- REST 서비스 빈 등록 -->
    </jaxrs:serviceBeans>
    <jaxrs:providers>
        <bean class="org.apache.cxf.jaxrs.provider.json.JSONProvider" />
        <bean class="com.example.JwtAuthenticationFilter" />
    </jaxrs:providers>
</jaxrs:server>
```

## JWT 생성 및 검증
JWT를 생성하고 검증하기 위해서는 다음과 같은 라이브러리를 사용할 수 있습니다.

1. `jjwt` 라이브러리 추가

```xml
<dependencies>
    ...
    <dependency>
        <groupId>io.jsonwebtoken</groupId>
        <artifactId>jjwt</artifactId>
        <version>0.9.1</version>
    </dependency>
    ...
</dependencies>
```

2. JWT 생성 예시

```java
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;

public class JwtUtils {

    public static String createJwt(String subject, String secretKey, long ttlMillis) {
        return Jwts.builder()
                .setSubject(subject)
                .signWith(SignatureAlgorithm.HS512, secretKey)
                .setExpiration(new Date(System.currentTimeMillis() + ttlMillis))
                .compact();
    }

}
```

3. JWT 검증 예시

```java
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;

public class JwtUtils {

    public static boolean validateJwt(String jwt, String secretKey) {
        try {
            Jwts.parser().setSigningKey(secretKey).parseClaimsJws(jwt);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

}
```

## 결론
이제 Java Apache CXF와 JSON Web Token(JWT)을 함께 사용하는 방법에 대해 알아보았습니다. CXF를 사용하여 웹 서비스를 개발하고 JWT를 사용하여 인증 및 인가를 처리할 수 있습니다. 이를 통해 보안이 강화된 웹 애플리케이션을 개발할 수 있습니다.

## 참고자료
- Apache CXF 공식 문서: [https://cxf.apache.org/](https://cxf.apache.org/)
- JWT 공식 사이트: [https://jwt.io/](https://jwt.io/)
- jjwt 라이브러리 GitHub: [https://github.com/jwtk/jjwt](https://github.com/jwtk/jjwt)