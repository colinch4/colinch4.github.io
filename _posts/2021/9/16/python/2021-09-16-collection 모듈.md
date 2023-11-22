---
layout: post
title: "[파이썬] collection 모듈"
description: " "
date: 2021-09-16
tags: [python]
comments: true
share: true
---

## collection 모듈

collection.Counter()

- 요약

컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체이다.

## 1. counter() 에 입력되는 입력값

### 1) 리스트(list)

- 리스트로 들어가도 딕셔너리로 출력됨, keys = 입력값, value = 입력값 별 개수

  ```python
  import collections
  lst = ['aa','cc','bb','dd','aa']
  print(collections.Counter(lst))
  ----------------------------------------------------
  출력값 = Counter({'aa': 2, 'cc': 1, 'bb': 1, 'dd': 1})
  ```

  

### 2) 딕셔너리(dictionary)

- 딕셔너리를 출력하되 내림차순으로 개소가 높은 것 부터 출력해 준다. 

```python
import collection
dic = {'가': 1 , '나': 2 , '다' : 3, '라' : 4}
print(collections.Counter(dic))
---------------------------------------------------
출력값 = Counter({'라': 4, '다': 3, '나': 2, '가': 1})
```



### 3) 값 = 개수 형태

- 값 = 개수 형태로 입력 가능

```python
c = collections.Counter(a=2, b=3, c=2)  # 값 = 개수 형태로 입력
print(collections.Counter(c))
print(sorted(c.elements()))  # elements() 함수 사용, sorted를 이용
print(c.elements()) # sorted 를 안하면 값이 출력안됨

---------------------------------------------------------
Counter({'b': 3, 'a': 2, 'c': 2})
['a', 'a', 'b', 'b', 'b', 'c', 'c']
<itertools.chain object at 0x0000016449BB9C50>
```



### 4) 문자열 (string)

- 문자열을 입력 하면 문자열 안에 하나하나 개소를 구해줌

```python
c = collections.Counter("안녕하신가요, 안녕하세요")       # 한글도 가능
print(c)             # collections.Counter 에 설정되는 방식  
--------------------------------------------------------
Counter({'안': 2, '녕': 2, '하': 2, '요': 2, '신': 1, '가': 1, ',': 1, ' ': 1, '세': 1})

```



## 2. Counter 의 메소드

### 1) update()

- counter 의 값을 갱신하는 것을 의미
- 딕셔너리의 update 와 비슷하지만 입력값을 문자열 형태로도 입력 가능함
- 이전 개소와 합쳐서 갱신

```python
c = collections.Counter('ababab')
print(c)
c.update("ccffxx")
print(c)
c.update({'f': 1, 'x' : 5, 'z' : 100})
print(c)
---------------------------------------------------------
Counter({'a': 3, 'b': 3})
Counter({'a': 3, 'b': 3, 'c': 2, 'f': 2, 'x': 2})
Counter({'z': 100, 'x': 7, 'a': 3, 'b': 3, 'f': 3, 'c': 2})
```



### 2) elements()

-  입력된 값의 개소에 해당하는 값을 풀어서 반환한다.
-  개소는 무작위로 반환, 개소 수가 1보다 작을 경우 반환하지 않는다.

```python
c = collection.Counter('hellow python')
print(list(c.elements()))
print(sorted(c.elements()))
-----------------------------------------------------------
['h', 'h', 'e', 'l', 'l', 'o', 'o', 'w', ' ', 'p', 'y', 't', 'n']
[' ', 'e', 'h', 'h', 'l', 'l', 'n', 'o', 'o', 'p', 't', 'w', 'y']
## 띄어 쓰기도 포함
```



### 3) most_common(n)

- 입력값의 개소들 중 빈도수가 높은 순으로 상위 (n)개를 리스트안의 튜플로 반환한다
- n을 입력하지 않으면 전체를 반환한다

```python
c2 = collections.Counter('apple, orange, grape')
print(c2.most_common())
print(c2.most_common(3))
-----------------------------------------------------------
[('a', 3), ('p', 3), ('e', 3), (',', 2), (' ', 2), ('r', 2), ('g', 2), ('l', 1), ('o', 1), ('n', 1)]
[('a', 3), ('p', 3), ('e', 3)]
```



### 4) subtrant()

- 말그대로 개소를 빼는 것을 의미한다. 다만 요소가 없을 경우 음수를 출력한다.

```python
c3 = collections.Counter('hello python')
c4 = collections.Counter('i love python')
c3.subtract(c4)
print(c3)


t = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
t.subtract(d)
print(c)

------------------------------------------------------------
Counter({'h': 1, 'l': 1, 'e': 0, 'o': 0, 'p': 0, 'y': 0, 't': 0, 'n': 0, ' ': -1, 'i': -1, 'v': -1})
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})  # t-d
```



- 덧셈, 뺄셈, 비교연산자(& , |) 사용가능

```python
a = collections.Counter('aabbccdd')
b = collections.Counter('aabbbce')
print(a & b)

```

