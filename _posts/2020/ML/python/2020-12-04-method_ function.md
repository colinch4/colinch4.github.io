---
layout: post
title: "[python] python method, function 정리"
description: " "
date: 2020-12-04
tags: [python]
comments: true
share: true
---

# python method, function 정리

> 알고리즘을 하면서 배우는 method, function을 정리한다.



* 숫자, 문자열인지 확인

```python
print('a'.isalpha())
# True

print('한글'.isalpha())
# True

print(3.isdigit())
# True
```



* `lambda`함수를 활용한 정렬

```python
points =[(2, 2), (0, 3), (1, 1), (4, 1)]
points.sort(key=lambda x: x[0])
print(points)

# [(0, 3), (1, 1), (2, 2), (4, 1)]
```



* inf 값 활용

```python
import math
a = math.inf
print(a)
# inf
print(-math.inf)
# -inf
```



* 순열 및 조합

```python
from itertools import permutations, combinations

my_list = ['1', '2', '3', '4']
perm = permutations(my_list,2)
print(list(perm))

comb = combinations(my_list,2)
print(list(comb))
# [('1', '2'), ('1', '3'), ('1', '4'), ('2', '1'), ('2', '3'), ('2', '4'), ('3', '1'), ('3', '2'), ('3', '4'), ('4', '1'), ('4', '2'), ('4', '3')]
# [('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '4')]

```



* list를 활용한 dictionary 만들기

```python
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list_alpha = [ (alpha[k],k) if k<=13 else (alpha[k],26-k) for k in range(len(alpha))   ]   # list comprehension 으로 list생성
dict_alpha = dict(list_alpha) # dictionary
```

