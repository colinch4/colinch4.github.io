---
layout: post
title: "[numpy] 집계함수"
description: " "
date: 2020-12-04
tags: [numpy]
comments: true
share: true
---

# 집계함수

> Numpy에서 제공해주는 집계함수와 이를 사용할때 필요한 axis에 대하여 서술한다.



## axis란?

> `axis`는 수학에서 말하는 축을 의미한다.
* `axis`의 개수는 `dimension` 의 수와 일치한다. 즉, 1-dimesnional `ndarray` 의 경우 1개의 `axis` 가 존재하고 2-dimensional `ndarray`의 경우 2개의 `axis`가 존재한다. 

* 만약 `axis`를 지정하지 않으면 `ndarray` 전체가 집계함수의 대상이 된다.

* 일반 `for문` 이나 `python` 함수와 달리 빠른 속도로 연산을 수행한다.

* 1-dimension : axis = 0 : row방향

* 2-dimension : axis = 0, 1 : row방향, col 방향

* 3-dimension : axis = 0, 1, 2  : depth방향, row방향, col방향

* 설명을 위해 밑의 예제를 사용하도록 한다.

  ```python
  import numpy as np
  
  arr = np.arange(1,10).reshape(3,3).copy()
  ```





## 1. numpy.sum

> `ndarray`의 합을 계산한다.

```python
print(arr)
#[[1 2 3]
# [4 5 6]
# [7 8 9]]
#----------------------------------------
print(np.sum(arr))         # 45
print(np.sum(arr, axis=0)) # [12 15 18]
print(np.sum(arr, axis=1)) # [ 6 15 24]
```



## 2. numpy.cumsum

> `ndarray`의 누적합을 계산한다.

```python
print(arr)
#[[1 2 3]
# [4 5 6]
# [7 8 9]]
#----------------------------------------
print(np.cumsum(arr))             # [ 1  3  6 10 15 21 28 36 45]
print(np.cumsum(arr, axis=0))     # [[ 1  2  3]
								  #  [ 5  7  9]
                                  #  [12 15 18]]							
print(np.cumsum(arr, axis=1))     
# [[ 1  3  6]
#  [ 4  9 15]]
#  [ 7 15 24]]
```



## 3. numpy.mean, numpy.std

> `ndarray`의 평균과 표준편차를 계산한다.

```python
print(arr)
#[[1 2 3]
# [4 5 6]
# [7 8 9]]
print(np.mean(arr))    # 5.0
print(np.std(arr))     # 2.581988897471611
```



## 4. numpy.max, numpy.min

> `ndarray`의 최댓값과 최솟값을 계산한다. `numpy.max`에 대한 예제에 대해서만 언급한다.

```python
print(arr)
#[[1 2 3]
# [4 5 6]
# [7 8 9]]
print(np.max(arr))          # 9
print(np.max(arr, axis=0))  # [7 8 9]
print(np.max(arr, axis=1))  # [3 6 9]
```



## 5. numpy.argmax, numpy.argmin

> `ndarray`의 최댓값과 최솟값의 index를 찾아준다. `numpy.argmax`에 대한 예제에 대해서만 언급한다.

```python
print(arr)
#[[1 2 3]
# [4 5 6]
# [7 8 9]]
print(np.argmax(arr))         # 8
print(np.argmax(arr, axis=0)) # [2 2 2]
print(np.argmax(arr, axis=1)) # [2 2 2]
```



## 6. numpy.exp, numpy.log, numpy.log10

> `ndarray` 에 대하여`exp(arr)`, `ln(arr)`(자연로그),  `log(arr)`(상용로그) 값을 계산한다.



## 7 . numpy.unique

> `ndarray` 의 중복 원소를 제거해 유일한 원소들을 제공해준다. `axis`를 지정할 수는 있지만 제대로 작동하지 못한다.

```python
np.random.seed(3)
arr = np.random.randint(0,10,(2,4))
print(arr)
# [[8 9 3 8]
#  [8 0 5 3]]
print(np.unique(arr))  # [0 3 5 8 9]
```

