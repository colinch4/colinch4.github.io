---
layout: post
title: "[java] Java에서 Google Protocol Buffers를 활용한 데이터 직렬화"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Google Protocol Buffers는 구조화된 데이터의 직렬화 및 역직렬화를 위한 효율적인 방법을 제공하는 Google에서 개발한 오픈 소스 프로토콜입니다. 이를 Java에서 활용하면 객체를 이진 형식으로 직렬화하고 역직렬화할 수 있습니다.

## 설치

Java에서 Protocol Buffers를 사용하려면 먼저 Protocol Buffers Compiler (`protoc`)를 설치해야 합니다. [Protocol Buffers Release 페이지](https://github.com/protocolbuffers/protobuf/releases)에서 해당 운영체제에 맞는 컴파일러를 다운로드하여 설치합니다.

그리고 다음과 같이 Maven 또는 Gradle 등의 빌드 도구에서 Protocol Buffers의 의존성을 추가합니다.

```xml
<dependency>
    <groupId>com.google.protobuf</groupId>
    <artifactId>protobuf-java</artifactId>
    <version>3.15.8</version>
</dependency>
```
또는
```groovy
implementation 'com.google.protobuf:protobuf-java:3.15.8'
```

## .proto 파일 작성

Protocol Buffers를 사용하기 위해 먼저 `.proto` 파일에 데이터 구조를 정의해야 합니다. 이 파일에는 메시지 유형과 필드 정의를 작성합니다. 예를 들어 `Person` 메시지와 `name`과 `age` 필드를 가지도록 다음과 같이 작성할 수 있습니다.

```proto
syntax = "proto3";

message Person {
    string name = 1;
    int32 age = 2;
}
```

## 코드 생성

`.proto` 파일을 작성한 후에는 Protocol Buffers 컴파일러를 사용하여 Java 코드를 생성해야 합니다. 다음 명령을 실행하면, `.proto` 파일이 있는 디렉토리에 Java 클래스 파일이 생성됩니다.

```shell
$ protoc --java_out=. person.proto
```

## 직렬화 및 역직렬화

Java에서 Protocol Buffers를 사용하여 데이터를 직렬화하고 역직렬화하는 방법은 다음과 같습니다.

```java
import com.example.Person;

...

// 직렬화
Person person = Person.newBuilder()
    .setName("John Doe")
    .setAge(30)
    .build();

byte[] serializedData = person.toByteArray();

// 역직렬화
Person deserializedPerson = Person.parseFrom(serializedData);
String name = deserializedPerson.getName();
int age = deserializedPerson.getAge();
```

위 예제에서는 `Person` 객체를 생성한 후 `toByteArray()`를 사용하여 이를 바이트 배열로 직렬화합니다. 역직렬화할 때는 `parseFrom()`을 사용하여 바이트 배열을 `Person` 객체로 변환합니다. 이후 `getName()` 및 `getAge()`와 같은 getter 메서드를 사용하여 필드 값을 얻을 수 있습니다.

## 결론

Java에서 Google Protocol Buffers를 사용하면 빠르고 효율적인 데이터 직렬화 및 역직렬화를 수행할 수 있습니다. `.proto` 파일을 작성하고 코드를 생성하여 사용하면 됩니다. Protocol Buffers는 다양한 언어에서 지원되므로 여러 플랫폼 간의 데이터 교환에도 용이합니다.

---

참고 자료:
- [Protocol Buffers GitHub Repository](https://github.com/protocolbuffers/protobuf)
- [Protocol Buffers Language Guide](https://developers.google.com/protocol-buffers/docs/proto3)