---
layout: post
title: "[머신러닝] Multiple Linear Regression 3"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---


# Multiple Linear Regression(3)-Sklearn

> 앞에서 Preprocessing DataSet을 가지고 **Sklearn**를 가지고 Multiple Linear Regression 모델을 만들어 본다.



## Training_data 정의

> 앞에서 preprocessing DataSet을 `x_data`, `t_data`(Label)로 나눠준다.

```python
x_data = training_data.drop(['Ozone'], axis=1).values  
t_data = training_data['Ozone'].values.reshape(-1,1)   # 2차원으로 만들어준다. 
```



## Model 생성

> `sklearn` 에서 `linearmodel`의 `LinearRegression` 모델을 생성한다.

```python
model = linear_model.LinearRegression()
```



## 학습 진행

> `model.fit`을 이용해 간단히 학습을 진행한다.

```python
model.fit(x_data, t_data)
```



## Weight, Bias 확인하기

```python
W = model.coef_
b = model.intercept_
print('W : {}, b : {}'.format(W,b))
# W : [[ 0.24999232 -0.33513494  0.71641872]], b : [0.01870675]
```



## 예측하기

> `data`를 입력해 오존량을 추측해본다.

```python
predict_data_x = np.array([[150, 8, 65]])
predict_data_x = scaler_x.transform(predict_data_x)

predict_val = model.predict(predict_data_x)
result = scaler_t.inverse_transform(predict_val)
print(result)
# [[10.56936901]]
```

