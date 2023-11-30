---
layout: post
title: "[java] Apache Commons Collections의 다양한 데이터 구조"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 자바 애플리케이션에서 다양한 데이터 구조를 쉽게 다루기 위한 유용한 라이브러리입니다. 이 라이브러리는 다양한 컬렉션, 맵, 리스트, 세트 등을 제공하여 데이터를 보다 효율적으로 관리할 수 있도록 도와줍니다.

## ArrayList

ArrayList는 가변 크기의 배열을 구현한 클래스로, List 인터페이스를 구현합니다. ArrayList는 동적으로 크기를 조절할 수 있으며, 내부적으로 배열을 사용하여 요소를 저장합니다. 

다음은 ArrayList를 사용하는 예제 코드입니다.

```java
import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();
        
        // 요소 추가
        fruits.add("사과");
        fruits.add("바나나");
        fruits.add("딸기");
        
        // 요소 접근
        System.out.println(fruits.get(0)); // 사과
        
        // 요소 삭제
        fruits.remove("바나나");
        
        // 요소 개수
        System.out.println(fruits.size()); // 2
    }
}
```

## HashMap

HashMap은 키-값 쌍으로 데이터를 저장하며, 맵의 구현체입니다. HashMap은 해시 테이블을 사용하여 데이터를 저장하므로, 데이터를 빠르게 검색할 수 있습니다.

다음은 HashMap을 사용하는 예제 코드입니다.

```java
import java.util.HashMap;

public class HashMapExample {
    public static void main(String[] args) {
        HashMap<String, Integer> ages = new HashMap<>();
        
        // 요소 추가
        ages.put("John", 25);
        ages.put("Emily", 30);
        ages.put("Michael", 35);
        
        // 요소 접근
        System.out.println(ages.get("John")); // 25
        
        // 요소 삭제
        ages.remove("Emily");
        
        // 요소 개수
        System.out.println(ages.size()); // 2
    }
}
```

## HashSet

HashSet은 중복을 허용하지 않는 데이터 집합을 구현한 클래스입니다. HashSet은 해시 테이블을 사용하여 요소의 존재 여부를 빠르게 확인할 수 있습니다.

다음은 HashSet을 사용하는 예제 코드입니다.

```java
import java.util.HashSet;

public class HashSetExample {
    public static void main(String[] args) {
        HashSet<String> cities = new HashSet<>();
        
        // 요소 추가
        cities.add("서울");
        cities.add("도쿄");
        cities.add("파리");
        
        // 요소 접근
        for (String city : cities) {
            System.out.println(city);
        }
        
        // 요소 삭제
        cities.remove("도쿄");
        
        // 요소 개수
        System.out.println(cities.size()); // 2
    }
}
```

## 참고 자료

- [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)
- [Java API 문서 - ArrayList](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/ArrayList.html)
- [Java API 문서 - HashMap](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/HashMap.html)
- [Java API 문서 - HashSet](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/HashSet.html)

Apache Commons Collections는 다양한 데이터 구조를 제공하여 자바 애플리케이션의 개발과 관리를 좀 더 편리하게 해줍니다. 위의 설명과 예제 코드를 통해, 이 라이브러리를 활용하여 데이터를 효과적으로 다룰 수 있는 방법을 알아보았습니다.