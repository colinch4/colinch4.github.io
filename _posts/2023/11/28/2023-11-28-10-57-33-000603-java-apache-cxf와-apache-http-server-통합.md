---
layout: post
title: "[java] Java Apache CXF와 Apache HTTP Server 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Apache CXF는 Java 기반의 웹 서비스 프레임워크이고, Apache HTTP Server는 널리 사용되는 웹 서버입니다. 이 두 가지를 통합하여 CXF 웹 서비스를 Apache HTTP Server로 배포하고 실행할 수 있습니다.

## Apache CXF와 Apache HTTP Server

Apache CXF는 Java 언어로 작성된 웹 서비스 개발 프레임워크입니다. CXF는 다양한 웹 서비스 스택을 지원하며, SOAP 및 RESTful 웹 서비스를 구축하기 위한 다양한 기능을 제공합니다. CXF는 널리 사용되는 Apache Software Foundation의 오픈 소스 프로젝트입니다.

Apache HTTP Server는 가장 인기있는 웹 서버 중 하나로, 대부분의 웹 애플리케이션과 웹 사이트를 호스팅하는 데 사용됩니다. Apache HTTP Server는 안정성, 확장성 및 보안 기능을 제공하여 널리 사용되고 믿을 수 있는 웹 서버입니다.

## Apache CXF와 Apache HTTP Server 통합 방법

Apache HTTP Server를 사용하여 CXF 웹 서비스를 실행하려면 다음 단계를 따르면 됩니다.

1. **Apache CXF 웹 서비스 개발**: CXF를 사용하여 웹 서비스를 개발하고 구축합니다. 필요한 기능 및 서비스를 정의하고, 웹 서비스 인터페이스를 정의하고 구현합니다.

2. **Maven 빌드 구성**: Maven을 사용하여 CXF 웹 서비스를 빌드하고 패키징합니다. Maven은 종속성 관리 및 빌드 자동화를 지원하는 강력한 도구입니다.

3. **Apache HTTP Server 설정**: Apache HTTP Server에 mod_proxy 및 mod_proxy_http 모듈을 활성화하여 웹 서비스 요청을 CXF로 전달합니다. 이를 통해 Apache HTTP Server는 외부로부터 들어오는 요청을 CXF로 프록시할 수 있습니다.

4. **웹 서비스 배포**: CXF 웹 서비스를 Apache HTTP Server에 배포하고 실행합니다. 이를 위해 CXF JAX-WS 애플리케이션을 WAR 파일로 패키징하고, Apache HTTP Server의 웹 애플리케이션 디렉토리에 배치합니다.

5. **Apache HTTP Server 재시작**: Apache HTTP Server를 재시작하여 변경 사항을 적용합니다. 이제 CXF 웹 서비스는 Apache HTTP Server를 통해 외부로부터 요청을 받을 수 있습니다.

## 예시 코드

다음은 Apache CXF를 사용하여 Hello World 웹 서비스를 개발하고 Apache HTTP Server와 통합하는 예시 코드입니다.

```java
package com.example;

import javax.jws.WebService;

@WebService
public class HelloWorld {

    public String sayHello(String name) {
        return "Hello, " + name + "!";
    }
}
```

위의 코드는 CXF를 사용하여 간단한 Hello World 웹 서비스를 정의합니다. 이 코드는 마치 일반적인 자바 클래스와 같이 보입니다.

## 참고 자료

- [Apache CXF 공식 사이트](http://cxf.apache.org/)
- [Apache HTTP Server 공식 사이트](https://httpd.apache.org/)