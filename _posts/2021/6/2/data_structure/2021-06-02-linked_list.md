---
layout: post
title: "[자료구조] 링크드 리스트"
description: " "
date: 2021-06-02
tags: [자료구조]
comments: true
share: true
---

## 링크드 리스트 구현해보기

## 기본 링크드 리스트 

```python

class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head    # 링크드 리스트를 돌기 위해 필요한 노드 변수

        # 링크드 리스트 전체를 돈
        while iterator is not None:
            if iterator.data == data:   # iterator 노드의 데이터가 찾는 데이터면 iterator를 리턴한다.
                return iterator
            else:
                iterator = iterator.next    # 다음 노드로 넘어간다.

        # 없으면 None을 리턴한다.
        return None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다

    def __str__(self):
        """링크드  리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str
```
<br>

## Doubly Linked List

```python


class Node:
    """링크드 리스트 노드"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    """링크드 리스트"""
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다.
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다.
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next    # 다음 노드로 넘어간다.

        return res_str

    def find_node_at(self, idx):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정한다."""

        iterator = self.head

        for _ in range(idx):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다."""
        iterator = self.head # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next

        return None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:   # 링크드 리스트에 데이터가 이미 있는 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, previous_node, data):
        """주어진 노드 다음에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)   # 새로운 노드 생성

        # tail 노드 다음에 노드를 삽입할 때
        if self.tail == previous_node:
            new_node.prev = self.tail   # 새로운 노드의 이전 노드를 tail 노드로 지정한다. tail <- new_node
            self.tail.next = new_node   # tail 노드의 다음 노드를 새로운 노드로 지정한다. tail -> new_node
            self.tail = new_node        # 새로운 노드를 tail 노드로 지정한다. tail = new_node
        else:
            # 새롭게 생성한 노드를 이미 있는 prev, next 노드들과 연결시킨다.
            new_node.prev = previous_node
            new_node.next = previous_node.next

            # prev 노드와, next 노드를 새롭게 생긴 노드와 연결시킨다.
            previous_node.next = new_node
            previous_node.next.prev = new_node

    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)   # 새로운 노드 생성
        # 빈 링크드 리스트일 떄
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head   # new_node -> self.head
            self.head.prev = new_node   # new_node <- self.head
            self.head = new_node        # head 노드를 new_node 로 지정

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소"""

        # 1개만있는 링크드리스트
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        # 지울려는 노드가 head일 떄
        elif node_to_delete == self.head:
            self.head = self.head.next
            self.head.prev = None
        # 지울려는 노드가 tail일 때
        elif node_to_delete == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        # 지울려는 노드가 중간에있을 때
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.data
```

