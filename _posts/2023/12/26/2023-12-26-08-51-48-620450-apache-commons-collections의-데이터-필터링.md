---
layout: post
title: "[java] Apache Commons Collections의 데이터 필터링"
description: " "
date: 2023-12-26
tags: [java]
comments: true
share: true
---

Apache Commons Collections 라이브러리는 자바 언어로 데이터 구조 및 컬렉션을 다루는 데 도움을 주는 라이브러리입니다. 이 라이브러리는 컬렉션 데이터를 필터링하고 조작하는 데 편리한 유틸리티들을 제공합니다. 이번 게시물에서는 Apache Commons Collections를 사용하여 자바에서 데이터를 필터링하는 방법에 대해 알아보겠습니다.

## Apache Commons Collections 라이브러리 추가하기
먼저 Maven 또는 Gradle과 같은 의존성 관리 도구를 사용하여 Apache Commons Collections 라이브러리를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, 아래와 같이 의존성을 추가할 수 있습니다.
```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-collections4</artifactId>
    <version>4.4</version>
</dependency>
```
Gradle을 사용하는 경우 아래와 같이 의존성을 추가할 수 있습니다.
```gradle
implementation 'org.apache.commons:commons-collections4:4.4'
```

## 데이터 필터링 예제
이제 Apache Commons Collections를 사용하여 데이터를 필터링해보겠습니다. 예제로 사용할 Student 클래스는 다음과 같습니다.
```java
public class Student {
    private String name;
    private int age;

    // Constructor, getters, and setters
}
```

아래 코드는 Apache Commons Collections를 사용하여 Student 객체의 리스트를 나이가 20 이상인 학생들로 필터링하는 예제입니다.

```java
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.collections4.Predicate;

// Student 객체를 담은 리스트 생성
List<Student> students = new ArrayList<>();
students.add(new Student("John", 25));
students.add(new Student("Jane", 18));
students.add(new Student("Dave", 22));

// Predicate 정의
Predicate agePredicate = new Predicate() {
    @Override
    public boolean evaluate(Object object) {
        Student student = (Student) object;
        return student.getAge() >= 20;
    }
};

// 필터링 수행
Collection filteredStudents = CollectionUtils.select(students, agePredicate);

// 결과 출력
for (Object student : filteredStudents) {
    System.out.println(student.getName() + " - " + student.getAge());
}
```

위의 예제는 Apache Commons Collections의 `Predicate` 인터페이스를 구현하여 나이가 20 이상인 학생들을 필터링한 후 결과를 출력하는 방법을 보여줍니다.

## 결론
Apache Commons Collections를 사용하면 필터링, 변환, 맵핑 등 다양한 작업을 손쉽게 수행할 수 있습니다. 이는 자바에서 컬렉션 데이터를 다룰 때 유용한 라이브러리 중 하나입니다.

이를 통해 Apache Commons Collections를 이용하여 데이터를 필터링하는 방법에 대해 알아보았습니다. 이 라이브러리를 사용하면 데이터 처리 작업을 보다 쉽고 간편하게 수행할 수 있습니다.

[Apache Commons Collections](https://commons.apache.org/proper/commons-collections/)에서 라이브러리의 자세한 정보를 확인할 수 있습니다.

다음으로는 Apache Commons Collections의 더 많은 유틸리티 기능에 대해 알아보도록 하겠습니다.