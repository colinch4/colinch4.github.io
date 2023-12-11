---
layout: post
title: "[java] AES-GCM (Galois Counter Mode) 암호화 모델"
description: " "
date: 2023-12-11
tags: [java]
comments: true
share: true
---

AES-GCM (Galois Counter Mode)은 대칭 키를 사용하여 데이터를 암호화하는 고급 암호화 표준입니다. 이 모델은 안전하고 효율적인 인증 및 암호화를 제공하여 널리 사용되고 있습니다.

## AES-GCM의 기능
AES-GCM은 인증과 암호화를 하나로 결합한 모델로 다음과 같은 주요 기능을 제공합니다:

- **데이터의 기밀성 및 무결성 보호:** 암호화된 데이터가 안전하게 전송되고 저장되도록 합니다.
- **인증 태그:** 데이터의 무결성을 보호하기 위해 인증 태그를 생성합니다. 이를 사용하여 데이터가 변경되지 않았음을 검증할 수 있습니다.
- **적응형 암호화:** GCM 모드는 데이터의 길이에 관계없이 효율적으로 암호화할 수 있습니다.

## AES-GCM 사용 예시
다음은 Java에서 AES-GCM을 사용하여 데이터를 암호화하는 예시 코드입니다.

```java
import javax.crypto.Cipher;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.SecureRandom;
import java.util.Base64;

public class AESEncryption {

    public static void main(String[] args) throws Exception {
        byte[] key = new byte[16];
        SecureRandom secureRandom = new SecureRandom();
        secureRandom.nextBytes(key);

        Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
        SecretKeySpec secretKey = new SecretKeySpec(key, "AES");
        byte[] iv = new byte[12];
        GCMParameterSpec parameterSpec = new GCMParameterSpec(128, iv);

        cipher.init(Cipher.ENCRYPT_MODE, secretKey, parameterSpec);
        byte[] encrypted = cipher.doFinal("Hello, AES-GCM!".getBytes());

        String encryptedBase64 = Base64.getEncoder().encodeToString(encrypted);
        System.out.println("Encrypted: " + encryptedBase64);
    }
}
```

위의 코드는 임의의 16바이트 키를 생성하고, GCM 모드에 필요한 초기화 벡터(IV)를 생성한 뒤, 주어진 데이터를 AES-GCM으로 암호화합니다.

코드를 통해 암호화된 데이터를 Base64로 인코딩하여 출력합니다.

## 결론
AES-GCM (Galois Counter Mode)은 데이터의 안전한 암호화 및 무결성을 보장하는 데 사용되는 강력한 암호화 모델입니다. 안전한 통신 및 데이터 보호를 위해 안전한 운영 환경에서 AES-GCM을 적절히 구현하는 것이 중요합니다.

참고문헌:
- [Oracle Java Documentation](https://docs.oracle.com/en/java/javase/16/docs/api/index.html)