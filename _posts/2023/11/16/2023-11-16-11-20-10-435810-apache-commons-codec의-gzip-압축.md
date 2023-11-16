---
layout: post
title: "[java] Apache Commons Codec의 GZIP 압축"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이 블로그 포스트에서는 Apache Commons Codec 라이브러리를 사용하여 Java에서 GZIP 압축을 수행하는 방법에 대해 알아보겠습니다. GZIP 압축은 데이터를 압축하여 저장 공간을 절약하거나 네트워크 전송 시간을 단축시키기 위해 사용됩니다.

## 1. Apache Commons Codec 라이브러리 추가

GZIP 압축을 수행하기 위해 먼저 Apache Commons Codec 라이브러리를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우 `pom.xml`에 다음 의존성을 추가하세요:

```xml
<dependency>
    <groupId>commons-codec</groupId>
    <artifactId>commons-codec</artifactId>
    <version>1.15</version>
</dependency>
```

Gradle을 사용하는 경우 `build.gradle`에 다음 의존성을 추가하세요:

```groovy
implementation 'commons-codec:commons-codec:1.15'
```

## 2. GZIP 압축 수행하기

다음은 Apache Commons Codec를 사용하여 GZIP 압축을 수행하는 예제 코드입니다:

```java
import org.apache.commons.codec.binary.Base64OutputStream;
import org.apache.commons.codec.binary.StringUtils;
import org.apache.commons.codec.digest.DigestUtils;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.zip.GZIPOutputStream;

public class GzipCompressionExample {
    public static void main(String[] args) {
        String data = "Hello, World!";
        
        try {
            byte[] compressedData = compress(data);
            String base64EncodedData = StringUtils.newStringUtf8(Base64.encodeBase64(compressedData));
            System.out.println("Compressed and Base64-encoded data: " + base64EncodedData);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static byte[] compress(String data) throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        GZIPOutputStream gzipOutputStream = new GZIPOutputStream(baos);
        gzipOutputStream.write(data.getBytes());
        gzipOutputStream.close();
        return baos.toByteArray();
    }
}
```

이 예제는 "Hello, World!" 문자열을 GZIP 형식으로 압축하고, 그 결과를 Base64로 인코딩하여 출력합니다.

## 마무리

이렇게 Apache Commons Codec를 사용하여 Java에서 GZIP 압축을 수행하는 방법을 알아보았습니다. GZIP 압축은 데이터 전송 및 저장을 효율적으로 처리하기 위해 사용되는 강력한 도구입니다.

더 많은 정보를 원하신다면 [Apache Commons Codec 공식 문서](https://commons.apache.org/proper/commons-codec/)를 참조하세요.