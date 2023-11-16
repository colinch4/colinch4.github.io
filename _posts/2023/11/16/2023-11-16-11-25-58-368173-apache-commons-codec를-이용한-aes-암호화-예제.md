---
layout: post
title: "[java] Apache Commons Codec를 이용한 AES 암호화 예제"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이 예제에서는 Apache Commons Codec 라이브러리를 사용하여 AES 암호화를 수행하는 방법을 소개합니다. Apache Commons Codec는 다양한 인코딩 및 디코딩 기능을 제공하는 자바 라이브러리입니다.

## Maven 종속성 추가

먼저, Apache Commons Codec의 Maven 종속성을 프로젝트에 추가해야 합니다. `pom.xml` 파일에 다음 내용을 추가합니다:

```xml
<dependencies>
    <dependency>
        <groupId>commons-codec</groupId>
        <artifactId>commons-codec</artifactId>
        <version>1.15</version>
    </dependency>
</dependencies>
```

위의 코드는 Apache Commons Codec의 최신 버전인 1.15를 사용하는 종속성을 추가하는 것입니다.

## AES 암호화 예제

이제 AES 암호화를 수행하는 Java 코드를 작성해보겠습니다. 다음은 암호화를 수행하는 `encrypt` 메소드입니다:

```java
import org.apache.commons.codec.binary.Base64;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class AESEncryptionExample {
    
    private static final String SECRET_KEY = "abcdefghijklmnop";
    
    public static String encrypt(String plainText) throws Exception {
        SecretKeySpec secretKey = new SecretKeySpec(SECRET_KEY.getBytes(), "AES");
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        byte[] encryptedBytes = cipher.doFinal(plainText.getBytes());
        return Base64.encodeBase64String(encryptedBytes);
    }
    
    public static void main(String[] args) {
        try {
            String plainText = "Hello, World!";
            String encryptedText = encrypt(plainText);
            System.out.println("암호화된 텍스트: " + encryptedText);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드는 `SECRET_KEY` 변수에 암호화에 사용할 16바이트(128비트)의 키를 저장합니다. `encrypt` 메소드는 주어진 평문 문자열을 AES 알고리즘을 사용하여 암호화하고, Base64 인코딩된 문자열로 반환합니다. 메인 메소드에서는 "Hello, World!"를 암호화하고 결과를 출력합니다.

## 실행 결과

위의 코드를 실행하면 다음과 같은 결과가 출력됩니다:

```
암호화된 텍스트: OnVtpzUWJmX1z6V1v8xzFA==
```

암호화된 텍스트는 매번 실행할 때마다 달라질 수 있습니다.

## 참고 자료

- [Apache Commons Codec 공식 문서](https://commons.apache.org/proper/commons-codec/)
- [Java Cryptography Architecture (JCA) Reference Guide](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html)