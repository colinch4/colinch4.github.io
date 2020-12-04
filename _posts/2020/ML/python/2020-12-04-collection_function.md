---
layout: post
title: "[python] 컬렉션 관리 함수(enumerate, zip, any, all, filter,  map)"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---


## 컬렉션 관리 함수(enumerate, zip, any, all, filter,  map)



## 1. enumerate

```python
score = [88, 95, 70, 100, 99]
for no, s in enumerate(score):
    print('{}번 학생의 성적 : {}'.format(no, s))

# 0번 학생의 성적 : 88
# 1번 학생의 성적 : 95
# 2번 학생의 성적 : 70
# 3번 학생의 성적 : 100
# 4번 학생의 성적 : 99
```



```python
score = [88, 95, 70, 100, 99]
for no, s in enumerate(score,1):
    print('{}번 학생의 성적 : {}'.format(no, s))
# 1번 학생의 성적 : 88
# 2번 학생의 성적 : 95
# 3번 학생의 성적 : 70
# 4번 학생의 성적 : 100
# 5번 학생의 성적 : 99
```





## 2. zip

```python
yoil = ['월', '화', '수', '목', '금', '토', '일']
food = ['갈비탕', '순대국', '칼국수', '삼겹살']

menu = zip(yoil,food)
for y, f in menu:
    print(y,f)
# 월 갈비탕
# 화 순대국
# 수 칼국수
# 목 삼겹살

d = dict(zip(yoil, food))
print(d)
{'월': '갈비탕', '화': '순대국', '수': '칼국수', '목': '삼겹살'}
```



## 3. any, all

```python
# any => 하나라도 True
# all => 모두가 True

adult = [True, True, False, False]
print(any(adult)) # True
print(all(adult)) # False
```



## 4. filter

```python
score = [45, 89, 72, 53, 94]
for s in filter(lambda s: s<60, score):
    print(s)
# 45
# 53

l_filter = list(filter(lambda s: s<60, score))
print(l_filter)
# [45, 53]
```



## 5. map

```python
for s in map(lambda s: s/2 ,score):
    print(s)  
# 22.5
# 44.5
# 36.0
# 26.5
# 47.0 

print(list(map(lambda s: s/2 ,score)))
# [22.5, 44.5, 36.0, 26.5, 47.0]
```