---
layout: post
title: "[스프링] 스프링 시큐리티와 CSRF(Cross-Site Request Forgery) 방어"
description: " "
date: 2023-12-21
tags: [스프링]
comments: true
share: true
---

## 개요
웹 애플리케이션에서 사용자 요청을 처리할 때, CSRF(Cross-Site Request Forgery) 공격에 대한 방어가 필요하다. **CSRF**는 인증된 사용자가 악의적인 웹 사이트를 통해 비밀 요청을 전송하는 공격이다. 스프링 시큐리티를 사용하여 CSRF 공격을 방어할 수 있다. 

## 스프링 시큐리티 설정
스프링 부트 애플리케이션에서 스프링 시큐리티를 이용하여 CSRF 공격으로부터 보호하려면 `WebSecurityConfigurerAdapter` 클래스를 확장하고 `configure` 메서드를 오버라이드하여 설정을 추가해야 한다. 

다음은 스프링 시큐리티를 사용하여 CSRF 공격으로부터 보호하는 간단한 설정 예시이다.

```java
@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf()
                .csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse());
    }
}
```

위의 설정에서 `CookieCsrfTokenRepository.withHttpOnlyFalse()`는 CSRF 토큰을 쿠키에 저장하고 JavaScript에서 읽을 수 있도록 설정한다. 

## 테스트
이제 CSRF 공격으로부터 보호되는지 확인하는 테스트를 작성할 수 있다. 

```java
@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class CsrfProtectionTest {
    @Autowired
    private TestRestTemplate restTemplate;

    @LocalServerPort
    private int port;

    @Test
    public void givenAuthenticatedUser_whenNoXsrfTokenPresentInRequest_shouldFailWith403() throws Exception {
        HttpHeaders headers = new HttpHeaders();
        headers.set("Cookie", "JSESSIONID=" + getCookie("JSESSIONID"));
      
        final ResponseEntity<String> response = restTemplate.exchange("/protected-resource", HttpMethod.GET,
                new HttpEntity<>(headers), String.class);
        assertThat(response.getStatusCode()).isEqualTo(403);
    }

    private String getCookie(String cookieName) {
        RequestConfig requestConfig = RequestConfig.custom().setCookieSpec(CookieSpecs.STANDARD).build();
        HttpClient client = HttpClientBuilder.create().setDefaultRequestConfig(requestConfig).build();
        List<Cookie> cookies = cookieStore.getCookies();
        for (Cookie cookie : cookies) {
            if (cookie.getName().equals(cookieName)) {
                return cookie.getValue();
            }
        }
        return null;
    }
}
```

위의 테스트는 CSRF 공격으로부터 특정 리소스를 보호하는지를 확인하는 예시이다.

## 마무리
스프링 시큐리티를 사용하여 CSRF 공격으로부터 보호하는 방법을 살펴보았다. 이를 통해 보안성을 향상시키고 웹 애플리케이션을 안전하게 유지할 수 있다.

## 참고 자료
- [스프링 공식 문서 - Cross Site Request Forgery (CSRF)](https://docs.spring.io/spring-security/site/docs/current/reference/html/csrf.html)