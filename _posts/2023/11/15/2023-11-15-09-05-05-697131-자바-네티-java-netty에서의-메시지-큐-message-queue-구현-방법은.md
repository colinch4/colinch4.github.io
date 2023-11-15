---
layout: post
title: "[java] 자바 네티 (Java Netty)에서의 메시지 큐 (Message Queue) 구현 방법은?"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

메시지 큐(Message Queue)는 비동기 메시지 전달 시스템으로, 메시지를 송신자(Sender)와 수신자(Receiver) 간에 안전하고 신뢰성 있게 전달하는 역할을 합니다. 자바에서는 Netty 프레임워크를 사용하여 메시지 큐를 구현할 수 있습니다.

## 1. Netty의 Channel, EventLoopGroup 초기화

Netty를 사용하기 위해 먼저 필요한 것은 Channel과 EventLoopGroup입니다. Channel은 네트워크 연결을 나타내고, EventLoopGroup은 쓰레드 풀을 제공합니다. 아래 예제 코드에서는 NioEventLoopGroup을 사용하도록 합니다.

```java
EventLoopGroup eventLoopGroup = new NioEventLoopGroup();
Channel channel = null;
try {
    Bootstrap bootstrap = new Bootstrap();
    bootstrap.group(eventLoopGroup)
        .channel(NioSocketChannel.class)
        .handler(new ChannelInitializer<SocketChannel>() {
            @Override
            protected void initChannel(SocketChannel socketChannel) {
                // 메시지 처리 핸들러 등록
                socketChannel.pipeline().addLast(new MessageHandler());
            }
        });
    channel = bootstrap.connect("localhost", 8080).sync().channel();
} catch (Exception e) {
    // 예외 처리
} finally {
    eventLoopGroup.shutdownGracefully();
}
```

## 2. 메시지 처리 핸들러 구현

ChannelInitializer에서 등록한 MessageHandler 클래스는 실제 메시지를 처리하는 역할을 합니다. 예제 코드에서는 다음과 같이 MessageHandler를 구현합니다.

```java
public class MessageHandler extends ChannelInboundHandlerAdapter {
    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) {
        // 수신한 메시지 처리 로직 구현
        ByteBuf buf = (ByteBuf) msg;
        // 메시지 큐에 메시지 추가
        processMessage(buf.toString(CharsetUtil.UTF_8));
    }
    
    private void processMessage(String message) {
        // 메시지 처리 로직 실행
        System.out.println("Received Message: " + message);
    }
}
```

위의 예제 코드에서는 채널로부터 수신된 메시지를 처리하기 위해 `channelRead` 메소드를 오버라이드하였습니다. 메시지 처리 로직은 `processMessage` 메소드에 구현되어 있습니다. 이 예제에서는 수신한 메시지를 간단히 화면에 출력하도록 하였습니다.

## 3. 메시지 송신

메시지 큐를 구현할 때에는 메시지를 송신하는 기능도 필요합니다. Netty에서는 Channel을 통해 메시지를 송신할 수 있습니다. 아래 예제 코드는 메시지를 전송하는 기능을 구현한 예입니다.

```java
public class MessageSender {
    private Channel channel;
    
    public MessageSender(Channel channel) {
        this.channel = channel;
    }
    
    public void send(String message) {
        // 메시지 전송
        ByteBuf buf = Unpooled.copiedBuffer(message, CharsetUtil.UTF_8);
        channel.writeAndFlush(buf);
    }
}
```

위의 예제 코드에서는 `MessageSender` 클래스를 생성하여 메시지를 전송할 수 있도록 구현하였습니다. `send` 메소드는 인자로 받은 메시지를 ByteBuf 형태로 변환하고, 해당 Channel을 통해 메시지를 송신합니다.

## 4. 사용 예시

아래는 앞서 구현한 메시지 큐를 사용하는 예시입니다.

```java
// 초기화
EventLoopGroup eventLoopGroup = new NioEventLoopGroup();
Channel channel = null;
try {
    Bootstrap bootstrap = new Bootstrap();
    bootstrap.group(eventLoopGroup)
        .channel(NioSocketChannel.class)
        .handler(new ChannelInitializer<SocketChannel>() {
            @Override
            protected void initChannel(SocketChannel socketChannel) {
                // 메시지 처리 핸들러 등록
                socketChannel.pipeline().addLast(new MessageHandler());
            }
        });
    channel = bootstrap.connect("localhost", 8080).sync().channel();

    // 메시지 송신
    MessageSender messageSender = new MessageSender(channel);
    messageSender.send("Hello, Netty!");

    // 송신 및 수신 대기
    channel.closeFuture().sync();
} catch (Exception e) {
    // 예외 처리
} finally {
    eventLoopGroup.shutdownGracefully();
}
```

위의 예시 코드에서는 초기화 단계에서 Netty Channel 및 EventLoopGroup을 초기화하고, 메시지를 송신하는 `MessageSender`를 생성하여 사용하였습니다. 송신 후에는 코드 흐름을 유지하기 위해 `channel.closeFuture().sync()`로 수신 대기 상태에 놓여집니다.

위의 예시 코드를 통해 자바 Netty를 사용하여 메시지 큐를 구현하는 방법을 살펴보았습니다. Netty는 많은 기능을 제공하기 때문에 자세한 정보는 [Netty 공식 문서](https://netty.io)를 참고하시길 바랍니다.