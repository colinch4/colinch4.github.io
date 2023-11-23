---
layout: post
title: "[java] Java에서 Protocol Buffers를 사용하여 메시지 필드의 필드 JSON 표현 설정하기"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Protocol Buffers는 구조화된 데이터를 직렬화하고 역직렬화하는 데 사용되는 개방형 표준이다. 이 기술을 사용하면 데이터를 효율적이고 간결하게 직렬화할 수 있으며, 서로 다른 플랫폼 및 언어 간의 데이터 교환에 매우 유용하다.

Protocol Buffers 메시지에서 필드 값의 JSON 표현을 설정하는 방법을 알아보자. 아래 예제에서는 Java 언어를 사용한다.

## 1. Protocol Buffers 메시지 정의하기

먼저, Protocol Buffers를 사용하여 메시지를 정의해야 한다. 예를 들어, 사용자 정보를 나타내는 User 메시지를 정의하자.

```proto
syntax = "proto3";

message User {
   string name = 1;
   int32 age = 2;
   repeated string hobbies = 3;
}
```

위의 예제에서는 User라는 메시지를 정의하였다. name은 string 타입의 필드로, age는 int32 타입의 필드로, hobbies는 복수의 string 타입의 필드로 정의되었다.

## 2. Protocol Buffers 코드 생성하기

Protocol Buffers 메시지를 사용하기 위해 코드를 생성해야 한다. 다음 명령을 사용하여 protoc 컴파일러를 설치하고, 해당 메시지의 Java 코드를 생성한다.

```
$ protoc --java_out=generated/ path/to/user.proto
```

위의 예제에서는 `user.proto` 파일을 기반으로 Java 코드를 `generated/` 디렉토리에 생성하도록 설정하였다.

## 3. 메시지 필드의 필드 JSON 표현 설정하기

Java에서 Protocol Buffers 메시지의 필드 값의 JSON 표현을 설정하려면, 생성된 Java 코드에서 `JsonFormat` 클래스를 사용해야 한다. `JsonFormat.Printer`를 사용하여 메시지를 JSON 문자열로 직렬화하고, `JsonFormat.Parser`를 사용하여 JSON 문자열을 메시지로 역직렬화한다.

아래 예제에서는 User 메시지의 필드 값을 JSON으로 직렬화하는 방법과, JSON 문자열을 User 메시지로 역직렬화하는 방법을 보여준다.

```java
import com.google.protobuf.InvalidProtocolBufferException;
import com.google.protobuf.util.JsonFormat;

public class UserJsonExample {
    public static void main(String[] args) {
        // User 메시지 생성
        User.Builder userBuilder = User.newBuilder();
        userBuilder.setName("John Doe");
        userBuilder.setAge(25);
        userBuilder.addHobbies("Reading");
        userBuilder.addHobbies("Gaming");
        User user = userBuilder.build();

        try {
            // 메시지를 JSON 문자열로 직렬화
            String jsonString = JsonFormat.printer()
                    .includingDefaultValueFields()
                    .print(user);

            System.out.println(jsonString);

            // JSON 문자열을 메시지로 역직렬화
            User.Builder userBuilder2 = User.newBuilder();
            JsonFormat.parser()
                    .merge(jsonString, userBuilder2);
            User user2 = userBuilder2.build();

            System.out.println(user2.getName());
            System.out.println(user2.getAge());
            System.out.println(user2.getHobbiesList());
        } catch (InvalidProtocolBufferException e) {
            e.printStackTrace();
        }
    }
}
```

## 4. 결과 확인하기

위의 예제를 실행하면 다음과 같은 결과가 출력된다.

```
{
  "name": "John Doe",
  "age": 25,
  "hobbies": ["Reading", "Gaming"]
}
John Doe
25
[Reading, Gaming]
```

위의 결과에서는 User 메시지의 필드 값이 JSON 문자열로 직렬화되어 출력되고, 다시 해당 JSON 문자열이 메시지로 역직렬화되어 필드 값이 출력되는 것을 확인할 수 있다.

이처럼, Java에서 Protocol Buffers를 사용하여 메시지 필드의 필드 JSON 표현을 설정할 수 있다. Protocol Buffers는 데이터 표현의 효율성과 유연성을 제공하므로, 데이터 교환에 매우 유용한 도구이다.

## 참고 자료

- [Protocol Buffers 공식 문서](https://developers.google.com/protocol-buffers)
- [Protocol Buffers GitHub 저장소](https://github.com/protocolbuffers/protobuf)