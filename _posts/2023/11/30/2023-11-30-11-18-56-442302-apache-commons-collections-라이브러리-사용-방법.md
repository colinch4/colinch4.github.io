---
layout: post
title: "[java] Apache Commons Collections 라이브러리 사용 방법"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 자바 개발에 자주 사용되는 공용 컬렉션 클래스를 제공하는 라이브러리입니다. 이 라이브러리는 JDK에서 제공하는 컬렉션 클래스보다 더 다양한 기능을 제공하여 개발자들이 더 효율적으로 작업할 수 있도록 도와줍니다. 이번 글에서는 Apache Commons Collections 라이브러리의 사용 방법에 대해 알아보겠습니다.

## 1. Apache Commons Collections 라이브러리 추가

먼저, 프로젝트에 Apache Commons Collections 라이브러리를 추가해야 합니다. Maven을 사용하는 경우, 프로젝트의 `pom.xml` 파일에 다음 의존성을 추가합니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.commons</groupId>
        <artifactId>commons-collections4</artifactId>
        <version>4.4</version>
    </dependency>
</dependencies>
```

Gradle을 사용하는 경우, 프로젝트의 `build.gradle` 파일에 다음 의존성을 추가합니다.

```groovy
dependencies {
    implementation 'org.apache.commons:commons-collections4:4.4'
}
```

의존성을 추가한 후에는 빌드 도구를 사용하여 라이브러리를 다운로드하고 프로젝트에 추가합니다.

## 2. Apache Commons Collections 라이브러리 사용

Apache Commons Collections 라이브러리에서 제공하는 다양한 기능을 사용해보겠습니다.

### 2.1. 컬렉션의 크기 확인

Apache Commons Collections를 사용하여 컬렉션의 크기를 확인하는 예제 코드는 다음과 같습니다.

```java
import org.apache.commons.collections4.CollectionUtils;

public class CollectionSizeExample {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Orange");
        list.add("Banana");

        System.out.println("List size: " + CollectionUtils.size(list));
    }
}
```

### 2.2. 컬렉션의 원소 삭제

Apache Commons Collections를 사용하여 컬렉션에서 특정 원소를 삭제하는 예제 코드는 다음과 같습니다.

```java
import org.apache.commons.collections4.CollectionUtils;

public class CollectionRemoveExample {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Orange");
        list.add("Banana");

        System.out.println("Before removing: " + list);
        CollectionUtils.removeIf(list, "Orange"::equals);
        System.out.println("After removing: " + list);
    }
}
```

## 3. 참고 자료

- [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)
- [Apache Commons Collections GitHub 저장소](https://github.com/apache/commons-collections)

이상으로 Apache Commons Collections 라이브러리 사용 방법에 대해 알아보았습니다. 이 라이브러리를 적절하게 활용하여 개발 작업을 보다 효율적으로 수행할 수 있습니다.