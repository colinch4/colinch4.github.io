---
layout: post
title: "[java] Java Play Framework에서의 GraphQL 사용 방법은 어떻게 되나요?"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

GraphQL은 데이터 쿼리 및 조작 언어로, API를 쉽게 설계하고 사용할 수 있는 기술입니다. Java Play Framework는 웹 애플리케이션 개발을 위한 프레임워크이며, GraphQL을 통해 API를 개발할 수 있는 기능을 제공합니다. Java Play Framework에서의 GraphQL 사용 방법은 다음과 같습니다.

1. 의존성 추가
   먼저, Java Play Framework 프로젝트에 GraphQL을 사용하기 위한 의존성을 추가해야 합니다. `build.sbt` 파일에 다음과 같은 의존성을 추가합니다.

   ```java
   libraryDependencies += "com.graphql-java" % "graphql-java" % "3.0.0"
   libraryDependencies += "com.graphql-java" % "graphiql-scala" % "1.0.0"
   libraryDependencies += "com.graphql-java" % "graphql-java-tools" % "5.2.4"
   ```

2. 스키마 정의
   GraphQL은 스키마를 정의하여 데이터의 형식과 사용 가능한 쿼리를 정의합니다. `app/graphql` 디렉토리에 `.graphqls` 확장자를 가진 스키마 파일을 작성합니다.

   ```graphql
   type Query {
     hello: String
   }
   ```

3. 리졸버 작성
   스키마에 정의한 쿼리의 구현을 위해 리졸버 클래스를 작성해야 합니다. `app/graphql/resolvers` 디렉토리에 리졸버 클래스를 작성합니다.

   ```java
   package graphql.resolvers;

   import com.coxautodev.graphql.tools.GraphQLQueryResolver;

   public class QueryResolver implements GraphQLQueryResolver {
     public String hello() {
       return "Hello, World!";
     }
   }
   ```

4. 라우터 설정
   GraphQL 엔드포인트를 설정하기 위해 라우터를 설정해야 합니다. `conf/routes` 파일에 다음과 같은 라우팅 설정을 추가합니다.

   ```java
   GET     /        controllers.GraphQLController.graphiql
   POST    /graphql controllers.GraphQLController.graphql
   ```

5. 컨트롤러 작성
   라우팅에 설정한 컨트롤러를 작성해야 합니다. `app/controllers/GraphQLController.java` 파일을 생성하고, 다음과 같이 작성합니다.

   ```java
   package controllers;

   import play.mvc.Controller;
   import play.mvc.Result;
   import views.html.graphiql;

   public class GraphQLController extends Controller {
     public Result graphiql() {
       return ok(graphiql.render());
     }

     public Result graphql() {
       return TODO;
     }
   }
   ```

6. 실행 및 테스트
   애플리케이션을 실행하고, 웹 브라우저에서 `http://localhost:9000/`에 접속하여 GraphQL Playground(GraphiQL)을 확인할 수 있습니다.

이제 Java Play Framework에서 GraphQL을 사용하는 방법을 알게 되셨습니다. GraphQL을 통해 API를 개발하면 클라이언트는 필요한 데이터만 요청할 수 있고, 불필요한 데이터를 전송하지 않아 효율적인 통신을 구현할 수 있습니다.

참고 자료:
- [Java Play Framework 공식 문서](https://www.playframework.com/documentation/2.8.x/Home)
- [GraphQL Java 공식 문서](https://www.graphql-java.com/documentation/v15/)
- [GraphQL Java Tools 공식 문서](https://www.graphql-java-kickstart.com/tools/)