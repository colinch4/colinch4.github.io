---
layout: post
title: "[머신러닝] Multiple Linear Regression 4"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---


# Multiple Linear Regression(4)-Tensorflow

> 앞에서 Preprocessing DataSet을 가지고 **Tensorflow**를 가지고 Multiple Linear Regression 모델을 만들어 본다.



## Training_data 정의

> 앞에서 preprocessing DataSet을 `x_data`, `t_data`(Label)로 나눠준다.

```python
x_data = training_data.drop(['Ozone'], axis=1).values
t_data = training_data['Ozone'].values.reshape(-1,1)   # 반드시 size 조정 필요
```



## Placeholder 사용

> `x_data`, `t_data`를 바로 사용하지 않고 `tf.placeholder`를 사용해 구현한다.

```python
X = tf.placeholder(shape = [None, 3], dtype = tf.float32)
T = tf.placeholder(shape = [None, 1], dtype = tf.float32)
```



## Weight & bias 초기값 설정

> `tf.random.normal`를 이용해 **weight**와 **bias**에 대한 초기값을 설정해준다.

```python
W = tf.Variable(tf.random.normal([3,1]), name='weight')   
b = tf.Variable(tf.random.normal([1]), name='bias')
# name은 내부적으로 사용되므로 설정해준다.
```



## Hypothesis 정의

> linear model(Hypothesis)를 정의해준다.

```python
H = tf.matmul(X,W) + b
```



## Train node 생성

> train 하기 위한 traing node를 생성해준다.

```python
train = tf.train.GradientDescentOptimizer(learning_rate=1e-4).minimize(loss)
```



## Session 생성

> tensorflow를 실행하기 위해서 session을 생성 하고 초기화 해준다.

```python
sess = tf.Session()
sess.run(tf.global_variables_initializer())
```



## 학습 진행

> `forloop`를 이용해 학습을 진행한다.

```python
for step in range(300000):
    _, W_val, b_val, loss_val = sess.run([train, W, b, loss], feed_dict={X: x_data, T: t_data})
    
    if step%30000 == 0:
        print('W : {}, b : {}, loss : {}'.format(W_val, b_val, loss_val))
```



## 결과 예측하기

> `data`를 가지고 오존량을 예측해본다.

```python
predict_data_x = np.array([[150, 8, 65]])
predict_data_x = scaler_x.transform(predict_data_x)

result = sess.run(H, feed_dict={X:predict_data_x}) 
result = scaler_t.inverse_transform(result)
print(result)
# [[10.75479]]
```

