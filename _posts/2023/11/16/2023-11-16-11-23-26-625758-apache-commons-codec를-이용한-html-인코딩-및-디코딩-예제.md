---
layout: post
title: "[java] Apache Commons Codec를 이용한 HTML 인코딩 및 디코딩 예제"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java에서 HTML을 인코딩하고 디코딩하는 작업은 보안 및 데이터 처리에 중요한 역할을 합니다. Apache Commons Codec 라이브러리는 이러한 작업을 간편하게 수행할 수 있는 많은 기능을 제공해줍니다.

## Apache Commons Codec 라이브러리 추가하기

먼저, Apache Commons Codec 라이브러리를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음의 의존성을 추가합니다:

```xml
<dependency>
    <groupId>commons-codec</groupId>
    <artifactId>commons-codec</artifactId>
    <version>1.15</version>
</dependency>
```

## HTML 인코딩하기

다음은 Apache Commons Codec를 사용하여 HTML을 인코딩하는 예제 코드입니다:

```java
import org.apache.commons.codec.net.URLCodec;

public class HtmlEncoder {

    public static String encodeHtml(String html) {
        URLCodec urlCodec = new URLCodec();
        String encodedHtml = urlCodec.encode(html);
        return encodedHtml;
    }
    
    public static void main(String[] args) {
        String htmlToEncode = "<h1>Hello, World!</h1>";
        String encodedHtml = encodeHtml(htmlToEncode);
        
        System.out.println("Encoded HTML: " + encodedHtml);
    }
}
```

위의 코드에서는 `URLCodec` 클래스를 사용하여 HTML 문자열을 인코딩합니다. `encodeHtml` 메서드는 HTML 문자열을 입력받아 인코딩된 문자열을 반환합니다. `main` 메서드에서는 인코딩할 HTML 문자열을 정의하고, `encodeHtml` 메서드를 호출하여 인코딩된 결과를 출력합니다.

## HTML 디코딩하기

Apache Commons Codec를 사용하여 인코딩된 HTML 문자열을 디코딩하는 예제 코드는 다음과 같습니다:

```java
import org.apache.commons.codec.net.URLCodec;

public class HtmlDecoder {

    public static String decodeHtml(String encodedHtml) {
        URLCodec urlCodec = new URLCodec();
        String decodedHtml = urlCodec.decode(encodedHtml);
        return decodedHtml;
    }
    
    public static void main(String[] args) {
        String encodedHtml = "%3Ch1%3EHello%2C%20World%21%3C%2Fh1%3E";
        String decodedHtml = decodeHtml(encodedHtml);
        
        System.out.println("Decoded HTML: " + decodedHtml);
    }
}
```

위의 코드에서도 `URLCodec` 클래스를 사용하여 인코딩된 HTML 문자열을 디코딩합니다. `decodeHtml` 메서드는 인코딩된 HTML 문자열을 입력받아 디코딩된 문자열을 반환합니다. `main` 메서드에서는 디코딩할 HTML 문자열을 정의하고, `decodeHtml` 메서드를 호출하여 디코딩된 결과를 출력합니다.

## 결론

Apache Commons Codec을 사용하면 Java에서 간편하게 HTML을 인코딩하고 디코딩할 수 있습니다. 이를 통해 보안과 데이터 처리에 관련된 작업을 더욱 쉽게 수행할 수 있습니다.

## 참고 자료
- [Apache Commons Codec 공식 문서](https://commons.apache.org/proper/commons-codec/)