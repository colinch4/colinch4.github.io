---
layout: post
title: "[java] JHipster와 Microsoft SQL Server"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

JHipster는 서비스 기반 아키텍처(SOA)를 구축하기 위한 도구로, 자바 스프링 부트 프레임워크와 앵귤러, 리액트 등의 최신 웹 기술을 통합하여 사용자 친화적인 개발 경험을 제공합니다. JHipster는 다양한 데이터베이스와 호환되는데, 이 중 하나는 Microsoft SQL Server입니다.

Microsoft SQL Server는 대규모 데이터베이스 처리와 고성능 데이터 액세스를 지원하는 강력한 관계형 데이터베이스 관리 시스템(RDBMS)입니다. JHipster 프로젝트를 Microsoft SQL Server와 통합하려면 몇 가지 단계를 따라야 합니다.

## Microsoft SQL Server 설정하기

1. 먼저, SQL Server를 설치합니다. 이후, SQL Server Management Studio(SSMS)와 같은 도구를 사용하여 데이터베이스를 생성합니다.

2. 생성한 데이터베이스에 접근하기 위해 JDBC 드라이버를 다운로드하고 JHipster 프로젝트의 `pom.xml` 파일에 추가합니다. 다음은 Maven을 사용하는 경우의 예시입니다:

```xml
<dependency>
    <groupId>com.microsoft.sqlserver</groupId>
    <artifactId>mssql-jdbc</artifactId>
    <version>8.4.1.jre8</version>
</dependency>
```

## JHipster와 Microsoft SQL Server 연동하기

1. JHipster 프로젝트의 `application-dev.yml` 파일에서 데이터베이스 연결 정보를 설정합니다. 다음 예시는 SQL Server의 기본 설정을 사용하는 경우입니다:

```yml
spring:
  datasource:
    url: jdbc:sqlserver://localhost:1433;databaseName=mydatabase
    username: myusername
    password: mypassword
```

2. JHipster 애플리케이션을 실행합니다. JHipster는 자동으로 지정한 데이터베이스에 필요한 테이블을 생성하고 초기 데이터를 추가합니다.

## 주의사항

- Microsoft SQL Server는 윈도우 환경에서 주로 사용되는 데이터베이스이므로, JHipster 애플리케이션 실행을 위해 윈도우 운영체제가 필요합니다.

- 데이터베이스 연결 정보는 보안에 민감한 정보이므로, 실제 환경에서는 암호화되고 보안적으로 안전한 방식으로 저장 및 사용되어야 합니다.

## 참고 자료

- [JHipster Documentation](https://www.jhipster.tech/)
- [Microsoft SQL Server Documentation](https://docs.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver15)