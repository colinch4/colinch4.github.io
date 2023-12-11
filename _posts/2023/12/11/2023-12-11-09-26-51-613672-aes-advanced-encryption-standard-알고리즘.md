---
layout: post
title: "[java] AES (Advanced Encryption Standard) 알고리즘"
description: " "
date: 2023-12-11
tags: [java]
comments: true
share: true
---

AES는 데이터를 안전하게 암호화하고 복호화하는데 사용되는 대칭키 블록 암호 알고리즘입니다. 이 알고리즘은 128비트 블록 크기와 128, 192, 256비트의 키 길이를 지원합니다. AES는 현재 대중적으로 사용되는 암호 알고리즘 중 하나로, 안전하고 효율적인 암호화를 위해 널리 사용됩니다.

## AES 특징

- **고도로 안전한 알고리즘**: AES는 키 길이에 따라 128, 192, 256비트에 대해 안전한 암호화를 제공합니다.
- **성능 향상**: 암호화 및 복호화 속도가 빠르며, 대용량 데이터를 안전하게 처리할 수 있습니다.
- **롤린 시프트와 서브바이트**: 블록의 바이트들을 이동시켜 혼란을 줌으로써 보안성을 강화합니다.

## Java에서의 AES 구현

Java에서는 AES를 사용하여 데이터를 암호화하고 복호화할 수 있는 다양한 라이브러리와 클래스가 있습니다. 대표적으로 `javax.crypto` 패키지의 `Cipher` 클래스를 사용하여 AES를 구현할 수 있습니다.

아래는 AES 알고리즘을 사용하여 데이터를 암호화하고 복호화하는 Java 코드의 예시입니다.

```java
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.Key;

public class AESExample {
    private static final String ALGORITHM = "AES";
    private static final String MODE = "AES/ECB/PKCS5Padding";

    public static byte[] encrypt(byte[] input, byte[] keyBytes) throws Exception {
        Key key = new SecretKeySpec(keyBytes, ALGORITHM);
        Cipher cipher = Cipher.getInstance(MODE);
        cipher.init(Cipher.ENCRYPT_MODE, key);
        return cipher.doFinal(input);
    }

    public static byte[] decrypt(byte[] input, byte[] keyBytes) throws Exception {
        Key key = new SecretKeySpec(keyBytes, ALGORITHM);
        Cipher cipher = Cipher.getInstance(MODE);
        cipher.init(Cipher.DECRYPT_MODE, key);
        return cipher.doFinal(input);
    }

    public static void main(String[] args) throws Exception {
        String originalText = "Secret message";
        String keyString = "MySecretKey12345";
        byte[] keyBytes = keyString.getBytes();
        byte[] encrypted = encrypt(originalText.getBytes(), keyBytes);
        byte[] decrypted = decrypt(encrypted, keyBytes);
        System.out.println("Original: " + originalText);
        System.out.println("Encrypted: " + new String(encrypted));
        System.out.println("Decrypted: " + new String(decrypted));
    }
}
```

위의 코드는 AES 알고리즘을 사용하여 데이터를 암호화하고 복호화하는 Java 예제입니다. 위 코드는 ECB 모드를 사용하며, 패딩으로 PKCS5Padding을 사용하여 데이터를 처리합니다.

AES 알고리즘을 사용한 데이터의 안전한 암호화 및 복호화를 위해서는 키 관리와 안전한 키 교환을 유의해야 합니다.

AES 알고리즘에 대한 보다 자세한 내용은 공식 문서와 참고 자료를 참조하시기 바랍니다.

## 참고 자료

- Oracle Java Documentation: [Java Cryptography Architecture](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html)
- National Institute of Standards and Technology (NIST): [AES (Advanced Encryption Standard)](https://csrc.nist.gov/publications/detail/fips/197/final)