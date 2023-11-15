---
layout: post
title: "[java] 자바 네트워크 프로그래밍(Java network programming)"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

자바는 다양한 네트워크 애플리케이션을 구축하기 위한 강력한 프로그래밍 언어입니다. 네트워크 프로그래밍은 컴퓨터 간의 데이터 통신을 가능하게 하는 기술입니다. 이 기술은 인터넷을 통한 웹 애플리케이션, 클라이언트-서버 애플리케이션, 멀티플레이어 게임 등 여러분야에 활용됩니다.

## 자바 소켓 프로그래밍

자바에서 제공하는 Socket 클래스와 ServerSocket 클래스를 사용하여 소켓 프로그래밍을 할 수 있습니다. Socket 클래스는 클라이언트와 서버 간의 연결을 설정하고 데이터를 송수신하는데 사용됩니다. ServerSocket 클래스는 서버 측에서 클라이언트의 연결 요청을 수락하고 새로운 소켓을 생성하는데 사용됩니다.

다음은 간단한 소켓 통신 예제 코드입니다.

```java
import java.io.*;
import java.net.*;

public class SocketExample {
    public static void main(String[] args) {
        try {
            // 클라이언트 소켓 생성 및 서버에 연결
            Socket socket = new Socket("localhost", 5000);

            // 소켓의 입출력 스트림 생성
            OutputStream outputStream = socket.getOutputStream();
            PrintWriter out = new PrintWriter(outputStream, true);
            InputStream inputStream = socket.getInputStream();
            BufferedReader in = new BufferedReader(new InputStreamReader(inputStream));

            // 서버로 메시지 전송
            out.println("Hello, Server!");

            // 서버로부터 응답 받음
            String response = in.readLine();
            System.out.println("서버 응답: " + response);

            // 소켓 및 입출력 스트림 닫음
            out.close();
            in.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

위 코드에서는 클라이언트가 로컬호스트의 5000번 포트로 서버에 연결하고 "Hello, Server!" 메시지를 서버로 전송하며, 서버로부터 응답을 받아 출력합니다. 필요에 따라 클라이언트 및 서버 측의 소켓 통신 코드를 수정하여 다양한 네트워크 애플리케이션을 개발할 수 있습니다.

## 자바 네트워크 라이브러리

또한, 자바는 다양한 네트워크 라이브러리를 제공하여 네트워크 프로그래밍을 더욱 효율적으로 할 수 있습니다. 예를 들어, Apache HttpClient는 HTTP를 통한 웹 서비스에 접속하고 데이터를 주고받는 기능을 제공합니다. 그 외에도 Netty, OkHttp 등 다양한 라이브러리를 활용할 수 있습니다.

## 참고 자료

- Oracle 자바 네트워크 프로그래밍 가이드: [https://docs.oracle.com/javase/tutorial/networking/index.html](https://docs.oracle.com/javase/tutorial/networking/index.html)
- Apache HttpClient: [https://hc.apache.org/httpcomponents-client-ga/](https://hc.apache.org/httpcomponents-client-ga/)
- Netty: [https://netty.io/](https://netty.io/)
- OkHttp: [https://square.github.io/okhttp/](https://square.github.io/okhttp/)