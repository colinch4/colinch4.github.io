---
layout: post
title: "[java] Apache Commons Codec를 이용한 GZIP 압축 예제"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Codec는 GZIP 압축을 쉽게 처리할 수 있는 유용한 도구입니다. 이 예제에서는 Apache Commons Codec를 사용하여 텍스트 데이터를 GZIP 형식으로 압축하는 방법을 보여줍니다.

먼저, Apache Commons Codec를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 아래의 의존성을 추가합니다.

```xml
<dependency>
    <groupId>commons-codec</groupId>
    <artifactId>commons-codec</artifactId>
    <version>1.15</version>
</dependency>
```

그런 다음, 다음과 같은 코드를 사용하여 텍스트 데이터를 GZIP 형식으로 압축할 수 있습니다.

```java
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.codec.binary.StringUtils;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.zip.GZIPOutputStream;

public class GzipCompressionExample {

    public static void main(String[] args) throws IOException {
        String input = "This is a sample text to be compressed using GZIP.";

        // 문자열을 바이트 배열로 변환
        byte[] inputBytes = StringUtils.getBytesUtf8(input);

        // GZIP 압축을 위해 버퍼 지정
        ByteArrayOutputStream byteStream = new ByteArrayOutputStream();
        GZIPOutputStream gzipStream = new GZIPOutputStream(byteStream);

        // 원본 데이터를 GZIP으로 압축
        gzipStream.write(inputBytes);
        gzipStream.close();

        // 압축된 데이터를 Base64로 인코딩
        byte[] compressedBytes = byteStream.toByteArray();
        String base64Encoded = Base64.encodeBase64String(compressedBytes);

        System.out.println("Compressed and encoded output: " + base64Encoded);
    }
}
```

이 코드는 주어진 문자열을 GZIP 형식으로 압축한 다음, 압축된 데이터를 Base64로 인코드하여 출력합니다. 

위의 예제에서는 Apache Commons Codec의 `Base64`와 `StringUtils` 클래스를 사용하여 데이터를 인코드하고 디코드할 수 있습니다.

Apache Commons Codec 공식 문서에는 더 많은 정보와 유용한 기능들이 있으니 참고하시기 바랍니다.

- [Apache Commons Codec 공식 문서](https://commons.apache.org/proper/commons-codec/)
- [Apache Commons Codec GitHub 저장소](https://github.com/apache/commons-codec)

Apache Commons Codec는 텍스트뿐만 아니라 바이너리 데이터의 인코딩/디코딩에도 사용될 수 있으므로 유용한 도구입니다. GZIP 압축 외에도 여러 다른 유형의 인코딩/디코딩 작업을 지원합니다.