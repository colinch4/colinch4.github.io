---
layout: post
title: "[java] Tomcat과 Spring MVC의 통합과 REST API 개발"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

이번 블로그에서는 Tomcat과 Spring MVC를 통합하여 REST API를 개발하는 방법에 대해 알아보겠습니다. 

## 1. Tomcat 설치

Tomcat은 Java 웹 애플리케이션을 실행하기 위한 웹 서버입니다. Tomcat을 설치하려면 다음 단계를 따르세요:

1. Tomcat 공식 웹 사이트에서 원하는 버전의 Tomcat 다운로드
2. 압축을 해제하고 원하는 디렉토리로 이동
3. bin 디렉토리로 이동하여 startup.bat(windows) 또는 startup.sh(macOS, Linux)을 실행하여 Tomcat 시작

## 2. Spring MVC 프로젝트 생성

Spring MVC는 Spring 프레임워크의 일부로, 웹 애플리케이션의 개발을 쉽게 할 수 있도록 도와줍니다. Spring MVC 프로젝트를 생성하는 방법은 다음과 같습니다:

1. Spring Initializer (https://start.spring.io/)에 접속하여 프로젝트 설정을 선택
2. Maven이나 Gradle을 선택하여 프로젝트 의존성 설정
3. "Generate" 버튼을 클릭하여 프로젝트 압축 파일 다운로드
4. 압축을 해제하고 원하는 디렉토리로 이동

## 3. REST API 개발

이제 Spring MVC 프로젝트에서 REST API를 개발해보겠습니다. 

1. Controller 클래스를 생성하고 `@RestController` 어노테이션을 추가하여 RESTful 웹 서비스 엔드포인트로 사용할 수 있도록 지정합니다.

```java
@RestController
public class ApiController {
    
    @GetMapping("/api/hello")
    public String hello() {
        return "Hello, World!";
    }
}
```

2. 위의 예제에서는 `/api/hello` 엔드포인트를 생성하고, HTTP GET 요청에 대한 응답으로 "Hello, World!"를 반환합니다.

3. Tomcat 서버를 시작한 후, 웹 브라우저나 HTTP 클라이언트 도구를 사용하여 `http://localhost:{포트번호}/api/hello` 주소로 요청을 보내면 "Hello, World!" 응답을 받을 수 있습니다.

## 결론

이제 Tomcat과 Spring MVC를 통합하여 REST API를 개발하는 방법을 알아보았습니다. Tomcat을 설치하고 Spring MVC 프로젝트를 생성한 후, Controller 클래스를 작성하여 RESTful 웹 서비스를 개발할 수 있습니다. 이를 통해 간단한 API를 개발하고 테스트할 수 있습니다.

이번 포스트는 참고 문서로 Spring 공식 문서 (https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/web.html)를 사용했습니다.