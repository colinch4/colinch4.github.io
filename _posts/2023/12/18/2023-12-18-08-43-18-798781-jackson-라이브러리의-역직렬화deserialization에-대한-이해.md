---
layout: post
title: "[java] Jackson 라이브러리의 역직렬화(Deserialization)에 대한 이해"
description: " "
date: 2023-12-18
tags: [java]
comments: true
share: true
---

Jackson 라이브러리는 자바에서 JSON 데이터를 다루는 강력한 도구로 널리 사용됩니다. 이 라이브러리를 사용하여 JSON 데이터를 자바 객체로 변환하는 과정을 **역직렬화(Deserialization)**라고 합니다. 이번 포스팅에서는 Jackson 라이브러리의 역직렬화에 대해 자세히 알아보도록 하겠습니다.

## 1. Jackson 라이브러리 설정

먼저, Jackson 라이브러리를 Maven 또는 Gradle과 같은 빌드 도구를 이용하여 프로젝트에 추가합니다. Maven을 사용한다면 다음과 같이 `pom.xml` 파일에 의존성을 추가합니다.

```xml
<dependencies>
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
        <version>2.12.3</version>
    </dependency>
</dependencies>
```

## 2. 간단한 역직렬화 예제

다음은 Jackson 라이브러리를 사용하여 JSON 데이터를 자바 객체로 역직렬화하는 간단한 예제입니다. 

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class DeserializationExample {
    public static void main(String[] args) {
        String json = "{\"name\":\"John\", \"age\":30}";
        
        try {
            ObjectMapper mapper = new ObjectMapper();
            Person person = mapper.readValue(json, Person.class);
            
            System.out.println(person.getName());   // John
            System.out.println(person.getAge());    // 30
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

위 예제에서 `ObjectMapper` 클래스는 JSON 데이터를 자바 객체로 변환해주는 핵심적인 역할을 담당합니다.

## 3. Jackson Annotation 활용

Jackson 라이브러리는 역직렬화를 위한 다양한 **Annotation**을 제공합니다. 이를 활용하여 JSON 데이터의 필드명과 자바 클래스의 필드를 매핑하거나, 필드를 무시하는 등의 작업을 할 수 있습니다.

```java
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Person {
    @JsonProperty("name")
    private String fullName;
    private int age;
  
    // Getters and Setters
    // ...
}
```

위의 예제에서 `@JsonProperty` 어노테이션을 사용하여 JSON 데이터의 `name` 필드를 자바 클래스의 `fullName` 필드에 매핑했고, `@JsonIgnoreProperties` 어노테이션은 알 수 없는 속성을 무시하도록 설정했습니다.

## 4. 결론

이렇게 Jackson 라이브러리를 사용하여 JSON 데이터를 자바 객체로 역직렬화하는 방법에 대해 간략하게 살펴보았습니다. Jackson은 강력한 기능과 다양한 옵션을 제공하므로, 다양한 형태의 JSON 데이터를 처리하는데 유용하게 활용될 수 있습니다.

더 많은 자세한 내용은 [Jackson 공식 문서](https://github.com/FasterXML/jackson-databind)를 참고하시기 바랍니다.