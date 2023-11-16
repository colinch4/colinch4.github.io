---
layout: post
title: "[java] Apache Commons Codec의 Hex 인코딩과 디코딩"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Codec 라이브러리는 다양한 인코딩 및 디코딩 기능을 제공하는 유용한 도구 모음입니다. 이 중에서 Hex 인코딩과 디코딩 기능은 특히 유용하며, 이 글에서는 이 기능에 대해 알아보겠습니다.

## Hex 인코딩

Hex 인코딩은 이진 데이터를 16진수로 변환하는 방법입니다. 이는 이진 데이터를 텍스트 기반의 형식으로 표현할 수 있게 해주는 기능이며, 주로 네트워크 통신이나 파일 전송 등에서 사용됩니다.

Apache Commons Codec의 Hex 클래스는 이러한 Hex 인코딩 기능을 제공합니다. 아래는 Hex 클래스를 사용하여 문자열을 Hex로 인코딩하는 예제 코드입니다.

```java
import org.apache.commons.codec.binary.Hex;

public class HexEncodingExample {
    public static void main(String[] args) {
        String text = "Hello, world!";
        byte[] encodedBytes = Hex.encodeHexString(text.getBytes());
        String encodedText = new String(encodedBytes);

        System.out.println("Encoded text: " + encodedText);
    }
}
```

위 코드에서 `Hex.encodeHexString()` 메서드는 주어진 바이트 배열을 Hex 형식의 문자열로 인코딩합니다. 이렇게 인코딩된 문자열을 다시 문자열 형태로 변환하여 출력합니다.

## Hex 디코딩

Hex 디코딩은 Hex 인코딩의 역과정으로, 16진수로 표현된 데이터를 이진 데이터로 변환하는 과정입니다. 역시 Apache Commons Codec의 Hex 클래스를 사용하여 이 과정을 수행할 수 있습니다.

아래는 Hex 디코딩을 실행하는 예제 코드입니다.

```java
import org.apache.commons.codec.binary.Hex;

public class HexDecodingExample {
    public static void main(String[] args) {
        String encodedText = "48656c6c6f2c20776f726c6421";
        byte[] decodedBytes = Hex.decodeHex(encodedText.toCharArray());
        String decodedText = new String(decodedBytes);

        System.out.println("Decoded text: " + decodedText);
    }
}
```

위 코드에서 `Hex.decodeHex()` 메서드는 Hex 형식의 문자열을 바이트 배열로 디코딩합니다. 이렇게 디코딩된 바이트 배열을 다시 문자열로 변환하여 출력합니다.

## 결론

Apache Commons Codec의 Hex 클래스를 사용하면 간편하게 Hex 인코딩과 디코딩을 수행할 수 있습니다. 이 기능을 활용하여 이진 데이터를 텍스트로 표현하거나, 역으로 텍스트를 이진 데이터로 변환할 수 있습니다. 자세한 내용은 [공식 문서](https://commons.apache.org/proper/commons-codec/apidocs/org/apache/commons/codec/binary/Hex.html)를 참조하시기 바랍니다.