---
layout: post
title: "[java] DES (Data Encryption Standard) 알고리즘"
description: " "
date: 2023-12-11
tags: [java]
comments: true
share: true
---

DES는 Data Encryption Standard의 약자로, 고전적인 대칭키 암호 알고리즘 중 하나입니다. DES는 데이터를 64비트 블록으로 나누어 16개의 순열 및 대치 작업을 수행하여 64비트 암호화 키를 사용하여 데이터를 암호화합니다.

## DES 알고리즘의 동작

- **초기 순열 (Initial Permutation, IP)**: 64비트의 평문을 64비트의 순열에 따라 재배치합니다.
- **라운드 함수 (Round Function)**: 64비트의 평문을 받아 순열 및 대치 작업을 16회 반복합니다.
- **최종 순열 (Final Permutation, FP)**: 라운드 함수를 거친 결과를 다시 한 번 64비트의 순열에 따라 재배치하여 암호문을 생성합니다.

## Java에서 DES 알고리즘 사용하기

```java
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESKeySpec;

public class DESExample {
    public static void main(String[] args) {
        try {
            String plainText = "Hello, DES!";
            String key = "secretK"; // 8바이트의 키
            byte[] plainBytes = plainText.getBytes("UTF8");

            SecretKeyFactory keyFactory = SecretKeyFactory.getInstance("DES");
            SecretKey secretKey = keyFactory.generateSecret(new DESKeySpec(key.getBytes("UTF8")));

            Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
            cipher.init(Cipher.ENCRYPT_MODE, secretKey);
            byte[] encryptedBytes = cipher.doFinal(plainBytes);

            System.out.println("Encrypted text: " + new String(encryptedBytes, "UTF8"));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위 예제는 Java에서 DES 알고리즘을 사용하여 문자열을 암호화하는 방법을 보여줍니다.

DES에 대한 자세한 내용은 [Oracle Java Documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#Examples)를 참고하세요.