---
layout: post
title: "[java] Apache Commons Collections의 데이터 이동"
description: " "
date: 2023-12-26
tags: [java]
comments: true
share: true
---

Java 개발을 하다 보면 데이터를 컬렉션에서 다른 컬렉션으로 효과적으로 이동해야 하는 경우가 많이 있습니다. 이러한 작업을 손쉽게 처리하기 위해 Apache Commons Collections 라이브러리를 사용할 수 있습니다. 이 라이브러리는 다양한 유용한 메서드와 유틸리티 클래스를 제공하여 데이터 이동을 간편하게 해줍니다.

## 컬렉션에서 컬렉션으로 데이터 이동하기

Apache Commons Collections를 사용하여 컬렉션에서 컬렉션으로 데이터를 이동하는 방법은 매우 간단합니다. 우선 다음과 같이 Maven을 사용하여 Apache Commons Collections 라이브러리를 프로젝트에 추가합니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-collections4</artifactId>
    <version>4.4</version>
</dependency>
```

라이브러리를 추가한 후에는 다음과 같이 데이터를 이동할 수 있습니다.

```java
import org.apache.commons.collections4.CollectionUtils;

List<String> sourceList = new ArrayList<>();
sourceList.add("A");
sourceList.add("B");
sourceList.add("C");

List<String> destinationList = new ArrayList<>();
destinationList.add("D");
destinationList.add("E");

CollectionUtils.addAll(destinationList, sourceList);

System.out.println(destinationList); // 출력: [D, E, A, B, C]
```

위의 예제에서는 `CollectionUtils.addAll` 메서드를 사용하여 소스 리스트에 있는 데이터를 대상 리스트로 이동시켰습니다.

Apache Commons Collections를 사용하면 데이터 이동과 같은 작업을 더욱 편리하게 처리할 수 있으며, 반복적인 코드를 줄일 수 있습니다.

## 결론

Apache Commons Collections를 사용하여 데이터를 효과적으로 이동하는 방법을 알아보았습니다. 이를 통해 더욱 간편하고 효율적으로 데이터 이동 작업을 수행할 수 있게 되었습니다.

더 많은 세부적인 기능과 메서드에 대해서는 [Apache Commons Collections 문서](https://commons.apache.org/proper/commons-collections/)를 참고하시기 바랍니다.