---
layout: post
title: "[java] Apache Commons Collections의 데이터 파싱과 시리얼라이제이션"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 자바의 데이터 구조와 컬렉션을 다루는 라이브러리로서 많은 유용한 기능을 제공합니다. 이번 블로그 포스트에서는 Apache Commons Collections를 사용하여 데이터 파싱과 시리얼라이제이션을 어떻게 수행하는지 알아보겠습니다.

## 1. 데이터 파싱

Apache Commons Collections는 다양한 형식의 데이터를 파싱하는 기능을 제공합니다. 예를 들어, CSV(Comma-Separated Values) 형식의 데이터를 파싱하는 기능을 사용하려면 다음과 같이 코드를 작성할 수 있습니다.

```java
import org.apache.commons.collections4.CSVParser;
import org.apache.commons.collections4.CSVParserBuilder;
import org.apache.commons.collections4.CSVRecord;

import java.io.FileReader;
import java.io.IOException;

public class DataParsingExample {

    public static void main(String[] args) {
        try (FileReader reader = new FileReader("data.csv")) {
            CSVParser parser = new CSVParserBuilder().build();
            Iterable<CSVRecord> records = parser.parse(reader);

            for (CSVRecord record : records) {
                String name = record.get(0);
                int age = Integer.parseInt(record.get(1));
                System.out.println("Name: " + name + ", Age: " + age);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

위의 코드는 "data.csv" 파일에서 CSV 형식의 데이터를 파싱하고 각 record의 첫 번째 열을 `name` 변수에 할당하고 두 번째 열을 `age` 변수에 할당하는 예제입니다. 실제로는 데이터를 원하는 대로 처리하면 됩니다.

## 2. 시리얼라이제이션

Apache Commons Collections는 자바의 시리얼라이제이션(Serialization)을 보다 쉽게 수행할 수 있도록 도와줍니다. 예를 들어, 객체를 직렬화하고 파일에 저장하려면 다음과 같이 코드를 작성할 수 있습니다.

```java
import org.apache.commons.collections4.SerializationUtils;

import java.io.*;

public class SerializationExample {

    public static void main(String[] args) {
        // 객체 생성
        Person person = new Person("John Doe", 25);

        // 객체를 바이트 배열로 직렬화
        byte[] serializedData = SerializationUtils.serialize(person);

        try (FileOutputStream fileOut = new FileOutputStream("person.ser")) {
            fileOut.write(serializedData);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 파일에서 직렬화된 데이터를 읽고 객체로 복원
        try (FileInputStream fileIn = new FileInputStream("person.ser")) {
            byte[] serializedData = fileIn.readAllBytes();
            Person deserializedPerson = SerializationUtils.deserialize(serializedData);
            System.out.println("Name: " + deserializedPerson.getName() + ", Age: " + deserializedPerson.getAge());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static class Person implements Serializable {
        private String name;
        private int age;

        // 생성자, getter, setter 등 생략

        // ...
    }
}
```

위의 코드는 `Person` 클래스를 직렬화하여 `person.ser` 파일에 저장하고, 이 파일에서 데이터를 읽어와 객체로 복원하는 예제입니다. `Person` 클래스는 `Serializable` 인터페이스를 구현하고 있어 직렬화가 가능하도록 되어 있습니다.

## 결론

Apache Commons Collections는 데이터 파싱과 시리얼라이제이션을 보다 쉽고 편리하게 수행할 수 있는 도구를 제공합니다. 위의 예제 코드를 참고하여 프로젝트에 필요한 기능을 활용해보세요.

## 참고 자료

- [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)
- [Apache Commons Collections GitHub 저장소](https://github.com/apache/commons-collections)