---
layout: post
title: "[java] Java Apache CXF와 WSDL(Web Services Description Language)"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

웹 서비스는 다양한 기술과 프로토콜을 사용하여 구현할 수 있습니다. 그 중 하나는 Apache CXF와 WSDL(Web Services Description Language)입니다. 이 기술들은 Java를 기반으로한 웹 서비스 개발에 매우 유용합니다. 이번 글에서는 Java Apache CXF와 WSDL에 대해 알아보겠습니다.

## 1. Apache CXF란?

Apache CXF는 Java 언어로 구현된 오픈 소스 웹 서비스 프레임워크입니다. CXF는 간단한 HTTP 서비스부터 복잡한 SOAP 기반의 서비스까지 다양한 유형의 웹 서비스를 구현할 수 있도록 지원합니다. CXF는 다른 웹 서비스 프레임워크와의 연동이 쉽고, 고성능이며, 확장성이 뛰어나기 때문에 많은 개발자들에게 선호되고 있습니다.

## 2. WSDL(Web Services Description Language)이란?

WSDL은 웹 서비스의 인터페이스를 기술하는 XML 형식의 언어입니다. WSDL은 웹 서비스의 기능, 메소드, 매개변수, 반환 값 등을 정의하는데 사용됩니다. WSDL은 웹 서비스를 개발하는데 필요한 정보를 제공하여 클라이언트가 웹 서비스를 호출할 때 필요한 모든 정보를 제공합니다. 클라이언트는 WSDL 파일을 사용하여 웹 서비스에 연결하고, 웹 서비스에서 제공하는 메소드를 호출할 수 있습니다.

## 3. Apache CXF와 WSDL 사용하기

Apache CXF를 사용하여 웹 서비스를 개발하고자 한다면 먼저 WSDL 파일을 생성해야 합니다. WSDL 파일은 웹 서비스의 인터페이스를 정의하는데 사용됩니다. WSDL 파일은 SOAP 기반 웹 서비스의 경우 WSDL2Java 도구를 사용하여 Java 클래스로 변환할 수 있습니다.

```
$ wsdl2java -d [output_directory] [wsdl_file]
```

이제 생성된 Java 클래스를 사용하여 Apache CXF를 통해 웹 서비스를 구현할 수 있습니다. Apache CXF는 Java 클래스를 이용하여 클라이언트나 서버를 개발할 수 있는 다양한 기능을 제공합니다.

```java
import org.apache.cxf.frontend.ClientProxy;
import org.apache.cxf.jaxws.JaxWsProxyFactoryBean;

public class WebClient {
    public static void main(String[] args) {
        JaxWsProxyFactoryBean factory = new JaxWsProxyFactoryBean();
        factory.setServiceClass(HelloWorld.class);
        factory.setAddress("http://localhost:8080/HelloWorldService");
        HelloWorld client = (HelloWorld) factory.create();
        
        String result = client.sayHello("World");
        System.out.println(result);
    }
}
```

위의 예제에서는 Apache CXF의 JaxWsProxyFactoryBean을 사용하여 클라이언트를 생성하고, 웹 서비스를 호출합니다.

## 4. 정리

이번 포스트에서는 Java Apache CXF와 WSDL에 대해 알아보았습니다. Apache CXF는 Java 기반 웹 서비스 개발을 위한 강력한 프레임워크로, 다양한 기능과 유연한 성능을 제공합니다. WSDL은 웹 서비스의 인터페이스를 정의하는데 사용되며, 클라이언트가 웹 서비스와 통신할 때 필요한 정보를 전달합니다. Apache CXF와 WSDL을 사용하면 좀 더 효과적이고 편리한 웹 서비스 개발을 할 수 있습니다.