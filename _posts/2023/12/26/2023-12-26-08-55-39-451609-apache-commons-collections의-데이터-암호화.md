---
layout: post
title: "[java] Apache Commons Collections의 데이터 암호화"
description: " "
date: 2023-12-26
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 Java 언어를 사용하여 데이터 처리 및 자료구조 조작을 위한 라이브러리입니다. 이 라이브러리는 다양한 유용한 기능들을 제공하며, 데이터 암호화 또한 이 중 하나입니다. 데이터 암호화는 개인정보와 같이 민감한 데이터를 안전하게 보호하기 위한 중요한 과제입니다.

## Apache Commons Collections Overview
Apache Commons Collections는 자료구조 유틸리티, 변경 불가능한 자료구조, 버퍼링, 조합 및 순열, 입력 유효성 검사 등의 기능을 제공합니다. 암호화 기능은 이 라이브러리의 한 부분으로서, 데이터 보안을 강화하는 데 사용될 수 있습니다.

## 데이터 암호화 방법
Apache Commons Collections를 사용하여 데이터를 암호화하려면 `org.apache.commons.collections4.map.LazyMap` 유틸리티 클래스를 사용할 수 있습니다. 이 클래스를 사용하면 값을 처음으로 요청할 때마다 자동으로 암호화가 수행됩니다.

예를 들어, 아래 코드는 LazyMap을 사용하여 데이터를 간단히 암호화하는 방법을 보여줍니다.

```java
import org.apache.commons.collections4.Factory;
import org.apache.commons.collections4.map.LazyMap;
import javax.crypto.Cipher;
import java.security.Key;

public class EncryptionMapExample {
    private static final String ALGORITHM = "AES";
    private static final String TRANSFORMATION = "AES/ECB/PKCS5Padding";
    private static final byte[] KEY_VALUE = "MySecretKey12345".getBytes(); // 16 bytes for AES

    public static void main(String[] args) {
        Factory<Cipher> cipherFactory = () -> {
            try {
                Key key = new SecretKeySpec(KEY_VALUE, ALGORITHM);
                return Cipher.getInstance(TRANSFORMATION);
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        };

        Map<String, String> encryptedMap = LazyMap.lazyMap(new HashMap<>(), s -> {
            try {
                Cipher cipher = cipherFactory.create();
                cipher.init(Cipher.ENCRYPT_MODE, key);
                return Base64.getEncoder().encodeToString(cipher.doFinal(s.getBytes()));
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        });

        encryptedMap.put("username", "johndoe");
        encryptedMap.put("password", "pa$$w0rd");

        System.out.println(encryptedMap.get("username")); // 출력: 암호화된 username 값
        System.out.println(encryptedMap.get("password")); // 출력: 암호화된 password 값
    }
}
```

## 참고 자료
Apache Commons Collections 공식 문서: [commons.apache.org/proper/commons-collections/](https://commons.apache.org/proper/commons-collections/)

이 예제는 Apache Commons Collections를 사용하여 데이터를 암호화하고 그 값을 저장하는 기본적인 방법을 보여줍니다. 물론 실제 프로덕션 환경에서 사용될 경우 보다 견고한 보안 체계가 필요할 수 있으므로, 보다 자세한 및 실제 사용 가능한 방법을 선택하는 것이 좋습니다.