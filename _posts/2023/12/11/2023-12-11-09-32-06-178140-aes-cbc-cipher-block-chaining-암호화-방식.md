---
layout: post
title: "[java] AES-CBC (Cipher Block Chaining) 암호화 방식"
description: " "
date: 2023-12-11
tags: [java]
comments: true
share: true
---

AES-CBC (Advanced Encryption Standard - Cipher Block Chaining)는 대칭 키 알고리즘으로, 데이터를 블록 단위로 암호화하는 데 사용됩니다. 이 방식은 이전 블록의 암호문을 현재 블록의 평문과 XOR 연산하여 사용하는 블록 암호화 모드입니다.

## AES-CBC 암호화 동작 원리

AES-CBC 모드는 다음과 같은 단계로 동작합니다.

1. 데이터를 블록 단위로 나눕니다.
2. 초기화 벡터(IV)를 사용하여 첫 번째 블록을 암호화합니다.
3. 이전 블록의 암호문과 현재 블록의 평문을 XOR하여 다음 블록을 암호화합니다.
4. 모든 블록이 암호화될 때까지 이전 블록의 암호문과 현재 블록의 평문을 XOR하여 암호화를 계속합니다.

## 예시

다음은 Java를 사용하여 AES-CBC 암호화를 수행하는 간단한 예시입니다.

```java
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class AESCBCExample {

    public static byte[] encrypt(byte[] plaintext, byte[] key, byte[] iv) throws Exception {
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        SecretKeySpec secretKey = new SecretKeySpec(key, "AES");
        IvParameterSpec ivSpec = new IvParameterSpec(iv);
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);
        return cipher.doFinal(plaintext);
    }

    public static void main(String[] args) {
        try {
            byte[] key = "1234567890123456".getBytes();
            byte[] iv = "1234567890123456".getBytes();
            byte[] plaintext = "Hello, AES-CBC!".getBytes();
            byte[] ciphertext = encrypt(plaintext, key, iv);
            System.out.println("Ciphertext: " + new String(ciphertext));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위 예시에서는 "1234567890123456"을 키와 IV로 사용하여 "Hello, AES-CBC!"를 암호화합니다.

## 결론

AES-CBC는 안전한 암호화 방식으로, 데이터의 기밀성을 유지하기 위한 다양한 응용 프로그램에서 사용됩니다. 그러나 올바른 키 및 초기화 벡터의 관리가 중요하며, 안전한 키 관리를 위해 신중한 노력이 필요합니다.

참고문헌:
- Oracle Java Documentation: https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html
- AES (Advanced Encryption Standard): https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
- CBC (Cipher Block Chaining): https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC)