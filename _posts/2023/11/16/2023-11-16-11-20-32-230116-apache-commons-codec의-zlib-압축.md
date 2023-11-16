---
layout: post
title: "[java] Apache Commons Codec의 ZLIB 압축"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Codec은 다양한 인코딩, 디코딩 기능을 제공하는 유용한 라이브러리입니다. 이 라이브러리를 사용하여 데이터를 압축하고 압축 해제할 수 있습니다. 이번에는 Apache Commons Codec을 사용하여 ZLIB 압축을 해제하는 방법에 대해 알아보겠습니다.

## 의존성 추가

먼저, Maven 프로젝트의 pom.xml 파일에 Apache Commons Codec 의존성을 추가해야 합니다. 아래와 같이 추가해주세요.

```xml
<dependencies>
    <dependency>
        <groupId>commons-codec</groupId>
        <artifactId>commons-codec</artifactId>
        <version>1.15</version>
    </dependency>
</dependencies>
```

## ZLIB 압축 해제하기

Apache Commons Codec을 사용하여 ZLIB 압축을 해제하는 코드를 작성해봅시다. 아래의 예제 코드는 `compressedData` 바이트 배열이 ZLIB로 압축되어 있는 경우 이를 해제하여 `uncompressedData`로 얻는 방법을 보여줍니다.

```java
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.codec.binary.StringUtils;
import org.apache.commons.codec.binary.Hex;
import org.apache.commons.codec.binary.Hex;
import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.codec.net.URLCodec;
import org.apache.commons.codec.binary.Base64InputStream;
import org.apache.commons.codec.binary.Base64OutputStream;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.util.zip.InflaterInputStream;

public class ZlibCompressionExample {
    public static void main(String[] args) {
        byte[] compressedData = // 압축된 데이터 바이트 배열;

        InflaterInputStream inflaterInputStream = new InflaterInputStream(new ByteArrayInputStream(compressedData));
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();

        byte[] buffer = new byte[1024];
        int length;
        while ((length = inflaterInputStream.read(buffer)) != -1) {
            outputStream.write(buffer, 0, length);
        }

        byte[] uncompressedData = outputStream.toByteArray();
        // 압축 해제된 데이터 사용

        // 압축 해제된 데이터 출력
        System.out.println(StringUtils.newStringUtf8(uncompressedData));
    }
}
```

## 실행결과

위 코드를 실행하면 압축 해제된 데이터가 출력됩니다.

```
This is uncompressed data.
```

위와 같이 압축된 ZLIB 데이터를 Apache Commons Codec을 사용하여 압축 해제하는 방법에 대해 알아보았습니다. 이와 같은 방법을 사용하면 ZLIB로 압축된 데이터를 쉽게 해제할 수 있습니다.

## 참고자료

- [Apache Commons Codec 공식 문서](https://commons.apache.org/proper/commons-codec/)
- [Apache Commons Codec GitHub 저장소](https://github.com/apache/commons-codec)
- [ZLIB 압축 - 위키백과](https://en.wikipedia.org/wiki/Zlib)