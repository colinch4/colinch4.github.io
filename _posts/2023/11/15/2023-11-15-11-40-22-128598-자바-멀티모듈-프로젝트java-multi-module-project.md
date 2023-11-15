---
layout: post
title: "[java] 자바 멀티모듈 프로젝트(Java multi-module project)"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

자바에서 멀티모듈 프로젝트를 생성하는 방법에 대해 알아보겠습니다. 멀티모듈 프로젝트는 여러 개의 모듈로 구성되어 있으며, 각 모듈은 독립적으로 빌드되고 패키징될 수 있습니다. 이를 통해 프로젝트의 구조를 체계적으로 관리하고 코드의 재사용성을 높일 수 있습니다.

## 프로젝트 구성하기

1. 프로젝트 디렉토리 생성하기: 
   ```
   mkdir MyProject
   cd MyProject
   ```

2. 루트 모듈 생성하기:
   ```
   mkdir MyProject
   cd MyProject
   ```

3. 서브 모듈 생성하기:
   ```
   mkdir module1
   mkdir module2
   ```

4. 각 모듈의 디렉토리로 이동한 후 Maven 프로젝트 구조 생성하기:
   ```
   cd module1
   mvn archetype:generate -DgroupId=com.example.module1 -DartifactId=module1 -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
   
   cd ../module2
   mvn archetype:generate -DgroupId=com.example.module2 -DartifactId=module2 -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
   ```

## 의존성 설정하기

각 모듈은 필요한 의존성을 별도로 설정할 수 있으며, 루트 모듈(`pom.xml`)에서 전체 프로젝트의 의존성을 관리할 수도 있습니다. 이를 통해 모듈 간의 의존성 충돌을 방지하고 관리를 용이하게 할 수 있습니다.

1. 루트 모듈(`pom.xml`)에 모듈간 의존성 추가하기:
   ```xml
   <modules>
       <module>module1</module>
       <module>module2</module>
   </modules>
   ```

2. 각 모듈(`pom.xml`)에 필요한 의존성 추가하기:
   ```xml
   <dependencies>
       <!-- 의존성 추가 -->
   </dependencies>
   ```

## 빌드 및 실행하기

각 모듈은 독립적으로 빌드되고 패키징될 수 있으며, 필요에 따라 모든 모듈을 한 번에 빌드할 수도 있습니다.

1. 개별 모듈 빌드하기:
   ```
   cd module1
   mvn clean install
   
   cd ../module2
   mvn clean install
   ```

2. 전체 프로젝트 빌드하기:
   ```
   cd MyProject
   mvn clean install
   ```

빌드가 완료된 후 각 모듈은 각자의 `target` 디렉토리에 패키징된 결과물을 가지고 있습니다.

## 결론

자바 멀티모듈 프로젝트를 통해 프로젝트를 구조적으로 관리할 수 있으며, 모듈 별로 독립적인 빌드와 패키징이 가능합니다. 이를 통해 코드의 재사용성과 유지보수성을 높일 수 있습니다. 자세한 내용은 [마이크로서비스 아키텍처 패턴과 구현(구글북)](https://books.google.co.kr/books/about/%EB%A7%88%EC%9D%B4%EC%B9%B4%EB%A5%BC_%EC%84%9C%EB%B9%84%EC%8A%A4%ED%95%98%EB%8A%94_%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98_%ED%8C%A8%ED%84%B4%EA%B3%BC_%EA%B5%AC%ED%98%84.html?id=xgv6DwAAQBAJ) 참고하시기 바랍니다.

## 참고 자료

- [마이크로서비스 아키텍처 패턴과 구현(구글북)](https://books.google.co.kr/books/about/%EB%A7%88%EC%9D%B4%EC%B9%B4%EB%A5%BC_%EC%84%9C%EB%B9%84%EC%8A%A4%ED%95%98%EB%8A%94_%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98_%ED%8C%A8%ED%84%B4%EA%B3%BC_%EA%B5%AC%ED%98%84.html?id=xgv6DwAAQBAJ)
- [Apache Maven 공식 문서](https://maven.apache.org/guides/index.html)