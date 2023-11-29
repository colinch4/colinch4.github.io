---
layout: post
title: "[java] Java Jersey에서 Swagger UI를 사용하여 API 문서를 시각화하는 방법은?"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

Swagger는 RESTful API를 문서화하고 시각화하는 도구입니다. 이를 통해 개발자들은 API의 사용법을 쉽게 이해하고, 테스트하고, 통합할 수 있습니다. Java Jersey 프레임워크에서 Swagger UI를 사용하여 API 문서를 시각화하는 방법을 알아보겠습니다.

1. Swagger Maven 종속성 추가하기:

먼저, Maven 프로젝트의 `pom.xml` 파일에 Swagger Maven 종속성을 추가해야 합니다. 아래의 코드를 `<dependencies>` 태그 내에 추가하세요.

```xml
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-jersey2-jaxrs</artifactId>
    <version>{Swagger 버전}</version>
</dependency>
```

위의 코드에서 `{Swagger 버전}`을 실제 사용할 Swagger 버전으로 대체해야 합니다.

2. Swagger 설정 파일 작성하기:

다음으로, Swagger 설정 파일을 작성해야 합니다. 프로젝트의 `src/main/resources` 디렉토리에 `swagger.yaml` 또는 `swagger.json` 파일을 생성하세요. 예를 들어, `swagger.yaml` 파일을 작성해 보겠습니다.

```yaml
swagger: "2.0"
info:
  version: 1.0.0
  title: My API
  description: API 문서 예시

# Swagger UI에서 표시할 API 엔드포인트 설정
host: localhost:8080
basePath: /my-api

# API 엔드포인트 정의
paths:
  /users:
    get:
      summary: Get all users
      operationId: getAllUsers
      produces:
        - application/json
      responses:
        200:
          description: Successful operation

  /users/{id}:
    get:
      summary: Get user by ID
      operationId: getUserById
      produces:
        - application/json
      parameters:
        - name: id
          in: path
          description: ID of the user
          required: true
          type: integer
      responses:
        200:
          description: Successful operation
        404:
          description: User not found
```

위의 설정 파일에서는 API의 기본 정보 및 각 엔드포인트의 요약, 호출 가능한 메서드, 응답 형식 등을 정의합니다. 필요에 따라 더 많은 엔드포인트를 추가할 수 있습니다.

3. Swagger UI 설정:

마지막으로, Swagger UI를 설정해야 합니다. Jersey 애플리케이션의 `ResourceConfig` 클래스를 확장하여 Swagger와 관련된 설정을 추가하세요.

```java
import io.swagger.jaxrs.config.BeanConfig;

public class MyApplication extends ResourceConfig {
    public MyApplication() {
        // Swagger 설정
        register(io.swagger.jaxrs.listing.ApiListingResource.class);
        register(io.swagger.jaxrs.listing.SwaggerSerializers.class);
        
        // Swagger UI를 위한 설정
        BeanConfig beanConfig = new BeanConfig();
        beanConfig.setVersion("1.0.0");
        beanConfig.setSchemes(new String[]{"http"});
        beanConfig.setHost("localhost:8080");
        beanConfig.setBasePath("/my-api");
        beanConfig.setResourcePackage("com.example.api");
        beanConfig.setScan(true);
    }
}
```

위의 코드에서 `com.example.api`는 API 엔드포인트를 포함한 패키지 경로로 바꿔야 합니다.

4. API 문서 확인하기:

모든 설정이 완료되면, 애플리케이션을 실행하고 `http://localhost:8080/my-api/swagger.json`에 접속하여 Swagger UI에서 생성된 API 문서를 확인할 수 있습니다. Swagger UI에서 각 엔드포인트의 정보와 테스트할 수 있는 기능을 제공합니다.

이제 Java Jersey에서 Swagger UI를 사용하여 API 문서를 손쉽게 시각화할 수 있습니다. 이러한 문서화는 개발자들이 API를 이해하고 사용하는 데 도움을 줄 것입니다.

참고 자료:
- [Swagger documentation](https://swagger.io/docs/)
- [Jersey and Swagger integration example](https://github.com/swagger-api/swagger-core/wiki/Swagger-2.X---Integration-and-configuration)