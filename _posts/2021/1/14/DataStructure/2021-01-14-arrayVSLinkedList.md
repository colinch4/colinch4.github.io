---
layout: post
title: "[자료구조] Array vs LinkedList"
description: " "
date: 2021-01-14
tags: [cs]
comments: true
share: true
---


잘 알고 있다고 생각했는데 막상 말로 설명하려니 두서없이 말했던 게 생각나서 기록합니다.<br>Array와 LinkedList 모두 연속해 있는 선형자료구조로 데이터를 나열한다는 공통점을 가지고 있지만, 그 특징에 있어서는 차이가 있기 때문에 데이터를 저장한 후 어떻게 사용할 것인지에 따라 다릅니다.



## Array

- 데이터의 삽입/삭제가 거의 없고, 데이터 접근이 빈번하게 일어날 때 좋음. **(for lookup 👍 / for insert, delete 👎)**

- 데이터를 논리적 순서에 따라 순차적으로 데이터 삽입 -> 데이터의 논리적 순서 == 데이터의 물리적 순서

- 따라서 찾고자 하는 원소의 `index` 를 통해 데이터에 접근(random access) 할 수 있다. <br>( `Big-O(1)` 의 시간복잡도로 검색 가능)

- 하지만 데이터를 삽입/삭제할 때는 배열의 **연속적 특징**을 유지하기 위해, 그만큼 나머지 데이터들을 앞 혹은 뒤로 `shift` 해주어야 하는데 이 경우 `Big-O(n)` 의 시간복잡도가 발생한다.

- 또한, 크기가 고정되어 있어 예상한 크기를 초과할 시에는 배열의 크기를 재정의 해야하는(Resizing) 번거로움이 존재한다.

  ​



## LinkedList

- 데이터의 삽입/삭제가 빈번하고, 데이터의 양이 상대적으로 많지 않으며, 데이터의 접근이 빈번하지 않을 때 좋음 <br>**(for lookup👎 / for insert, delete👍 )**
- linked list안의 각 원소들은, 1) 데이터 값 과 2) 자기 자신 다음에 어떤 원소를 가지고 있는지만을 기억하고 있다.<br>(single linked list 기준. double linked list의 경우 자기 자신 이전의 원소가 무엇인지 역시 기억한다.)
- 이와 같은 특성은 데이터의 논리적 순서와 실제 컴퓨터 내에 저장 된 물리적 순서가 다르다는 단점이 있다.<br> 따라서 linked list에 저장된 원하는 데이터를 찾으려면, 링크드리스트의 첫 번째 원소부터 원하는 데이터가 나올 때 까지 검색을 해야한다. 따라서 링크드리스트에서의 검색은 `Big-O(n)` 의 시간복잡도를 가져 삽입삭제에 있어선 성능이 좋지 못하다.
- 하지만 데이터를 원하는 위치에 추가하거나 데이터를 삭제하는 것에는 강점을 가지고 있다. 원소가 가리키고 있는 포인터의 위치만 조정해주면 되기 때문이다. `Big-O(1)` 의 시간복잡도를 가진다.
- Array와는 다르게 배열의 크기가 제한적이지 않아 Resizing의 번거로움이 없다.





## 추가) Dynamic Array

현업에서는 데이터의 lookup, 삽입, 삭제 모두 빈번히 일어나기 때문에 자료구조의 Array와 Linked List를 둘 다 쓰지 않는다고 한다. (라고 모 기업 입사설명회에서 CTO님이 하시는 말씀을 들은 바가 있다. 자바의 ArrayList를 주로 쓰신다고...)

예를 들어, 자바스크립트, 파이썬(List)의 경우 언어 자체에서 제공하는 동적배열(Dynamic Array) 이기 때문에, 자유롭게 확장할 수 있는 구조를 가져 Resizing 이슈에 대해 고민할 필요가 없다. 자바의 경우 `ArrayList` , C++의 경우 STL의 `vector` 을 사용하면, 일정 배열의 크기가 차면 내부적으로 크기를 자동으로 늘려주어 코드를 짜는 사람이 Resizing에 대해 고민하지 않아도 된다.

(엄밀히 말하면 이러한 동적 배열 역시도 자료구조의 Array를 기반으로 하는 것은 맞지만, 언어 내부적으로 이 Array의 크기를 일정 크기로 자연스럽게 늘려주는 것이다.)



### 참고 URL

[Array vs LinkedList](https://github.com/JaeYeopHan/Interview_Question_for_Beginner/tree/master/DataStructure#array-vs-linkedlist)

[파이썬 컬렉션:리스트](http://pythonstudy.xyz/python/article/12-%EC%BB%AC%EB%A0%89%EC%85%98--List)

