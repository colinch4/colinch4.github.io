---
layout: post
title: "[java] Protocol Buffers를 사용하여 Java에서 동기적 RPC 통신 구현하기"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Protocol Buffers는 구조화된 데이터를 직렬화하고, 다양한 환경에서 효율적으로 통신하기 위한 IDL (Interface Description Language)입니다. 이 기술을 사용하여 Java에서 동기적 RPC (Remote Procedure Call) 통신을 구현하는 방법을 알아보겠습니다.

## 1. Protocol Buffers 설치하기
먼저 Protocol Buffers와 관련 도구를 설치해야 합니다. [여기](https://developers.google.com/protocol-buffers/)에서 Protocol Buffers의 최신 버전을 다운로드 받아 설치하세요.

## 2. 프로토콜 정의하기
RPC 통신에 사용할 메시지 형식을 정의하기 위해 프로토콜을 작성해야 합니다. 일반적으로 `.proto` 확장자를 사용합니다. 아래는 간단한 예시입니다:

```protobuf
syntax = "proto3";

message Request {
  string message = 1;
}

message Response {
  string message = 1;
}
```

위의 예시에서는 `Request`와 `Response`라는 두 개의 메시지 형식을 정의하였습니다. 각각 문자열 형식의 `message` 필드를 가지고 있습니다.

## 3. Protocol Buffers 코드 생성하기
프로토콜 정의 파일로부터 Java 코드를 생성해야 합니다. 이를 위해서는 `protoc` 명령을 사용해야 합니다. 다음 명령을 실행하여 Java 코드를 생성하세요:

```
protoc --java_out=<output_directory> <your_proto_file.proto>
```

`<output_directory>`는 생성된 Java 코드의 출력 경로를 지정하는 부분입니다.

## 4. RPC 서버 구현하기
Protocol Buffers 코드를 사용하여 Java에서 RPC 서버를 구현할 수 있습니다. 예를 들어, 다음과 같이 `Server` 클래스를 작성할 수 있습니다:

```java
import com.your.package.YourProtoFile.*;

public class Server {

  public static void main(String[] args) throws IOException {
    // 서버 초기화 코드
    ServerSocket serverSocket = new ServerSocket(8080);
    Socket clientSocket = serverSocket.accept();
    InputStream inputStream = clientSocket.getInputStream();
    OutputStream outputStream = clientSocket.getOutputStream();
    
    // 클라이언트로부터 요청 메시지 수신
    Request request = Request.parseDelimitedFrom(inputStream);

    // 요청 처리
    String responseMessage = processRequest(request.getMessage());

    // 응답 메시지 전송
    Response response = Response.newBuilder()
                                  .setMessage(responseMessage)
                                  .build();
    response.writeDelimitedTo(outputStream);
    
    // 클라이언트와 연결 종료
    clientSocket.close();
    serverSocket.close();
  }

  private static String processRequest(String message) {
    // 요청 처리 로직 구현
    return "Hello, " + message + "!";
  }
}
```

위의 예시에서는 단일 소켓 연결을 통해 클라이언트의 요청을 수신하고, 요청에 대한 처리 후 응답을 보내는 간단한 RPC 서버를 구현하였습니다.

## 5. RPC 클라이언트 구현하기
RPC 통신을 위한 클라이언트를 구현해보겠습니다. 다음은 `Client` 클래스의 예시입니다:

```java
import com.your.package.YourProtoFile.*;

public class Client {

  public static void main(String[] args) throws IOException {
    // 서버에 접속
    Socket socket = new Socket("localhost", 8080);
    InputStream inputStream = socket.getInputStream();
    OutputStream outputStream = socket.getOutputStream();

    // 요청 메시지 생성 및 전송
    Request request = Request.newBuilder()
                             .setMessage("World")
                             .build();
    request.writeDelimitedTo(outputStream);

    // 응답 메시지 수신
    Response response = Response.parseDelimitedFrom(inputStream);

    // 응답 처리
    System.out.println("서버 응답: " + response.getMessage());
    
    // 서버와 연결 종료
    socket.close();
  }
}
```

위의 예시에서는 서버에 연결하여 요청 메시지를 전송하고, 서버로부터 응답 메시지를 수신하는 간단한 RPC 클라이언트를 구현하였습니다.

## 마무리
이제 Protocol Buffers를 사용하여 Java에서 동기적 RPC 통신을 구현하는 방법을 알게 되었습니다. Protocol Buffers의 큰 장점은 간결하고 효율적인 데이터 직렬화 및 통신을 가능하게 해준다는 점입니다. 이를 통해 서로 다른 시스템 간에 데이터를 주고받을 때 활용할 수 있습니다. 자세한 내용은 [공식 문서](https://developers.google.com/protocol-buffers/)를 참조하시기 바랍니다.