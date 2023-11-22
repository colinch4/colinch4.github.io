---
layout: post
title: "[python] 파이썬 PyTorch에서 주요 모델 아키텍처인 ResNet, VGG, Inception 등을 사용하는 방법은?"
description: " "
date: 2023-11-22
tags: [python]
comments: true
share: true
---

## ResNet 사용하기
```python
import torch
import torchvision.models as models

# 사전 훈련된 ResNet 모델 불러오기
resnet_model = models.resnet18(pretrained=True)

# 모델을 사용하여 이미지 분류
input_tensor = torch.randn(1, 3, 224, 224)
output = resnet_model(input_tensor)
```

## VGG 사용하기
```python
import torch
import torchvision.models as models

# 사전 훈련된 VGG 모델 불러오기
vgg_model = models.vgg16(pretrained=True)

# 모델을 사용하여 이미지 분류
input_tensor = torch.randn(1, 3, 224, 224)
output = vgg_model(input_tensor)
```

## Inception 사용하기
```python
import torch
import torchvision.models as models

# 사전 훈련된 Inception 모델 불러오기
inception_model = models.inception_v3(pretrained=True)

# 모델을 사용하여 이미지 분류
input_tensor = torch.randn(1, 3, 299, 299)
output = inception_model(input_tensor)
```

주의: 각각의 모델은 입력 텐서의 크기와 형식에 맞게 조정되어야 합니다. 예시에서는 간단히 랜덤 입력 텐서를 사용했지만, 실제로 사용할 때에는 적절한 크기의 이미지로 대체해야 합니다.

더 자세한 내용은 [PyTorch 공식 문서](https://pytorch.org/docs/stable/torchvision/models.html)를 참조하시기 바랍니다.