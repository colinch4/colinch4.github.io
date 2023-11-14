---
layout: post
title: "[java] Spring Security를 이용한 JWT(Json Web Token) 인증 구현"
description: " "
date: 2023-11-14
tags: [java]
comments: true
share: true
---

Spring Security를 사용하여 JWT(Json Web Token) 기반의 인증 구현을 해보겠습니다.

## 참고 자료

- [Spring Security 공식 문서](https://docs.spring.io/spring-security/site/docs/current/reference/html5/)
- [JWT 공식 문서](https://jwt.io/introduction/)

## JWT 인증의 개요

JWT는 클레임(Claim) 기반의 토큰을 사용하여 사용자 인증을 처리하는 방식입니다. 이 토큰은 서버에서 발급하며, 클라이언트는 이를 이용하여 인증을 수행합니다. 인증이 필요한 요청마다 토큰을 헤더에 포함하여 전송하고, 서버는 이를 검증하여 인증을 처리합니다.

JWT는 일반적으로 Header, Payload, Signature 세 부분으로 구성됩니다. Header는 토큰의 타입과 암호화 알고리즘 등을 정의하고, Payload는 클레임 정보를 담고 있습니다. Signature는 암호화된 헤더와 페이로드의 조합으로, 서버가 토큰의 유효성을 검증할 때 사용됩니다.

## Spring Security와 JWT 연동하기

Spring Security에서 JWT를 사용하기 위해 다음 단계를 따릅니다.

1. 의존성 추가: `pom.xml` 파일에 Spring Security와 JWT 관련 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>

<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.9.1</version>
</dependency>
```

2. JWT 유틸리티 클래스 생성: JWT를 생성, 검증, 파싱하는 유틸리티 클래스를 작성합니다.
   
```java
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.springframework.security.core.userdetails.UserDetails;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;

public class JwtUtil {
    private static final String SECRET_KEY = "mysecretkey";

    public static String generateToken(UserDetails userDetails) {
        Map<String, Object> claims = new HashMap<>();
        return createToken(claims, userDetails.getUsername());
    }

    private static String createToken(Map<String, Object> claims, String subject) {
        Date now = new Date();
        Date expirationDate = new Date(now.getTime() + 1000 * 60 * 60 * 10); // 10 hours

        return Jwts.builder()
                .setClaims(claims)
                .setSubject(subject)
                .setIssuedAt(now)
                .setExpiration(expirationDate)
                .signWith(SignatureAlgorithm.HS256, SECRET_KEY)
                .compact();
    }

    public static String extractUsername(String token) {
        return extractClaim(token, Claims::getSubject);
    }

    public static Date extractExpiration(String token) {
        return extractClaim(token, Claims::getExpiration);
    }

    public static <T> T extractClaim(String token, Function<Claims, T> claimsResolver) {
        Claims claims = extractAllClaims(token);
        return claimsResolver.apply(claims);
    }

    private static Claims extractAllClaims(String token) {
        return Jwts.parser().setSigningKey(SECRET_KEY).parseClaimsJws(token).getBody();
    }

    private static Boolean isTokenExpired(String token) {
        Date expiration = extractExpiration(token);
        return expiration.before(new Date());
    }

    public static Boolean validateToken(String token, UserDetails userDetails) {
        String username = extractUsername(token);
        return (username.equals(userDetails.getUsername()) && !isTokenExpired(token));
    }
}
```

3. 사용자 정보 가져오기: Spring Security에서 사용자 정보를 가져오는 `UserDetailsService`를 구현합니다.

```java
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.stereotype.Service;

@Service
public class UserDetailsServiceImpl implements UserDetailsService {
    // 사용자 정보를 가져오는 로직을 구현합니다.
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        // 예시: username을 이용하여 DB에서 사용자 정보를 조회하고 UserDetails 객체를 생성합니다.
        User user = userRepository.findByUsername(username);
        if(user == null) {
            throw new UsernameNotFoundException("User not found with username: " + username);
        }
        return new org.springframework.security.core.userdetails.User(user.getUsername(), user.getPassword(), new ArrayList<>());
    }
}
```

4. 인증 필터 추가: JWT를 검증하는 필터를 추가하여 인증을 수행합니다.

```java
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.authentication.AbstractAuthenticationProcessingFilter;
import org.springframework.security.web.util.matcher.AntPathRequestMatcher;
import org.springframework.security.web.util.matcher.RequestMatcher;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class JwtAuthenticationFilter extends AbstractAuthenticationProcessingFilter {
    public JwtAuthenticationFilter(RequestMatcher requestMatcher) {
        super(requestMatcher);
    }

    @Override
    public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response) {
        String token = request.getHeader("Authorization");

        // JWT 토큰 유효성 검사 로직
        // 예시: 유틸리티 클래스를 사용하여 토큰 검증 후 인증 객체를 반환합니다.
        UserDetails userDetails = userDetailsService.loadUserByUsername(username);
        if (JwtUtil.validateToken(token, userDetails)) {
            return new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
        } else {
            throw new JwtAuthenticationException("Invalid token");
        }
    }

    @Override
    protected void successfulAuthentication(HttpServletRequest request, HttpServletResponse response, FilterChain chain, Authentication authResult) throws IOException, ServletException {
        SecurityContextHolder.getContext().setAuthentication(authResult);
        chain.doFilter(request, response);
    }
}
```

5. Spring Security 설정 수정: Spring Security 설정 클래스에 JWT 관련 설정을 추가합니다.

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.builders.WebSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.password.NoOpPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Autowired
    private UserDetailsService userDetailsService;

    @Autowired
    private JwtAuthenticationEntryPoint jwtAuthenticationEntryPoint;

    @Autowired
    private JwtRequestFilter jwtRequestFilter;

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.userDetailsService(userDetailsService);
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf().disable()
                .authorizeRequests()
                .antMatchers("/api/authenticate").permitAll() // 인증하지 않아도 접근 가능한 경로
                .anyRequest().authenticated()
                .and().exceptionHandling().authenticationEntryPoint(jwtAuthenticationEntryPoint)
                .and().sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS);

        http.addFilterBefore(jwtRequestFilter, UsernamePasswordAuthenticationFilter.class);
    }

    @Override
    public void configure(WebSecurity web) throws Exception {
        web.ignoring().antMatchers("/resources/**"); // 무시할 경로 설정
    }

    @Override
    @Bean
    public AuthenticationManager authenticationManagerBean() throws Exception {
        return super.authenticationManagerBean();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return NoOpPasswordEncoder.getInstance();
    }
}
```

위의 단계를 따라서 Spring Security와 JWT를 연동하여 웹 애플리케이션의 인증을 처리할 수 있습니다. 안전한 통신을 위해 토큰을 HTTPS 프로토콜을 통해 전송하는 것을 권장합니다.

이 예시에서는 JWT를 생성, 검증하는 유틸리티 클래스와, 사용자 정보를 가져오는 `UserDetailsService`를 작성했습니다. 또한 JWT 토큰의 검증을 처리하는 필터인 `JwtAuthenticationFilter`를 추가하고, 필요한 경우 해당 필터를 Spring Security 설정에 등록하여 사용합니다.

이를 통해 Spring Security를 사용한 JWT 기반의 인증 구현이 가능합니다. 추가적인 보안과 개선 사항은 프로젝트의 요구사항에 따라 구현하면 됩니다.

**주의:** 위의 코드는 예시를 위해 간단히 작성되었으며, 실제 프로덕션 환경에서는 보안, 예외 처리 등에 유의하여 구현해야 합니다.