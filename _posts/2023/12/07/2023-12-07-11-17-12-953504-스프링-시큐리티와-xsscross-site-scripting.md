---
layout: post
title: "[java] 스프링 시큐리티와 XSS(Cross-site Scripting)"
description: " "
date: 2023-12-07
tags: [java]
comments: true
share: true
---

## 개요
스프링 시큐리티는 웹 애플리케이션의 보안을 강화하기 위한 프레임워크이다. 이 프레임워크를 통해 사용자 인증, 인가, 보안 설정 등을 쉽게 구현할 수 있다. 하지만 웹 애플리케이션은 여전히 XSS(Cross-site Scripting) 공격에 취약할 수 있다. 이번 포스트에서는 스프링 시큐리티를 사용하여 XSS 공격을 방어하는 방법에 대해 알아보겠다.

## XSS(Cross-site Scripting)란?
XSS는 악의적인 사용자가 웹 페이지에 스크립트를 삽입하여 공격하는 기법이다. 이를 통해 사용자의 쿠키 정보를 탈취하거나 사용자를 다른 사이트로 유도할 수 있다. XSS 공격은 사용자의 신뢰를 저해하고 웹 애플리케이션의 안전성을 약화시키는 위험성이 있다.

## 스프링 시큐리티와 XSS 방어
스프링 시큐리티는 기본적으로 XSS 공격에 대한 방어 기능을 제공하지 않는다. 하지만 스프링 시큐리티를 활용하여 XSS 공격을 방어할 수 있는 몇 가지 방법이 있다.

### 입력값 검증
XSS 공격을 방지하기 위해서는 사용자로부터 입력받은 값에 대해 검증하는 것이 중요하다. 스프링 시큐리티에서는 `WebSecurityConfigurerAdapter` 클래스를 사용하여 입력값 검증을 적용할 수 있다. 아래는 예시 코드이다.

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
                .antMatchers("/").permitAll()
                .anyRequest().authenticated()
                .and()
            .formLogin()
                .loginPage("/login")
                .permitAll()
                .and()
            .csrf().disable()
            .headers().xssProtection().block(true);
    }
}
```

### 출력값 이스케이프
XSS 공격을 방지하기 위해 출력값을 이스케이프하여 안전하게 렌더링해야 한다. 스프링에서는 Thymeleaf, JSP, Freemarker 등 다양한 템플릿 엔진을 지원하며, 이들 템플릿 엔진을 사용하여 출력값 이스케이프를 적용할 수 있다.

- Thymeleaf: `<div th:text="${#strings.escapeXml(value)}"></div>`
- JSP: `<c:out value="${value}"/>`
- Freemarker: `${value?html}`

### Content Security Policy(CSP)
CSP를 사용하면 웹 애플리케이션에서 실행되는 JavaScript, CSS, 이미지 등 외부 리소스에 대한 제한을 설정할 수 있다. 이를 통해 XSS 공격을 방지할 수 있다. CSP 설정은 `ContentSecurityPolicy` 클래스를 통해 적용할 수 있다.

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
                .antMatchers("/").permitAll()
                .anyRequest().authenticated()
                .and()
            .formLogin()
                .loginPage("/login")
                .permitAll()
                .and()
            .csrf().disable()
            .headers().contentSecurityPolicy("script-src 'self'");
    }
}
```

## 결론
스프링 시큐리티를 사용하면 XSS 공격에 대비하여 웹 애플리케이션의 보안을 강화할 수 있다. 입력값 검증, 출력값 이스케이프, Content Security Policy 등을 적절히 활용하여 웹 애플리케이션의 안전성을 높이도록 노력해야 한다.

## 참고 자료
- [Cross-site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/)
- [Spring Security Reference](https://docs.spring.io/spring-security/site/docs/5.5.0/reference/html5/)
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)