---
layout: post
title: "[java] Apache Commons Codec를 이용한 ZLIB 압축 예제"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Codec는 다양한 인코딩 및 디코딩 작업을 수행하는 라이브러리입니다. 이 예제에서는 Apache Commons Codec를 사용하여 ZLIB 압축을 수행하는 방법을 보여줄 것입니다.

## ZLIB 압축이란?
ZLIB은 데이터 압축과 해제를 위한 알고리즘 및 포맷입니다. 이를 사용하여 데이터를 압축하고 해제하여 저장 용량을 줄일 수 있습니다.

## Maven 종속성 추가
먼저 Maven 프로젝트에 Apache Commons Codec 종속성을 추가해야합니다. `pom.xml` 파일에 다음 의존성을 추가해주세요.

```xml
<dependency>
    <groupId>commons-codec</groupId>
    <artifactId>commons-codec</artifactId>
    <version>1.15</version>
</dependency>
```

## ZLIB 압축 예제 코드

이제 실제로 ZLIB 압축을 수행하는 예제 코드를 작성해보겠습니다.

```java
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.codec.binary.StringUtils;
import org.apache.commons.codec.binary.Hex;
import org.apache.commons.codec.binary.BinaryCodec;
import org.apache.commons.codec.binary.StringEncoder;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.zip.Deflater;
import java.util.zip.DeflaterOutputStream;

public class ZlibCompressionExample {

    public static void main(String[] args) {
        String text = "Hello, World!";

        // 문자열을 바이트 배열로 변환하여 압축 진행
        byte[] compressedData = compress(text.getBytes());

        // 압축된 데이터를 Base64 문자열로 인코딩
        String encodedData = Base64.encodeBase64String(compressedData);

        System.out.println("Original Text: " + text);
        System.out.println("Compressed Text: " + encodedData);
    }

    public static byte[] compress(byte[] data) {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        DeflaterOutputStream dos = new DeflaterOutputStream(baos, new Deflater());
        try {
            dos.write(data);
            dos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return baos.toByteArray();
    }
}
```

위 예제는 주어진 문자열을 ZLIB 압축하고 압축된 데이터를 Base64로 인코딩합니다. `compress()` 메소드를 사용하여 ZLIB 압축을 수행하고, `Base64.encodeBase64String()` 메소드를 사용하여 압축된 데이터를 Base64로 인코딩합니다.

위의 코드를 실행하면 원래 텍스트와 압축된 텍스트가 출력됩니다.

## 결론
이 예제로 Apache Commons Codec를 사용하여 ZLIB 압축을 수행하는 방법을 살펴보았습니다. Apache Commons Codec를 사용하면 다양한 인코딩 및 디코딩 작업을 쉽게 수행할 수 있습니다.

## 참고 자료
- [Apache Commons Codec 공식 문서](https://commons.apache.org/proper/commons-codec/)
- [JavaDoc - Apache Commons Codec](https://commons.apache.org/proper/commons-codec/apidocs/index.html)