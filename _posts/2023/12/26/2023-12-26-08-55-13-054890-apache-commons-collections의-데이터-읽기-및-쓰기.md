---
layout: post
title: "[java] Apache Commons Collections의 데이터 읽기 및 쓰기"
description: " "
date: 2023-12-26
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 Java 개발자들이 컬렉션과 데이터 구조를 다루는 데 유용한 많은 기능을 제공합니다. 이 라이브러리를 사용하여 데이터를 효과적으로 읽고 쓰는 방법을 살펴보겠습니다.

## 데이터 읽기

Apache Commons Collections의 CollectionUtils 클래스에는 데이터를 읽는 데 사용할 수 있는 다양한 메서드가 있습니다. 그 중에서도 **get(Object, int)** 메서드는 List나 배열에서 특정 인덱스의 값을 가져오는 데 유용합니다.

```java
List<String> list = new ArrayList<>();
list.add("apple");
list.add("banana");
String secondElement = (String) CollectionUtils.get(list, 1);
```

위의 예제에서는 List에서 두 번째 요소를 얻기 위해 CollectionUtils.get() 메서드를 사용하였습니다.

## 데이터 쓰기

Apache Commons Collections의 CollectionUtils 클래스에는 데이터를 쓰는 데 사용할 수 있는 여러 메서드도 포함되어 있습니다. **addIgnoreNull(Collection, Object)** 메서드를 사용하면 null이 아닌 요소를 추가할 수 있습니다.

```java
List<String> list = new ArrayList<>();
CollectionUtils.addIgnoreNull(list, "apple");
CollectionUtils.addIgnoreNull(list, null);
```

위의 예제에서는 addIgnoreNull() 메서드를 사용하여 null이 아닌 "apple" 요소를 list에 추가하였습니다.

Apache Commons Collections를 사용하여 데이터를 효율적으로 읽고 쓰는 방법을 살펴 보았습니다. 추가적으로 라이브러리의 다른 유용한 기능들을 알고 싶다면 [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)를 참고해보세요.

---
**참고 문헌:**
- [Apache Commons Collections 공식 문서](https://commons.apache.org/proper/commons-collections/)