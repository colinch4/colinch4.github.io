---
layout: post
title: "[자료구조] 해시 테이블 구현하기 with Doubly Linked List"
description: " "
date: 2021-06-02
tags: [자료구조]
comments: true
share: true
---

# 해시 테이블 구현하기 with Doubly Linked List

## 목차

1. [해시 테이블을 위한 이중 링크드 리스트](##-해시-테이블을-위한-이중-링크드-리스트)

2. [Hash Table](##-hash-table)

3. [Open Addressing을 이용한 충돌 해결](##-open-addressing을-이용한-충돌-해결)

<br>

## 해시 테이블을 위한 이중 링크드 리스트

```python
class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def find_node_with_key(self, key):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.key == key:
                return iterator

            iterator = iterator.next

        return None

    def append(self, key, value):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(key, value)

        # 빈 링크드 리스트라면 head와 tail을 새로 만든 노드로 지정
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 이미 노드가 있으면
        else:
            self.tail.next = new_node  # 마지막 노드의 다음 노드로 추가
            new_node.prev = self.tail
            self.tail = new_node  # 마지막 노드 업데이

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""

        # 링크드 리스트에서 마지막 남은 데이터를 삭제할 때
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None

        # 링크드 리스트 가장 앞 데이터 삭제할 때
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        # 링크드 리스트 가장 뒤 데이터 삭제할 떄
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        # 두 노드 사이에 있는 데이터 삭제할 때
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.value

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = ""

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str
```

<br>

## Hash Table

```python
class HashTable:
    """해시 테이블 클래스"""

    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 수용 크기 저장
        self._table = [LinkedList() for _ in range(self._capacity)]  # 파이썬 리스트 인덱스에 빈 링크드 리스트 저장

    def _hash_function(self, key):
        """
        주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
        주의: key는 파이썬 불변 타입이여야 한다.
        """
        return hash(key) % self._capacity

    def _get_linked_list_for_key(self, key):
        hashed_index = self._hash_function(key)

        return self._table[hashed_index]

    def _look_up_node(self, key):
        """파라미터로 받은 key를 갖고 있는 노드를 리턴하는 메소드"""
        linked_list = self._get_linked_list_for_key(key)
        return linked_list.find_node_with_key(key)

    def look_up_value(self, key):
        """
        주어진 key에 해당하는 데이터를 리턴하는 메소드
        """
        return self._look_up_node(key).value

    def insert(self, key, value):
        """
        새로운 key - value 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 해당하는 데이터를 바꿔준다
        """
        existing_node = self._look_up_node(key) # 이미 저장된 key인지 검사

        if existing_node is not None:
            existing_node.value = value     # 이미 저장된 key면 데이터만 바꾼다.
        else:
            # 없는 key면 링크드 리스트에 새롭게 삽입시킨다.
            linked_list = self._get_linked_list_for_key(key)
            linked_list.append(key, value)
    
    def delete_by_key(self, key):
        """주어진 key에 해당하는 key - value 쌍을 삭제하는 메소드"""
        node_to_delete = self._look_up_node(key)

        # 저장되어 있는 key면 삭제한다.
        if node_to_delete is not None:
            linked_list = self._get_linked_list_for_key(key)
            linked_list.delete(node_to_delete)

    def __str__(self):
        """해시 테이블 문자열 메소드"""
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]


test_scores = HashTable(50)  # 시험 점수를 담을 해시 테이블 인스턴스 생성

# 여러 학생들 이름과 시험 점수 삽입
test_scores.insert("현승", 85)
test_scores.insert("영훈", 90)
test_scores.insert("동욱", 87)
test_scores.insert("지웅", 99)
test_scores.insert("신의", 88)
test_scores.insert("규식", 97)
test_scores.insert("태호", 90)


# key인 이름으로 특정 학생 시험 점수 검색
print(test_scores.look_up_value("현승"))
print(test_scores.look_up_value("태호"))
print(test_scores.look_up_value("영훈"))

# 학생들 시험 점수 수정
test_scores.insert("현승", 10)
test_scores.insert("태호", 20)
test_scores.insert("영훈", 30)

print(test_scores)
```

<br>

## Open Addressing을 이용한 충돌 해결

> 다른 비어있는 공간을 찾아서 데이터를 저장하는 방법

### 선형탐사(linear probing)

> 충돌이 일어났을 때, 빈 인덱스를 하나씩 순서대로 선형적으로 찾는 방법




