---
layout: post
title: "[java] Apache Commons Collections의 데이터 검색 기능"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 자바 언어로 작성된 오픈 소스 라이브러리로서, 다양한 유용한 컬렉션 클래스와 유틸리티를 제공합니다. 이 라이브러리는 다양한 상황에서 데이터를 검색하는 기능을 제공하기 때문에, 개발자들에게 매우 편리합니다.

이번 포스트에서는 Apache Commons Collections의 데이터 검색 기능을 간략히 알아보고, 몇 가지 예제 코드를 통해 실제 활용 방법을 살펴보겠습니다.

## CollectionsUtils 클래스의 검색 기능

Apache Commons Collections는 CollectionsUtils 클래스를 통해 다양한 검색 기능을 제공합니다. 이 클래스를 활용하여 컬렉션 내에서 원하는 데이터를 검색할 수 있습니다.

1. **find** 메서드: 컬렉션 내에서 조건에 맞는 첫 번째 요소를 검색합니다.

```java
Person foundPerson = (Person) CollectionUtils.find(personList, new Predicate() {
    @Override
    public boolean evaluate(Object object) {
        Person person = (Person) object;
        return person.getName().equals("John");
    }
});

System.out.println("Found person: " + foundPerson.getName());
```

2. **select** 메서드: 컬렉션 내에서 조건에 맞는 모든 요소를 검색하여 새로운 컬렉션에 저장합니다.

```java
List<Person> foundPersons = CollectionUtils.select(personList, new Predicate() {
    @Override
    public boolean evaluate(Object object) {
        Person person = (Person) object;
        return person.getAge() > 30;
    }
});

for (Person person : foundPersons) {
    System.out.println("Found person: " + person.getName());
}
```

## 예제 코드

다음은 Apache Commons Collections를 사용하여 데이터를 검색하는 예제 코드입니다.

```java
import org.apache.commons.collections.CollectionUtils;
import org.apache.commons.collections.Predicate;

import java.util.ArrayList;
import java.util.List;

public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public static void main(String[] args) {
        List<Person> personList = new ArrayList<>();
        personList.add(new Person("John", 25));
        personList.add(new Person("Mike", 35));
        personList.add(new Person("Sarah", 30));

        Person foundPerson = (Person) CollectionUtils.find(personList, new Predicate() {
            @Override
            public boolean evaluate(Object object) {
                Person person = (Person) object;
                return person.getName().equals("John");
            }
        });

        System.out.println("Found person: " + foundPerson.getName());

        List<Person> foundPersons = CollectionUtils.select(personList, new Predicate() {
            @Override
            public boolean evaluate(Object object) {
                Person person = (Person) object;
                return person.getAge() > 30;
            }
        });

        for (Person person : foundPersons) {
            System.out.println("Found person: " + person.getName());
        }
    }
}
```

## 결론

Apache Commons Collections는 데이터 검색을 위한 다양한 기능과 유틸리티를 제공하여 개발자들에게 많은 편의성을 제공합니다. 이를 통해 코드를 간결하게 유지하고, 더 효율적으로 데이터를 검색할 수 있습니다.

더 자세한 내용은 [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)를 참고하시기 바랍니다.