---
layout: post
title: "[Tensorflow] 기초"
description: " "
date: 2020-12-04
tags: [Tensorflow]
comments: true
share: true
---

# Tensorflow 2.xx 기초

> 지금까지 **ML**에서 **TF1.15** 버전을 이용해서 구현했다. **TF1.15**는 **TF2.xx** 보다 하위 API로 즉, **ML**을 low level로 구현을 진행했다.
>
> 
>
> TF2.0은 크게 2가지 변경점이 있고 상당히 편리하게 사용한다. 마치 python 프로그래밍 처럼 구현이 가능하다.

## 특징

> **TF 2.xx** 버전은 크게 2가지 변경점이 있고 마치 **python**과 같이 상당히 편리하게 사용 가능하다.

* **Tensoflow**는 **google**의 **brain tensor**에서 만든 <u>Deep learning library</u>

*  2015년 1.0버전이 발표~ 2019년 9월 30일 **TF2.0** 발표, <u>현재 버전 2.3.0</u>

* **TF 2.xx** 
  1. Eager Execution : **TF**를 실행하는 방법이 바뀌었다. (`Session`을 더이상 사용하지 않는다.)
  2. `keras`가 유일한 상위 API 로 등장한다. (구현방식에 변화가 생겼다.)



## 다운로드

> 기존에 **TF1.xx** 가 있으므로 새로운 가상환경을 만들어 필요한 Library들을 설치해야 한다.

* 설치해야 할 **Library**
  * conda nb_conda 
  * conda install numpy 
  * conda install pandas 
  * conda install matplotlib
  * conda install seaborn 
  * pip install  sklearn 
  * conda install tensorflow 


```python
# 버전 확인
import tensorflow as tf
print(tf.__version__)
# 2.1.0
```

​    

## Keras 의 특징

> 상위 API인 `keras`의 특징을 알아본다. 

1. 간단하고 쉽다.
2. Modularity 를 사용한다.
   * Loss
   * Activation function
   * optimizer
   * Layer
3. **"Model",  "Layer"**를 이해해야한다.



## Logistic Regression

> **TF2.xx**에서의 Logistic Regression 에 대해서 알아본다.

![image-20201013024438217](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201013024438217.png?raw=true)

* 위의 그림은 간단한 <u>**Multiple Linear Regression**</u> 원리이다.

---------------------------------------------------------------------------------------------------------



![image-20201013033015246](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201013033015246.png?raw=true)

* 이때 **TF2.xx** 는 위와 같이 **layer**를 통해 구현된다.



## Multinomial classification

> **TF2.xx**에서의 Multinomial classification  에 대해서 알아본다.



![image-20201014024813498](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201014024813498.png?raw=true)



* 위의 그림은 `TF2.x`에서의  <u>**Multinomial classification**</u> 원리이다.


