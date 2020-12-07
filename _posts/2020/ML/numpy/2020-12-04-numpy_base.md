---
layout: post
title: "[numpy] numpy 기초"
description: " "
date: 2020-12-04
tags: [numpy]
comments: true
share: true
---

# Numpy

> `Numpy` 는 Numercial Pyhon의 약어로 Python의 Module이다.



## Numpy 특징

* Vector 와 Matrix 연산에 특화되어 있다.
* Pandas와 Matplotlib Module들의 기반이 되는 Module이다.
* Machine Learing, Deep Learing에서 많이 사용된다.
* Numpy는 `ndarray`라고 불리는 n-차원 배열을 제공한다.



##  ndarray 특징

- python의 list와 상당히 유사하다.

- python `list`는 다른 데이터 타입을 함꼐 list안에 저장 가능하지만

  Numpy의 `ndarray`는 **모두 같은 데이터 타입**을 사용해야 한다.

* Python의 `list`보다 Numpy의 `ndarray`는 메모리 효율이나 실행속도면에서 우위에 있다.



## Numpy module의 설치 및 실행

우선 numpy module을 설치를 진행해야 한다.

1. `Anaconda prompt` 를 권리자 권한으로 실행한다.

2.  `data_env` 라는 이름으로 만든 가상환경 시스템을 불러온다.

   ```bash
   (base) C:\windows\system32> activate data_env
   ```

3. 다음으로 `pip install` 을 이용하든지  `conda install`  을 이용해 `numpy` 설치를 진행한다.

   ```bash
   (data_env) C:\windows\system32> conda install numpy
   ```

4.  이제 `jupyter notebook`에서 `numpy`를  불러와 `ndarray` 를 간단히 사용해 본다.

   ```python
   import numpy as np   # numpy는 너무 길기 때문에 np 라는 약어를 많이 사용한다.
   
   a= [1, 2, 3, 4, 5]
   arr =np.array(a)
   print(arr)            # [1 2 3 4 5]
   print(type(arr))      # <class 'numpy.ndarray'>
   print(arr.dtype)      # int32 : 정수 32bit
   ```

   ```python
   arr = np.array([100, 3.14, True, 'Hello'])
   print(arr)             # ['100' '3.14' 'True' 'Hello'] 
   ```

   

## 느낀점

> 학사때나 석사때나 `Matlab` 밖에 사용 안해봤는데  `numpy` 와 `Matlab` 이 상당히 유사하다는 것을 알 수 있었다. 기본적인 함수의 용어가 겹치는게 많아서 어느정도 쉽게 이해가 되는게 많았다.
>
> 그러나 가장 큰 차이점은 `row-wise` 와 `column-wise` 이다.
>
> 또한 Matlab만 사용하다보면 정수와 실수의 `data-type` 을 구분하지 않는데 구분한다는 점에서도 차이가 있다.

