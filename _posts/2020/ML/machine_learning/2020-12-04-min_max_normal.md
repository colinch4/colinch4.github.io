---
layout: post
title: "[머신러닝] Min-Max Normalization"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---


# Min-Max Normalization

>데이터가 가진 feature들의 scale이 심하게 차이나는경우 scale의 조정이 필요하다.
>
>대표적으로 **Min-Max Normalization**과 **Z-Score Normalization**이 있지만 **Min-Max Normalization**에 대해서만 알아보도록 한다. **Min-Max Normalization**의 경우 data의 모든 feature들을 0과 1 사이의 scaling로 변환해준다.



## 공식

> 공식은 다음과 같다. 모든 data에 대해서 다음과 같이 transform 해주면 0~1사이의 값으로 변환해준다.
>
> (최댓값=1, 최솟값=0)

![image-20201005183635131](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201005183635131.png?raw=true)



## 코드

> sklearn(사이킷런)에서 제공해주는 `MinMaxScaler`를 사용해 쉽게 구현할 수 있다. 
>
> `sklearn.preprocessing` 에서 `MinMaxScaler`를 **import** 해주면 된다. 객체를 생성한 뒤 **scaling** 해준다.

* data

```python
# data
import numpy as np

data = np.array([1,2,3,4,5,6,7, 8,9, 10,11,12,13,14, 22.1])
print(data)
# [ 1.   2.   3.   4.   5.   6.   7.   8.   9.  10.  11.  12.  13.  14. 22.1]
```

* scaling

```python
from sklearn.preprocessing import MinMaxScaler()

scaler_data = MinMaxScaler()
scaler_data.fit(data.reshape(-1,1))  # Nx1 shape으로 바꾸어 주어야 한다.

# scaler_data 정보
print(scaler_data.n_sample_seen_)    # 15
print(scaler_data.data_min_)         # [1.]
print(scaler_data.data_max_)         # [22.1]

# scaling
scaled_data = scaler_data.transform(data.reshape(-1,1))
print(scaled_data)
# [[0.        ]
#  [0.04739336]
#  [0.09478673]
#  [0.14218009]
#  [0.18957346]
#  [0.23696682]
#  [0.28436019]
#  [0.33175355]
#  [0.37914692]
#  [0.42654028]
#  [0.47393365]
#  [0.52132701]
#  [0.56872038]
#  [0.61611374]
#  [1.        ]]

```

