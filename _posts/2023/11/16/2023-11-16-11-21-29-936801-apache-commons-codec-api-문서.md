---
layout: post
title: "[java] Apache Commons Codec API 문서"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Codec은 다양한 인코딩과 디코딩 기능을 제공하는 유용한 라이브러리입니다. 이 문서에서는 Apache Commons Codec API의 주요 기능과 사용법에 대해 알아보겠습니다.

## 1. Base64 인코딩/디코딩

Base64는 바이너리 데이터를 텍스트로 인코딩하는 방법입니다. Apache Commons Codec을 사용하여 Base64 인코딩과 디코딩을 쉽게 할 수 있습니다.

아래는 Base64 인코딩과 디코딩의 예시 코드입니다.

```java
import org.apache.commons.codec.binary.Base64;

public class Base64Example {
    public static void main(String[] args) {
        String originalString = "Hello, world!";
        
        // 문자열을 Base64로 인코딩
        byte[] encodedBytes = Base64.encodeBase64(originalString.getBytes());
        String encodedString = new String(encodedBytes);
        System.out.println("Encoded string: " + encodedString);
        
        // Base64 문자열을 디코딩
        byte[] decodedBytes = Base64.decodeBase64(encodedString.getBytes());
        String decodedString = new String(decodedBytes);
        System.out.println("Decoded string: " + decodedString);
    }
}
```

## 2. URL 인코딩/디코딩

URL 인코딩은 특수 문자를 % 기호를 이용해 인코딩하는 방법입니다. Apache Commons Codec을 사용하여 URL 인코딩과 디코딩을 간편하게 처리할 수 있습니다.

아래는 URL 인코딩과 디코딩의 예시 코드입니다.

```java
import org.apache.commons.codec.net.URLCodec;

public class URLCodecExample {
    public static void main(String[] args) {
        String originalURL = "https://www.example.com/search?q=apache commons codec";
        
        // URL 인코딩
        URLCodec urlCodec = new URLCodec();
        String encodedURL = urlCodec.encode(originalURL);
        System.out.println("Encoded URL: " + encodedURL);
        
        // URL 디코딩
        String decodedURL = urlCodec.decode(encodedURL);
        System.out.println("Decoded URL: " + decodedURL);
    }
}
```

## 3. 암호화 해시 함수

Apache Commons Codec은 다양한 암호화 해시 함수를 제공합니다. 주요 암호화 해시 함수는 MD5, SHA-1, SHA-256, SHA-512 등이 있습니다.

아래는 SHA-256 해시 함수를 사용하여 문자열을 해시하는 예시 코드입니다.

```java
import org.apache.commons.codec.digest.DigestUtils;

public class HashFunctionExample {
    public static void main(String[] args) {
        String originalString = "Hello, world!";
        
        // SHA-256으로 문자열 해싱
        String hashedString = DigestUtils.sha256Hex(originalString);
        System.out.println("Hashed string: " + hashedString);
    }
}
```

위의 코드는 Apache Commons Codec의 `DigestUtils` 클래스를 사용하여 SHA-256 해시 함수를 호출하는 예시입니다.

더 많은 기능과 사용법은 [Apache Commons Codec 문서](https://commons.apache.org/proper/commons-codec/)를 참고해주세요.