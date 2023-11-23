---
layout: post
title: "[java] Java Jolokia를 사용하여 JVM(Machine) 정보 확인하기"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Jolokia는 Java 애플리케이션의 관리 및 모니터링을 위한 에이전트입니다. 이제 Jolokia를 사용하여 JVM(Java Virtual Machine)의 정보를 쉽게 확인하는 방법에 대해 알아보겠습니다.

## 1. Jolokia 설치하기

Jolokia는 Maven 저장소에서 다운로드하여 프로젝트에 추가할 수 있습니다. 아래의 의존성을 프로젝트의 `pom.xml` 파일에 추가해주세요.

```xml
<dependency>
    <groupId>org.jolokia</groupId>
    <artifactId>jolokia-core</artifactId>
    <version>1.7.0</version>
</dependency>
```

## 2. Jolokia 로컬 서버 시작하기

Jolokia는 원격으로 JVM에 접근하여 정보를 가져오기 위해 로컬 서버를 시작해야 합니다. 다음은 Jolokia 로컬 서버를 시작하는 간단한 예제입니다.

```java
import org.jolokia.http.AgentServlet;
import org.jolokia.http.AgentServletConfig;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class JolokiaLocalServerExample extends HttpServlet {

    private AgentServlet agentServlet;

    @Override
    public void init() {
        final AgentServletConfig config = new AgentServletConfig();
        agentServlet = new AgentServlet();
        try {
            agentServlet.init(config);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) {
        try {
            agentServlet.service(request, response);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public void destroy() {
        if (agentServlet != null) {
            agentServlet.destroy();
        }
    }

}
```

위의 예제는 `javax.servlet`를 사용하여 간단한 로컬 서블릿을 만들고, 이를 `AgentServlet`으로 초기화하여 Jolokia 로컬 서버를 시작합니다. 

## 3. JVM 정보 가져오기

Jolokia로 로컬 서버를 시작한 후에는 코드에서 Jolokia를 사용하여 JVM 정보를 가져올 수 있습니다. 다음은 JVM 메모리 사용량을 가져오는 예제입니다.

```java
import org.jolokia.client.J4pClient;
import org.jolokia.client.exception.J4pException;
import org.jolokia.client.request.J4pReadRequest;
import org.jolokia.client.request.J4pReadResponse;
import org.jolokia.client.request.J4pResponse;

public class JvmInfoExample {

    public static void main(String[] args) {
        J4pClient j4pClient = new J4pClient("http://localhost:8080/jolokia");
        
        try {
            J4pReadRequest readRequest = new J4pReadRequest("java.lang:type=Memory", "HeapMemoryUsage");
            J4pReadResponse readResponse = j4pClient.execute(readRequest);
            
            if (readResponse.hasError()) {
                System.out.println("Error: " + readResponse.getError());
            } else {
                System.out.println("Heap Memory Usage: " + readResponse.getValue());
            }
        } catch (J4pException e) {
            e.printStackTrace();
        }
    }

}
```

위의 예제는 Jolokia 클라이언트를 사용하여 JVM의 Heap 메모리 사용량을 가져오는 코드입니다. `http://localhost:8080/jolokia`는 Jolokia 로컬 서버의 URL입니다. 가져온 결과를 출력하여 Heap 메모리 사용량을 확인할 수 있습니다.

## 결론

Java Jolokia는 JVM 정보 확인을 더욱 쉽게 만들어주는 도구입니다. Jolokia를 사용하여 JVM의 다양한 정보를 간단하게 확인하고 모니터링할 수 있습니다. 위의 예제를 참고하여 Jolokia를 사용해보세요!

---

### 참고 자료

- [Jolokia 공식 웹 사이트](https://jolokia.org/)
- [Jolokia GitHub 저장소](https://github.com/rhuss/jolokia)