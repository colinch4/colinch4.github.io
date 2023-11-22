---
layout: post
title: "[java] Java에서 Google Protocol Buffers 사용 방법"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Google Protocol Buffers는 구조화된 데이터를 직렬화하고 전송하는 데 사용되는 프로토콜 버퍼 형식입니다. 이를 사용하면 데이터를 쉽게 정의하고 다양한 언어 간에 효율적으로 직렬화 할 수 있습니다. 이번 블로그에서는 Java에서 Google Protocol Buffers를 사용하는 방법에 대해 알아보겠습니다.

## 1. Protocol Buffers 설치

Java에서 Protocol Buffers를 사용하려면 먼저 Protocol Buffers 컴파일러 `protoc`를 설치해야 합니다. 
1. [Protocol Buffers 다운로드 페이지](https://developers.google.com/protocol-buffers/docs/downloads)에서 Java용 Protocol Buffers를 다운로드하고 설치하세요.
2. 압축 해제 후 `protoc` 실행 파일을 시스템 경로에 추가하세요.

## 2. Protocol Buffers 정의 파일 작성

다음으로 Protocol Buffers 정의 파일을 작성해야 합니다. 이 파일은 데이터 구조를 정의하고 직렬화 및 역직렬화하는 데 사용됩니다.

```proto
syntax = "proto2";

message Person {
    required string name = 1;
    optional int32 age = 2;
    repeated string hobbies = 3;
}
```

위의 예제에서는 `Person`이라는 메시지 타입을 정의하고 세 가지 필드를 정의합니다. `name` 필드는 반드시 있어야 하며, `age` 필드는 선택적이며, `hobbies` 필드는 반복될 수 있습니다.

## 3. Protocol Buffers 컴파일하기

작성한 정의 파일을 컴파일하여 Java 클래스를 생성해야 합니다. 다음 명령을 사용하여 컴파일할 수 있습니다.

```
protoc --java_out=<output_directory> <proto_file>
```

위 명령에서 `<output_directory>`는 Java 클래스가 저장될 디렉토리 경로를 나타내고, `<proto_file>`은 작성한 정의 파일의 경로와 파일 이름입니다.

## 4. Protocol Buffers 사용하기

이제 Protocol Buffers를 Java 프로젝트에서 사용할 수 있습니다.

```java
import com.example.Person;

public class Main {
    public static void main(String[] args) {
        // Person 객체 생성
        Person person = Person.newBuilder()
            .setName("John")
            .setAge(30)
            .addHobbies("coding")
            .addHobbies("reading")
            .build();

        // 직렬화
        byte[] serializedData = person.toByteArray();

        // 역직렬화
        Person deserializedPerson = Person.parseFrom(serializedData);

        // 데이터 출력
        System.out.println("Name: " + deserializedPerson.getName());
        System.out.println("Age: " + deserializedPerson.getAge());
        System.out.println("Hobbies: " + deserializedPerson.getHobbiesList());
    }
}
```

위의 예제에서는 `Person` 클래스를 import하고, `Person` 객체를 생성한 후 직렬화하고 역직렬화합니다. 마지막으로 데이터를 출력합니다.

## 결론

Java에서 Google Protocol Buffers를 사용하는 방법에 대해 알아봤습니다. 이를 통해 데이터를 효율적이고 간단하게 직렬화하고 전송할 수 있습니다. 자세한 내용은 [Google Protocol Buffers 공식 문서](https://developers.google.com/protocol-buffers)를 참조하시기 바랍니다.