---
layout: post
title: "[java] 자바 통신 라이브러리(Netty, Apache HttpClient 등) 사용하기"
description: " "
date: 2023-12-08
tags: [java]
comments: true
share: true
---

자바 애플리케이션에서 외부와의 통신은 매우 중요합니다. 이를 위해서는 다양한 라이브러리들을 사용하여 네트워크 통신을 구현할 수 있습니다. 이번 게시물에서는 Netty와 Apache HttpClient를 사용하여 각각의 라이브러리가 제공하는 기능을 살펴보고, 간단한 예제를 통해 사용 방법을 안내하겠습니다.

## 목차

- [Netty 소개](#netty-소개)
- [Netty 예제](#netty-예제)
- [Apache HttpClient 소개](#apache-httpclient-소개)
- [Apache HttpClient 예제](#apache-httpclient-예제)

## Netty 소개

[Netty](https://netty.io/)는 비동기 이벤트 기반의 네트워크 응용 프로그램을 빠르고 쉽게 개발할 수 있도록 고안된 오픈소스 프레임워크입니다. TCP, UDP, HTTP 및 다양한 다른 네트워크 프로토콜을 지원하며, 다양한 이벤트 핸들링과 높은 성능을 제공합니다.

## Netty 예제

다음은 Netty를 사용하여 서버와 클라이언트 간의 간단한 통신을 구현하는 예제 코드입니다.

```java
import io.netty.bootstrap.Bootstrap;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelOption;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.handler.codec.string.StringDecoder;
import io.netty.handler.codec.string.StringEncoder;

public class NettyClient {
    public static void main(String[] args) {
        EventLoopGroup group = new NioEventLoopGroup();
        try {
            Bootstrap b = new Bootstrap();
            b.group(group)
             .channel(NioSocketChannel.class)
             .handler(new ChannelInitializer<SocketChannel>() {
                 @Override
                 protected void initChannel(SocketChannel ch) {
                    ch.pipeline().addLast(new StringDecoder(), new StringEncoder(), new ClientHandler());
                 }
             })
             .option(ChannelOption.SO_KEEPALIVE, true);
            
            b.connect("localhost", 8080).sync().channel().closeFuture().sync();
        } finally {
            group.shutdownGracefully();
        }
    }
}

class ClientHandler extends ChannelInboundHandlerAdapter {
    @Override
    public void channelActive(ChannelHandlerContext ctx) {
        System.out.println("Connected to server!");
    }

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) {
        System.out.println("Received message from server: " + msg);
    }
}
```

## Apache HttpClient 소개

[Apache HttpClient](https://hc.apache.org/httpcomponents-client-4.5.x/index.html)는 Apache HttpClient Project에서 제공하는 강력하고 유연한 HTTP 클라이언트 라이브러리입니다. HTTP 프로토콜을 통해 통신하는 다양한 기능을 제공하며, 편리한 API를 통해 HTTP 요청 및 응답을 처리할 수 있습니다.

## Apache HttpClient 예제

다음은 Apache HttpClient를 사용하여 간단한 HTTP GET 요청을 보내고 응답을 받아오는 예제 코드입니다.

```java
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

public class ApacheHttpClientExample {
    public static void main(String[] args) throws IOException {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpGet httpGet = new HttpGet("https://api.example.com/data");
        
        HttpResponse response = httpClient.execute(httpGet);
        String responseBody = EntityUtils.toString(response.getEntity());
        
        System.out.println("Response from server: " + responseBody);
        
        httpClient.close();
    }
}
```

이와 같이 Netty와 Apache HttpClient를 사용하여 각각 네트워크 통신 및 HTTP 통신을 구현할 수 있습니다. 선택한 라이브러리에 따라 프로젝트의 요구사항과 성능을 고려하여 적절한 라이브러리를 선택하는 것이 중요합니다.

위의 예제 코드를 참고하여 각 라이브러리의 공식 문서나 추가 자료를 통해 보다 자세한 사용법을 학습하시기를 권장합니다.

## 참고 자료
- [Netty 공식 홈페이지](https://netty.io/)
- [Apache HttpClient 공식 홈페이지](https://hc.apache.org/httpcomponents-client-4.5.x/index.html)