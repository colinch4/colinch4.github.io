---
layout: post
title: "[python] Jupyter Notebook에서 이미지 처리 라이브러리 (pillow, opencv 등) 사용하기"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

Jupyter Notebook은 이미지 처리와 관련된 작업을 쉽게 수행할 수 있는 훌륭한 환경입니다. 다양한 이미지 처리 작업을 수행하기 위해 Pillow와 OpenCV와 같은 이미지 처리 라이브러리를 쉽게 사용할 수 있습니다.

## Pillow 라이브러리 활용하기

Pillow는 파이썬 이미지 라이브러리로, 이미지 처리 및 조작을 위한 다양한 기능을 제공합니다. Jupyter Notebook에서 Pillow 라이브러리를 사용하여 이미지를 로드하고 조작하는 방법을 살펴보겠습니다.

```python
from PIL import Image

# 이미지 로드
image = Image.open('example.jpg')

# 이미지 크기 조정
resized_image = image.resize((200, 200))

# 이미지 저장
resized_image.save('resized_image.jpg')
```

위의 예제에서는 Pillow의 `Image` 모듈을 사용하여 이미지를 로드하고 크기를 조정한 다음, 새로운 파일로 저장하는 방법을 보여줍니다.

## OpenCV 라이브러리 활용하기

OpenCV는 컴퓨터 비전을 위한 오픈소스 컴퓨터 비전 및 머신 러닝 소프트웨어 라이브러리입니다. Jupyter Notebook에서 OpenCV를 사용하여 이미지를 처리하는 방법을 살펴보겠습니다.

```python
import cv2
import matplotlib.pyplot as plt

# 이미지 로드
image = cv2.imread('example.jpg')

# 이미지 보기
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
```

위의 예제에서는 OpenCV를 사용하여 이미지를 로드하고 Matplotlib를 활용하여 이미지를 보여주는 방법을 보여줍니다.

이처럼 Jupyter Notebook에서 Pillow와 OpenCV와 같은 이미지 처리 라이브러리를 사용하여 다양한 이미지 처리 및 분석 작업을 쉽게 수행할 수 있습니다.

## 참고 자료
- Pillow 공식 문서: [링크](https://pillow.readthedocs.io/en/stable/)
- OpenCV 공식 문서: [링크](https://opencv.org/)
- Jupyter Notebook 공식 사이트: [링크](https://jupyter.org/)