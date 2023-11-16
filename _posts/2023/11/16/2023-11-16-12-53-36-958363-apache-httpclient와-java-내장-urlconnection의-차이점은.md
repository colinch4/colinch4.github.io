---
layout: post
title: "[java] Apache HttpClient와 Java 내장 URLConnection의 차이점은?"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java에서 HTTP 요청을 보낼 때, Apache HttpClient과 Java 내장 URLConnection을 모두 사용할 수 있습니다. 둘 다 HTTP 요청을 처리하고 응답을 받는데 사용되지만, 각각에는 몇 가지 중요한 차이점이 있습니다.

## Apache HttpClient

Apache HttpClient는 Apache Software Foundation에서 개발한 오픈 소스 라이브러리입니다. 이 라이브러리는 Java SE 1.5 이상에서 사용할 수 있으며, 다양한 기능과 설정 옵션을 제공합니다.

Apache HttpClient의 장점은 다음과 같습니다:

- 세부적인 커스터마이징이 가능합니다. 연결 설정, 타임아웃, 인증 등 다양한 설정을 자유롭게 변경할 수 있습니다.
- Connection Pooling 기능을 제공하여 동시에 여러 개의 HTTP 요청을 처리할 때 성능을 향상시킬 수 있습니다.
- 더 많은 기능과 유연성을 제공합니다. HTTP/2, SSL/TLS, 프락시, 리다이렉션, 캐싱 등과 같은 다양한 기능을 지원합니다.

아래는 Apache HttpClient를 사용하여 HTTP GET 요청을 보내는 예제 코드입니다:

```java
CloseableHttpClient httpClient = HttpClients.createDefault();
HttpGet request = new HttpGet("https://example.com");
CloseableHttpResponse response = httpClient.execute(request);
try {
    // 응답 처리 로직
    // ...
} finally {
    response.close();
    httpClient.close();
}
```

## Java 내장 URLConnection

Java 내장 URLConnection은 Java SE에서 기본으로 제공하는 HTTP 통신 기능입니다. URLConnection 클래스를 사용하여 HTTP 요청을 전송하고 응답을 받을 수 있습니다.

Java 내장 URLConnection의 특징은 다음과 같습니다:

- 자바의 표준 라이브러리로 제공되기 때문에 별도의 라이브러리를 추가로 설치할 필요가 없습니다.
- 간단하고 사용하기 쉽습니다. 기본적인 HTTP 기능을 제공하며 설정이 필요 없는 경우에 적합합니다.

아래는 Java 내장 URLConnection을 사용하여 HTTP GET 요청을 보내는 예제 코드입니다:

```java
URL url = new URL("https://example.com");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setRequestMethod("GET");
int responseCode = conn.getResponseCode();

BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
String line;
StringBuilder response = new StringBuilder();
while ((line = reader.readLine()) != null) {
    response.append(line);
}
reader.close();
conn.disconnect();

// 응답 처리 로직
// ...
```

## 결론

Apache HttpClient와 Java 내장 URLConnection은 모두 HTTP 요청을 처리하는 도구로 사용될 수 있으며, 각각 강점을 가지고 있습니다. 만약 HTTP 요청에 대해 자세하게 제어하고 세부적인 설정을 할 필요가 있다면 Apache HttpClient를 사용하는 것이 좋습니다. 반면에 간단한 HTTP 요청을 처리하고자 할 때는 Java 내장 URLConnection을 통해 제공되는 기본 기능을 사용하는 것이 편리합니다.

더 자세한 내용은 아래의 참고 자료를 참고하시기 바랍니다:

- Apache HttpClient 공식 문서: [https://hc.apache.org/httpcomponents-client-ga/](https://hc.apache.org/httpcomponents-client-ga/)
- Java URLConnection 공식 문서: [https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/URLConnection.html](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/net/URLConnection.html)