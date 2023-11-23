---
layout: post
title: "[java] Java에서 Protocol Buffers를 사용하여 비동기 RPC 통신 구현하기"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Protocol Buffers는 구조화된 데이터를 직렬화하고, 다른 시스템 간에 효율적인 통신을 할 수 있게 해주는 언어 중립적인 인터페이스 정의 언어입니다. 이 기술을 사용하면 다양한 프로그래밍 언어 환경에서 데이터를 손쉽게 주고받을 수 있습니다.

이 글에서는 Java에서 Protocol Buffers를 사용하여 비동기 RPC(원격 프로시저 호출) 통신을 구현하는 방법에 대해 알아보겠습니다.

## Protocol Buffers의 설치

먼저, Protocol Buffers를 사용하기 위해 Protobuf 컴파일러를 설치해야 합니다. Protobuf는 Google에서 개발한 Protocol Buffers의 공식 컴파일러입니다.

1. [Protocol Buffers 컴파일러 다운로드 페이지](https://github.com/protocolbuffers/protobuf/releases)에서 해당하는 운영체제의 컴파일러를 다운로드합니다.
2. 압축을 해제한 후, PATH 환경 변수에 컴파일러 실행 파일의 경로를 추가합니다.

## Proto 파일 작성

Proto 파일은 Protocol Buffers의 데이터 구조와 메시지를 정의하는 파일입니다. RPC 통신을 할 때 사용할 메시지 타입과 메서드를 정의해야 합니다.

```protobuf
syntax = "proto3";

package com.example.rpc;

service RpcService {
  rpc SayHello(Request) returns (Response) {}
}

message Request {
  string name = 1;
}

message Response {
  string message = 1;
}
```

위의 예시는 `RpcService`라는 서비스를 정의하고, `SayHello`라는 메서드를 가지는 것을 보여줍니다. `Request`와 `Response`는 각각 해당 메서드의 요청과 응답에 사용되는 메시지입니다.

## Proto 파일 컴파일

Proto 파일을 컴파일하여 Java 클래스를 생성해야 합니다. 이를 위해 다음과 같은 명령을 사용합니다.

```
protoc --java_out=[output directory] [proto file]
```

여기서 `[output directory]`는 자바 클래스 파일을 생성할 디렉토리 경로를, `[proto file]`은 작성한 Proto 파일의 경로를 나타냅니다.

## Java 코드 작성

Proto 파일을 컴파일한 후에는 Java 코드에서 해당 메시지 타입과 RPC 메서드를 사용할 수 있습니다.

```java
import com.example.rpc.RpcService;
import com.example.rpc.Request;
import com.example.rpc.Response;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class RpcClient {

    public static void main(String[] args) {
        ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 50051)
                .usePlaintext()
                .build();

        RpcService.RpcServiceBlockingStub stub = RpcService.newBlockingStub(channel);

        Request request = Request.newBuilder().setName("John").build();
        Response response = stub.sayHello(request);

        System.out.println("Response: " + response.getMessage());

        channel.shutdown();
    }
}
```

위의 예시는 Protocol Buffers를 기반으로 한 gRPC 클라이언트 코드입니다. gRPC는 Protocol Buffers를 사용하여 클라이언트와 서버 간에 효율적인 통신을 할 수 있는 플랫폼 중 하나입니다.

## 서버 구현

클라이언트와 마찬가지로 서버도 Protocol Buffers를 사용하여 구현할 수 있습니다. 다음은 gRPC 서버를 구현하는 Java 코드의 예시입니다.

```java
import com.example.rpc.RpcService;
import com.example.rpc.Request;
import com.example.rpc.Response;
import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;

import java.io.IOException;

public class RpcServer {

    public static void main(String[] args) throws IOException, InterruptedException {
        Server server = ServerBuilder.forPort(50051)
                .addService(new RpcServiceImpl())
                .build();

        server.start();
        System.out.println("Server started");

        server.awaitTermination();
    }

    static class RpcServiceImpl extends RpcService.RpcServiceImplBase {

        @Override
        public void sayHello(Request request, StreamObserver<Response> responseObserver) {
            String name = request.getName();
            String message = "Hello, " + name + "!";

            Response response = Response.newBuilder().setMessage(message).build();
            responseObserver.onNext(response);
            responseObserver.onCompleted();
        }
    }
}
```

위의 예시는 gRPC 서버를 구현하는 Java 코드입니다. `RpcServiceImpl` 클래스는 `RpcService` 인터페이스를 상속받아 메서드를 구현합니다.

## 실행

Java 코드를 컴파일하고 실행하기 위해서는 다음과 같은 단계를 따릅니다.

1. Proto 파일을 컴파일하여 Java 클래스를 생성합니다.
2. 클라이언트와 서버 코드를 컴파일합니다.
3. 서버를 먼저 실행한 후, 클라이언트를 실행합니다.

```
javac *.java
java RpcServer
java RpcClient
```

위의 명령을 순서대로 실행하면, 클라이언트가 서버에 요청을 보내고 응답을 받아 출력합니다.

---

참고 문서:
- [Protocol Buffers 소개](https://developers.google.com/protocol-buffers/docs/proto)
- [gRPC 공식 사이트](https://grpc.io/)