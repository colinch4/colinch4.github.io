---
layout: post
title: "[numpy] ndarray의 연산"
description: " "
date: 2020-12-04
tags: [numpy]
comments: true
share: true
---

# ndarray의 연산

> 사칙연산, 행렬곱, 전치행렬을 알아본다.



## 사칙연산(+,-,*,/)

1. 원칙적으로  같은 `shape`의 `array`들 간의 대응되는 **성분들**끼리 연산한다.

   ```python
   import numpy as np
   arr1 = np.array([[1,2,3], [4,5,6]])
   arr2 = np.array([[7,8,9], [10,11,12]])
   print(arr1+arr2)
   #[[ 8 10 12]
   # [14 16 18]]
   print(arr1-arr2)
   #[[-6 -6 -6]
   # [-6 -6 -6]]
   print(arr1*arr2)
   #[[ 7 16 27]
   # [40 55 72]]
   print(arr1/arr2)
   #[[0.14285714 0.25       0.33333333]
   # [0.4        0.45454545 0.5       ]]
   ```

2. `shape`이 다른 `array ` 들간의 연산

   * 더 작은 size를 지닌것을 broadcasting 해서 연산한다.
   * 항상 broadcasting이 되는것이 아니다.

   ```python
   # 1. 상수 + array
   arr1 = np.array([[1,2,3], [4,5,6]])
   print(arr1+ 100)
   #[[101 102 103]
   # [104 105 106]]
   
   # 2. shape의 성분 중 하나가 같을때
   arr1 = np.array([[1,2,3], [4,5,6]])
   arr2 = np.array([7,8,9])
   print(arr1+arr2)
   #[[ 8 10 12]     :  [7 8 9]를 broadcasting한다. 
   # [11 13 15]]
   
   # 3. broadcasting 실패
   arr1 = np.array([[1,2,3], [4,5,6]])
   arr2 = np.array([7,8])
   print(arr1+arr2)
   # ValueError: operands could not be broadcast together with shapes (2,3) (2,) 
   
   ```

   

## Transpose

* `arr.T` 와 같이 사용할 수 있다.

* `View`를 `return` 한다.

* 1-dimensinal array에는 효과가 없다.

  ```python
  import numpy as np
  arr = np.array([[1, 2, 3], [4, 5, 6]])
  print(arr)   # [[1 2 3]
  			 #  [4 5 6]]
  print(arr.T) # [[1 4]
  			 #  [2 5]
  			 #  [3 6]]
  			
  ```

  

## 행렬곱

* `numpy.dot` 을 이용해 연산 가능하다.

  ```python
  arr1 = np.array([[1,2,3],[4,5,6]])
  arr2 = np.array([[7,8],[9,10], [11,12]])
  print(np.dot(arr1,arr2))
  #[[ 58  64]
  # [139 154]]
  ```

  