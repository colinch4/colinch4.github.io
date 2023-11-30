---
layout: post
title: "[java] Apache Commons Collections와 관련된 디자인 패턴과 아키텍처"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 많은 유용한 컬렉션 유틸리티를 제공하는 오픈 소스 라이브러리입니다. 이 라이브러리는 자바 언어의 컬렉션 프레임워크를 보완하고 확장하여 다양한 유형의 컬렉션을 더 쉽게 다룰 수 있게 해줍니다.

이 글에서는 Apache Commons Collections의 디자인 패턴과 아키텍처에 대해 살펴보겠습니다.

## 1. Singleton 패턴

Singleton 패턴은 오직 하나의 인스턴스만을 생성하고, 어디서든 이 인스턴스에 접근할 수 있도록 해주는 패턴입니다. Apache Commons Collections에서는 이 패턴을 활용하여 SingletonCollection이라는 클래스를 제공합니다. 이 클래스는 오직 하나의 요소만을 가지는 컬렉션을 생성하고 사용할 수 있도록 해줍니다.

```java
SingletonCollection<String> collection = SingletonCollection.singleton("Hello");
```

## 2. Factory 메서드 패턴

Factory 메서드 패턴은 객체를 생성하는 공통 인터페이스를 정의하고, 이를 상속받는 구체적인 클래스에서 객체를 생성하는 패턴입니다. Apache Commons Collections에서는 여러 개의 팩토리 메서드 패턴을 사용하여 컬렉션을 생성하고 초기화할 수 있도록 해줍니다. 예를 들어, ListUtils 클래스는 다양한 방법으로 List를 생성하고 조작하는 메서드를 제공합니다.

```java
List<String> list = ListUtils.union(list1, list2);
```

## 3. 데코레이터 패턴

데코레이터 패턴은 기본 객체의 기능에 추가적인 기능을 동적으로 덧붙일 수 있게 해주는 패턴입니다. Apache Commons Collections에서는 데코레이터 패턴을 활용하여 컬렉션에 여러 종류의 데코레이터를 적용할 수 있습니다. 예를 들어, CollectionUtils 클래스는 컬렉션의 변환, 필터링, 정렬 등 다양한 기능을 제공하는 데코레이터 메서드를 제공합니다.

```java
Collection<Integer> transformedCollection = CollectionUtils.collect(collection, transformer);
```

## 4. 메멘토 패턴

메멘토 패턴은 객체의 상태를 저장하고 복원할 수 있는 기능을 제공하는 패턴입니다. Apache Commons Collections에서는 메멘토 패턴을 활용하여 컬렉션의 상태를 저장하고 복원할 수 있도록 해줍니다. 예를 들어, ListUtils 클래스는 List 상태를 저장하고 복원하기 위한 메서드를 제공합니다.

```java
ListMemento<String> memento = ListUtils.getState(list);
List<String> restoredList = ListUtils.restoreState(memento);
```


이제 Apache Commons Collections의 디자인 패턴과 아키텍처에 대해 알아보았습니다. 이러한 패턴과 아키텍처를 적절히 활용하면 컬렉션을 보다 효율적으로 다룰 수 있습니다. Apache Commons Collections는 이러한 패턴과 아키텍처를 활용하여 유연하고 강력한 컬렉션 유틸리티를 제공하므로, 개발자들은 이를 활용하여 자신의 프로젝트를 더욱 효율적으로 구현할 수 있습니다.

더 자세한 내용은 [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)를 참고하시기 바랍니다.