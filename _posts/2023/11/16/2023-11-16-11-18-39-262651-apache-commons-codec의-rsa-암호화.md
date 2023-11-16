---
layout: post
title: "[java] Apache Commons Codec의 RSA 암호화"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

RSA 암호화는 공개키 암호화 방식입니다. Apache Commons Codec 라이브러리는 Java에서 Base64, Hex 등 다양한 인코딩 및 디코딩 작업을 수행하기 위한 유용한 도구를 제공합니다. 이번 포스트에서는 Apache Commons Codec를 사용하여 RSA 암호화를 수행하는 방법을 알아보겠습니다.

## Apache Commons Codec 의존성 추가

먼저, Maven 또는 Gradle을 사용하여 프로젝트에 Apache Commons Codec 의존성을 추가해야 합니다. Maven의 경우, `pom.xml` 파일에 다음 의존성을 추가하십시오.

```xml
<dependency>
    <groupId>commons-codec</groupId>
    <artifactId>commons-codec</artifactId>
    <version>1.15</version>
</dependency>
```

Gradle의 경우, `build.gradle` 파일에 다음 종속성을 추가하십시오.

```groovy
implementation 'commons-codec:commons-codec:1.15'
```

## RSA 암호화

RSA 암호화를 위해 `KeyPairGenerator`를 사용하여 공개 키와 비밀 키를 생성해야 합니다. 다음은 RSA 암호화 및 복호화 작업을 수행하는 예제 코드입니다.

```java
import org.apache.commons.codec.binary.Base64;

import java.security.*;
import java.util.Arrays;

public class RSAEncryptionExample {

    public static void main(String[] args) throws Exception {
        // RSA 키 쌍 생성
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
        keyPairGenerator.initialize(2048);
        KeyPair keyPair = keyPairGenerator.genKeyPair();

        // 공개 키와 비밀 키 추출
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // 암호화할 데이터
        String plainText = "Hello, RSA Encryption!";
        byte[] plainTextBytes = plainText.getBytes();

        // 공개 키로 데이터 암호화
        Cipher encryptCipher = Cipher.getInstance("RSA");
        encryptCipher.init(Cipher.ENCRYPT_MODE, publicKey);
        byte[] encryptedBytes = encryptCipher.doFinal(plainTextBytes);

        // 암호화된 데이터를 Base64 인코딩하여 출력
        String encryptedText = Base64.encodeBase64String(encryptedBytes);
        System.out.println("Encrypted Text: " + encryptedText);

        // 암호화된 데이터를 비밀 키로 복호화
        byte[] encryptedBytesDecoded = Base64.decodeBase64(encryptedText);
        Cipher decryptCipher = Cipher.getInstance("RSA");
        decryptCipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = decryptCipher.doFinal(encryptedBytesDecoded);

        // 복호화된 데이터 출력
        String decryptedText = new String(decryptedBytes);
        System.out.println("Decrypted Text: " + decryptedText);

        // 암호화 전과 복호화 후의 데이터가 일치하는지 확인
        boolean isMatch = Arrays.equals(plainTextBytes, decryptedBytes);
        System.out.println("Match: " + isMatch);
    }
}
```

위의 코드에서 `KeyPairGenerator`를 사용하여 2048비트의 RSA 키 쌍을 생성했습니다. 그리고 생성한 공개 키와 비밀 키를 추출하여 암호화 및 복호화에 사용했습니다. 암호화된 데이터는 Base64 인코딩된 문자열로 출력되며, 이를 비밀 키로 복호화하여 원래의 데이터를 확인합니다.

## 결론

Apache Commons Codec 라이브러리를 사용하면 Java에서 RSA 암호화를 손쉽게 수행할 수 있습니다. 이를 통해 개인 정보와 민감한 데이터를 안전하게 암호화하여 보호할 수 있습니다.

더 많은 정보를 원한다면 [Apache Commons Codec 공식 문서](https://commons.apache.org/proper/commons-codec/)를 참고하십시오.