---
layout: post
title: "from tensorflow.keras.preprocessing.image import imagedatagenerator 예제"
description: " "
date: 2023-09-22
tags: [tensorflow, keras]
comments: true
share: true
---

먼저, 필요한 라이브러리를 import합니다.

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
```

다음으로, `ImageDataGenerator`를 초기화하고 필요한 매개변수를 설정합니다. 이미지 데이터를 전처리하기 위해 다양한 옵션들을 제공합니다. 예를 들어, `rescale`, `rotation_range`, `width_shift_range`, `height_shift_range`, `shear_range`, `zoom_range`, `horizontal_flip`, `vertical_flip` 등의 옵션을 사용하여 데이터를 변형할 수 있습니다.

```python
datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=True
)
```

이제 `ImageDataGenerator`를 사용하여 이미지 데이터를 불러올 수 있습니다. `flow_from_directory()` 메서드를 사용하여 디렉토리에서 이미지 데이터를 불러올 수 있습니다. 이 메서드는 이미지 데이터가 있는 디렉토리 경로와 이미지 크기, 배치 크기 등을 인자로 받습니다.

```python
train_data = datagen.flow_from_directory(
    'train_dir',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary'
)
```

위의 코드에서는 `train_dir` 경로에 있는 이미지 데이터를 불러옵니다. 불러온 데이터는 (224, 224) 크기로 조정되며, 배치 크기는 32로 설정됩니다. 클래스 모드는 `binary`로 설정되어 이진 분류 문제에 적합한 데이터를 생성합니다.

이제 데이터를 적절하게 전처리하고 학습에 사용할 수 있는 형태로 불러올 수 있습니다. 이것은 딥 러닝 모델을 학습시키기 위한 중요한 전처리 단계입니다.

이상으로 TensorFlow의 Keras API를 사용하여 이미지 데이터를 전처리하는 예제를 알아보았습니다. `ImageDataGenerator`를 사용하여 데이터를 증강하고, `flow_from_directory()`를 사용하여 이미지 데이터를 불러올 수 있습니다.

#tensorflow #keras