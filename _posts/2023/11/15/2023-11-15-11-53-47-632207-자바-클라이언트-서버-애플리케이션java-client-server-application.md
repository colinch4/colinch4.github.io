---
layout: post
title: "[java] 자바 클라이언트-서버 애플리케이션(Java client-server application)"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

자바는 네트워크 기능을 지원하기 위한 다양한 라이브러리와 API를 제공합니다. 이를 활용하여 클라이언트-서버 모델로 동작하는 애플리케이션을 개발할 수 있습니다. 이번 블로그 글에서는 자바를 사용하여 클라이언트-서버 애플리케이션을 개발하는 방법에 대해 알아보겠습니다.

## 클라이언트-서버 모델

클라이언트-서버 모델은 애플리케이션을 클라이언트와 서버로 구분하여 동작시키는 아키텍처입니다. 클라이언트는 서버에 요청을 보내고, 서버는 요청에 대한 응답을 반환하는 방식으로 동작합니다. 클라이언트는 일반적으로 사용자가 사용하는 디바이스(예: 컴퓨터, 스마트폰)를 말하며, 서버는 요청을 처리하고 응답을 반환하는 컴퓨터를 말합니다.

## 자바로 클라이언트-서버 애플리케이션 개발하기

자바에서 클라이언트-서버 애플리케이션을 개발하기 위해서는 다음과 같은 단계를 따를 수 있습니다.

1. 서버 소켓 생성: `ServerSocket` 클래스를 사용하여 서버 소켓을 생성합니다.
```java
ServerSocket serverSocket = new ServerSocket(8080);
```

2. 클라이언트 요청 수락: `accept()` 메서드를 호출하여 클라이언트의 접속을 기다립니다. 클라이언트가 접속하면 `Socket` 객체를 반환합니다.
```java
Socket clientSocket = serverSocket.accept();
```

3. 데이터 통신: 클라이언트와 서버는 `Socket` 객체를 사용하여 데이터를 주고받을 수 있습니다. `InputStream`과 `OutputStream`을 사용하여 데이터를 읽고 쓸 수 있습니다.
```java
InputStream inputStream = clientSocket.getInputStream();
OutputStream outputStream = clientSocket.getOutputStream();
```

4. 클라이언트 연결 종료: 데이터 통신이 끝난 후에는 `Socket`을 닫아 클라이언트와의 연결을 종료합니다.
```java
clientSocket.close();
```

자바 클라이언트-서버 애플리케이션을 개발하는 방법에 대해 간단하게 알아보았습니다. 클라이언트와 서버 간의 통신에는 더 다양한 기능과 프로토콜을 활용할 수 있습니다. 자세한 내용은 자바 공식 문서 및 관련 자료를 참고하시기 바랍니다.

## 참고 자료

- [자바 공식 문서](https://docs.oracle.com/en/java/)
- [Java Network Programming](https://www.oreilly.com/library/view/java-network-programming/9781449370067/) by Elliotte Rusty Harold