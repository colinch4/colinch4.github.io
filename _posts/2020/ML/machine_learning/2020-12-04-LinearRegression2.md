---
layout: post
title: "[머신러닝] Decision Tree 3"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---

## Linear Regression(sklearn)

> ` sklearn`(사이킷런) 을 이용한 linear regression 방법에 대해서 알아본다. `sklearn` 은 데이터분석, ML library 중 하나로 굉장히 유명하고 효율적인 library이다.



## 1. Raw Data Loading(raw 데이터 불러오기)

> 예제로써 온도에 따른 오존량을 추측하는 ML 시스템을 만든다.  `csv` 파일로 된 데이터를 가져온다.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model     # sklearn에서 linear_model을 불러온다.

df = df.read_csv('./data/ozone.csv')
display(df)

training_data=df[['Temp','Ozone']]
display(training_data)
```

![image-20200926031405480](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200926031405480.png?raw=true)



## 2. Data Preprocessing(데이터 전처리)

> 데이터를 다룰 때 여러가지의 전처리가 있지만 여기서는 결측치 제거만 한다.

```python
training_data = training_data.dropna(how='any')
display(training_data)
```

![s](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200926031905552.png?raw=true)



## 3. Training Data Set

> `x_data`와 `t_data`를 정의한다.

```python
x_data = training_data['Temp'].values.reshape(-1,1)
t_data = training_data['Ozone'].values.reshape(-1,1)
```



## 4. linear regression model 객체 생성

> `sklearn`을 활용해 **학습되지 않은** linear regression model 객체를 생성한다.

```python
model = linear_model.LinearRegression()
```



## 5. Training Data Set을 이용해서 학습 진행

>`fit` method를 이용해서 학습을 진행한다.

```python
model.fit(x_data, t_data)
```



## 6. W와 b 값을 알아내기

> weight는 `ceef_`, bias는 `intercept_` 라는 명령어로 알아 낼 수 있다.

```python
W = model.coef_
b = model.intercept_
print('W : {}, b : {}'.format(W,b))
## W : [[2.4287033]], b : [-146.99549097]
```



## 7. 그래프로 확인

```python
plt.scatter(x_data, t_data)
plt.plot(x_data, np.dot(x_data,W) + b , color='r')
plt.show()
```

![image-20200928010603728](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200928010603728.png?raw=true)



## 8. 예측

```python
predict_val = model.predict([[80]])  # 이중 list가 아니면 error
print(predict_val)  
## [[47.30077342]]
```





## 알아야 할 keyword

`model = linear_model.LinearRegression`, `model.fit`, `model.coef_`, `model.intercept_`, `model.predict`