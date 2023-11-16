---
layout: post
title: "[java] HttpClient의 Connection Pooling 기능은 무엇인가요?"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

HttpClient는 Apache HttpComponents 라이브러리에서 제공하는 Java 기반의 HTTP 클라이언트 라이브러리입니다. HttpClient를 사용하여 HTTP 요청을 보내고 응답을 받을 수 있습니다. Connection Pooling은 HttpClient에서 제공하는 중요한 기능 중 하나입니다.

Connection Pooling은 HTTP 연결을 관리하는 기능으로, 미리 생성된 연결을 재사용하여 사용자 요청에 대한 응답을 더 빠르게 받을 수 있게 도와줍니다. 일반적으로 HTTP 연결을 맺는 과정은 시간이 많이 소요되는 작업이므로, 매번 새로운 연결을 맺는 대신 미리 생성된 연결을 사용하면 시간을 절약할 수 있습니다.

HttpClient의 Connection Pooling 기능을 사용하려면, ConnectionManager 클래스와 ConnectionReuseStrategy 인터페이스를 사용해야 합니다. ConnectionManager는 연결 풀을 관리하고, ConnectionReuseStrategy는 어떤 연결을 재사용할지 결정하는 역할을 합니다.

아래는 HttpClient를 사용하여 Connection Pooling을 설정하는 예제 코드입니다.

```java
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.impl.conn.PoolingHttpClientConnectionManager;

public class HttpClientExample {
    public static void main(String[] args) throws Exception {
        PoolingHttpClientConnectionManager connectionManager = new PoolingHttpClientConnectionManager();
        connectionManager.setMaxTotal(100); // 최대 연결 수 설정
        connectionManager.setDefaultMaxPerRoute(10); // 최대 라우트당 연결 수 설정

        HttpClient httpClient = HttpClientBuilder.create()
                .setConnectionManager(connectionManager)
                .build();

        HttpGet request = new HttpGet("https://www.example.com");
        HttpResponse response = httpClient.execute(request);

        // 응답 처리 로직...
    }
}
```

위의 예제 코드에서는 PoolingHttpClientConnectionManager를 생성하고 최대 연결 수와 최대 라우트당 연결 수를 설정한 후, HttpClient의 connectionManager 속성으로 연결 관리자를 설정합니다. 이렇게 하면 HttpClient가 Connection Pooling을 사용하여 미리 생성된 연결을 재사용할 수 있습니다.

Connection Pooling은 여러 클라이언트가 동시에 다수의 웹 서버로 요청을 보내는 상황에서 특히 유용합니다. 올바로 구성된 Connection Pooling은 네트워크 연결 지연 시간을 최소화하고, 리소스를 효율적으로 사용하여 성능을 향상시킵니다.

참고 자료:
- HttpClient 공식 문서: https://hc.apache.org/httpcomponents-client-ga/tutorial/html/connmgmt.html

[출처: https://wiki.apache.org/HttpComponents/PoolingHttpClientConnectionManager]