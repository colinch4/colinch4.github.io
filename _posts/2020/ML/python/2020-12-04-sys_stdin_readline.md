---
layout: post
title: "[python] sys.stdin.readline()"
description: " "
date: 2020-12-04
tags: [python]
comments: true
share: true
---

# sys.stdin.readline()

> `input` 함수의 속도를 개선할 수 있는 방법이다.



## 1. input

> `input` 함수는 다음과 같이 간단히 값을 받아낼 수 있다.

* 하나의 값을 받을 때

```python
a = input()
>> 5 3 2
# 5 3 2
```



* 입력의 개수를 알고 있을 때

```python
a, b = input().split()
>> 23 10
print(a, b)
# 23 10

```



* 입력을 `list` 로 변경할 때

```python
a = input().split()
>> 1 2 3 3 x
print(a)
# ['1', '2', '3', '3', 'x']
```



## 2. sys.stdin.readline()

> `input` 보다 빠른 속도로 값을 받아낼 수 있다.

* 하나의 input을 받을 때

```python
a = sys.stdin.readline()
>> 1 3 x
print(a)
# 1 3 x
```



* 입력의 개수를 알고 있을 때

```python
a,b  = sys.stdin.readline().split()
>> 23 x4
print(a, b)
# 23 x4
```



* 입력을 `list` 로 변경할 때

```python
a  = sys.stdin.readline().split()
>> 23 4 x
print(a)
# ['23', '4', 'x']
```



* 입력값을 받아 `int`로 변경

```python
lst = list(map(int, sys.stdin.readline().split()))
# [1, 4, 3, 23, 4]
```