---
layout: post
title: "[java] Java에서 Protocol Buffers를 사용하여 RPC 통신 구현하기"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

이번 블로그 포스트에서는 Java에서 Protocol Buffers를 사용하여 RPC(Remote Procedure Call) 통신을 구현하는 방법에 대해 알아보겠습니다. Protocol Buffers는 구조화된 데이터를 직렬화하고, 이를 다양한 프로그래밍 언어에서 사용할 수 있도록 도와주는 프로토콜입니다. RPC는 네트워크를 통해 다른 프로세스에게 함수 호출을 요청하고 응답을 받는 통신 방식입니다.

## 1. Protocol Buffers 설치하기

Protocol Buffers는 Google에서 개발한 오픈소스 프로젝트로, 구글의 [공식 사이트](https://developers.google.com/protocol-buffers)에서 Protocol Buffers 컴파일러를 다운로드할 수 있습니다. 컴파일러를 설치한 후, protobuf 스키마 파일(.proto)을 작성하여 데이터 구조를 정의합니다.

## 2. 프로토콜 정의하기

먼저, .proto 파일을 작성하여 데이터 구조를 정의해야 합니다. 이 파일은 메시지 타입과 필드를 정의하며, Protocol Buffers에서 데이터를 직렬화하기 위한 규칙을 정의합니다. 아래는 간단한 예시입니다.

```protobuf
syntax = "proto3";

message Request {
  string message = 1;
}

message Response {
  string message = 1;
}
```

## 3. 프로토콜 컴파일하기

다음으로, 작성한 .proto 파일을 Protocol Buffers 컴파일러를 사용하여 Java 클래스로 컴파일해야 합니다. 아래 명령어를 사용하여 컴파일할 수 있습니다.

```bash
protoc --java_out=./src/main/java/ --proto_path=./src/main/proto/ ./src/main/proto/example.proto
```

위 명령어를 실행하면, example.proto 파일이 컴파일되어 ./src/main/java/ 경로에 Protocol Buffers에서 사용할 수 있는 Java 클래스가 생성됩니다.

## 4. RPC 서버 구현하기

RPC 서버를 구현하기 위해서는 컴파일된 Protocol Buffers Java 클래스를 사용하여 서버를 작성해야 합니다. 아래는 예시 코드입니다.

```java
import com.example.protos.example.Request;
import com.example.protos.example.Response;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

class RpcServer {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(50051);

        while (true) {
            Socket socket = serverSocket.accept();
            processRequest(socket);
            socket.close();
        }
    }

    private static void processRequest(Socket socket) throws IOException {
        Request request = Request.parseDelimitedFrom(socket.getInputStream());
        String message = request.getMessage();

        // 요청 처리 로직 구현

        Response response = Response.newBuilder()
                .setMessage("Hello, " + message)
                .build();
        response.writeDelimitedTo(socket.getOutputStream());
    }
}
```

위 예시 코드에서는 서버 소켓을 생성하고 클라이언트로부터 요청을 받습니다. 요청은 Protocol Buffers로 직렬화되어서 소켓의 입력 스트림으로부터 읽어옵니다. 그리고 요청 처리 로직을 구현한 후, 결과를 Protocol Buffers 메시지 형태로 직렬화하여 클라이언트에게 전송합니다.

## 5. RPC 클라이언트 구현하기

RPC 클라이언트를 구현하기 위해서도 마찬가지로 컴파일된 Protocol Buffers Java 클래스를 사용해야 합니다. 아래는 예시 코드입니다.

```java
import com.example.protos.example.Request;
import com.example.protos.example.Response;

import java.io.IOException;
import java.net.Socket;

class RpcClient {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost", 50051);

        Request request = Request.newBuilder()
                .setMessage("World")
                .build();
        request.writeDelimitedTo(socket.getOutputStream());

        Response response = Response.parseDelimitedFrom(socket.getInputStream());
        String message = response.getMessage();
        System.out.println("Response: " + message);

        socket.close();
    }
}
```

위 예시 코드에서는 서버와 소켓을 연결한 후, 요청 메시지를 생성하여 직렬화하여 서버에게 전송합니다. 그 후, 서버로부터 응답을 받아 역직렬화하여 결과를 출력합니다.

## 결론

이제 Protocol Buffers를 사용하여 Java에서 RPC 통신을 구현하는 방법에 대해 알아보았습니다. Protocol Buffers를 사용하면 구조화된 데이터를 직렬화하고, 네트워크를 통해 효율적으로 데이터를 주고받을 수 있습니다. 자세한 내용은 공식 사이트의 문서를 참고하시기 바랍니다.