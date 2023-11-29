---
layout: post
title: "[java] Java Jersey에서 로그인 인증을 위한 JSON Web Token (JWT) 구현하는 방법은?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

## 소개
JSON Web Token (JWT)은 웹 애플리케이션에서 사용자 인증과 권한 부여를 위해 사용되는 인증 방식입니다. JWT는 클라이언트와 서버 간의 안전한 정보 교환을 위해 사용되며, 서버의 세션 관리가 필요하지 않습니다. 이번 포스트에서는 Java Jersey에서 JWT를 구현하는 방법에 대해 알아보겠습니다.

## 의존성 추가
JWT를 구현하기 위해 먼저 Maven 또는 Gradle을 사용하여 관련 의존성을 추가해야 합니다. 다음은 Maven을 사용할 경우 `pom.xml`에 추가해야 하는 의존성 정보입니다.

```xml
<dependencies>
    <dependency>
        <groupId>io.jsonwebtoken</groupId>
        <artifactId>jjwt-api</artifactId>
        <version>0.11.2</version>
    </dependency>
    <dependency>
        <groupId>io.jsonwebtoken</groupId>
        <artifactId>jjwt-impl</artifactId>
        <version>0.11.2</version>
        <scope>runtime</scope>
    </dependency>
    <dependency>
        <groupId>io.jsonwebtoken</groupId>
        <artifactId>jjwt-jackson</artifactId>
        <version>0.11.2</version>
        <scope>runtime</scope>
    </dependency>
</dependencies>
```

Gradle을 사용하는 경우 `build.gradle`에 다음과 같이 의존성을 추가해야 합니다.

```groovy
dependencies {
    implementation 'io.jsonwebtoken:jjwt-api:0.11.2'
    runtimeOnly 'io.jsonwebtoken:jjwt-impl:0.11.2'
    runtimeOnly 'io.jsonwebtoken:jjwt-jackson:0.11.2'
}
```

## JWT 생성 및 검증
다음은 JWT를 생성하고 검증하는 예제 코드입니다. 

```java
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jws;
import io.jsonwebtoken.Jwts;

public class JwtUtil {

    private static final String SECRET_KEY = "your-secret-key";

    public static String generateJwt(String username, long expirationTime) {
        return Jwts.builder()
                .setSubject(username)
                .setExpiration(new Date(System.currentTimeMillis() + expirationTime))
                .signWith(SignatureAlgorithm.HS256, SECRET_KEY)
                .compact();
    }

    public static String getUsernameFromJwt(String jwt) {
        Claims claims = Jwts.parser()
                .setSigningKey(SECRET_KEY)
                .parseClaimsJws(jwt)
                .getBody();

        return claims.getSubject();
    }

    public static boolean validateJwt(String jwt) {
        try {
            Jwts.parser().setSigningKey(SECRET_KEY).parseClaimsJws(jwt);
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}
```

위의 예제 코드에서 `generateJwt()` 메서드는 주어진 사용자 이름과 만료 시간을 기반으로 JWT를 생성합니다. `getUsernameFromJwt()` 메서드는 주어진 JWT에서 사용자 이름을 추출하여 반환합니다. `validateJwt()` 메서드는 주어진 JWT가 유효한지 검증하고 결과를 반환합니다. 

## JWT 사용 예제
다음은 Java Jersey에서 JWT를 사용하는 간단한 예제입니다.

```java
import javax.ws.rs.GET;
import javax.ws.rs.HeaderParam;
import javax.ws.rs.Path;
import javax.ws.rs.core.Response;

@Path("/secured")
public class SecuredResource {

    @GET
    public Response securedEndpoint(@HeaderParam("Authorization") String jwt) {
        if (JwtUtil.validateJwt(jwt)) {
            // JWT가 유효한 경우에만 접근 허용
            return Response.ok("인증 성공").build();
        } else {
            return Response.status(Response.Status.UNAUTHORIZED).build();
        }
    }
}
```

위의 예제 코드에서 `securedEndpoint()` 메서드는 `Authorization` 헤더에서 받은 JWT를 검증하고, 유효한 JWT인 경우에만 접근을 허용합니다.

## 결론
이번 포스트에서는 Java Jersey에서 JSON Web Token (JWT)을 구현하는 방법을 알아보았습니다. JWT를 사용하면 클라이언트와 서버 간의 안전한 인증과 권한 부여를 구현할 수 있습니다. 이러한 기술은 웹 애플리케이션의 보안을 강화하는 데 도움이 됩니다.

더 자세한 정보와 예제 코드를 보려면 [JWT 홈페이지](https://jwt.io/)를 참고하세요.