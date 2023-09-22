---
layout: post
title: "keras imagedatagenerator 예제"
description: " "
date: 2023-09-22
tags: [Keras, ImageDataGenerator]
comments: true
share: true
---

`ImageDataGenerator` 클래스는 Keras에서 이미지 데이터를 증강하고 다양한 변환을 적용하기 위해 사용되는 도구입니다. 이 클래스를 사용하면 이미지 데이터셋을 더 다양하고 다양한 각도에서 기계 학습 모델을 훈련할 수 있습니다.

다음은 `ImageDataGenerator`를 사용하여 데이터 증강인 이미지 회전 예제입니다.

```python
from keras.preprocessing.image import ImageDataGenerator

# ImageDataGenerator 객체 생성
datagen = ImageDataGenerator(rotation_range=20)

# 이미지 데이터 로드
image = load_image('image.jpg')

# 이미지 변환 적용
transformed_image = datagen.random_transform(image)
```

위의 예제에서 `ImageDataGenerator` 객체를 생성하고 `rotation_range` 매개 변수를 사용하여 이미지 회전을 설정했습니다. 그런 다음 `random_transform` 메서드를 사용하여 이미지에 변환을 적용합니다.

또한 `ImageDataGenerator`를 사용하여 이미지 데이터의 크기 조정, 이동, 확대/축소, 수평/수직 반전 등 다양한 변환을 적용할 수도 있습니다. 이러한 변환은 데이터 증강을 통해 모델의 일반화 성능을 향상시킬 수 있습니다.

ImageDataGenerator를 사용하여 이미지 데이터를 증강하는 방법에 대한 자세한 내용은 Keras 공식 문서를 참조하세요.

[#Keras](https://www.keras.io/) [#ImageDataGenerator](https://www.keras.io/api/preprocessing/image/#imagedatagenerator-class)