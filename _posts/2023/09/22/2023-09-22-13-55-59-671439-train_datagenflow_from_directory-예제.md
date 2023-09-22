---
layout: post
title: "train_datagen.flow_from_directory 예제"
description: " "
date: 2023-09-22
tags: [ImageDataGenerator]
comments: true
share: true
---

`flow_from_directory` 함수는 디렉토리에서 이미지 데이터를 가져와서 데이터 생성기(generator)를 생성해주는 함수입니다. 이 함수를 사용하면 이미지 데이터를 실시간으로 로드하고, augmentation(증강) 및 정규화를 적용하여 모델 학습에 사용할 수 있습니다.

아래는 `flow_from_directory` 함수를 사용하여 디렉토리에서 데이터를 가져오는 예제 코드입니다.

```python
from keras.preprocessing.image import ImageDataGenerator

# 데이터 생성기 생성
train_datagen = ImageDataGenerator(
    rescale=1./255,  # 이미지 정규화
    shear_range=0.2,  # 이미지 변형 - 가로 선 긋기
    zoom_range=0.2,  # 이미지 변형 - 확대/축소
    horizontal_flip=True  # 이미지 변형 - 좌우 반전
)

# 학습 데이터 로드 및 augmentation 적용
train_generator = train_datagen.flow_from_directory(
    directory='train_images',  # 학습 데이터가 있는 디렉토리 경로
    target_size=(150, 150),  # 이미지 크기 조정
    batch_size=32,  # 배치 크기
    class_mode='binary'  # 분류 문제인 경우 'categorical' 또는 'binary'로 설정
)
```

위 코드에서는 `ImageDataGenerator` 클래스를 사용하여 데이터 생성기 객체 `train_datagen`을 생성합니다. 이 객체에는 이미지 정규화, 이미지 변형 등의 augmentation 설정들이 포함되어 있습니다.

그리고 `flow_from_directory` 함수를 사용하여 학습 데이터를 로드하고, augmentation을 적용한 데이터를 생성합니다. `directory` 매개변수에는 학습 데이터가 있는 디렉토리 경로를 지정하고, `target_size` 매개변수에는 이미지를 원하는 크기로 조정합니다. `batch_size` 매개변수는 한 번에 로드될 데이터의 개수를 의미하며, `class_mode` 매개변수는 분류 문제인 경우 'categorical' 또는 'binary'로 설정합니다.

위 예제 코드를 참고하여 디렉토리에서 데이터 생성을 위한 코드를 작성해보세요!

hashtags: `#데이터생성기`, `#ImageDataGenerator`