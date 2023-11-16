---
layout: post
title: "[java] Apache Commons Codec를 이용한 Hex 인코딩 및 디코딩 예제"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Commons Codec는 다양한 인코딩과 디코딩을 지원하는 유용한 라이브러리입니다. 이 중에서 Hex 인코딩과 디코딩을 할 수 있는 기능을 사용해보겠습니다.

## Hex 인코딩 예제

```java
import org.apache.commons.codec.binary.Hex;

public class HexEncodingExample {
    public static void main(String[] args) {
        String input = "Hello, World!";
        byte[] inputBytes = input.getBytes();

        // Hex로 인코딩
        String hexEncoded = Hex.encodeHexString(inputBytes);

        System.out.println("Hex encoded: " + hexEncoded);
    }
}
```

위의 예제는 주어진 문자열을 `getBytes()` 메서드를 통해 바이트 배열로 변환한 후, `Hex.encodeHexString()` 메서드를 사용하여 Hex로 인코딩한 결과를 출력하는 예제입니다.

## Hex 디코딩 예제

```java
import org.apache.commons.codec.binary.Hex;

public class HexDecodingExample {
    public static void main(String[] args) {
        String hexEncoded = "48656c6c6f2c20576f726c6421";

        try {
            // Hex를 디코딩
            byte[] decodedBytes = Hex.decodeHex(hexEncoded);

            String decodedString = new String(decodedBytes);
            System.out.println("Decoded string: " + decodedString);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위의 예제는 주어진 Hex 문자열을 `Hex.decodeHex()` 메서드를 사용하여 디코딩한 후, `String`으로 변환하여 디코딩된 문자열을 출력하는 예제입니다. 예외 처리를 통해 디코딩 중 발생할 수 있는 오류를 처리하도록 작성되었습니다.

## 결론

Apache Commons Codec의 Hex 인코딩과 디코딩 기능을 사용하면 간편하게 문자열을 Hex로 인코딩하고 디코딩할 수 있습니다. 이 예제들을 통해 Hex 인코딩과 디코딩을 쉽게 사용할 수 있는 방법을 알아보았습니다.

### 참고 자료
- [Apache Commons Codec 홈페이지](https://commons.apache.org/proper/commons-codec/)
- [Apache Commons Codec API 문서](https://commons.apache.org/proper/commons-codec/apidocs/index.html)