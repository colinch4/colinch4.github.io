---
layout: post
title: "[java] Apache Commons Collections의 사용자 정의 컬렉션 클래스"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 자바에서 컬렉션을 다루는 데 유용한 기능을 제공하는 라이브러리입니다. 이 라이브러리를 사용하면 기존 자바 컬렉션 인터페이스의 한계를 극복하고, 더 풍부한 기능을 가진 컬렉션을 만들 수 있습니다. 이번 글에서는 Apache Commons Collections를 사용하여 사용자 정의 컬렉션 클래스를 작성하는 방법에 대해 알아보겠습니다.

## Apache Commons Collections 추가하기

먼저, Apache Commons Collections를 사용하기 위해서는 해당 라이브러리를 프로젝트에 추가해야 합니다. Maven과 같은 의존성 관리 도구를 사용하고 있다면, `pom.xml` 파일에 다음과 같은 의존성을 추가합니다:

```
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-collections4</artifactId>
    <version>4.4</version>
</dependency>
```

의존성을 추가한 후에는 라이브러리를 import하여 사용할 수 있습니다.

## 사용자 정의 컬렉션 클래스 작성하기

Apache Commons Collections를 사용하여 사용자 정의 컬렉션 클래스를 작성하는 것은 간단합니다. 컬렉션 클래스를 작성할 때는 `AbstractCollectionDecorator` 클래스를 상속받아야 합니다.

```java
import org.apache.commons.collections4.collection.AbstractCollectionDecorator;

public class CustomCollection<T> extends AbstractCollectionDecorator<T> {

    public CustomCollection(Collection<T> decorated) {
        super(decorated);
    }

    // 사용자 정의 메소드 및 로직 작성
}
```

`AbstractCollectionDecorator` 클래스는 컬렉션의 기능을 확장하고, 컬렉션 메소드에 대한 구현을 담당합니다. `CustomCollection` 클래스는 `Collection` 인터페이스를 구현하지 않았지만, `AbstractCollectionDecorator` 클래스의 상속을 통해 `Collection` 인터페이스의 모든 메소드를 사용할 수 있습니다.

여기서는 `CustomCollection` 클래스에 사용자 정의 메소드 및 로직을 추가할 수 있습니다. 예를 들어, 원소를 특정 조건에 따라 필터링하거나, 특정 연산을 수행하는 메소드를 추가할 수 있습니다.

## 사용자 정의 컬렉션 클래스 사용하기

사용자 정의 컬렉션 클래스를 사용하는 방법은 일반적인 자바 컬렉션과 동일합니다. 다음은 사용자 정의 컬렉션 클래스 `CustomCollection`을 사용하는 예시 코드입니다:

```java
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("apple");
        list.add("banana");
        list.add("grape");

        CustomCollection<String> customCollection = new CustomCollection<>(list);
        System.out.println(customCollection.size()); // 출력: 3

        customCollection.add("orange");
        System.out.println(customCollection.size()); // 출력: 4

        customCollection.remove("banana");
        System.out.println(customCollection.size()); // 출력: 3
    }
}
```

위의 코드에서는 일반적인 `ArrayList`를 생성한 후, 이를 `CustomCollection`의 인스턴스로 감싸서 사용하고 있습니다. `CustomCollection`은 `ArrayList`의 메소드를 모두 사용할 수 있으며, 필요한 경우 추가적인 사용자 정의 메소드를 호출할 수도 있습니다.

## 결론

Apache Commons Collections를 사용하여 사용자 정의 컬렉션 클래스를 작성하는 방법을 알아보았습니다. 이를 통해 자바의 컬렉션을 보다 유연하게 다룰 수 있으며, 더 많은 기능을 추가하여 효율적인 코드를 작성할 수 있습니다.