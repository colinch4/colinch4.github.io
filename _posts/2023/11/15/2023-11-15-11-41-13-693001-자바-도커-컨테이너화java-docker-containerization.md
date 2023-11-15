---
layout: post
title: "[java] 자바 도커 컨테이너화(Java Docker containerization)"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

최근에는 도커(Docker)의 인기로 인해 많은 어플리케이션이 도커 컨테이너에 배포되고 있습니다. 도커를 사용하여 자바 어플리케이션을 컨테이너화하는 것은 이점을 많이 제공합니다. 컨테이너는 의존성 관리, 배포 및 확장에 편리하며, 여러 개발 환경에서 일관되게 실행할 수 있습니다.

## 도커 이미지 작성하기

도커 이미지는 자바 어플리케이션의 실행에 필요한 모든 구성 요소를 포함하고 있습니다. 이를 위해 먼저 도커 이미지를 작성해야 합니다. 다음은 간단한 자바 웹 애플리케이션의 도커 이미지를 작성하는 예제입니다.

```java
FROM openjdk:11-jdk-slim

WORKDIR /app

COPY target/myapp.jar /app/myapp.jar

EXPOSE 8080

CMD ["java", "-jar", "myapp.jar"]
```

위의 Dockerfile은 OpenJDK 11의 slim 베이스 이미지를 사용하여 자바 어플리케이션을 실행하는 도커 이미지를 작성합니다. 먼저 작업 디렉토리를 설정하고, 어플리케이션 JAR 파일을 복사한 다음, 8080 포트를 열고 JAR 파일을 실행합니다.

## 도커 이미지 빌드하기

이제 도커 이미지를 빌드할 차례입니다. 다음 명령어를 터미널에 입력하여 도커 이미지를 빌드합니다.

```bash
docker build -t myapp .
```

위의 명령어는 현재 디렉토리의 Dockerfile을 사용하여 `myapp`이란 이름의 도커 이미지를 빌드합니다.

## 도커 컨테이너 실행하기

마지막으로, 빌드한 도커 이미지를 실행하여 컨테이너를 실행해 보겠습니다. 다음 명령어를 사용합니다.

```bash
docker run -p 8080:8080 myapp
```

위의 명령어는 `myapp` 도커 이미지를 8080 포트와 연결하여 컨테이너를 실행합니다.

## 결론

자바 도커 컨테이너화는 자바 어플리케이션의 배포 및 관리를 더욱 효율적으로 만들어줍니다. 도커를 사용하면 어플리케이션 실행 환경의 일관성과 가용성을 유지할 수 있습니다. 도커를 통해 자바 어플리케이션을 컨테이너화하는 방법에 대해 알아보았습니다.

---

참고:

- [Docker Documentation](https://docs.docker.com/)
- [OpenJDK Docker Official Images](https://hub.docker.com/_/openjdk)