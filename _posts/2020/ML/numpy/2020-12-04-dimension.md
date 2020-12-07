---
layout: post
title: "[numpy] ndarray"
description: " "
date: 2020-12-04
tags: [numpy]
comments: true
share: true
---

# ndarray(차원,크기)

> Python의 일반적인 `list`와 달리 다른 data-type이 들어올 수 있고 하나의 data-type을 element로 갖는다.
>
> 그냥 Matrix 또는 Vector로 받아들이면 굉장히 편할 듯 하다. 참고로 ndarray에는 , 로 element를 구분하지 않는다.



## ndarray 의 차원

> ndarray를 matrix로 생각하면 `dimension(차원)` 이 존재한다. 1차원, 2차원, 3차원의 ndarray를 만들어 보도록 한다.



* 1-dimensional ndarray : 가장 쉽게 만드는 방법은 python `list`를 numpy.array에 대입하는 방법이다.

  ```python
  import numpy as np
  
  a = [1, 2, 3, 4, 5]  # 물론 tuple로도 만들수 있다.
  arr = np.arrray(a)
  print(arr)          # [1 2 3 4 5] : 행벡터로 생각 가능
  b = [[1], [2], [3], [4], [5]]
  arr = np.array(b)
  print(arr)      #[[1]
                  # [2]
                  # [3]
                  # [4]
                  # [5]] : 열벡터로 생각 가능
  
  ```

* 2-dimensional ndarray : 가장 기본적인 방법은 이중리스트를 만들어  numpy.array에 대입하는 방법이다.

  ```python
  a = [[1,2,3],[4,5,6]]
  arr = np.array(a)
  print(arr)      #[[1 2 3]
                  # [4 5 6]] 
  print(arr[1,1]) #  5
  ```

  : row 부분에 1번째 row에 1,2,3 을 채우고 2번째 row에 4,5,6 을 채운다.

* 3-dimensional ndarray : 같은 크기의 행렬이 여러장 쌓여있다라고 생각할 수 있다. 여러표현이 있지만 page라는 용어를 사용하겠다.  3-dimensional ndarry를 처음 만들때 혼동 되는 부분이 조금 있었지만 다음과 같은 순서로 이해하면 크게 어렵지 않을것 같다.

  1. 우선 `list` : [ ] 안에 몇개의 page를 넣을지를 정한 후 그만큼의 list안에 list를 만들어준다.

     (예) page=3 라면 [ [], [], [] ] 과 같이 3개의 list를 만들어 주자. 각각을(page1, page2, page3) 라고 칭하자.

  2.  다음으로 각각의 list(page)에 위에서와 같이  같은 크기의 2-dimensional ndarray(이중 리스트)를 넣어준다.

     (예) 3x2x2 크기의 ndarray를 만들기위해 1~12를 차례대로 포함하도록 위에서 2-mensional ndarra 각 page에  만들어준다.

     ```python
     a = [ [[1,2],[3,4]], [[5,6],[7,8]], [[9,10],[11,12]] ]
     print(a)
     # [[[ 1  2]
     #  [ 3  4]]
     
     # [[ 5  6]
     #  [ 7  8]]
     
     # [[ 9 10]
     #  [11 12]]]
     ```

     

  

## ndarray 크기 : 속성

* #### ndim

  * 차원을 나타내는 속성이다. (즉, page 개수이다.)

  ```python
  arr1 = np.ndarray([1, 2, 3, 4])
  print(arr1.ndim)  # 1
  
  arr2 = np.ndarray([ [[1,2],[3,4]], [[5,6],[7,8]], [[9,10],[11,12]] ]) # 위에서 사용한 예제
  print(arr2.ndim)  # 3
  ```



* #### size

  * 모든 원소의 개수이다.

  ```python
  arr1 = np.ndarray([1, 2, 3, 4])
  print(arr1.size)  # 4
  
  arr2 = np.ndarray([ [[1,2],[3,4]], [[5,6],[7,8]], [[9,10],[11,12]] ]) # 위에서 사용한 예제
  print(arr2.size)  # 12
  ```



