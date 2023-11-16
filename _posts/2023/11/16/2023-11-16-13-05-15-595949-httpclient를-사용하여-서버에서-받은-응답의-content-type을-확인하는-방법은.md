---
layout: post
title: "[java] HttpClient를 사용하여 서버에서 받은 응답의 Content-Type을 확인하는 방법은?"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

```java
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.HttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;

public class HttpClientExample {
    public static void main(String[] args) {
        HttpClient httpClient = HttpClientBuilder.create().build();
        HttpGet httpGet = new HttpGet("http://example.com");

        try {
            HttpResponse response = httpClient.execute(httpGet);
            HttpEntity entity = response.getEntity();
            String contentType = entity.getContentType().getValue();
            System.out.println("Content-Type: " + contentType);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위의 예제 코드는 HttpClient를 사용하여 GET 요청을 보내고, 서버에서 받은 응답의 Content-Type을 확인하는 방법을 보여줍니다.

`entity.getContentType().getValue()`를 사용하면 응답의 Content-Type을 문자열로 가져올 수 있습니다.

이를 통해 받은 응답의 Content-Type을 확인하고 필요한 처리를 할 수 있습니다.

더 자세한 내용은 [Apache HttpClient documentation](https://hc.apache.org/httpcomponents-client-ga/tutorial/html/fundamentals.html)을 참고하시기 바랍니다.