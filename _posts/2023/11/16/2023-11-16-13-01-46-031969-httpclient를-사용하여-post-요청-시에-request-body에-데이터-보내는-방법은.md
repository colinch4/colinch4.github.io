---
layout: post
title: "[java] HttpClient를 사용하여 POST 요청 시에 Request Body에 데이터 보내는 방법은?"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

```java
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClientBuilder;

public class HttpPostExample {
    public static void main(String[] args) throws Exception {
        // HttpClient 인스턴스 생성
        HttpClient httpClient = HttpClientBuilder.create().build();
        
        // POST 요청을 보낼 URL 설정
        String url = "http://example.com/api/endpoint";
        
        // HttpPost 객체 생성 및 URL 설정
        HttpPost httpPost = new HttpPost(url);
        
        // Request Body에 보낼 데이터 설정
        String requestBody = "{\"name\": \"John\", \"age\": 30}";
        StringEntity entity = new StringEntity(requestBody);
        httpPost.setEntity(entity);
        
        // Request Header 설정 (옵션)
        httpPost.setHeader("Content-type", "application/json");
        
        // POST 요청 실행
        httpClient.execute(httpPost);
        
        // 응답 처리 등 추가 작업 수행
    }
}
```

위 코드에서는 HttpClient 및 관련 클래스를 사용하여 POST 요청을 보내는 방법을 보여줍니다. `HttpPost` 클래스를 사용하여 HTTP POST 요청을 설정하고, `StringEntity` 클래스를 사용하여 Request Body에 데이터를 설정합니다. 이후, `setEntity` 메서드를 사용하여 HttpPost 객체에 Request Body를 설정하고, 필요한 경우 `setHeader` 메서드를 사용하여 Request Header를 설정할 수 있습니다.

참고 문서:
- [HttpClient API 문서](https://hc.apache.org/httpcomponents-client-ga/tutorial/html/advanced.html)
- [Maven Repository: Apache HttpClient](https://mvnrepository.com/artifact/org.apache.httpcomponents/httpclient)