---
layout: post
title: "[python] CNN(Convolutional Neural Network)"
description: " "
date: 2023-12-12
tags: [python]
comments: true
share: true
---

이미지 분류는 기계 학습의 중요한 응용 분야 중 하나이다. CNN은 이미지 분류 작업에 효과적으로 사용되는 인기 있는 신경망 구조 중 하나이다.

## CNN의 개요

CNN은 이미지 분류를 위해 설계된 신경망으로, 이미지의 특징을 추출하고 이를 기반으로 이미지를 분류한다. CNN은 여러 계층으로 이루어진다. 각 계층은 **합성곱 계층(Convolutional Layer)**, **풀링 계층(Pooling Layer)**, **완전 연결 계층(Fully Connected Layer)**으로 구성된다. 합성곱 계층은 이미지의 특징을 감지하고 추출하는 역할을 한다. 풀링 계층은 이미지의 크기를 줄이는 역할을 하고, 완전 연결 계층은 최종적으로 이미지를 분류하는 역할을 수행한다.

## CNN의 구현

Python의 Keras 라이브러리를 사용하여 간단한 CNN을 구현해보자.

```python
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# CNN 모델 생성
model = Sequential()

# 첫 번째 합성곱 계층 추가
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))

# 첫 번째 풀링 계층 추가
model.add(MaxPooling2D(pool_size=(2, 2)))

# 두 번째 합성곱 계층 추가
model.add(Conv2D(32, (3, 3), activation='relu'))

# 두 번째 풀링 계층 추가
model.add(MaxPooling2D(pool_size=(2, 2)))

# 이미지를 1차원 배열로 변환
model.add(Flatten())

# 완전 연결 계층 추가
model.add(Dense(units=128, activation='relu'))

# 출력 계층 추가
model.add(Dense(units=1, activation='sigmoid'))

# 모델 컴파일
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

위의 코드는 Keras를 사용하여 간단한 CNN 모델을 생성하는 예시이다.

CNN은 이미지 분류 작업에서 뛰어난 성능을 보이며, Python의 Keras와 같은 라이브러리를 사용하여 비교적 쉽게 구현할 수 있다.

이상으로 이미지 분류에 CNN을 사용하는 방법에 대해 설명했다.

## Reference
- [Keras documentation](https://keras.io)