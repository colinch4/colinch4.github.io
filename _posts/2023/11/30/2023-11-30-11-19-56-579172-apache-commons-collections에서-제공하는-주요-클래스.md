---
layout: post
title: "[java] Apache Commons Collections에서 제공하는 주요 클래스"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Apache Commons Collections는 유용한 데이터 구조와 알고리즘을 제공하는 자바 라이브러리입니다. 이 라이브러리는 자바 컬렉션 프레임워크의 기능을 확장하고, 개발자가 다양한 작업을 보다 쉽게 수행할 수 있도록 도와줍니다. 이번 글에서는 Apache Commons Collections에서 제공하는 주요 클래스들에 대해 알아보겠습니다.

## 1. **CollectionUtils**

`CollectionUtils` 클래스는 컬렉션에 대한 유용한 메소드를 제공합니다. 예를 들어, 다음과 같은 메소드들이 있습니다:
- `size`: 컬렉션의 크기를 반환합니다.
- `isEmpty`: 컬렉션이 비어있는지 여부를 반환합니다.
- `addAll`: 한 컬렉션의 모든 요소를 다른 컬렉션에 추가합니다.
- `subtract`: 첫 번째 컬렉션에서 두 번째 컬렉션의 요소를 제거합니다.

## 2. **MapUtils**

`MapUtils` 클래스는 맵에 대한 유용한 메소드들을 포함하고 있습니다. `MapUtils`의 주요 기능은 다음과 같습니다:
- `isEmpty`: 맵이 비어있는지 여부를 반환합니다.
- `getOrDefault`: 주어진 키에 해당하는 값을 반환하거나, 키가 존재하지 않을 경우 디폴트 값을 반환합니다.

## 3. **ListUtils**

`ListUtils` 클래스는 리스트에 대한 유용한 메소드들을 제공합니다. 예를 들어, 다음과 같은 메소드들이 있습니다:
- `partition`: 리스트를 지정된 크기로 쪼개서 리스트의 리스트로 반환합니다.
- `indexOf`: 주어진 객체가 리스트에서 처음으로 나타나는 인덱스를 반환합니다.

## 4. **BagUtils**

`BagUtils` 클래스는 양적 집합을 나타내는 `Bag` 인터페이스에 대해 유용한 기능들을 제공합니다. 양적 집합은 객체들의 개수에 초점을 맞춘 데이터 구조입니다.

## 5. **BidiMap**

`BidiMap` 인터페이스는 이중 맵을 나타내며, 키와 값 사이의 양방향 매핑을 제공합니다. 이중 맵은 키와 값 모두 유일해야 합니다.

이 외에도 Apache Commons Collections에는 더 많은 유용한 클래스와 인터페이스들이 있습니다. 개발자들은 이 라이브러리를 사용하여 다양한 컬렉션과 알고리즘을 쉽게 활용할 수 있습니다.

더 자세한 정보와 사용 예제를 알고 싶다면 [Apache Commons Collections 홈페이지](https://commons.apache.org/proper/commons-collections/)를 참고해주세요.