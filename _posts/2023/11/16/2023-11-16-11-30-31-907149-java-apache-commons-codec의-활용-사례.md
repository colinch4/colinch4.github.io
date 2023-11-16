---
layout: post
title: "[java] Java Apache Commons Codec의 활용 사례"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

## 1. Apache Commons Codec이란?

Apache Commons Codec은 Apache Software Foundation에서 제공하는 자바 라이브러리로, 다양한 인코딩 및 디코딩 기능을 제공합니다. 이 라이브러리를 사용하면 문자열, 바이트 배열, URL 등의 데이터를 다양한 인코딩 형식으로 변환할 수 있습니다.

## 2. Base64 인코딩 기능

Apache Commons Codec을 사용하면 Base64 인코딩과 디코딩을 간편하게 수행할 수 있습니다. 다음은 Base64 인코딩의 예제 코드입니다.

```java
import org.apache.commons.codec.binary.Base64;

public class Base64Example {
    public static void main(String[] args) {
        String originalString = "Hello, world!";
        byte[] originalBytes = originalString.getBytes();

        // Base64 인코딩
        byte[] encodedBytes = Base64.encodeBase64(originalBytes);
        String encodedString = new String(encodedBytes);

        System.out.println("Encoded String: " + encodedString);

        // Base64 디코딩
        byte[] decodedBytes = Base64.decodeBase64(encodedBytes);
        String decodedString = new String(decodedBytes);

        System.out.println("Decoded String: " + decodedString);
    }
}
```

이 예제에서는 먼저 문자열을 바이트 배열로 변환한 후, Base64 인코딩을 수행합니다. 인코딩된 바이트 배열은 다시 문자열로 변환되어 출력됩니다. 이후 디코딩 과정을 통해 원래의 문자열을 복원합니다.

## 3. URL 인코딩 기능

Apache Commons Codec을 사용하면 URL 인코딩을 쉽게 수행할 수 있습니다. 다음은 URL 인코딩의 예제 코드입니다.

```java
import org.apache.commons.codec.net.URLCodec;

public class UrlEncodingExample {
    public static void main(String[] args) {
        URLCodec urlCodec = new URLCodec();

        String originalUrl = "https://example.com/?query=한글";
        String encodedUrl = urlCodec.encode(originalUrl);

        System.out.println("Encoded URL: " + encodedUrl);

        String decodedUrl = urlCodec.decode(encodedUrl);

        System.out.println("Decoded URL: " + decodedUrl);
    }
}
```

이 예제에서는 주어진 URL을 URLCodec을 사용해서 인코딩합니다. 인코딩된 URL은 다시 디코딩되어 원래의 URL을 복원합니다.

## 4. 참고 자료

- [Apache Commons Codec 공식 문서](https://commons.apache.org/proper/commons-codec/)
- [Apache Commons Codec GitHub 저장소](https://github.com/apache/commons-codec)

Apache Commons Codec의 다양한 기능과 사용 방법에 대한 자세한 내용은 공식 문서와 GitHub 저장소를 참고하시면 됩니다.