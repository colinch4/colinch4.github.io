---
layout: post
title: "[Tensorflow] Multinomial Logistic Regression"
description: " "
date: 2020-12-04
tags: [Tensorflow]
comments: true
share: true
---

## Multinomial Logistic Regression

> **TF2.x**를 가지고 **Multinomial Logistic Regression** 모델을 `MNIST` 예제를 통해 구현해 본다.



## Library, DataSet, Normalization, DataSplit

* Library

```python
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import SGD

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
```



* DataSet

```python
df = pd.read_csv('./data/mnist/train.csv')
display(df.head())
```

![image-20201015035329729](C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20201015035329729.png?raw=true)

```python
x_data = df.drop(['label'], axis=1, inplace=False)
t_data = df['label']
```



* Normalization

```python
scaler_x = MinMaxScaler()
scaler_x.fit(x_data)
x_data_norm = scaler_x.transform(x_data)
```



* DataSplit

```python
x_data_train_norm, x_data_test_norm, t_data_train, t_data_test = \
train_test_split(x_data_norm, t_data, test_size=0.3, randorm_state=0)
```



## Tensorflow 구현

> **TF2.xx**를 통해 실질적인 구현을 해본다.

* 모델 및 layer 생성, compile

```python
keras_model = Sequential()
keras_model.add(Flatten(input_size=(x_data_train_norm.shape[1],)))
keras_model.add(Dense(10, activation='softmax'))
                
keras_model.compile(optimizer = SGD(learning_rate = 1e-2),
                    loss = 'sparse_categorical_crossentropy',
                    metrics = ['sparse_categorical_accuracy'])
                
```

* 학습

```python
history = keras_model.fit(x_data_train_norm, t_data_train,
           		         epochs=500,
                		 batch_size=100,
		                 verbose=1,
         		         validation_split=0.3)
```

* 결과

```python
print(keras_model.evaluate(x_data_test_norm,t_data_test))
## [0.28793775080688416, 0.9206349]  : loss, sparse_categorical_accuracy
```

```python
print(classification_report(t_data_test, 
                            (tf.argmax(keras_model.predict(x_data_test_norm), axis=1)).numpy()))
##               precision    recall  f1-score   support
## 
##            0       0.95      0.96      0.95      1242
##            1       0.96      0.97      0.97      1429
##            2       0.93      0.90      0.92      1276
##            3       0.91      0.90      0.90      1298
##            4       0.92      0.92      0.92      1236
##            5       0.89      0.88      0.88      1119
##            6       0.92      0.97      0.94      1243
##            7       0.94      0.92      0.93      1334
##            8       0.89      0.88      0.89      1204
##            9       0.88      0.89      0.89      1219
## 
##     accuracy                           0.92     12600
##    macro avg       0.92      0.92      0.92     12600
## weighted avg       0.92      0.92      0.92     12600

```

* 그래프

```python
plt.plot(history.history['sparse_categorical_accuracy'], color='b')
plt.plot(history.history['val_sparse_categorical_accuracy'], color='r')
plt.show()
```

![image-20201015215233998](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201015215233998.png?raw=true)

## sklearn과 비교

> 결과를 확인하기 위해 sklearn의 결과와 비교해 본다.

```python
sklearn_model = LogisticRegression(solver='saga')
sklearn_model.fit(x_data_train_norm, t_data_train)
sklearn_model.score(x_data_train_norm, t_data_train)
## 0.9448639455782313
classification_report(t_data_test, sklearn_model.predict(x_data_test_norm))
##               precision    recall  f1-score   support
## 
##            0       0.96      0.96      0.96      1242
##            1       0.95      0.97      0.96      1429
##            2       0.92      0.90      0.91      1276
##            3       0.91      0.90      0.90      1298
##            4       0.92      0.92      0.92      1236
##            5       0.88      0.88      0.88      1119
##            6       0.93      0.96      0.94      1243
##            7       0.94      0.93      0.94      1334
##            8       0.89      0.88      0.88      1204
##            9       0.89      0.89      0.89      1219
## 
##     accuracy                           0.92     12600
##    macro avg       0.92      0.92      0.92     12600
## weighted avg       0.92      0.92      0.92     12600
```