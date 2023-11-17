---
layout: post
title: "imagedatagenerator flow 예제"
description: " "
date: 2023-09-22
tags: [python]
comments: true
share: true
---

ImageDataGenerator는 Keras에서 제공하는 이미지 데이터를 증강하기 위한 유용한 도구입니다. 이를 사용하면 이미지 데이터에 다양한 변형을 적용하여 데이터셋의 다양성을 높일 수 있습니다. 아래는 ImageDataGenerator의 flow 메서드를 사용하는 예제입니다.

```python
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 데이터 경로 설정
train_data_dir = 'train_data_directory'
validation_data_dir = 'validation_data_directory'

# 데이터 증강을 위한 ImageDataGenerator 객체 생성
datagen = ImageDataGenerator(
    rescale=1./255,       # 이미지 스케일 조정
    rotation_range=30,    # 이미지 회전
    width_shift_range=0.1,    # 가로 방향으로 이동
    height_shift_range=0.1,   # 세로 방향으로 이동
    shear_range=0.2,      # 이미지 왜곡
    zoom_range=0.2,       # 이미지 확대/축소
    horizontal_flip=True,    # 수평 방향으로 뒤집기
    vertical_flip=True    # 수직 방향으로 뒤집기
)

# 학습 데이터셋 가져오기
train_generator = datagen.flow_from_directory(
    train_data_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

# 검증 데이터셋 가져오기
validation_generator = datagen.flow_from_directory(
    validation_data_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)

# 모델 생성 및 컴파일
model = tf.keras.models.Sequential(...)
model.compile(...)

# 모델 학습
model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=10,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size
)
```

위의 코드는 ImageDataGenerator를 사용하여 데이터 증강을 구현한 예제입니다. 주어진 디렉토리에서 이미지 데이터를 읽어와서 증강된 데이터를 생성하고, 이를 기반으로 학습 및 검증 데이터셋을 생성합니다. 마지막으로 모델을 생성하고 학습을 시작합니다.

ImageDataGenerator의 다양한 옵션을 사용하여 데이터를 증강하고, 생성된 데이터셋을 모델에 적용하여 성능을 향상시킬 수 있습니다. 이를 통해 더욱 풍부하고 다양한 데이터로 모델을 학습시킬 수 있게 됩니다.

#DeepLearning #ImageDataGenerator