---
layout: post
title: "[java] Java Apache Commons Codec vs. 기본 Java 인코딩 기능"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java는 다양한 인코딩 및 디코딩 작업을 수행하기 위한 기능을 포함하고 있습니다. 이 중에서도 기본 인코딩 기능과 Apache Commons Codec 라이브러리를 비교해보겠습니다.

## 1. 기본 Java 인코딩 기능

Java의 기본 인코딩 기능은 `java.nio.charset` 패키지에 포함되어 있습니다. 이 패키지를 사용하여 문자열을 다른 인코딩으로 변환하거나, 인코딩된 문자열을 디코딩할 수 있습니다.

```java
String text = "안녕하세요";
byte[] utfBytes = text.getBytes("UTF-8"); // 문자열을 UTF-8로 인코딩하여 byte 배열로 변환
String decodedText = new String(utfBytes, "UTF-8"); // UTF-8로 디코딩하여 문자열로 변환

System.out.println(decodedText); // 출력: 안녕하세요
```

기본 인코딩 기능은 간단하고 편리하지만, 일부 특수한 인코딩에 대한 지원이 제한적일 수 있습니다.

## 2. Apache Commons Codec

Apache Commons Codec은 Apache 소프트웨어 재단에서 제공하는 인코딩 및 디코딩 기능을 포함한 라이브러리입니다. 이 라이브러리는 기본 Java 인코딩 기능보다 더 많은 인코딩 형식을 지원하며, 높은 성능과 풍부한 기능을 제공합니다.

Apache Commons Codec을 사용하려면 먼저 의존성을 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음의 의존성을 추가합니다.

```xml
<dependency>
    <groupId>commons-codec</groupId>
    <artifactId>commons-codec</artifactId>
    <version>1.15</version>
</dependency>
```

Apache Commons Codec을 사용하여 문자열을 인코딩하거나 디코딩하는 예제 코드는 다음과 같습니다.

```java
import org.apache.commons.codec.binary.Base64; // Base64 인코딩을 위한 클래스

String text = "안녕하세요";
byte[] utfBytes = text.getBytes("UTF-8");

String encodedText = Base64.encodeBase64String(utfBytes); // Base64로 인코딩된 문자열로 변환
byte[] decodedBytes = Base64.decodeBase64(encodedText); // Base64로 디코딩된 byte 배열로 변환
String decodedText = new String(decodedBytes, "UTF-8"); // byte 배열을 UTF-8로 디코딩하여 문자열로 변환

System.out.println(decodedText); // 출력: 안녕하세요
```

Apache Commons Codec을 사용하면 다양한 인코딩 형식에 대한 지원과 추가적인 기능을 활용할 수 있습니다. 예를 들어, Base64 인코딩, URL 인코딩, SHA-256 해시 등의 작업을 간편하게 수행할 수 있습니다.

## 3. 결론

기본 Java 인코딩 기능과 Apache Commons Codec은 각각 장단점이 있습니다. 기본 기능은 간단하고 쉽게 사용할 수 있지만, 특정 인코딩 형식에 제한이 있을 수 있습니다. 반면 Apache Commons Codec은 다양한 인코딩 형식을 지원하며, 풍부한 기능을 제공하지만 의존성 추가와 런타임 성능에 약간의 부하가 있을 수 있습니다.

프로젝트의 요구사항에 맞는 선택을 고려하여 기본 Java 인코딩 기능 또는 Apache Commons Codec을 적절하게 활용해야 합니다.

## 참고 자료
- [Apache Commons Codec 공식 문서](https://commons.apache.org/proper/commons-codec/)
- [Java `java.nio.charset` 패키지 공식 문서](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/nio/charset/package-summary.html)