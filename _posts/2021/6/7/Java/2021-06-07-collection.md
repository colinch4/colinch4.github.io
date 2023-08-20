---
layout: post
title: "[java] Collection Framework 컬렉션 프레임워크"
description: " "
date: 2021-06-07
tags: [java]
comments: true
share: true
---

## 🥎 Collection Framework 컬렉션 프레임워크 🏈

## 컬렉션 프레임워크란?

> 널리 알려져 있는 자료구조를 이용해서 객체를 **효율적으로 추가/삭제/검색** 할 수 있도록 **java.util** 패키지에서 제공하는 인터페이스와 구현 클래스

<br>

### List 리스트 :

#### - ArrayList, Vector, LinkedList

> - 배열과 비슷하게 객체를 인덱스로 관리
> - 하지만 저장용량이 자동으로 추가되고 인덱스도 부여된다는 점에서 배열과 다름
> - 동일 객체 중복저장 (O) / null 저장 (O)

<br >

#### - 사용 매소드

1. **add()** : 컬렉션 개체 추가시 사용

```java
List<String> mylist = new ArrayList<String>();
// or List<String> mylist = new ArrayList<>();

	mylist.add("Mr.Hong");
	mylist.add("Dooly");
	mylist.add("Mr.Hong");
```

2. **get()** : 컬렉션 개체 조회

```java
for(int i=0; i<mylist.size(); i++) {
	value = (String)mylist.get(i);
	System.out.println(value);
}
```

2. **remove()** : 개체 삭제

```java
    mylist.remove(0); // 인덱스로 객체 삭제
    mylist.remove("Dooly"); // 객체 삭제
```

<br>

### Set 셋

<br>

### Map 맵

```

```
