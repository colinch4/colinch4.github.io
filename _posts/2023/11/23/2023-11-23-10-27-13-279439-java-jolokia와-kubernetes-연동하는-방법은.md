---
layout: post
title: "[java] Java Jolokia와 Kubernetes 연동하는 방법은?"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Kubernetes는 컨테이너 오케스트레이션 플랫폼으로서, 대규모 분산 시스템을 관리하기 위해 사용됩니다. Jolokia는 JVM(Java Virtual Machine)에서 제공되는 모니터링 및 관리를 위한 도구입니다. 이 두 기술을 함께 사용하면 Kubernetes 환경에서 Java 어플리케이션을 모니터링하고 관리할 수 있습니다.

## 1. Jolokia를 Java 어플리케이션에 추가하기

Jolokia를 Java 어플리케이션에 추가하기 위해서는 다음과 같은 단계를 따릅니다:

1. Maven or Gradle 설정에 Jolokia 종속성을 추가합니다.
   
   - Maven:
   ```xml
   <dependency>
       <groupId>org.jolokia</groupId>
       <artifactId>jolokia-core</artifactId>
       <version>1.6.2</version>
   </dependency>
   ```
   
   - Gradle:
   ```groovy
   implementation 'org.jolokia:jolokia-core:1.6.2'
   ```

2. Jolokia 에이전트를 Java 어플리케이션에 추가합니다. 예를 들어, Spring Boot 어플리케이션의 경우, `spring-boot-starter-actuator`와 함께 사용할 수 있습니다.

   - Maven:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-actuator</artifactId>
   </dependency>
   ```
   
   - Gradle:
   ```groovy
   implementation 'org.springframework.boot:spring-boot-starter-actuator'
   ```

3. Java 어플리케이션의 구성 파일(`application.properties` 혹은 `application.yml`)에 Jolokia 관련 설정을 추가합니다. 아래는 예시입니다:
   
   ```yaml
   management:
     endpoints:
       web:
         exposure:
           include: "*"
   
   jolokia:
     config:
       debug: true
   ```
   
   위 설정은 모든 엔드포인트를 노출하고, Jolokia의 디버그 모드를 활성화합니다.

## 2. Kubernetes에서 Jolokia 연동하기

Kubernetes에서 Jolokia를 사용하기 위해서는 다음과 같은 단계를 따릅니다:

1. Jolokia Docker 이미지를 사용하여 컨테이너를 빌드합니다. Dockerfile에 다음과 같은 내용을 추가합니다:
   
   ```dockerfile
   FROM openjdk:8-jre
   
   # 어플리케이션 jar 파일 복사
   COPY app.jar app.jar
   
   # Jolokia Agent 다운로드 및 설치
   RUN mkdir -p /opt/jolokia && \
       wget -O /opt/jolokia/jolokia.jar https://search.maven.org/remotecontent?filepath=org/jolokia/jolokia-jvm/1.6.2/jolokia-jvm-1.6.2-agent.jar
   
   # 시작 스크립트 수정
   ENTRYPOINT ["java", "-javaagent:/opt/jolokia/jolokia.jar=port=8778,host=0.0.0.0,protocol=http"]
   CMD ["-jar", "app.jar"]
   ```

2. Jolokia로 노출된 포트를 Kubernetes 서비스로 정의합니다. `targetPort`는 Jolokia가 노출되는 포트와 일치하도록 설정해야 합니다. 아래는 예시입니다:
   
   ```yaml
   apiVersion: v1
   kind: Service
   metadata:
     name: my-app-service
   spec:
     selector:
       app: my-app
     ports:
       - name: jolokia
         protocol: TCP
         port: 8778
         targetPort: 8778
   ```

3. Kubernetes에서 Java 어플리케이션을 배포합니다. 이전 단계에서 정의한 서비스를 참조하는 파드 템플릿을 사용하면 됩니다.

   예시를 들어보면:
   
   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: my-app-pod
   spec:
     containers:
       - name: my-app-container
         image: my-app-image
         ports:
           - containerPort: 8778
   ```

## 결론

위 방법을 따르면 Kubernetes 환경에서 Java Jolokia를 활용하여 어플리케이션을 모니터링하고 관리할 수 있습니다. Jolokia를 Java 어플리케이션에 추가하고, Kubernetes에서 Jolokia를 연동하기 위한 단계를 따르면 됩니다.

자세한 내용은 [Jolokia 공식 문서](https://jolokia.org/reference/html/)를 참고하시기 바랍니다.