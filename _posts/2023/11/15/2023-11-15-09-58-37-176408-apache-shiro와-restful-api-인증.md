---
layout: post
title: "[java] Apache Shiro와 RESTful API 인증"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

## 목차

- [Apache Shiro 소개](#apache-shiro-소개)
- [RESTful API 인증](#restful-api-인증)
- [Apache Shiro를 사용한 RESTful API 인증 구현](#apache-shiro를-사용한-restful-api-인증-구현)

## Apache Shiro 소개

Apache Shiro는 자바 기반의 오픈 소스 보안 프레임워크로, 인증, 인가, 세션 관리 등의 기능을 제공합니다. Shiro는 간단한 설정만으로 다양한 보안 요구사항을 처리할 수 있고, 웹 애플리케이션, RESTful API, 분산 시스템 등 다양한 환경에서 활용될 수 있습니다.

## RESTful API 인증

RESTful API는 HTTP를 기반으로 한 웹 서비스 아키텍처로, 클라이언트와 서버 간의 통신을 위해 자원을 사용합니다. 이러한 RESTful API를 보호하기 위해서는 클라이언트의 신원을 확인하고, 요청된 작업의 권한을 확인하는 인증과 인가 기능이 필요합니다.

인증은 사용자의 신원을 확인하는 과정으로, 주로 아이디와 비밀번호를 사용하여 사용자를 인증합니다. 인가는 인증된 사용자의 권한을 확인하여 요청된 작업이 허용되는지 검사하는 과정입니다.

## Apache Shiro를 사용한 RESTful API 인증 구현

Apache Shiro를 사용하면 RESTful API의 인증과 인가를 간편하게 구현할 수 있습니다. 다음은 Apache Shiro를 사용하여 RESTful API 인증을 구현하는 간단한 예제 코드입니다.

```java
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.AuthenticationException;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.subject.Subject;

@Path("/login")
public class LoginResource {

    @POST
    public Response login(@FormParam("username") String username,
                          @FormParam("password") String password) {
        Subject currentUser = SecurityUtils.getSubject();
        if (!currentUser.isAuthenticated()) {
            UsernamePasswordToken token = new UsernamePasswordToken(username, password);
            try {
                currentUser.login(token);
            } catch (AuthenticationException e) {
                return Response.status(Response.Status.UNAUTHORIZED).build();
            }
        }
        return Response.ok().build();
    }
}
```

위의 코드는 `/login` 엔드포인트에서 클라이언트의 아이디와 비밀번호를 받아 인증을 수행하는 기능을 구현한 예제입니다. Apache Shiro의 `SecurityUtils`를 사용하여 현재 사용자를 가져오고, 로그인이 되어있지 않은 경우에만 인증을 시도합니다. 인증에 실패한 경우 `Response.Status.UNAUTHORIZED`를 반환합니다.

이와 같이 Apache Shiro를 사용하여 RESTful API의 인증을 구현하면 보안 요구사항을 쉽게 처리할 수 있습니다.

## 참고 자료

- [Apache Shiro 홈페이지](https://shiro.apache.org/)
- [RESTful API 개념 설명](https://en.wikipedia.org/wiki/Representational_state_transfer)