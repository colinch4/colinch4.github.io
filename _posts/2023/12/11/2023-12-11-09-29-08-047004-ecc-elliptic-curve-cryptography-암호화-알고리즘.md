---
layout: post
title: "[java] ECC (Elliptic Curve Cryptography) 암호화 알고리즘"
description: " "
date: 2023-12-11
tags: [java]
comments: true
share: true
---

ECC (Elliptic Curve Cryptography)는 현대 암호학에서 널리 사용되는 대칭 암호화 방법 중 하나입니다. **ECC**는 소형 디지털 장치 및 접근성이 제한된 환경에서 효율적으로 작동하는데, 이러한 특성은 네트워크 보안 및 모바일 플랫폼에서 중요한 역할을 합니다.

## ECC의 주요 특징
    1. **효율성**: RSA 및 DSA 알고리즘에 비해 훨씬 작은 키 크기로 동등한 보안 수준을 제공합니다.
    2. **속도**: 빠른 연산 속도로 작은 디바이스 및 네트워크 통신에서 유용합니다.
    3. **안전성**: 강력한 보안 수준을 유지하는 데, 소수의 특정한 보안 키를 생성하고 관리할 수 있습니다.
    4. **자원 효율성**: 계산 및 저장 공간의 효율적인 활용으로, 시스템 자원을 절약합니다.

## ECC 암호화와 복호화 과정
ECC에서 암호화 및 복호화는 곡선 위의 점들을 사용하여 이루어집니다. 여기에는 *포인트 곱* 및 *스칼라 곱* 연산이 포함됩니다. ECC 암호화 알고리즘은 대칭 및 비대칭적인 키를 사용하여 메시지를 암호화 및 복호화합니다.

## 예제 코드
```java
import java.security.*;
import java.security.spec.ECGenParameterSpec;
import javax.crypto.*;
import java.util.Base64;

public class ECCExample {
    public static void main(String[] args) throws Exception {
        // ECC 키 페어 생성
        KeyPairGenerator keyGen = KeyPairGenerator.getInstance("EC");
        SecureRandom random = SecureRandom.getInstanceStrong();
        ECGenParameterSpec ecSpec = new ECGenParameterSpec("secp256r1");
        keyGen.initialize(ecSpec, random);
        KeyPair keyPair = keyGen.generateKeyPair();

        // 평문
        String plainText = "Hello, ECC!";
        
        // 암호화
        Cipher cipher = Cipher.getInstance("ECIES");
        cipher.init(Cipher.ENCRYPT_MODE, keyPair.getPublic());
        byte[] encryptedText = cipher.doFinal(plainText.getBytes());

        // 출력
        System.out.println("암호화된 텍스트: " + Base64.getEncoder().encodeToString(encryptedText));

        // 복호화
        cipher.init(Cipher.DECRYPT_MODE, keyPair.getPrivate());
        byte[] decryptedText = cipher.doFinal(encryptedText);
        System.out.println("복호화된 텍스트: " + new String(decryptedText));
    }
}
```

위 코드는 ECC를 사용하여 텍스트를 암호화 및 복호화하는 간단한 Java 예제입니다.

## 결론
ECC는 작은 키 크기로 높은 보안 수준을 제공하며, 작은 기기 및 제한된 환경에서 효율적으로 사용됩니다. 이러한 특성으로 인해 ECC는 모바일 플랫폼 및 인터넷 보안 시스템에서 널리 사용되고 있습니다.

참고문헌:
- https://en.wikipedia.org/wiki/Elliptic-curve_cryptography