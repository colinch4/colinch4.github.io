---
layout: post
title: "[java] HttpClient의 Request Interceptor 기능은 무엇인가요?"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

HttpClient는 웹 서버와 통신하기 위한 Java의 라이브러리입니다. HttpClient의 Request Interceptor는 클라이언트가 웹 서버로 요청을 보내기 전에 요청 객체를 수정하거나 필터링하는 기능을 제공합니다.

Request Interceptor는 HttpClient의 HttpRequestInterceptor 인터페이스를 구현하여 만들 수 있습니다. 이 인터페이스에는 process 메서드가 정의되어 있으며, 이 메서드를 오버라이딩하여 요청 객체를 수정할 수 있습니다.

예를 들어, Request Interceptor를 사용하여 요청 객체에 헤더를 추가하거나, 파라미터를 변경하거나, 인증 토큰을 설정할 수 있습니다. 이를 통해 클라이언트에서 간단한 요청 수정이 필요한 경우에 유용하게 사용할 수 있습니다.

아래는 HttpClient의 Request Interceptor를 사용하는 예제 코드입니다.

```java
import org.apache.http.HttpRequest;
import org.apache.http.HttpRequestInterceptor;
import org.apache.http.protocol.HttpContext;

public class CustomRequestInterceptor implements HttpRequestInterceptor {
    @Override
    public void process(HttpRequest request, HttpContext context) {
        // 요청 객체를 수정하는 로직을 작성합니다.
        // 예를 들어, 헤더 추가
        request.addHeader("Authorization", "Bearer <access_token>");
    }
}

public class HttpClientExample {
    public static void main(String[] args) {
        // HttpClient 인스턴스 생성
        CloseableHttpClient httpClient = HttpClients.custom()
                .addInterceptorFirst(new CustomRequestInterceptor())
                .build();

        try {
            // 요청 객체 생성
            HttpGet httpGet = new HttpGet("http://example.com/api/users");

            // 요청 실행
            CloseableHttpResponse response = httpClient.execute(httpGet);

            // 응답 처리 로직 작성

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            // HttpClient 종료
            try {
                httpClient.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
```

위의 예제에서는 CustomRequestInterceptor 클래스가 HttpRequestInterceptor를 구현하고 있습니다. process 메서드에서는 요청 객체에 "Authorization" 헤더를 추가하고 있습니다. 이렇게 하면 요청이 전송될 때마다 해당 헤더를 자동으로 추가할 수 있습니다.

결론적으로, HttpClient의 Request Interceptor 기능을 사용하면 클라이언트의 요청 객체를 프로그래밍 방식으로 수정할 수 있습니다. 이를 통해 요청에 필요한 자세한 설정을 추가하거나 요청을 필터링하는 등의 작업을 수행할 수 있습니다.

[참고 자료]
- HttpClient 문서: https://hc.apache.org/httpcomponents-client-ga/
- HttpRequestInterceptor 문서: https://hc.apache.org/httpcomponents-core-ga/httpcore/apidocs/org/apache/http/HttpRequestInterceptor.html