---
layout: post
title: "[java] Java Apache Commons Collections와 Spring Framework 통합 방법"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 Java 언어의 기본 컬렉션 프레임워크의 기능을 확장하고 보완하기 위한 유용한 도구 모음입니다. Spring Framework는 엔터프라이즈급 자바 애플리케이션을 개발하기 위한 유연한 프레임워크로, 컬렉션 데이터를 다루기 위한 다양한 기능을 제공합니다. 이번 블로그에서는 Apache Commons Collections와 Spring Framework를 결합하여 사용하는 방법에 대해 알아보겠습니다.

## 1. Apache Commons Collections 라이브러리 추가

먼저, Apache Commons Collections 라이브러리를 프로젝트에 추가해야 합니다. 아래의 Maven 종속성을 프로젝트 `pom.xml` 파일 내에 추가합니다.

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-collections4</artifactId>
    <version>4.4</version>
</dependency>
```

라이브러리를 다운로드하고 프로젝트에 추가한 후, Apache Commons Collections의 다양한 기능을 사용할 수 있게 됩니다.

## 2. Spring Framework와 Apache Commons Collections 사용

Apache Commons Collections와 Spring Framework를 함께 사용하여 데이터를 다루는 방법은 다양합니다. 몇 가지 일반적인 사용 사례를 살펴보겠습니다.

### 2.1. 컬렉션 변환

Apache Commons Collections는 `CollectionUtils` 클래스를 통해 다른 컬렉션 유형 간의 변환을 쉽게 할 수 있도록 지원합니다. Spring Framework에서는 이러한 변환 작업을 더욱 간편하게 처리하기 위해 `CollectionUtils`를 사용하는 `SpringUtils` 클래스를 제공합니다. 예를 들어, List를 Set으로 변환하려면 다음과 같이 코드를 작성할 수 있습니다.

```java
import org.apache.commons.collections4.CollectionUtils;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class SpringUtils {

    public static <T> Set<T> convertListToSet(List<T> list) {
        return new HashSet<>(CollectionUtils.emptyIfNull(list));
    }

    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Orange");
        list.add("Banana");

        Set<String> set = convertListToSet(list);
        System.out.println(set);
    }
}
```

### 2.2. 필터링과 변환

Spring Framework의 `StreamUtils` 클래스와 Apache Commons Collections의 `PredicateUtils` 클래스는 데이터를 필터링하고 변환하는 데 사용될 수 있습니다. 예를 들어, List에서 홀수를 필터링하고 각 숫자를 제곱한 결과를 가져오려면 다음과 같이 코드를 작성할 수 있습니다.

```java
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.collections4.PredicateUtils;

import java.util.ArrayList;
import java.util.List;

public class SpringUtils {

    public static <T> List<T> filterAndTransformList(List<T> list) {
        return CollectionUtils.collect(
                CollectionUtils.select(list, PredicateUtils.instanceofPredicate(Integer.class)),
                obj -> {
                    Integer num = (Integer) obj;
                    return num * num;
                });
    }

    public static void main(String[] args) {
        List<Object> list = new ArrayList<>();
        list.add(1);
        list.add("Apple");
        list.add(3);
        list.add("Orange");
        list.add(5);
        list.add("Banana");

        List<Integer> result = filterAndTransformList(list);
        System.out.println(result);
    }
}
```

## 결론

Apache Commons Collections와 Spring Framework를 함께 사용하면 Java 애플리케이션에서 컬렉션 데이터를 더욱 효과적으로 다룰 수 있습니다. 이 블로그에서는 라이브러리 추가와 기본적인 사용 방법에 대해 알아보았으며, 실제 프로젝트에 적용하여 다양한 기능을 활용해보시기 바랍니다. 자세한 내용은 Apache Commons Collections [공식 문서](https://commons.apache.org/proper/commons-collections/)와 Spring Framework [공식 문서](https://spring.io/)를 참조하시기 바랍니다.