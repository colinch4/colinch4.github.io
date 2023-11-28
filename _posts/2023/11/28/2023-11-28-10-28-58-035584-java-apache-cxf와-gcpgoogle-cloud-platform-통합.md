---
layout: post
title: "[java] Java Apache CXF와 GCP(Google Cloud Platform) 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Apache CXF는 Java 기반의 오픈 소스 웹 서비스 프레임워크로, 다양한 웹 서비스 기술을 지원하고 있습니다. 이번 블로그에서는 Apache CXF를 사용하여 Google Cloud Platform(GCP)과 통합하는 방법을 살펴보겠습니다.

## 1. GCP 클라이언트 라이브러리 추가

먼저, GCP와 통합하기 위해 필요한 클라이언트 라이브러리를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, `pom.xml` 파일에 다음 의존성을 추가합니다.

```xml
<dependencies>
  <dependency>
    <groupId>com.google.cloud</groupId>
    <artifactId>google-cloud-storage</artifactId>
    <version>1.113.7</version>
  </dependency>
</dependencies>
```

Gradle을 사용하는 경우, `build.gradle` 파일에 다음 의존성을 추가합니다.

```groovy
dependencies {
    implementation 'com.google.cloud:google-cloud-storage:1.113.7'
}
```

## 2. GCP 인증 설정

GCP와 통합하기 위해서는 인증 정보를 설정해야 합니다. 가장 간단한 방법은 서비스 계정 키를 사용하는 것입니다. 서비스 계정 키를 생성하고 다운로드한 후, 애플리케이션 코드에서 다음과 같이 인증 파일 경로를 설정합니다.

```java
System.setProperty("GOOGLE_APPLICATION_CREDENTIALS", "/path/to/service-account-key.json");
```

인증 파일 경로를 설정한 후, GCP의 다양한 서비스를 사용할 수 있습니다.

## 3. Apache CXF로 GCP와 통합

Apache CXF를 사용하여 GCP와 통합하려면, GCP의 서비스 API를 호출하는 클라이언트를 구현해야 합니다. 예를 들어, Google Cloud Storage 서비스에 파일을 업로드하는 기능을 구현하려면 다음과 같이 Apache CXF 클라이언트를 생성할 수 있습니다.

```java
import org.apache.cxf.jaxrs.client.WebClient;
import javax.ws.rs.core.MediaType;

public class GCPIntegrationClient {
    
    private static final String GCS_UPLOAD_URL = "https://storage.googleapis.com/upload/storage/v1/b/{bucketName}/o?uploadType=media&name={fileName}";

    public void uploadFile(String bucketName, String fileName, byte[] fileData) {
        String url = GCS_UPLOAD_URL.replace("{bucketName}", bucketName)
                                   .replace("{fileName}", fileName);

        WebClient client = WebClient.create(url);
        client.type(MediaType.APPLICATION_OCTET_STREAM);

        Response response = client.post(fileData);
        if (response.getStatus() == Response.Status.OK.getStatusCode()) {
            System.out.println("File uploaded successfully");
        }
    }
}
```

위의 코드에서 `GCPIntegrationClient` 클래스는 `uploadFile` 메서드를 가지고 있습니다. 이 메서드는 Apache CXF의 `WebClient`를 사용하여 GCP의 Google Cloud Storage 서비스에 파일을 업로드하는 기능을 수행합니다.

## 4. 통합 테스트

이제 통합 코드를 테스트해보겠습니다. 예를 들어, 다음의 메인 메서드를 가진 테스트 클래스를 작성할 수 있습니다.

```java
public class GCPIntegrationTest {

    public static void main(String[] args) {
        GCPIntegrationClient client = new GCPIntegrationClient();
        
        String bucketName = "my-bucket";
        String fileName = "example.txt";
        byte[] fileData = "Hello, GCP!".getBytes();
        
        client.uploadFile(bucketName, fileName, fileData);
    }
}
```

위의 코드에서는 `GCPIntegrationClient`를 인스턴스화한 후 `uploadFile` 메서드를 호출하여 파일 업로드를 수행합니다. 업로드가 성공하면 "File uploaded successfully"라는 메시지가 출력됩니다.

## 결론

이제 Apache CXF를 사용하여 GCP와 통합하는 방법을 알아보았습니다. Apache CXF를 사용하면 간편하게 GCP의 다양한 서비스를 사용할 수 있으며, 위의 예시에서는 Google Cloud Storage를 사용하는 방법을 살펴보았습니다. 자세한 내용은 [Apache CXF 공식 문서](https://cxf.apache.org/)를 참조하시기 바랍니다.