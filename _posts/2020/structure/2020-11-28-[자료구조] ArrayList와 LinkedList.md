---
layout: post
title: "[자료구조] ArrayList와 LinkedList"
description: " "
date: 2020-11-28
tags: [자료구조]
comments: true
share: true
---



## ArrayList ([링크](https://github.com/forceson/DataStructure-Study/blob/master/src/com/company/util/ArrayList.java))

![](https://beginnersbook.com/wp-content/uploads/2013/12/Adding_Element_ArrayList_diagram.png)

ArrayList는 자바의 List 중 하나이다. 기본적으로 배열을 내장하고 있어 일정 크기가 정해져있다. 배열을 기반으로 하기 때문에 검색 속도는 기본 주소로부터의 오프셋으로 계산할 수 있어 빠르고, 삽입, 삭제 연산 시에는 처음이나 중간에서 연산을 진행할 경우 값을 당겨오거나 밀어주는 과정에서 시간이 소요되고 추가나 삭제시 복사에 관련된 연산이 발생할 수 있기 때문에 또한 시간이 소요된다.

**장점**

간단하고 사용이 쉬움

항목으로의 접근이 빠름

메모리 접근에 대한 지역성에서 장점 가짐. 현대의 CPU 캐싱 기법에 유리함

**단점**

삽입 삭제 연산 시간

## LinkedList

![](https://beginnersbook.com/wp-content/uploads/2013/12/singly_linkedlist.png)

LinkedList는 데이터의 집합을 저장하기 위해 사용되는 데이터 구조인데, 이 역시 자바의 List 중 하나로 구현되어있다. 배열을 사용하지 않고 포인터를 사용하는게 특징이다. 연속되는 항목들이 포인터로 연결되고 마지막 항목은 NULL을 포인트한다. 프로그램이 수행되는 동안 크기가 커지거나 작아질 수 있다. 시스템 메모리가 허용하는 한 필요한 만큼 길어질 수 있다. 배열에 비해 메모리의 공간을 낭비하지 않지만 추가적으로 포인터를 위한 추가 메모리가 필요하다.

LinkedList는 단일 연결 뿐만 아니라 이중 연결, 원형 연결 리스트로 구성되어 있다. 위의 특징은 주로 단일 연결 리스트에 해당한다.

**장점**

자료의 삽입과 삭제에 용이

리스트 내에서 자료의 이동이 필요하지 않음

**단점**

포인터의 사용으로 인해 저장 공간 낭비

알고리즘 복잡

특정자료 탐색 시간이 많이 소요

### Single LinkedList ([링크](https://github.com/forceson/DataStructure-Study/blob/master/src/com/company/util/SingleLinkedList.java))

가장 일반적인 LinkedList이다.

### Double LinkedList ([링크](https://github.com/forceson/DataStructure-Study/blob/master/src/com/company/util/DoubleLinkedList.java))

이중 연결 리스트의 장점은 리스트의 특정 노드로부터 양방향 탐색을 할 수 있다는 것이다. 단일 연결 리스트의 노드는 바로 전 노드를 가리키는 포인터를 얻기 전까지는 삭제될 수 없다. 하지만 이중 연결 리스트에서는 이전 노드의 주소를 모르더라도 노드를 삭제할 수 있다. 단점은 각 노드가 포인터를 하나씩 더 필요로 하기 때문에 저장 공간이 더 필요하다. 포인터 연산이 더 많아지므로 삽입, 삭제 연산이 조금 더 오래 걸린다.

### Circular LinkedList ([링크](https://github.com/forceson/DataStructure-Study/blob/master/src/com/company/util/CircularLinkedList.java))

원형 연결 리스트에는 끝이 없다. 그러므로 원형 연결 리스트를 탐색할 때는 주의하지 않으면 무한히 돌게 된다. 원형 연결 리스트에서는 모든 노드에 뒤따르는 노드가 있다. 경우에 따라 무척 유용한 리스트인데 예를 들면 라운드 로빈 알고리즘에 사용될 수 있다. 라운드 로빈 알고리즘은 여러 프로세스가 같은 컴퓨터 자원을 동일한 시간 동안 사용해야 한다는 것이다. 어떤 프로세스도 다른 프로세스보다 더 많이 자원에 접근하면 안된다는 것이다.

## ArrayList vs LinkedList

목차 | ArrayList | LinkedList
-------|:------:|:-----------------:
 Indexing | O(1) | O(n)
Insert/Delete at Beginning | O(n) | O(1)
Insert/Delete at End | O(1) | O(n)
Insert/Delete in Middle | O(n) | O(n)
Wasted Space | O(n) | O(n)

**결론 1. 순차적으로(뒤에서부터) 추가/삭제하는 경우에는 ArrayList가 LinkedList보다 빠르다.**

단순히 저장하는 시간만을 비교할 수 있도록 하기 위해서 ArrayList를 생성할 때는 저장할 데이터의 개수만큼 충분한 초기용량을 확보하면, 저장공간이 부족해서 새로운 ArrayList를 생성해야하는 상황이 일어나지 않는다. 만일 ArrayList의 크기가 충분하지 않으면, 새로운 크기의 ArrayList를 생성하고 데이터를 복사하는 일이 발생하게 되므로 순차적으로 데이터를 추가해도 ArrayList보다 LinkedList가 더 빠를 수 있다.

순차적으로 삭제한다는 것은 마지막 데이터부터 역순으로 삭제해나간다는 것을 의미하며, ArrayList는 마지막 데이터부터 삭제할 경우 각 요소들의 재배치가 필요하지 않으므로 상당히 빠르다. 단지 마지막 요소를 null로 바꾸면 된다.

**결론 2. 처음이나 중간에 데이터를 추가/삭제하는 경우에는 LinkedList가 ArrayList보다 빠르다.**

처음이나 중간에 요소를 추가, 삭제하는 경우, LinkedList는 탐색 후에 각 요소의 연결만 변경해주면 되기 때문에 처리속도가 상당히 빠르다. 반면에 ArrayList는 각 요소들을 재배치하여 추가할 공간을 확보하거나 빈 공간을 채워야하기 때문에 처리속도가 늦다.

**결론 3. 검색의 경우, ArrayList가 LinkedList보다 빠르다.**

이는 ArrayList가 Array를 기반으로 만들어져 있기에 메모리 주소의 오프셋을 통한 검색이 가능하므로 빠른 것이다. LinkedList는 순차 탐색을 해야하므로 느린 것은 자명하다.

## 레퍼런스

다양한 예제로 학습하는 데이터 구조와 알고리즘 for Java, 나라심하 카루만치

Java의 정석, 남궁성

[http://www.nextree.co.kr/p6506/](http://www.nextree.co.kr/p6506/)