* #### shape

  * 1차원 - column 수, 2차원 - (row의 수, col의 수), 3차원 -(page의 수, row의 수, col의 수)를 `tuple`로 나타낸다.

  ```python
  arr1 = np.ndarray([1, 2, 3, 4])
  print(arr1.shape)    # (4,) : tuple에서는 원소 한개는 ,로 표시해준다.    
  
  arr2 = np.ndarray([[1, 2, 3], [4, 5, 6]])
  print(arr2.shape)   # (2,3)
  
  arr3 = np.ndarray([ [[1,2],[3,4]], [[5,6],[7,8]], [[9,10],[11,12]] ]) # 위에서 사용한 예제
  print(arr3.shape)   # (3, 2, 2)
  ```

  * shape 속성을 변경해 reshape 해줄 수 있다. ( reshape은 method로도 존재한다. 이는 아래서 다루자.)

  ```python
  arr1 = np.array([1, 2, 3, 4])
  print(arr1)         # [1 2 3 4]
  
  arr1.shape = (4,1)  
  print(arr1)         # [[1 2 3 4]]
  
  arr1.shape = (2,2)
  print(aar1)         # [[1 2]
  				    # [3 4]]
  arr1.shape = (1,4)
  print(arr1)         # [[1]
  					# [2]
  					# [3]
  					# [4]]
              
  arr1.shape = (2,1,2)
  print(arr1)         # [[[1 2]]
  					# [[3 4]]]
  ```

  * shape의 경우 원래의 원소의 개수를 벗어나는 값을 주면 error가 발생한다.

  ```python
  arr1.shape = (5, 2)
  ---------------------------------------------------------------------------
  ValueError                                Traceback (most recent call last)
  <ipython-input-194-802bbf748986> in <module>
        9 print(arr1)
       10 
  ---> 11 arr1.shape = (5,2)
  
  ValueError: cannot reshape array of size 4 into shape (5,2)
  ```

  

## reshape : method

> `reshape`  method를 이용해서 `ndarray`의 `shape`의 속성을 변경하지 않고도 `ndarray` 의 shape을 변경 할 수 있다. 하지만 reshape의 경우 `view`를 return 하기 때문에 추가적으로 python method인 `copy()` 를 사용해야 한다.

***여기서***  `View` 는 원래의 데이터를 가지고 모양만 바꿔서 __보여주기만__ (진짜 원래의 값을 바꾸는게 아니다.) 하는 결과를 얘기한다. 

* 사용법은 arr.reshape(a,b) 로 사용하고 (a,b) 는 원하는 shape이다.

	```	python
import numpy as np
arr = np.array([(1,2,3),(4,5,6)])
print(arr)       # [[1 2 3]
				 # [4 5 6]]
	
	arr1 = arr.reshape(3,2)
	print(arr1)      # [[1 2]
					 # [3 4]
	                 # [5 6]]
	arr[1,1]=500
	print(arr1)      # [[  1 2]
					 #  [  3 4]
	                 #  [500 6]]   
	```
	
	`arr[1,1]=500` 으로 값을 변경했을때 `arr1` 은 영향을 안받을것이라고 생각할 수 있지만 `reshape` 은 `view`를 리턴하기 때문에 `arr1` 를 건드리지 않았음에도 `5` 자리가 `500` 으로 바껴있다.



* `copy()` 를 이용하자.

  ```python
  arr = np.array([(1,2,3),(4,5,6)])
  print(arr)       # [[1 2 3]
  				 # [4 5 6]]
  
  arr1 = arr.reshape(3,2).copy()
  print(arr1)      # [[1 2]
  				 # [3 4]
                   # [5 6]]
  
  arr[1,1]=500
  print(arr1)      # [[1   2]
  				 #  [3   4]
                   #  [5   6]]
  ```
  
  `copy()` 를 사용하면 `view` 를 return 하지 않기 때문에 `arr` 값 변화에 `arr1` 는 영향받지 않는다.



* `shape` 의 값중 하나에  `-1`을 주면 자동으로 알맞은 크기로 변화해준다.

  예를 들어 `(2, 3)` 대신 `(-1, 3)` 또는 `(2, -1)` 도 같은 결과를 가져온다.

  ```python
  arr = np.array([(1,2,3),(4,5,6)])
  
  print(arr.reshape(3,2))
  print(arr.reshape(3,-1))
  print(arr.reshape(-1,2))
  
  # 모두 같은 결과를 가져온다.
  # [[1 2]
  #  [3 4]
  #  [5 6]]
  ```

  

## ravel

* 1차원 ndarray로 바꿔준다. row vector 로 바꿔준다고 생각하면 마음 편하다. 

  ```python
  arr = np.array([(1,2,3),(4,5,6)])
  print(arr.ravel())
  # [1 2 3 4 5 6]
  ```

* `reshape`과 마찬가지로 `view`를 return 한다.



## resize

* `reshape` method와 유사하다.
* `reshape` 과 달리 어떤 `shape`을 대입하든 다 `resize`되고 원소가 부족하면 `0`으로 채우고 넘치면 원소를 버린다.
* 