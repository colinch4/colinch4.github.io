---
layout: post
title: "[java] Java Apache Commons Configuration과 외부 프로퍼티 데이터 소스 간의 연동"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

이번 포스트에서는 Java Apache Commons Configuration 라이브러리를 사용하여 외부 프로퍼티 데이터 소스와의 연동 방법에 대해 알아보겠습니다.

## Apache Commons Configuration이란?
Apache Commons Configuration은 Apache 소프트웨어 재단에서 개발한 Java 기반의 구성 정보 라이브러리입니다. 이 라이브러리를 사용하면 XML, 프로퍼티 파일, 환경 변수 등 다양한 데이터 소스로부터 구성 정보를 읽고 쓸 수 있습니다.

## 외부 프로퍼티 데이터 소스 연동하기
Apache Commons Configuration을 사용하여 외부 프로퍼티 데이터 소스와 연동하는 방법은 다음과 같습니다.

1. Maven 또는 Gradle과 같은 종속성 관리 도구를 사용하여 Apache Commons Configuration 라이브러리를 프로젝트에 추가합니다.

2. 연동하려는 프로퍼티 파일을 작성합니다. 프로퍼티 파일은 key-value 형식으로 데이터를 저장하는 파일입니다. 예를 들어, `config.properties` 파일에는 다음과 같은 내용이 포함될 수 있습니다.

   ```properties
   database.url = jdbc:mysql://localhost:3306/mydb
   database.username = myuser
   database.password = mypassword
   ```

3. Java 코드에서 Apache Commons Configuration을 사용하여 외부 프로퍼티 데이터 소스를 읽습니다. 다음은 `config.properties` 파일을 읽는 예제 코드입니다.

   ```java
   import org.apache.commons.configuration2.Configuration;
   import org.apache.commons.configuration2.builder.FileBasedConfigurationBuilder;
   import org.apache.commons.configuration2.builder.fluent.Parameters;
   import org.apache.commons.configuration2.ex.ConfigurationException;

   public class AppConfig {
       private static final String CONFIG_FILE = "config.properties";

       public static void main(String[] args) {
           Parameters parameters = new Parameters();
           FileBasedConfigurationBuilder<PropertiesConfiguration> builder =
                   new FileBasedConfigurationBuilder<>(PropertiesConfiguration.class)
                           .configure(parameters.fileBased()
                                   .setFileName(CONFIG_FILE));

           try {
               Configuration config = builder.getConfiguration();
               String databaseUrl = config.getString("database.url");
               String username = config.getString("database.username");
               String password = config.getString("database.password");
               // TODO: 데이터베이스 연결 및 처리 로직 작성
           } catch (ConfigurationException e) {
               e.printStackTrace();
           }
       }
   }
   ```

   위의 코드에서는 `FileBasedConfigurationBuilder` 클래스를 사용하여 `config.properties` 파일을 로드하고, `getConfiguration()` 메서드를 통해 `Configuration` 객체를 얻어옵니다. 그리고 `getString()` 메서드를 사용하여 프로퍼티 값을 가져올 수 있습니다.

   위의 예제에서는 데이터베이스 관련 프로퍼티 값을 가져와서 데이터베이스 연결 및 처리 로직을 작성하도록 주석으로 표시되어 있습니다.

4. 외부 프로퍼티 데이터 소스와의 연동이 끝나면, 프로그램에서 필요한 구성 정보를 프로퍼티 파일에서 읽어와서 사용할 수 있습니다.

## 마치며
Java Apache Commons Configuration을 사용하면 외부 프로퍼티 데이터 소스와 간단하게 연동할 수 있습니다. 이를 통해 프로그램의 구성 정보를 외부에서 관리할 수 있고, 유연하게 변경할 수 있습니다.

추가 자세한 내용은 [Apache Commons Configuration 문서](https://commons.apache.org/proper/commons-configuration/userguide/index.html)를 참조하시기 바랍니다.