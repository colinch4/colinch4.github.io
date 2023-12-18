---
layout: post
title: "[python] Jupyter Notebook에서 기계 학습 라이브러리 (scikit-learn, tensorflow 등) 사용하기"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

Jupyter Notebook을 사용하면 데이터 분석 및 기계 학습 모델을 개발하고 테스트하는 과정을 시각적으로 효율적으로 관리할 수 있습니다. 이 블로그 포스트에서는 Jupyter Notebook에서 기계 학습 라이브러리를 효과적으로 활용하는 방법에 대해 알아보겠습니다.

## scikit-learn으로 간단한 분류 모델 개발하기

scikit-learn은 파이썬의 기계 학습 라이브러리로, 간편하게 사용할 수 있는 API를 제공합니다. 먼저, Jupyter Notebook에서 다음과 같이 scikit-learn을 import하여 분류 모델을 개발할 수 있습니다.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
```

위 코드에서는 scikit-learn의 붓꽃 데이터셋을 로드하고, K-최근접 이웃 분류기를 사용하여 간단한 분류 모델을 개발하는 예시입니다. 개발한 모델은 다양한 평가 기준을 활용하여 성능을 평가할 수 있습니다.

## TensorFlow로 신경망 모델 훈련하기

TensorFlow는 딥 러닝 라이브러리로, Jupyter Notebook에서 신경망 모델의 훈련 및 시각화를 효과적으로 수행할 수 있습니다. 다음은 TensorFlow를 활용하여 간단한 신경망 모델을 훈련하는 예시입니다.

```python
import tensorflow as tf
from tensorflow.keras import layers

model = tf.keras.Sequential([
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 데이터를 로드하고 모델을 훈련하는 코드
```

위 코드에서는 TensorFlow 라이브러리를 사용하여 신경망 모델을 구성하고, 훈련에 필요한 설정을 지정하는 예시입니다.

## 결론

Jupyter Notebook을 활용하여 scikit-learn 및 TensorFlow와 같은 기계 학습 라이브러리를 효과적으로 활용할 수 있습니다. 데이터 분석 및 모델 개발 프로세스를 시각적으로 관리하면서, 라이브러리의 다양한 기능을 활용하여 복잡한 모델도 간편하게 구성할 수 있습니다.

위 예시를 통해 Jupyter Notebook에서 기계 학습 라이브러리를 활용하는 방법을 익히고, 데이터 과학 및 기계 학습 프로젝트를 보다 효율적으로 수행할 수 있습니다.

참고문헌:
- https://scikit-learn.org/stable/
- https://www.tensorflow.org/