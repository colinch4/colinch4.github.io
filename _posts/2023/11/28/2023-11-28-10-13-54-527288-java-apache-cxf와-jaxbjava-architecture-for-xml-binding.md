---
layout: post
title: "[java] Java Apache CXF와 JAXB(Java Architecture for XML Binding)"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Apache CXF는 웹 서비스 개발을 위한 자바 기반의 프레임워크로서, 클라이언트와 서버 사이에 XML 기반의 데이터를 주고받을 수 있도록 도와줍니다. 이를 통해 웹 서비스와의 통신을 쉽게 구현할 수 있습니다.

JAXB (Java Architecture for XML Binding)는 자바 객체와 XML 문서 간의 변환을 처리하기 위한 기술입니다. JAXB는 자바 클래스를 XML 스키마로 바인딩하고, XML 문서를 자바 객체로 언마샬링하거나 자바 객체를 XML 문서로 마샬링하는 기능을 제공합니다.

Apache CXF와 JAXB를 함께 사용하면 웹 서비스에 대한 클라이언트와 서버 코드에서 XML 데이터의 처리를 간편하게 할 수 있습니다.

## Apache CXF와 JAXB를 사용한 웹 서비스 클라이언트 개발

1. 먼저 Apache CXF와 JAXB를 의존성으로 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음과 같은 의존성을 추가합니다:

```xml
<dependencies>
   <dependency>
       <groupId>org.apache.cxf</groupId>
       <artifactId>cxf-rt-frontend-jaxws</artifactId>
       <version>3.4.1</version>
   </dependency>
   <dependency>
       <groupId>org.apache.cxf</groupId>
       <artifactId>cxf-rt-transports-http</artifactId>
       <version>3.4.1</version>
   </dependency>
   <dependency>
       <groupId>javax.xml.bind</groupId>
       <artifactId>jaxb-api</artifactId>
       <version>2.3.1</version>
   </dependency>
   <dependency>
       <groupId>org.glassfish.jaxb</groupId>
       <artifactId>jaxb-runtime</artifactId>
       <version>2.3.1</version>
   </dependency>
</dependencies>
```

2. 웹 서비스의 WSDL 파일을 기반으로 Java 클래스를 생성합니다. `wsimport` 명령어를 사용하면 간단하게 Java 클래스를 생성할 수 있습니다. 명령 프롬프트 또는 터미널에서 다음과 같이 실행합니다:

```bash
$ wsimport -d [output_directory] [wsdl_url]
```

여기서 `[output_directory]`는 생성된 Java 클래스의 출력 디렉토리를 지정하고, `[wsdl_url]`은 WSDL 파일의 URL을 입력합니다.

3. 클라이언트 코드에서 생성된 Java 클래스를 사용하여 웹 서비스에 요청을 보냅니다. 예를 들어, 다음과 같이 클라이언트 코드를 작성할 수 있습니다:

```java
import com.example.WebServicePort;
import com.example.WebServicePortService;
import com.example.Request;
import com.example.Response;

public class WebServiceClient {
   public static void main(String[] args) {
       // 웹 서비스에 연결하는 포트 생성
       WebServicePortService service = new WebServicePortService();
       WebServicePort port = service.getWebServicePort();
       
       // 요청 객체 생성
       Request request = new Request();
       request.setParameter("Hello");
       
       // 웹 서비스 호출 및 응답 받기
       Response response = port.callWebService(request);
       
       // 응답 처리
       System.out.println("Response: " + response.getResult());
   }
}
```

위 코드에서 `com.example` 패키지는 wsimport를 사용하여 생성된 Java 클래스의 패키지를 나타냅니다.

## 참고 자료

- [Apache CXF Documentation](https://cxf.apache.org/docs/)
- [JAXB Documentation](https://javaee.github.io/jaxb-v2/)