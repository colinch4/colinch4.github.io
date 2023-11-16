---
layout: post
title: "[java] Apache Commons Codec의 URL 인코딩과 디코딩"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

URL은 웹에서 리소스를 식별하기 위해 사용되는 주소입니다. 때로는 URL에 퍼센트 인코딩이 필요할 수 있습니다. 퍼센트 인코딩은 URL에서 특수 문자를 대체 문자열로 변환하여 안전한 표현을 만듭니다.

Apache Commons Codec은 다양한 인코딩 및 디코딩 기능을 제공하는 유용한 라이브러리입니다. 이를 사용하여 URL을 인코딩하고 디코딩하는 방법을 살펴보겠습니다.

## 의존성 추가

먼저, Maven 프로젝트를 사용한다면 `pom.xml` 파일에 다음 종속성을 추가해야 합니다:

```xml
<dependency>
    <groupId>commons-codec</groupId>
    <artifactId>commons-codec</artifactId>
    <version>1.15</version>
</dependency>
```

## URL 인코딩

URL 인코딩은 특수 문자를 `%` 기호와 함께 16진수로 표현하는 작업입니다. Apache Commons Codec를 사용하여 URL 인코딩을 수행하는 방법은 다음과 같습니다:

```java
import org.apache.commons.codec.net.URLCodec;

public class UrlEncodingExample {
    public static void main(String[] args) {
        String url = "https://www.example.com/?query=한글";
        
        URLCodec codec = new URLCodec();
        String encodedUrl = codec.encode(url);
        
        System.out.println(encodedUrl);
    }
}
```

위의 예제에서는 `URLCodec` 객체를 생성하고 `encode` 메소드를 사용하여 URL을 인코딩했습니다. 결과로는 `https%3A%2F%2Fwww.example.com%2F%3Fquery%3D%ED%95%9C%EA%B8%80`와 같이 인코딩된 URL을 얻게 됩니다.

## URL 디코딩

URL 디코딩은 인코딩된 URL을 원래의 형태로 변환하는 작업입니다. Apache Commons Codec를 사용하여 URL 디코딩을 수행하는 방법은 다음과 같습니다:

```java
import org.apache.commons.codec.net.URLCodec;

public class UrlDecodingExample {
    public static void main(String[] args) {
        String encodedUrl = "https%3A%2F%2Fwww.example.com%2F%3Fquery%3D%ED%95%9C%EA%B8%80";
        
        URLCodec codec = new URLCodec();
        String decodedUrl = codec.decode(encodedUrl);
        
        System.out.println(decodedUrl);
    }
}
```

위의 예제에서는 `URLCodec` 객체를 생성하고 `decode` 메소드를 사용하여 URL을 디코딩했습니다. 결과로는 `https://www.example.com/?query=한글`과 같이 디코딩된 URL을 얻게 됩니다.

## 결론

Apache Commons Codec을 사용하면 손쉽게 URL을 인코딩하고 디코딩할 수 있습니다. 이를 통해 안전한 URL 표현을 유지하면서 웹 애플리케이션에서 URL을 다룰 때 발생할 수 있는 문제를 방지할 수 있습니다.

더 자세한 내용은 [Apache Commons Codec 공식 문서](https://commons.apache.org/proper/commons-codec/)를 참조하십시오.