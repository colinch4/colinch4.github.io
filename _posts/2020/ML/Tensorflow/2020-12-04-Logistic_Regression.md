---
layout: post
title: "[Tensorflow] Logistic Regression"
description: " "
date: 2020-12-04
tags: [Tensorflow]
comments: true
share: true
---

## Logistic Regression

> **TF2.x**를 가지고 **Logistic Regression** 모델을 타이타닉 예제를 통해 구현해 본다.



## Library

```python
import numpy as np
import pandas as pd
import tensorflow as tf

import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequntial
from tensorflow.keras.layers import Flattern, Dense
from tensorflow.keras.optimizers import SGD

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
## from scipy import stats

```





## Feature engineering

> 쓰지 않을 독립변수가 있기 때문에 그러한 독립변수를 제거하고 문자로 표현된것을 숫자로 바꿔주는 작업이 필요하다.

* DataSet 불러오기

```python
df = pd.read_csv('./data/titanic/train.csv')
display(df.head())
```

![image-20201015021637370](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201015021637370.png?raw=true)



* 쓰지 않을 column 제거 : `PassengerId`, `Cabin`, `Ticket`, `Fare`, `Name`  삭제

```python
training_data = df.drop(['PassengerId','Cabin','Ticket', 'Fare', 'Name'], axis=1)
```

![image-20201015021841745](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201015021841745.png?raw=true)



* 결측치 확인 : `innull()` 을 통해 결측치를 확인해 본다.

```python
print(training_data.isnull().sum())
## Survived      0
## Pclass        0
## Sex           0
## Age         177
## SibSp         0
## Parch         0
## Embarked      2
## dtype: int64
```



* `Sex` 처리 : `map` 함수를 사용해 처리한다.

```python
sex_mapping = {'male':0, 'female':1}
training_data['Sex'] = training_data['Sex'].map(sex_mapping) 
head
```

![image-20201015023532983](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201015023532983.png?raw=true)



* `SibSp`, ` Parch ` 처리 : 하나의 변수 Family` 로 합쳐준다.

```python
training_data['Family'] = training_data[['SibSp', 'Parch']].values.sum(axis=1)
training_data = training_data.drop(['SibSp', 'Parch'], axis=1)
```

![image-20201015023640286](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201015023640286.png?raw=true)



* `Age` 처리 : **median** 값으로 결측치를 바꿔주고 Age binning을 해준다.

```python
## 결측치 처리
age_median = np.nanmedian(training_data['Age'])
training_data['Age'] = training_data['Age'].fillna(age_median)

## binning
training_data.loc[training_data['Age']<25,'Age'] = 0
training_data.loc[(training_data['Age']>=25) & (training_data['Age']<50),'Age'] = 1
training_data.loc[(training_data['Age']>=50),'Age'] = 2
```

![image-20201015024431687](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201015024431687.png?raw=true)



* `Embarked` 처리 :  결측치를 `Q`로 처리 하고 `map` 함수를 이용해 처리한다.

```python
training_data['Embarked'] = training_data['Embarked'].fillna('Q')
embarked_mapping = {'S':0, 'C':1, 'Q':2}
training_data['Embarked'] = training_data['Embarked'].map(embarked_mapping)
```

![image-20201015030014939](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201015030014939.png?raw=true)



## Data Split 및 Normalization

> `train_set` 과 `test_set`으로 7:3 비율로 분할해주고 `Pclass` 변수에 대해서 Normalization 해준다.

* Data split

```python
x_data = training_data.drop('Survived', axis=1)
t_data = training_data['Survived']

x_data_train, x_data_train, t_data_train, t_data_test = \
train_test_split(x_data, t_data, test_size = 0.3, random_state=0)
```

* Normalization : `MinMaxScaler`를 사용해 처리한다.

```python
scaler_x = MinMaxScaler()
scaler_x.fit(x_data_train)
x_data_train_norm = scaler_x.transform(x_data_train)
x_data_test_norm  = scaler_x.transform(x_data_test)

del x_data_test
del x_data_train
```





## Tensorflow 구현

> **TF2.xx**를 통해 실질적인 구현을 해본다.

* 모델 및 layer 생성, compile

```python
keras_model = Sequential()
keras_model.add(Flatten(input_shape=(x_data_train_norm.shape[1],)))
keras_model.add(Dense(1, activation='sigmoid'))

keras_model.compile(optimizer=SGD(learning_rate=1e-3),
                    loss='binary_crossentropy',
                    metrics=['accuracy'])
```

* 학습

```python
result = keras_model.fit(x_data_train_norm, t_data_train_norm,
            	         epochs = 1000,
		                 verbose = 0,
         		         validataion_split = 0.3)
```

* 결과

```python
keras_result = keras_model.evaluate(x_data_test_norm, t_data_test)
print('TF2.0 정확도는 : {}'.format(keras_result))

#268/268 [==============================] - 0s 27us/sample - loss: 0.5160 - accuracy: #0.8097

## TF2.0 정확도는 : [0.5316909854091815, 0.78731346]
```



* 그래프 그려보기

```python
print(type(result))
## <class 'tensorflow.python.keras.callbacks.History'>
print(result.history)
## dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])

plt.plot(result.history['accuracy'], color='b')
plt.plot(result.history['val_accuracy'], color='r')

plt.show()
```

![image-20201015032402799](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20201015032402799.png?raw=true)



## sklearn 과 비교

> 결과를 확인하기 위해 sklearn의 결과와 비교해 본다.

```python
sklearn_model = LogisticRegression()
sklearn_model.fit(x_data_train_norm, t_data_train)
sklearn_result = sklearn_model.score(x_data_test_norm, t_data_test)

print('sklearn의 정확도는 : {}'.format(sklearn_result))
## sklearn의 정확도는 : 0.7947761194029851
```





## 결론

> `sklearn`과 `tensorflow`의 결과는 비슷하게 나왔다.