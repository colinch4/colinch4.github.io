---
layout: post
title: "imagedatagenerator flow_from_directory 예제"
description: " "
date: 2023-09-22
tags: [imagedatagenerator]
comments: true
share: true
---

```python
from keras.preprocessing.image import ImageDataGenerator

# 이미지 데이터 생성기 초기화
datagen = ImageDataGenerator(rescale=1./255)

# 학습용 데이터 가져오기
train_generator = datagen.flow_from_directory(
    '/path/to/train_directory',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# 검증용 데이터 가져오기
validation_generator = datagen.flow_from_directory(
    '/path/to/validation_directory',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# 테스트용 데이터 가져오기
test_generator = datagen.flow_from_directory(
    '/path/to/test_directory',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)
```

위 예제에서는 `ImageDataGenerator` 클래스를 사용하여 이미지 데이터를 처리합니다. `rescale` 매개변수를 사용하여 이미지 픽셀 값을 0과 1 사이로 정규화합니다.

`flow_from_directory` 함수를 호출하여 디렉토리에서 이미지 데이터를 가져옵니다. `target_size` 매개변수는 이미지의 크기를 지정할 수 있고, `batch_size`는 배치의 크기를 설정합니다. `class_mode` 매개변수는 분류 문제에서 사용할 클래스 모드를 지정합니다.

위 예제에서는 학습용, 검증용, 테스트용 데이터를 가져오는 세 개의 `generator`를 생성하고 있습니다. 각각의 이미지 데이터는 지정된 경로에 있는 디렉토리에서 가져오게 됩니다.