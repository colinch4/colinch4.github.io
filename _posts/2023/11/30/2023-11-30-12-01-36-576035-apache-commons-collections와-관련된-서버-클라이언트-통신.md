---
layout: post
title: "[java] Apache Commons Collections와 관련된 서버 클라이언트 통신"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

이번 글에서는 Apache Commons Collections를 사용하여 서버와 클라이언트 간의 통신을 구현하는 방법에 대해 알아보겠습니다.

## Apache Commons Collections란?

Apache Commons Collections는 Apache Software Foundation에서 제공하는 Java 라이브러리입니다. 이 라이브러리는 다양한 컬렉션 유형과 유용한 데이터 구조, 알고리즘을 제공하여 개발자들이 빠르고 효율적인 코드를 작성할 수 있도록 도와줍니다.

## 서버 클라이언트 통신 구현

서버와 클라이언트 간의 통신은 네트워크를 통해 이루어집니다. 일반적으로 서버는 클라이언트의 요청을 받고, 해당 요청을 처리한 후 결과를 클라이언트로 보냅니다. Apache Commons Collections를 사용하여 이러한 통신을 구현하는 방법을 살펴보겠습니다.

### 단계 1: 서버 구현

서버 구현을 위해 `ServerSocket` 클래스를 사용하여 서버 소켓을 생성합니다. 소켓은 클라이언트와의 통신을 위한 입출력 스트림을 제공합니다. 예시 코드는 다음과 같습니다.

```java
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.collections4.PredicateUtils;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class Server {
    private static final int PORT = 9999;
    private static List<String> data = new ArrayList<>();

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        // 서버 소켓 생성
        ServerSocket serverSocket = new ServerSocket(PORT);

        // 클라이언트로부터의 연결 대기
        System.out.println("Server is running and waiting for client connection...");
        Socket clientSocket = serverSocket.accept();
        System.out.println("Client connected: " + clientSocket.getInetAddress());

        // 클라이언트로부터의 입력 스트림 생성
        ObjectInputStream inputStream = new ObjectInputStream(clientSocket.getInputStream());

        // 클라이언트로의 출력 스트림 생성
        ObjectOutputStream outputStream = new ObjectOutputStream(clientSocket.getOutputStream());

        // 클라이언트로부터 데이터 수신 및 처리
        data = (List<String>) inputStream.readObject();
        System.out.println("Received data from client: " + CollectionUtils.select(data, PredicateUtils.notNull()));

        // 클라이언트로 결과 전송
        outputStream.writeObject("Data received successfully");

        // 리소스 해제
        outputStream.close();
        inputStream.close();
        clientSocket.close();
        serverSocket.close();
    }
}
```

### 단계 2: 클라이언트 구현

클라이언트 구현을 위해서는 `Socket` 클래스를 사용하여 서버에 접속하고 통신을 수행해야 합니다. 예시 코드는 다음과 같습니다.

```java
import org.apache.commons.collections4.CollectionUtils;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class Client {
    private static final String SERVER_ADDRESS = "localhost";
    private static final int PORT = 9999;

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        // 서버에 연결
        Socket socket = new Socket(SERVER_ADDRESS, PORT);

        // 서버로의 출력 스트림 생성
        ObjectOutputStream outputStream = new ObjectOutputStream(socket.getOutputStream());

        // 서버로의 입력 스트림 생성
        ObjectInputStream inputStream = new ObjectInputStream(socket.getInputStream());

        // 데이터 생성 및 서버로 전송
        List<String> data = new ArrayList<>();
        data.add("Data 1");
        data.add("Data 2");
        outputStream.writeObject(data);

        // 서버로부터 결과 수신
        String response = (String) inputStream.readObject();
        System.out.println("Server response: " + response);

        // 리소스 해제
        outputStream.close();
        inputStream.close();
        socket.close();
    }
}
```

위의 코드는 간단한 예제로, 실제 프로덕션 환경에서는 오류 처리 및 보안 등 다른 추가 작업이 필요할 수 있습니다.

## 결론

Apache Commons Collections를 사용하여 서버와 클라이언트 간의 통신을 구현하는 방법에 대해 알아보았습니다. 이를 통해 개발자들은 효율적이고 안전한 네트워크 통신을 구현할 수 있습니다. 자세한 내용은 관련 문서를 참조해주세요.