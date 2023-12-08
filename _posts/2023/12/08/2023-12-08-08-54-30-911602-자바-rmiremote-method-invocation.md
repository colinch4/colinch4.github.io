---
layout: post
title: "[java] 자바 RMI(Remote Method Invocation)"
description: " "
date: 2023-12-08
tags: [java]
comments: true
share: true
---

자바 RMI는 Remote Method Invocation의 약자로, 자바 애플리케이션 간에 원격으로 메소드 호출을 가능케 하는 기술입니다. RMI는 분산 시스템을 위한 자바 플랫폼의 핵심 기술 중 하나이며, 객체 지향적인 접근 방식을 통해 분산 객체를 쉽게 사용할 수 있도록 합니다.

RMI는 서버와 클라이언트 간의 통신을 위한 프로토콜을 제공하며, 실제로 원격 서버에 있는 객체의 메소드를 호출하는 것처럼 사용할 수 있습니다. RMI를 통해 애플리케이션은 로컬 객체를 사용하는 것과 동일한 방식으로 원격 객체를 사용할 수 있습니다.

## RMI의 주요 구성 요소

RMI는 네 가지 주요 구성 요소로 구성되어 있습니다.

1. **원격 인터페이스(Remote Interface)**: 원격 객체의 메소드와 연산을 정의하는 인터페이스입니다. 이는 클라이언트가 원격 객체를 호출할 수 있도록 합니다.

2. **원격 객체(Remote Object)**: 클라이언트가 원격으로 호출할 수 있는 메소드를 구현한 객체입니다. 이 객체는 서버에서 실행되고, 클라이언트는 이를 원격으로 호출하여 사용할 수 있습니다.

3. **RMI 레지스트리(RMI Registry)**: RMI 객체를 등록하고 찾을 수 있는 RMI 서비스입니다. 클라이언트는 RMI 레지스트리를 통해 원격 객체를 검색하고 호출할 수 있습니다.

4. **스텁(Stub) 및 스켈레톤(Skeleton)**: 클라이언트와 서버 간의 통신을 지원하는 RMI 런타임 시스템의 일부 구성 요소입니다. 클라이언트는 스텁을 통해 원격 객체의 메소드를 호출하고, 서버는 스켈레톤을 통해 해당 메소드를 수행합니다.

## RMI 예시

다음은 간단한 예시 코드로, RMI를 사용하여 클라이언트에서 서버에 있는 원격 객체의 메소드를 호출하는 방법을 보여줍니다.

```java
// Remote Interface
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Hello extends Remote {
    String sayHello() throws RemoteException;
}

// Remote Object
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class HelloImpl extends UnicastRemoteObject implements Hello {
    public HelloImpl() throws RemoteException {
        super();
    }

    public String sayHello() {
        return "Hello, world!";
}

// RMI Server
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Server {
    public static void main(String[] args) throws Exception {
        Registry registry = LocateRegistry.createRegistry(1099);
        HelloImpl obj = new HelloImpl();
        registry.bind("Hello", obj);
    }
}

// RMI Client
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
    public static void main(String[] args) throws Exception {
        Registry registry = LocateRegistry.getRegistry("serverHostname");
        Hello stub = (Hello) registry.lookup("Hello");
        String response = stub.sayHello();
        System.out.println("Response: " + response);
    }
}
```

위의 예시 코드에서는 `Hello`라는 원격 인터페이스와 `HelloImpl`이라는 원격 객체를 정의하고, 서버와 클라이언트의 코드를 작성하여 RMI를 사용하는 방법을 보여줍니다.

RMI는 분산 시스템에서 효율적인 통신을 위한 강력한 도구로서, 자바 애플리케이션의 분산 아키텍처를 구축하는 데 중요한 역할을 합니다.

## 참고 자료
- [The Java Tutorials - RMI](https://docs.oracle.com/javase/tutorial/rmi/index.html)
- [Remote Method Invocation (RMI) - GeeksforGeeks](https://www.geeksforgeeks.org/remote-method-invocation-rmi-in-java/)