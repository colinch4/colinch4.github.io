---
layout: post
title: "[java] Java Apache CXF와 Apache Tomcat 통합"
description: " "
date: 2023-11-28
tags: [java]
comments: true
share: true
---

Apache CXF와 Apache Tomcat은 둘 다 Java 기반의 오픈 소스 프레임워크이며, 웹 서비스 및 웹 어플리케이션 개발에 널리 사용됩니다. CXF는 SOAP 및 RESTful 웹 서비스를 개발할 수 있는 풍부한 기능을 제공하며, Tomcat은 웹 응용 프로그램을 개발하고 실행하기위한 서블릿 컨테이너로서 사용됩니다.

이번 블로그에서는 Apache CXF를 사용하여 웹 서비스를 개발하고, 이를 Apache Tomcat에 통합하는 방법을 알아보겠습니다.

## 1. Apache CXF 프로젝트 생성

먼저 Apache CXF 프로젝트를 생성해야 합니다. 이를 위해 다음과 같은 단계를 따릅니다.

1. Apache CXF 웹 사이트에서 최신 버전의 CXF를 다운로드합니다.
2. 압축 해제한 후, 프로젝트를 생성할 디렉토리에 복사합니다.
3. 명령 프롬프트나 터미널에서 프로젝트 디렉토리로 이동합니다.
4. CXF 프로젝트를 생성하기 위해 다음 명령어를 실행합니다:
   ```java
   mvn archetype:generate -DarchetypeGroupId=org.apache.cxf.archetype -DarchetypeArtifactId=simple-jaxws-jdk13 -DarchetypeVersion=3.4.3 -DgroupId=com.example -DartifactId=mywebservice -Dversion=1.0-SNAPSHOT
   ```

## 2. Apache Tomcat 설정

CXF 프로젝트를 생성한 후에는 Tomcat을 설치하고 설정해야 합니다. Tomcat을 다운로드하고 압축을 해제한 후, 다음과 같은 단계를 따릅니다.

1. 터미널을 열고 Tomcat 설치 디렉토리로 이동합니다.
2. 배포 디렉토리를 생성하기 위해 다음 명령어를 실행합니다:
   ```sh
   mkdir webapps/mywebservice
   ```
3. CXF 프로젝트의 WAR 파일을 배포 디렉토리로 복사합니다:
   ```sh
   cp mywebservice/target/mywebservice-1.0-SNAPSHOT.war webapps/mywebservice/
   ```

## 3. 웹 서비스 배포 및 실행

CXF 프로젝트와 Tomcat 설정이 완료되었으므로, 이제 웹 서비스를 배포하고 실행할 수 있습니다.

1. 터미널에서 Tomcat의 bin 디렉토리로 이동합니다.
2. 다음 명령어를 실행하여 Tomcat을 시작합니다:
   ```sh
   ./catalina.sh start
   ```
3. 웹 브라우저에서 `http://localhost:8080/mywebservice`로 이동합니다. CXF의 웹 서비스 화면이 표시되어야 합니다.

이제 Apache CXF와 Apache Tomcat을 통합하여 Java 웹 서비스를 개발 및 실행하는 방법을 알게 되었습니다. CXF의 강력한 기능과 Tomcat의 안정성 및 확장성을 결합하여 더욱 강력한 웹 어플리케이션을 개발할 수 있습니다.

> **참고 자료:**
> - [Apache CXF Documentation](https://cxf.apache.org/docs/)
> - [Apache Tomcat Documentation](https://tomcat.apache.org/tomcat-9.0-doc/)