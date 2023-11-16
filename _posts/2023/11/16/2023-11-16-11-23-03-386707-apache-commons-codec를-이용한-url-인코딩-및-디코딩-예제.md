---
layout: post
title: "[java] Apache Commons Codec를 이용한 URL 인코딩 및 디코딩 예제"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

URL 인코딩 및 디코딩은 웹 개발에서 자주 사용되는 작업입니다. Apache Commons Codec 라이브러리는 이러한 작업을 간편하게 수행할 수 있는 도구를 제공합니다. 이번 예제에서는 Apache Commons Codec를 사용하여 URL을 인코딩하고 디코딩하는 방법을 살펴보겠습니다.

## 1. Apache Commons Codec 라이브러리 추가

먼저, Apache Commons Codec 라이브러리를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, 프로젝트의 `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependencies>
    <dependency>
        <groupId>commons-codec</groupId>
        <artifactId>commons-codec</artifactId>
        <version>1.15</version>
    </dependency>
</dependencies>
```

Maven을 사용하지 않는 경우, [Apache Commons Codec 다운로드 페이지](https://commons.apache.org/proper/commons-codec/download_codec.cgi)에서 라이브러리를 직접 다운로드하여 프로젝트에 추가해야 합니다.

## 2. URL 인코딩 예제

아래 코드는 Apache Commons Codec를 사용하여 URL을 인코딩하는 예제입니다.

```java
import org.apache.commons.codec.net.URLCodec;

public class UrlEncoderExample {
    public static void main(String[] args) {
        String url = "https://www.example.com/?query=data with spaces";
        
        URLCodec urlCodec = new URLCodec();
        try {
            String encodedUrl = urlCodec.encode(url);
            System.out.println("Encoded URL: " + encodedUrl);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위 예제에서는 `URLCodec` 클래스를 사용하여 URL을 인코딩하고, 결과를 출력하고 있습니다.

## 3. URL 디코딩 예제

아래 코드는 Apache Commons Codec를 사용하여 URL을 디코딩하는 예제입니다.

```java
import org.apache.commons.codec.net.URLCodec;

public class UrlDecoderExample {
    public static void main(String[] args) {
        String encodedUrl = "https%3A%2F%2Fwww.example.com%2F%3Fquery%3Ddata%20with%20spaces";
        
        URLCodec urlCodec = new URLCodec();
        try {
            String decodedUrl = urlCodec.decode(encodedUrl);
            System.out.println("Decoded URL: " + decodedUrl);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위 예제에서는 `URLCodec` 클래스를 사용하여 인코딩된 URL을 디코딩하고, 결과를 출력하고 있습니다.

## 결론

Apache Commons Codec를 사용하면 웹 개발에서 URL 인코딩 및 디코딩 작업을 간편하게 수행할 수 있습니다. 이번 예제를 통해 URL 인코딩 및 디코딩에 대한 기본적인 사용법을 익힐 수 있었을 것입니다. 추가적으로 Apache Commons Codec 문서를 참고하여 더 다양한 기능을 사용해보시기 바랍니다.

## 참고 자료
- [Apache Commons Codec 다운로드 페이지](https://commons.apache.org/proper/commons-codec/download_codec.cgi)
- [Apache Commons Codec 문서](https://commons.apache.org/proper/commons-codec/)