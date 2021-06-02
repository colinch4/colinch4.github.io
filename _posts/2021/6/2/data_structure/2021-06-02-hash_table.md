---
layout: post
title: "[자료구조] Direct Access Table"
description: " "
date: 2021-06-02
tags: [자료구조]
comments: true
share: true
---

## Direct Access Table

- 배열 인덱스를 키로저장하고 그 키를 이용한 데이터 접근 방식
- 키를 이용해서 접근하기 때문에 시간복잡도 O(1)
- 자칫하면 메모리를 너무많이 잡아먹을 수 있다.(930까지의 공간이있는데 사용하는 인덱스가 띄엄띄엄 930까지 5개 있을때 나머지 925의 데이터공간은 낭비가 된다.)

## 해시 테이블(Hash Table)

- 시간과 공간을 둘다 효율적으로 사용하는 자료구조
- 특정 값을 원하는 범위의 자연수로 바꿔주는 함수(자연수 인덱스에 키와밸류값을 둘다 저장)

해시 테이블이 만들어지는 순서

1. 고정된 크기의 배열을 만든다.
2. 해시 함수를 이용해서 `key`를 원하는 범위의 자연수로 바꾼다.
3. 해시 함수 결과 값 인덱스에 `key` - `value` 쌍을 저장한다.

### 해시 함수

해시 함수에 key를 넣었을 때 원하는 범위의 자연수를 리턴해주는 어떤 함수

### Chaining

해시 테이블에서 키&밸류값을 같은 인덱스에 저장할 때 **충돌(Collision**)이 일어나는데, 이 충돌을 해결해주는 하나의 방법이 Chaining이다.

> 배열 인덱스에 링크드 리스트 저장해서 충돌 해결!(Chaning)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/66cba23c-173d-4b25-bbba-8f99d645eecb/_2021-05-12__4.42.04.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/66cba23c-173d-4b25-bbba-8f99d645eecb/_2021-05-12__4.42.04.png)

```python
class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, key, value):
        self.key   = key
        self.value = value
        self.next  = None
        self.prev  = None

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_with_key(self, key):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다."""
        iterator = self.head

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
        # 이미 노드가 있다면
        else:
            new_node.prev  = self.tail
            self.tail.next = new_node
            self.tail      = new_node

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""

        # 링크드 리스트에서 마지막 남은 데이터를 삭제할 떄
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None

        # 링크드 리스트 가장 앞 데이터 삭제할 떄
        elif node_to_delete is self.head:
            self.head      = self.head.next
            self.head.prev = None

        # 링크드 리스트 가장 뒤 데이터 삭제할 떄
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        # 두 노드 사이에 있는 데이터 삭제할 때
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = ""

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다.
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다.
            res_str += "{} : {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next

        return res_str

new_node = LinkedList()
new_node.append(101, '최지웅')
new_node.append(204, '강영훈')
new_node.append(305, '성태호')

print(new_node)

#-- Output
# 101 : 최지웅
# 204 : 강영훈
# 305 : 성태호
```

### 탐색 시간 복잡도

| 연산 	| 탐색 연산 각 단계들 	|
|-	|:-:	|
| 해시 함수 계산 	| O(1) 	|
| 배열 인덱스 접근 	| O(1) 	|
| 링크드 리스트 탐색 	| O(n) 	|
| 총합 	| O(n) 	|

### 삽입 시간 복잡도

| 연산 	| 탐색 연산 각 단계들 	|
|-	|:-:	|
| 해시 함수 계산 	| O(1) 	|
| 배열 인덱스 접근 	| O(1) 	|
| 링크드 리스트 노드 탐색 	| O(n) 	|
| 링크드 리스트 저장 / 노드 수정 	| O(1) 	|
| 총합 	| O(n) 	|

### 삭제 시간 복잡도

| 연산 	| 탐색 연산 각 단계들 	|
|-	|:-:	|
| 해시 함수 계산 	| O(1) 	|
| 배열 인덱스 접근 	| O(1) 	|
| 링크드 리스트 노드 탐색 	| O(n) 	|
| 링크드 리스트 노드 삭제 	| O(1) 	|
| 총합 	| O(n) 	|

위의 예시와는 다르게 실제로 해시 테이블을 사용할 때는 대부분의 경우 탐색, 저장, 삭제 3가지 연산들이 그냥 $O(1)$이 걸린다고 가정하고 사용한다.

하지만 이 연산들이 최악의 경우 시간복잡도 $O(n)$ 이 걸리는 것은 사실이다. 그래서 이런 혼란을 줄이기 위해서 좀 더 정확하게는

> 해시 테이블 삽입, 삭제, 탐색 연산들은 최악의 경우 시간 복잡도 $O(n)$ 이 걸리지만, 평균적으로는 $O(1)$ 이 걸린다.