---
layout: post
title: "[python] 파이썬 PyTorch에서 이미지 분류를 위한 전이 학습(transfer learning)을 사용하는 방법은?"
description: " "
date: 2023-11-22
tags: [python]
comments: true
share: true
---

이미지 분류에 대한 전이 학습은 딥러닝 모델을 미리 학습된 모델로 초기화하고, 이를 새로운 작업에 맞게 fine-tuning하는 방법입니다. 이를 통해 작은 데이터셋에 대해서도 탁월한 성능을 얻을 수 있습니다.

이제 PyTorch에서 전이 학습을 사용하여 이미지 분류를 진행하는 방법에 대해 살펴보겠습니다.

1. 라이브러리 import
```python
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from torch import nn, optim
from torch.utils.data import DataLoader, Dataset
```

2. 데이터 로드 및 변환
```python
# 데이터셋 폴더 경로
data_path = 'dataset/'

# 변환 작업 설정
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# 데이터셋 로드
dataset = YourDataset(data_path, transform=transform)
```

3. 미리 학습된 모델 불러오기
```python
# 사전 학습된 ResNet 모델 가져오기
model = models.resnet50(pretrained=True)
```

4. 모델 구조 수정
```python
# 모델의 마지막 레이어 교체
model.fc = nn.Linear(model.fc.in_features, num_classes)
```

5. Optimizer 및 Loss 함수 설정
```python
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
```

6. 학습 및 평가
```python
# 데이터 로더 설정
batch_size = 32
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# 학습 반복 횟수 설정
epochs = 10

# 모델 학습
for epoch in range(epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

# 모델 평가
accuracy = evaluate(model, test_dataloader)
print(f"Accuracy: {accuracy}")
```

위의 방법을 통해 PyTorch에서 전이 학습을 사용하여 이미지 분류를 진행할 수 있습니다. 데이터셋에 따라서 모델 설정 및 하이퍼파라미터를 조정해야 할 수도 있으니, 자신의 데이터에 맞게 적절하게 수정해 주세요. 또한, 모델의 성능을 개선하기 위해 추가적인 fine-tuning이나 데이터 증강을 적용해 볼 수도 있습니다.

참고 문서:
- [PyTorch 공식 문서](https://pytorch.org/tutorials/intermediate/transfer_learning_tutorial.html)
- [torchvision 모델 사용 예제](https://pytorch.org/hub/pytorch_vision_resnet/)
- [공개된 전이 학습 모델들](https://pytorch.org/docs/stable/torchvision/models.html)