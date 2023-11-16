---
layout: post
title: "[java] Java Apache Commons Configuration 활용 예제: 로그 파일 압축 설정"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Java 애플리케이션에서 로그 파일 압축을 설정하기 위해 Apache Commons Configuration 라이브러리를 사용하는 방법에 대해 알아보겠습니다.

## Apache Commons Configuration 소개

Apache Commons Configuration은 Java 애플리케이션에서 설정 파일을 다루기 위한 유용한 라이브러리입니다. 이 라이브러리는 다양한 설정 파일 포맷을 지원하며, 설정 값들을 쉽게 로드하고 저장할 수 있습니다. 

## 로그 파일 압축 설정 예제

아래 예제에서는 Apache Commons Configuration을 사용하여 로그 파일 압축을 설정하는 방법을 보여줍니다.

1. 먼저, Maven 등의 의존성 관리 도구를 이용하여 Apache Commons Configuration 라이브러리를 프로젝트에 추가해야 합니다. 

   ```xml
   <dependency>
       <groupId>org.apache.commons</groupId>
       <artifactId>commons-configuration2</artifactId>
       <version>2.7</version>
   </dependency>
   ```

2. 다음으로, 설정 파일인 `config.properties` 파일을 생성하고 아래와 같이 로그 파일 압축에 관련된 설정을 추가합니다.

   ```properties
   log.compress=true
   log.compress.threshold=10485760
   log.compress.max.num=5
   ```

   위 설정 파일은 로그 파일 압축 여부를 결정하는 `log.compress` 속성과 로그 파일 압축을 진행하는 데 필요한 파일 크기 임계값 `log.compress.threshold`, 그리고 최대 압축 파일 개수를 지정하는 `log.compress.max.num` 속성을 가지고 있습니다.

3. Java 코드에서 Apache Commons Configuration을 사용하여 설정 파일을 로드하고 로그 파일 압축 설정을 읽어옵니다.

   ```java
   import org.apache.commons.configuration2.Configuration;
   import org.apache.commons.configuration2.PropertiesConfiguration;
   
   public class LogConfiguration {
       private static final String CONFIG_FILE = "config.properties";
       
       private Configuration config;
       
       public LogConfiguration() {
           try {
               config = new PropertiesConfiguration(CONFIG_FILE);
           } catch (ConfigurationException e) {
               e.printStackTrace();
               config = null;
           }
       }
       
       public boolean isLogCompressionEnabled() {
           return config.getBoolean("log.compress", false);
       }
       
       public long getLogCompressionThreshold() {
           return config.getLong("log.compress.threshold", 0L);
       }
       
       public int getMaxLogCompressionFiles() {
           return config.getInt("log.compress.max.num", 0);
       }
   }
   ```

   위 코드에서 `LogConfiguration` 클래스는 `config.properties` 파일을 로드하고, `isLogCompressionEnabled()`, `getLogCompressionThreshold()`, `getMaxLogCompressionFiles()` 메소드를 통해 로그 파일 압축 설정 값을 반환합니다.

4. 로그 파일 압축 설정을 사용하는 예제 코드를 작성합니다.

   ```java
   public class LogFileManager {
       private static final String LOG_FILE_PATH = "/path/to/log/file.log";
       
       private LogConfiguration logConfig;
       
       public LogFileManager() {
           logConfig = new LogConfiguration();
       }
       
       public void manageLogFiles() {
           if (logConfig.isLogCompressionEnabled()) {
               long threshold = logConfig.getLogCompressionThreshold();
               int maxFiles = logConfig.getMaxLogCompressionFiles();
               
               // 로그 파일 압축 설정을 기반으로 로그 파일 관리 로직을 구현
               // ...
           } else {
               // 로그 파일 압축을 사용하지 않는 경우 로그 파일 관리 로직을 구현
               // ...
           }
       }
   }
   ```

   위 코드에서 `LogFileManager` 클래스는 `LogConfiguration` 객체를 생성하여 로그 파일 압축 설정을 읽어오고, `manageLogFiles()` 메소드를 통해 로그 파일을 관리합니다. `isLogCompressionEnabled()` 메소드를 사용하여 로그 파일 압축 설정이 활성화되어 있는지 확인하고, 그에 따른 로그 파일 관리 로직을 구현합니다.

## 결론

이번 예제에서는 Apache Commons Configuration을 사용하여 Java 애플리케이션에서 로그 파일 압축 설정을 관리하는 방법에 대해 알아보았습니다. Apache Commons Configuration을 사용하면 설정 파일을 쉽게 다룰 수 있으며, 다양한 설정 값들을 처리할 수 있습니다.

더 자세한 내용은 [Apache Commons Configuration 공식 문서](https://commons.apache.org/proper/commons-configuration/)에서 찾아볼 수 있습니다.