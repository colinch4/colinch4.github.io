---
layout: post
title: "[java] Apache Commons Collections의 주요 디자인 패턴"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 자바 언어를 위한 강력한 라이브러리로, 다양한 컬렉션 데이터 구조를 제공합니다. 이 라이브러리는 다양한 디자인 패턴을 활용하여 구성되어 있습니다. 이 글에서는 Apache Commons Collections 라이브러리의 주요 디자인 패턴에 대해 소개하겠습니다.

## 1. Iterator 패턴

Iterator 패턴은 컬렉션에 저장된 요소를 순차적으로 접근하는 데 사용됩니다. Apache Commons Collections 라이브러리에서는 `IteratorUtils` 클래스를 통해 Iterator 패턴을 지원합니다. 이 클래스를 사용하면 다양한 컬렉션에서 Iterator를 가져오고, 요소를 순회하며 조작할 수 있습니다.

```java
List<String> myList = new ArrayList<>();
myList.add("Apple");
myList.add("Banana");
myList.add("Cherry");

Iterator<String> iterator = IteratorUtils.getIterator(myList);

while(iterator.hasNext()) {
    String element = iterator.next();
    System.out.println(element);
}
```

## 2. Decorator 패턴

Decorator 패턴은 기존 객체에 기능을 동적으로 추가하기 위한 패턴입니다. Apache Commons Collections에서는 Decorator 패턴을 활용하여 컬렉션에 다양한 기능을 추가할 수 있는 클래스를 제공합니다.

예를 들어, `PredicatedCollection` 클래스는 특정 조건을 만족하는 요소만 취급할 수 있는 컬렉션을 생성할 수 있게 해줍니다.

```java
Collection<String> myCollection = new ArrayList<>();
myCollection.add("Apple");
myCollection.add("Banana");
myCollection.add("Cherry");

Collection<String> predicatedCollection = PredicatedCollection.predicatedCollection(myCollection, new Predicate<String>() {
    public boolean evaluate(String element) {
        return element.length() > 5;
    }
});

System.out.println(predicatedCollection);
```

## 3. Factory 패턴

Factory 패턴은 객체 생성을 추상화하여 클라이언트가 객체 생성 로직에 대한 직접적인 의존성을 없애는 패턴입니다. Apache Commons Collections에서는 다양한 컬렉션 객체를 생성하기 위한 `CollectionUtils` 클래스를 제공합니다.

```java
List<String> myList = new ArrayList<>();
myList.add("Apple");
myList.add("Banana");
myList.add("Cherry");

Set<String> mySet = CollectionUtils.asSet(myList);

System.out.println(mySet);
```

위 예제에서는 `asSet` 메소드를 사용하여 List 객체를 Set 객체로 변환하였습니다.

## 4. Composite 패턴

Composite 패턴은 객체들을 트리 구조로 구성하여 개별 객체와 복합 객체들을 동일하게 다룰 수 있게 해주는 패턴입니다. Apache Commons Collections에서는 Composite 패턴을 활용한 `CompositeCollection` 클래스를 제공합니다.

```java
List<String> myList1 = new ArrayList<>();
myList1.add("Apple");
myList1.add("Banana");

List<String> myList2 = new ArrayList<>();
myList2.add("Cherry");
myList2.add("Durian");

CompositeCollection<String> compositeCollection = new CompositeCollection<>();
compositeCollection.addComposited(myList1);
compositeCollection.addComposited(myList2);

System.out.println(compositeCollection);
```

위 예제에서는 `CompositeCollection`을 사용하여 두 개의 List 객체를 하나로 묶은 컬렉션을 생성하였습니다.

이외에도 Apache Commons Collections에서는 다양한 디자인 패턴을 활용한 클래스와 메소드들을 제공하고 있습니다. 추가적인 패턴과 사용법은 공식 문서와 예제 코드를 참고하시기 바랍니다.

## 참고 자료
- [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)
- [Iterator 패턴](https://ko.wikipedia.org/wiki/Iterator_%ED%8C%A8%ED%84%B4)
- [Decorator 패턴](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0_%ED%8C%A8%ED%84%B4)
- [Factory 패턴](https://ko.wikipedia.org/wiki/%ED%8C%A8%ED%84%B4_%ED%8C%8C%ED%84%B4)
- [Composite 패턴](https://ko.wikipedia.org/wiki/%EC%BB%B4%ED%8F%AC%EC%8A%A4%ED%8C%8C%ED%84%B4)