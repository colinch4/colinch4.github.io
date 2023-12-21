---
layout: post
title: "[스프링] 인증(Authentication)과 권한 부여(Authorization)"
description: " "
date: 2023-12-21
tags: [스프링]
comments: true
share: true
---

보안은 모든 웹 애플리케이션의 중요한 측면 중 하나이며, 스프링 프레임워크는 이를 쉽게 처리할 수 있는 기능을 제공합니다. 이번 블로그에서는 스프링 시큐리티를 사용하여 어떻게 사용자 인증과 권한 부여를 구현하는지 알아보겠습니다.

## 1. 인증(Authentication)

인증은 사용자가 시스템에 대해 누구인지 확인하는 프로세스를 말합니다. 

보통 스프링 시큐리티는 로그인 페이지를 제공하고 사용자가 아이디와 비밀번호를 입력하면, 이를 확인하여 사용자를 인증합니다. 

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
 
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth
            .inMemoryAuthentication()
                .withUser("user").password("password").roles("USER");
    }
}
```

## 2. 권한 부여(Authorization)

한번 사용자가 시스템에 로그인되면, 권한 부여가 이루어져야 합니다. 스프링 시큐리티에서는 `hasRole()`이나 `hasAuthority()` 메소드를 사용하여 특정 권한이 있는지 확인할 수 있습니다.

```java
@Override
protected void configure(HttpSecurity http) throws Exception {
    http
        .authorizeRequests()
            .antMatchers("/admin/**").hasRole("ADMIN")
            .antMatchers("/user/**").hasAnyRole("USER", "ADMIN")
            .anyRequest().authenticated()
            .and()
        .formLogin()
            .and()
        .httpBasic();
}
```

## 결론

스프링 시큐리티를 사용하면 보안에 대한 많은 부분을 쉽게 구현할 수 있습니다. 이를 통해 안전하고 보안된 웹 애플리케이션을 구축할 수 있습니다.

내부 링크: [인증과 권한 부여](#1-인증authentication)