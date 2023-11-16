---
layout: post
title: "[java] Apache Commons Codec를 이용한 RSA 암호화 예제"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

RSA 암호화는 공개키 암호화 방식 중 하나로, 안전한 데이터 통신 및 데이터 보호를 위해 널리 사용됩니다. 이번 예제에서는 Apache Commons Codec 라이브러리를 사용하여 RSA 암호화를 구현하는 방법을 알아보겠습니다.

### 1. Maven Dependency 추가

먼저, 프로젝트의 Maven POM 파일에 아래와 같이 Apache Commons Codec 의존성을 추가합니다.

```xml
<dependencies>
    <dependency>
        <groupId>commons-codec</groupId>
        <artifactId>commons-codec</artifactId>
        <version>1.15</version>
    </dependency>
</dependencies>
```

### 2. RSA 키 생성

RSA 암호화를 위해 공개키와 개인키를 생성해야 합니다. 아래 코드는 2048비트의 RSA 공개키와 개인키를 생성하는 방법을 보여줍니다.

```java
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.codec.binary.Hex;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

public class RSAExample {

    public static void main(String[] args) throws NoSuchAlgorithmException {
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
        keyPairGenerator.initialize(2048, new SecureRandom());

        KeyPair keyPair = keyPairGenerator.generateKeyPair();
        System.out.println("Public Key: " + Base64.encodeBase64String(keyPair.getPublic().getEncoded()));
        System.out.println("Private Key: " + Base64.encodeBase64String(keyPair.getPrivate().getEncoded()));
    }

}
```

### 3. 데이터 암호화 및 복호화

RSA 키를 생성한 후에는 이를 사용하여 데이터를 암호화하고 복호화할 수 있습니다. 아래 코드는 문자열을 RSA로 암호화한 후 다시 복호화하는 예제입니다.

```java
import org.apache.commons.codec.binary.Base64;

import javax.crypto.Cipher;
import java.nio.charset.StandardCharsets;
import java.security.*;

public class RSAExample {

    public static void main(String[] args) throws Exception {
        String message = "Hello, World!";

        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
        keyPairGenerator.initialize(2048, new SecureRandom());

        KeyPair keyPair = keyPairGenerator.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // 데이터 암호화
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        byte[] encryptedBytes = cipher.doFinal(message.getBytes(StandardCharsets.UTF_8));
        String encryptedMessage = Base64.encodeBase64String(encryptedBytes);

        // 데이터 복호화
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(Base64.decodeBase64(encryptedMessage));
        String decryptedMessage = new String(decryptedBytes, StandardCharsets.UTF_8);

        System.out.println("Encrypted Message: " + encryptedMessage);
        System.out.println("Decrypted Message: " + decryptedMessage);
    }

}
```

위의 코드에서는 `Cipher` 클래스를 사용하여 데이터를 암호화하고 복호화합니다. `Cipher.ENCRYPT_MODE`와 `Cipher.DECRYPT_MODE`를 사용하여 해당 모드로 암호화와 복호화를 수행할 수 있습니다.

이제 Apache Commons Codec을 사용하여 RSA 암호화 예제를 구현하는 방법을 알게 되었습니다. RSA는 안전하고 신뢰할 수 있는 데이터 암호화에 사용되는 강력한 기술입니다. 추가적인 정보를 얻기 위해 [Apache Commons Codec](https://commons.apache.org/proper/commons-codec/) 공식 문서를 참조해주세요.