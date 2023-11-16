---
layout: post
title: "[java] Java Apache Commons Codec 라이브러리"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java Apache Commons Codec는 Apache 소프트웨어 재단에서 제공하는 자바 라이브러리입니다. 이 라이브러리는 문자열 데이터의 인코딩, 디코딩, 해시 기능 등을 제공하여 다양한 암호화 및 인코딩 작업을 간단하게 수행할 수 있습니다.

## 설치

Java Apache Commons Codec 라이브러리를 프로젝트에 사용하려면 먼저 해당 라이브러리를 다운로드하고 빌드 경로에 추가해야 합니다. 다음은 Maven을 사용하여 라이브러리를 설치하는 방법입니다.

```xml
<dependencies>
    <dependency>
        <groupId>commons-codec</groupId>
        <artifactId>commons-codec</artifactId>
        <version>1.15</version>
    </dependency>
</dependencies>
```

위의 코드를 pom.xml 파일의 dependencies 섹션에 추가하면 Maven이 라이브러리를 자동으로 다운로드하고 프로젝트에 추가합니다.

## 사용법

Java Apache Commons Codec를 사용하여 다양한 작업을 수행할 수 있습니다. 다음은 몇 가지 주요 기능에 대한 예제입니다.

### Base64 인코딩/디코딩

```java
import org.apache.commons.codec.binary.Base64;

String originalText = "Hello, world!";
byte[] encodedBytes = Base64.encodeBase64(originalText.getBytes());
String encodedText = new String(encodedBytes);

// 인코딩된 텍스트 출력
System.out.println(encodedText);

byte[] decodedBytes = Base64.decodeBase64(encodedText.getBytes());
String decodedText = new String(decodedBytes);

// 디코딩된 텍스트 출력
System.out.println(decodedText);
```

### MD5 해시 생성

```java
import org.apache.commons.codec.digest.DigestUtils;

String originalText = "Hello, world!";
String md5Hash = DigestUtils.md5Hex(originalText);

// MD5 해시 출력
System.out.println(md5Hash);
```

### SHA-256 해시 생성

```java
import org.apache.commons.codec.digest.DigestUtils;

String originalText = "Hello, world!";
String sha256Hash = DigestUtils.sha256Hex(originalText);

// SHA-256 해시 출력
System.out.println(sha256Hash);
```

위의 코드에서는 Base64 인코딩과 디코딩, MD5 및 SHA-256 해시 생성을 보여주고 있습니다. 이외에도 Apache Commons Codec 라이브러리는 많은 다른 유용한 기능을 제공합니다.

## 참고 자료

- [Apache Commons Codec 공식 문서](https://commons.apache.org/proper/commons-codec/)
- [Apache Commons Codec GitHub 리포지토리](https://github.com/apache/commons-codec)