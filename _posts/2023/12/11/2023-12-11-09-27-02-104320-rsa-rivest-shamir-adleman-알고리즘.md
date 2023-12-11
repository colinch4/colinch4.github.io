---
layout: post
title: "[java] RSA (Rivest-Shamir-Adleman) 알고리즘"
description: " "
date: 2023-12-11
tags: [java]
comments: true
share: true
---

RSA 알고리즘은 공개키 암호 시스템 중 하나로, 데이터 전송 시 정보 보안을 위해 사용됩니다. RSA 알고리즘은 공개키 및 개인 키를 사용하여 암호화 및 복호화하는 방식을 기반으로 합니다.

이 알고리즘의 핵심은 **소인수 분해**입니다. 매우 큰 소수의 곱을 얻었을 때, 이를 소인수 분해하는 것은 어렵지만, 이미 알려진 두 소수의 곱을 효율적으로 구하는 것은 쉽다는 소수 이론에 기반합니다.

## 알고리즘 단계

RSA 알고리즘은 다음과 같은 단계로 동작합니다.

### 1. 키 생성

RSA 암호화를 위해 공개키와 개인 키를 생성합니다. 

- **소수(p, q) 선정**: 매우 큰 두 소수 p와 q를 선정합니다.
- **N 값 계산**: N = p * q로 계산합니다.
- **오일러 피 함수 값 계산**: φ(N) = (p-1)(q-1)로 계산합니다.
- **공개키(e) 선택**: 1 < e < φ(N)이고, e와 φ(N)이 서로소인 e를 선택합니다.
- **개인 키(d) 계산**: d * e ≡ 1 (mod φ(N))을 만족하는 d 값을 찾습니다.

### 2. 암호화

보내고자 하는 데이터를 받는 측의 공개키(N, e)를 사용하여 암호화합니다.

### 3. 복호화

암호화된 데이터를 받는 측의 개인 키(d)를 사용하여 복호화합니다.

RSA 알고리즘은 안전한 키 교환과 디지털 서명을 위한 기반으로 널리 사용됩니다.

## 예제 코드

다음은 Java를 사용한 RSA 알고리즘의 간단한 예제 코드입니다.

```java
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import javax.crypto.Cipher;

public class RSAExample {
    public static void main(String[] args) throws Exception {
        // KeyPair 생성
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048);
        KeyPair pair = keyPairGen.generateKeyPair();
        PublicKey publicKey = pair.getPublic();
        PrivateKey privateKey = pair.getPrivate();

        // 암호화
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        byte[] encryptedData = cipher.doFinal("암호화할 데이터".getBytes());

        // 복호화
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedData = cipher.doFinal(encryptedData);
        System.out.println(new String(decryptedData));
    }
}
```

## 결론

RSA는 안전한 키 교환, 디지털 서명 및 데이터 암호화에 널리 사용되는 강력한 알고리즘입니다. 따라서 RSA의 작동 방식과 구현을 이해하는 것은 보안 기술을 개발하고 사용하는 데 매우 중요합니다.

더 많은 정보 및 세부적인 사용 사례는 공식 Java 암호화 라이브러리 [Java Cryptography Architecture](https://docs.oracle.com/en/java/javase/11/security/java-cryptography-architecture-jca-reference-guide.html)를 참조하세요.

이것이 RSA 알고리즘에 대한 소개였습니다. 감사합니다!