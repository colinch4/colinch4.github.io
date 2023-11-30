---
layout: post
title: "[java] Apache Commons Collections의 다양한 데이터 타입 지원"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections에서 지원하는 다양한 데이터 타입에 대해 알아보겠습니다.

1. Lists (리스트): `List` 인터페이스를 구현한 클래스들은 데이터를 순서대로 저장하고 관리하는 기능을 제공합니다. `ArrayList`, `LinkedList`, `Stack`과 같은 클래스들을 사용할 수 있습니다. 이러한 클래스들은 데이터를 추가, 삭제, 조회 등 다양한 작업을 수행할 수 있는 메서드들을 제공합니다.

2. Sets (집합): `Set` 인터페이스를 구현한 클래스들은 중복되지 않은 요소들을 저장하고 관리하는 기능을 제공합니다. `HashSet`, `LinkedHashSet`, `TreeSet`과 같은 클래스들을 사용할 수 있습니다. 이러한 클래스들은 데이터의 중복 여부를 자동으로 체크하고 중복되지 않은 데이터만을 저장합니다.

3. Maps (맵): `Map` 인터페이스를 구현한 클래스들은 Key-Value 쌍으로 데이터를 저장하고 관리하는 기능을 제공합니다. `HashMap`, `LinkedHashMap`, `TreeMap`과 같은 클래스들을 사용할 수 있습니다. 이러한 클래스들은 Key를 통해 값을 조회하거나 추가하는 등의 작업을 수행할 수 있습니다.

4. Bags (가방): `Bag` 인터페이스를 구현한 클래스들은 데이터의 개수를 저장하고 관리하는 기능을 제공합니다. 데이터의 중복을 허용하며, 개수를 세는 용도로 사용될 수 있습니다.

5. Decorators (장식자): Apache Commons Collections은 장식자 패턴을 활용하여 더욱 유연하게 데이터를 다룰 수 있는 기능을 제공합니다. 예를 들어, `Synchronized`, `Unmodifiable`, `Predicated`와 같은 장식자 클래스들을 사용하여 컬렉션을 동기화하거나 수정 불가능하게 만들거나 특정 조건을 만족하는 값만을 저장할 수 있도록 할 수 있습니다.

Apache Commons Collections는 많은 유용한 클래스와 메서드를 제공하여 개발자들에게 강력한 도구를 제공합니다. 이를 활용하여 데이터 타입을 간편하게 다룰 수 있으며, 코드의 재사용성과 가독성을 높일 수 있습니다.

---
**참고 자료:**

- [Apache Commons Collections Documentation](https://commons.apache.org/proper/commons-collections/)
- [Apache Commons Collections API Documentation](https://commons.apache.org/proper/commons-collections/javadocs/api-release/)
- [Baeldung - Guide to Apache Commons Collections](https://www.baeldung.com/apache-commons-collections)