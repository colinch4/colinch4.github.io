---
layout: post
title: "[java] Java Apache Commons Configuration과 REST API 연동"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java Apache Commons Configuration은 설정 파일을 읽고 관리하는 라이브러리입니다. 이 라이브러리를 사용하여 RESTful API와 연동하는 방법에 대해 알아보겠습니다.

## Apache Commons Configuration 라이브러리 추가하기

먼저, Maven 또는 Gradle과 같은 빌드 도구를 사용하여 Apache Commons Configuration 라이브러리를 프로젝트에 추가해야 합니다. 다음은 Maven을 사용하는 예시입니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-configuration2</artifactId>
    <version>2.7</version>
</dependency>
```

## 설정 파일 로딩하기

Apache Commons Configuration은 다양한 설정 파일 형식을 지원합니다. 예를 들어, properties 파일, XML 파일, JSON 파일 등을 사용할 수 있습니다. 설정 파일을 로딩하기 위해 `Configurations` 클래스를 사용합니다.

```java
import org.apache.commons.configuration2.Configuration;
import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
import org.apache.commons.configuration2.builder.fluent.Parameters;

public class AppConfig {

    private static final String CONFIG_FILE_PATH = "config.properties";
    
    private Configuration configuration;

    public AppConfig() {
        // 설정 파일 빌더 생성
        FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
            new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                .configure(new Parameters().properties().setFileName(CONFIG_FILE_PATH));
        
        // 설정 로딩
        try {
            configuration = builder.getConfiguration();
        } catch (ConfigurationException e) {
            // 설정 파일 로딩 실패 처리
            e.printStackTrace();
        }
    }
    
    public String getApiBaseUrl() {
        return configuration.getString("api.base_url");
    }
    
    // 다른 설정 값들을 가져오는 메서드들...
}
```

위의 예제 코드에서는 properties 파일 형식의 설정 파일을 로딩하는 방법을 보여줍니다. `config.properties` 파일은 클래스패스 루트에 위치해야 하며, 다음과 같은 형식으로 작성되어야 합니다.

```properties
api.base_url=http://example.com/api
```

## REST API 호출하기

Apache Commons Configuration을 사용하여 설정 파일을 로딩한 후, 로딩한 설정 값을 사용하여 RESTful API를 호출할 수 있습니다. 다음은 Apache HttpClient 라이브러리를 사용하여 GET 요청을 보내는 예시입니다.

```java
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.HttpClientBuilder;

public class ApiClient {

    private HttpClient httpClient;

    public ApiClient() {
        // HttpClient 초기화
        httpClient = HttpClientBuilder.create().build();
    }

    public String fetchData(String url) {
        HttpGet getRequest = new HttpGet(url);

        try {
            // API 요청 보내기
            String response = httpClient.execute(getRequest, new BasicResponseHandler());
            return response;
        } catch (Exception e) {
            // API 호출 실패 처리
            e.printStackTrace();
            return null;
        }
    }
}
```

위의 예제에서는 `fetchData` 메서드를 사용하여 주어진 URL에 GET 요청을 보내고, 응답을 문자열로 반환합니다.

## 설정 값과 API 연동하기

마지막으로, `AppConfig` 클래스에서 로딩한 설정 값을 사용하여 REST API를 호출하는 예시 코드를 작성해 보겠습니다.

```java
public class Main {

    public static void main(String[] args) {
        AppConfig appConfig = new AppConfig();
        String apiBaseUrl = appConfig.getApiBaseUrl();

        ApiClient apiClient = new ApiClient();
        String responseData = apiClient.fetchData(apiBaseUrl + "/data");

        System.out.println(responseData);
    }
}
```

위의 예제에서는 `AppConfig` 클래스를 사용하여 `api.base_url` 설정 값을 가져오고, 이 값을 사용하여 API 요청을 보내고 응답을 출력합니다.

이렇게 Apache Commons Configuration과 REST API를 연동하여 Java 프로젝트에서 설정 파일을 관리하고 API를 호출할 수 있습니다.

## 참고 자료

- [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)
- [Apache HttpClient 공식 문서](https://hc.apache.org/httpcomponents-client-ga/)
- [Maven 공식 웹사이트](https://maven.apache.org/)
- [Gradle 공식 웹사이트](https://gradle.org/)