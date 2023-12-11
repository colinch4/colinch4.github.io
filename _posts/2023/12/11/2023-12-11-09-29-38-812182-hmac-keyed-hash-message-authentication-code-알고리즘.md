---
layout: post
title: "[java] HMAC (Keyed-Hash Message Authentication Code) 알고리즘"
description: " "
date: 2023-12-11
tags: [java]
comments: true
share: true
---

HMAC은 메시지 무결성을 보호하기 위해 사용되는 **해시 기반 메시지 인증 코드**이다. HMAC은 **공통 키**를 사용하여 데이터의 무결성을 검증하고 인증하는 데에 주로 사용된다. 이 알고리즘은 특허나 저작권으로 보호되지 않는다. 따라서 누구나 사용할 수 있다.

## HMAC 알고리즘 동작 방식

HMAC은 주어진 메시지와 **비밀 키**를 입력으로 받아, **해시 함수**를 사용하여 메시지에 대한 **고정 길이 키**를 생성한다. 이렇게 생성된 키는 메시지에 연결되어 인증 코드를 생성하는 데에 사용된다. 이때, 키를 변경하지 않으면, 동일한 메시지에 대해 항상 동일한 HMAC 값을 생성한다.

일반적으로, HMAC은 MD5, SHA-1, SHA-256과 같은 해시 함수를 사용하여 구현된다.

```java
import javax.crypto.SecretKey;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public class HmacExample {
  public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException {
    String message = "Hello, World!";
    String key = "secretKey";

    SecretKey secretKey = new SecretKeySpec(key.getBytes(), "HmacSHA256");
    Mac mac = Mac.getInstance("HmacSHA256");
    mac.init(secretKey);

    byte[] hmac = mac.doFinal(message.getBytes());

    System.out.println("HMAC: " + new String(hmac));
  }
}
```

## HMAC 사용 사례

HMAC은 **API 요청과 응답**의 무결성을 보호하기 위해 많이 사용된다. 또한, **웹 토큰**을 검증하고, **메시지 인증**을 하는 데에도 널리 사용된다.

## 결론

HMAC은 메시지 무결성을 보호하기 위한 강력한 도구로, 데이터 보안을 강화하는 데에 큰 도움이 된다. 그러므로, 적절한 키 관리와 함께 사용하는 경우, 데이터 인증 및 무결성 검증을 쉽게 구현할 수 있다.

## 참고 자료
- [RFC 2104](https://tools.ietf.org/html/rfc2104) - HMAC: Keyed-Hashing for Message Authentication
- [Java Cryptography Architecture](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html) - Java Cryptography Architecture (JCA) Documentation
- [Spring Security](https://spring.io/projects/spring-security) - Spring Security framework for adding authentication and authorization to Java applications