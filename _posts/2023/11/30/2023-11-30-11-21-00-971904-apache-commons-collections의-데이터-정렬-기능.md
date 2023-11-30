---
layout: post
title: "[java] Apache Commons Collections의 데이터 정렬 기능"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 Java 언어로 개발된 데이터 정렬 기능을 제공하는 라이브러리입니다. 이 라이브러리는 다양한 데이터 구조와 알고리즘을 제공하여 개발자가 효율적으로 데이터를 정렬할 수 있도록 도와줍니다.

## Apache Commons Collections 설치하기
Apache Commons Collections를 사용하기 위해서는 먼저 해당 라이브러리를 설치해야 합니다. Maven 프로젝트의 경우, pom.xml 파일에 다음과 같이 의존성을 추가합니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-collections4</artifactId>
    <version>4.4</version>
</dependency>
```

Gradle 프로젝트의 경우, build.gradle 파일에 다음과 같이 의존성을 추가합니다.

```groovy
implementation 'org.apache.commons:commons-collections4:4.4'
```

## 데이터 정렬하기
Apache Commons Collections를 이용하여 데이터를 정렬하는 방법은 매우 간단합니다. 먼저, 정렬하고자 하는 데이터를 기본적인 Java Collection에 담습니다. 그리고 `org.apache.commons.collections4.CollectionUtils` 클래스의 `sort` 메서드를 사용하여 데이터를 정렬합니다.

다음은 Integer 타입의 리스트를 오름차순으로 정렬하는 예제 코드입니다.

```java
import org.apache.commons.collections4.CollectionUtils;

List<Integer> numbers = new ArrayList<>();
numbers.add(4);
numbers.add(2);
numbers.add(3);
numbers.add(1);

CollectionUtils.sort(numbers);

System.out.println(numbers); // [1, 2, 3, 4]
```

위의 예제 코드에서 `CollectionUtils.sort` 메서드를 호출하여 리스트 `numbers`를 오름차순으로 정렬하였습니다. 정렬된 결과는 `[1, 2, 3, 4]`로 출력됩니다.

## 정렬 기준 변경하기
Apache Commons Collections를 이용하여 데이터를 정렬할 때는 정렬 기준을 변경할 수 있습니다. 기본적으로는 데이터의 natural order를 따르지만, 사용자가 직접 정의한 Comparator를 이용하여 정렬 기준을 변경할 수도 있습니다.

다음은 String 타입의 리스트를 길이에 따라 오름차순으로 정렬하는 예제 코드입니다.

```java
import org.apache.commons.collections4.ComparatorUtils;
import org.apache.commons.collections4.CollectionUtils;

List<String> words = new ArrayList<>();
words.add("apple");
words.add("banana");
words.add("cat");
words.add("dog");

Comparator<String> lengthComparator = ComparatorUtils.naturalComparator();
CollectionUtils.sort(words, lengthComparator);

System.out.println(words); // [cat, dog, apple, banana]
```

위의 예제 코드에서는 `ComparatorUtils.naturalComparator()`를 이용하여 natural order 기준의 Comparator를 생성하고, `CollectionUtils.sort` 메서드의 두 번째 인자로 해당 Comparator를 전달하여 길이에 따라 정렬하였습니다. 정렬된 결과는 `[cat, dog, apple, banana]`로 출력됩니다.

## 정리
Apache Commons Collections는 Java 개발자가 데이터를 효율적으로 정렬할 수 있도록 도와주는 유용한 라이브러리입니다. 해당 라이브러리를 사용하여 데이터 정렬을 간단하게 처리할 수 있으며, 정렬 기준을 변경하는 경우에도 유연하게 대응할 수 있습니다.

## 참고 자료
- [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)
- [Apache Commons Collections GitHub 저장소](https://github.com/apache/commons-collections)