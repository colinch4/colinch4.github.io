---
layout: post
title: "[java] TestNG와 Apache HttpClient를 활용한 API 테스트"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

이번 글에서는 TestNG와 Apache HttpClient를 사용하여 API 테스트를 수행하는 방법에 대해 알아보겠습니다. API 테스트는 소프트웨어 개발 과정에서 매우 중요한 부분이며, 실제로 서버와의 통신을 통해 API의 동작을 테스트하는 것은 필수적입니다. TestNG는 유연하고 강력한 테스트 프레임워크로 알려져 있으며, Apache HttpClient는 다양한 HTTP 기능을 제공하는 라이브러리입니다.

## 1. TestNG 설치 및 설정

먼저 TestNG를 설치하고 설정해야 합니다. TestNG는 Java 개발 환경에서 사용할 수 있는 테스트 프레임워크로, 다양한 기능을 제공합니다. Maven을 사용한다면 pom.xml에 다음과 같은 의존성을 추가하여 TestNG를 설치할 수 있습니다.

```xml
<dependency>
    <groupId>org.testng</groupId>
    <artifactId>testng</artifactId>
    <version>7.4.0</version>
    <scope>test</scope>
</dependency>
```

TestNG를 설치한 후, 테스트를 작성하기 위해 TestNG 어노테이션을 사용합니다. 예를 들어, `@Test` 어노테이션을 사용하여 해당 메소드가 테스트 메소드임을 정의할 수 있습니다.

## 2. Apache HttpClient 의존성 추가

API 테스트를 위해 Apache HttpClient를 사용하려면 먼저 의존성을 추가해야 합니다. Maven을 사용한다면 pom.xml에 다음과 같은 의존성을 추가할 수 있습니다.

```xml
<dependency>
    <groupId>org.apache.httpcomponents</groupId>
    <artifactId>httpclient</artifactId>
    <version>4.5.13</version>
</dependency>
```

## 3. API 테스트 작성하기

이제 API 테스트를 작성해보겠습니다. 예를 들어, GET 요청을 보내고 응답을 확인하는 테스트를 작성해볼 수 있습니다. 다음은 Apache HttpClient를 사용하여 GET 요청을 보내고 응답을 확인하는 예제 코드입니다.

```java
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.testng.Assert;
import org.testng.annotations.Test;

public class APITest {
    
    @Test
    public void testGetRequest() throws Exception {
        // HttpClient 생성
        CloseableHttpClient httpClient = HttpClients.createDefault();

        // GET 요청 생성
        HttpGet request = new HttpGet("http://api.example.com/get");

        // 요청 실행
        HttpResponse response = httpClient.execute(request);

        // 응답 코드 확인
        int statusCode = response.getStatusLine().getStatusCode();
        Assert.assertEquals(statusCode, 200);
    }
}
```

위 예제에서는 `@Test` 어노테이션을 사용하여 테스트 메소드임을 지정하고, HttpClient를 생성한 후 GET 요청을 생성하고 실행하는 방법을 보여줍니다. 마지막으로 응답의 상태 코드를 확인하여 테스트를 수행합니다.

## 4. API 테스트 실행하기

API 테스트를 실행하기 위해서는 TestNG를 사용하여 테스트를 실행해야 합니다. Maven을 사용한다면 다음과 같이 명령어를 입력하여 테스트를 실행할 수 있습니다.

```bash
mvn test
```

테스트 결과는 테스트 결과 리포트 파일이나 콘솔에 표시됩니다.

## 결론

이 글에서는 TestNG와 Apache HttpClient를 사용하여 API 테스트를 수행하는 방법에 대해 알아보았습니다. TestNG는 테스트 코드를 작성하고 실행하기 위한 강력한 테스트 프레임워크이며, Apache HttpClient는 API와의 통신을 위한 라이브러리입니다. 이러한 도구들을 사용하여 효율적으로 API 테스트를 수행할 수 있습니다.