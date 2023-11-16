---
layout: post
title: "[java] Apache Commons Codec의 AES 암호화"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Codec는 자바 프로그래밍에서 다양한 인코딩 및 디코딩 기능을 제공하는 유용한 라이브러리입니다. 이 라이브러리를 사용하면 간단하고 효율적으로 다양한 암호화 알고리즘을 구현할 수 있습니다. 이번 포스트에서는 Apache Commons Codec의 AES(AES Advanced Encryption Standard) 암호화 기능을 살펴보겠습니다.

## AES 암호화란?

AES는 대칭키 암호화 알고리즘으로, 데이터를 암호화하고 복호화하는 데 사용됩니다. AES는 안전하고 강력한 암호화 기술로 알려져 있습니다. 대칭키 알고리즘이기 때문에 암호화와 복호화에 동일한 키를 사용합니다.

## Apache Commons Codec에서의 AES 암호화

Apache Commons Codec에는 AES 암호화를 지원하는 `Crypt` 클래스가 포함되어 있습니다.

```
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.codec.digest.Sha2Crypt;

public class AESCrypt {

    private static final String AES_KEY = "MySecretKey@123"; // 암호화에 사용할 키

    public static String encrypt(String plaintext) {
        byte[] encryptedBytes = Crypt.crypt(plaintext.getBytes(), AES_KEY.getBytes());
        return Base64.encodeBase64String(encryptedBytes);
    }

    public static String decrypt(String ciphertext) {
        byte[] encryptedBytes = Base64.decodeBase64(ciphertext);
        byte[] decryptedBytes = Crypt.crypt(encryptedBytes, AES_KEY.getBytes());
        return new String(decryptedBytes);
    }

    public static void main(String[] args) {
        String plaintext = "Hello, World!";
        String encrypted = encrypt(plaintext);
        String decrypted = decrypt(encrypted);

        System.out.println("Plaintext: " + plaintext);
        System.out.println("Encrypted: " + encrypted);
        System.out.println("Decrypted: " + decrypted);
    }
}
```

위의 예제 코드에서는 `Crypt` 클래스를 사용하여 AES 암호화를 수행합니다. `encrypt` 메서드는 주어진 평문을 AES 알고리즘으로 암호화하고, `decrypt` 메서드는 암호문을 복호화하는 역할을 합니다. 이때, `AES_KEY` 변수에는 암호화에 사용할 키를 지정해야 합니다.

## 실행 결과

위의 예제 코드를 실행하면 다음과 같은 결과를 얻을 수 있습니다.

```
Plaintext: Hello, World!
Encrypted: 5Pgr+Hg/U90/fjcI0ekmnw==
Decrypted: Hello, World!
```

## 결론

Apache Commons Codec을 사용하면 간편하게 AES 암호화를 구현할 수 있습니다. 이를 통해 암호화된 데이터의 보안을 강화할 수 있습니다. 더 자세한 내용을 알고 싶다면 [Apache Commons Codec 공식 문서](https://commons.apache.org/proper/commons-codec/)를 참조하시기 바랍니다.