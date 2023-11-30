---
layout: post
title: "[java] 자바로 아파치 플링크 애플리케이션 작성하기(Writing Apache Flink applications with Java)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크는 대규모 데이터 처리를 위한 오픈 소스 분산 스트리밍 플랫폼입니다. 자바를 사용하여 플링크 애플리케이션을 작성하는 방법을 알아보겠습니다.

## 1. 개발 환경 설정

아파치 플링크를 사용하기 위해서는 개발 환경을 설정해야 합니다. 아래의 단계를 따라해주세요.

### 1.1 자바 개발 키트 (JDK) 설치

플링크는 자바로 작성되었으므로, 자바 개발 키트 (JDK)가 설치되어 있어야 합니다. 최신 버전의 JDK를 [Oracle 홈페이지](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)에서 다운로드하고 설치하세요.

### 1.2 아파치 플링크 다운로드

아파치 플링크를 다운로드하여 애플리케이션 개발에 사용할 수 있습니다. 플링크를 다운로드하고 압축을 해제하세요. 다운로드 링크는 아래와 같습니다.

- [아파치 플링크](https://flink.apache.org/downloads.html)

### 1.3 의존성 관리 도구 설치

자바 프로젝트에서 의존성 관리를 위해 [Apache Maven](https://maven.apache.org/)을 사용할 수 있습니다. Maven을 설치하고 환경 변수를 설정하면 편리하게 의존성을 관리할 수 있습니다.

## 2. 플링크 애플리케이션 작성하기

이제 실제로 플링크 애플리케이션을 작성해보겠습니다.

### 2.1 애플리케이션 클래스 생성하기

새로운 Java 프로젝트를 생성하고, `MyFlinkApp.java`라는 이름의 클래스를 생성하세요. 이 클래스는 `org.apache.flink.api.common.functions.MapFunction` 인터페이스를 구현할 것입니다.

```java
public class MyFlinkApp implements MapFunction<String, String> {

    @Override
    public String map(String value) throws Exception {
        // 값에 대한 변환 로직 작성
        return value.toUpperCase();
    }

    public static void main(String[] args) throws Exception {
        // 플링크 실행 환경 설정
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        // 입력 스트림 생성
        DataStream<String> inputStream = env.socketTextStream("localhost", 9000);

        // 변환 함수 적용
        DataStream<String> outputStream = inputStream.map(new MyFlinkApp());

        // 결과 출력
        outputStream.print();

        // 플링크 실행
        env.execute("MyFlinkApp");
    }
}
```

### 2.2 애플리케이션 실행하기

위의 코드에서 `map` 메서드는 입력 값을 대문자로 변환하는 로직을 구현하고 있습니다. `main` 메서드에서는 플링크 실행 환경을 설정하고, 소켓을 통해 입력 스트림을 생성하고, 변환 함수를 적용한 뒤, 결과를 출력합니다. 마지막으로 `env.execute` 메서드를 호출하여 애플리케이션을 실행합니다.

애플리케이션을 실행하기 전에, 소켓 서버를 실행하여 실시간으로 데이터를 받을 수 있도록 준비해야 합니다. 이를 위해 아래의 명령어를 터미널에서 실행하세요.

```shell
nc -lk 9000
```

이제 애플리케이션을 실행할 준비가 되었습니다. 프로젝트를 빌드하고, 생성된 JAR 파일을 아래의 명령어를 사용하여 실행할 수 있습니다.

```shell
./bin/flink run -c com.example.MyFlinkApp path/to/your/project.jar
```

## 결론

이제 자바를 사용하여 아파치 플링크 애플리케이션을 작성하는 방법에 대해 알아보았습니다. 플링크는 대규모 데이터 처리를 위한 강력한 분산 스트리밍 플랫폼이므로, 효율적인 데이터 처리를 위해 자바와 함께 활용해보시기 바랍니다.