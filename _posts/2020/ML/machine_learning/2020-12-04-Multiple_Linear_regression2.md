---
layout: post
title: "[머신러닝] Multiple Linear Regression 2"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---


# Multiple Linear Regression(2)-Numpy&Pandas

> 앞에서 Preprocessing DataSet을 가지고 **Numpy&Pandas**를 가지고 Multiple Linear Regression 모델을 만들어 본다.



## 추가 Package

> 앞에서 만들어 둔 수치미분 파일을 가져온다.

```python
from my_library.machine_learning_library import numerical_derivative
```



## Training_data 정의

> 앞에서 preprocessing DataSet을 `x_data`, `t_data`(Label)로 나눠준다.

```python
x_data = training_data.drop(['Ozone'], axis=1).values  # numpy.dot을 이용해야 하므로 values만 가져온다.
t_data = training_data['Ozone'].values.reshape(-1,1)   # 2차원으로 만들어준다. 
```



## Weight & Bias 초기값 설정

> Weight과 Bias가 통합된 `input_var`를 random 값을 활용해 만들어준다.

```python
input_var = np.random.rand(x_data.shape[1]+1,1)
```



## Linear Model 정의 (Hypothesis) 

> Hypothesis 를 정의한다.

```python
def hypothesis(input):
    
    A = np.concatenate([x_data, np.full((x_data.shape[0],1),1,dtype=np.float64)], axis=1)
    H = np.dot(A,input) + b
    
    return H
```



## Loss 함수 정의

> 위에서 정의한 Linear Model을 이용해 Loss 함수를 정의해준다.

```python
def loss(input):
    
    H = hypothesis(input)                # Hypothesis    
    L = np.mean(np.power(H - t_data,2))  # Loss

    return L
```



## 학습 진행

> **Learning Rate** 를 정의 하고 `forloop`를 이용해 학습을 진행한다.

```python
learning_rate = 1e-4

for step in range(300000):
    input_var -= learning_rate * numerical_derivative(loss,input_var)
    W = input_var[:-1] 
    b = input_var[-1,-1] 
    
    if step%30000 == 0:
        print('W : {}, b : {}, loss : {}'.format(W.reshpae(1,-1), b, loss(input_var))) 
        
# W : [[0.33774472 0.59702106 0.91244826]], b : 0.34576628035121904, loss : 1.6877422161418247
# W : [[0.14910521 0.14083617 0.76778394]], b : -0.09183588622570978, loss : 0.036627090537938514
# W : [[ 0.19253086 -0.00702312  0.80315532]], b : -0.07680314472571996, loss : 0.02797712392572623
# W : [[ 0.21942004 -0.10279433  0.81269906]], b : -0.0633375784216576, loss : 0.02446836282842487
# W : [[ 0.23580439 -0.16636131  0.80942587]], b : -0.05155711873369851, loss : 0.022914192186538677
# W : [[ 0.2455407  -0.20967655  0.80044323]], b : -0.04141812246897333, loss : 0.022153433439396877
# W : [[ 0.25109798 -0.23999601  0.78952631]], b : -0.032794111878912596, loss : 0.021743981070132583
# W : [[ 0.25405647 -0.26178006  0.77858967]], b : -0.02552252147410651, loss : 0.021506221637416126
# W : [[ 0.25542549 -0.27781357  0.76852548]], b : -0.019431720561419848, loss : 0.021360648301830012
# W : [[ 0.25584698 -0.28986825  0.75967754]], b : -0.014355943482384096, loss : 0.021268465653799314
```





## 예측하기

> `predict` 함수를 정의하고 data가 주어졌을때 오존량을 예측한다.

```python
def predict(input_var, predict_data):
    
    return np.dot(predict_data, input_var[:-1,:])+ input_var[-1] 

predict_data_x = np.array([[150, 8, 65]])   # 태양관 : 150, 바람 : 8, 온도 : 65
predict_data_X = scaler_x.transform(predict_data_x) # normalization을 해준다. 

result = predict(input_var, predict_data_x)  # 예측
result = scaler_t.inverse_transform(result)  # inverse normalizaion해 준다.
print(result)
# [[9.30144516]]
```



