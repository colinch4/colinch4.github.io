---
layout: post
title: "[스프링] 스프링 시큐리티와 CORS(Cross-Origin Resource Sharing)"
description: " "
date: 2023-12-21
tags: [스프링]
comments: true
share: true
---

---

## 스프링 시큐리티와 CORS 이해하기

스프링은 강력한 보안 기능을 제공하는데, 그 중 하나가 스프링 시큐리티다. 스프링 시큐리티는 웹 애플리케이션의 보안을 담당하며, **인증**과 **권한 부여**를 처리한다. 하지만, 스프링 시큐리티를 사용할 때에는 **CORS(Cross-Origin Resource Sharing)** 이슈에 대해서도 고려해야 한다.

CORS는 다른 도메인에 있는 리소스에 접근하기 위해 브라우저가 사용하는 메커니즘이다. 기본적으로 스프링 시큐리티는 CORS를 차단하므로, 프론트엔드와 백엔드가 다른 도메인에 있는 경우에는 CORS 문제를 해결해야 한다.

## CORS 문제 해결하기

스프링 시큐리티에서 CORS 문제를 해결하기 위해서는 크게 두 가지 방법이 있다. 첫 번째 방법은 **WebSecurityConfigurerAdapter**를 상속받아 **configure(HttpSecurity http)** 메서드를 오버라이딩하여 CORS 설정을 변경하는 것이다.

아래는 **configure(HttpSecurity http)** 메서드를 사용하여 CORS를 허용하는 예시이다.

```java
@Override
protected void configure(HttpSecurity http) throws Exception {
    http.cors();
}
```

두 번째 방법은 **WebMvcConfigurer** 인터페이스를 구현하여 CORS 설정을 변경하는 것이다.

아래는 **addCorsMappings(CorsRegistry registry)** 메서드를 사용하여 CORS를 허용하는 예시이다.

```java
@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**").allowedOrigins("http://localhost:3000");
    }
}
```

## 결론

스프링 시큐리티를 사용하면서 CORS 이슈에 대응하기 위해서는 충분한 이해와 설정이 필요하다. CORS 문제를 해결함으로써 프론트엔드와 백엔드 간의 통신을 원할하게 할 수 있으며, 보다 안전하고 효율적인 웹 애플리케이션을 구축할 수 있다.

---
### 참고 자료

- [스프링 공식 문서](https://spring.io/)