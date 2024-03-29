---
layout: post
title: "[python] 주성분 분석(PCA, Principal Component Analysis)"
description: " "
date: 2023-12-05
tags: [python]
comments: true
share: true
---

주성분 분석은 데이터셋의 차원을 줄이는데 사용되는 기법으로, 변수들 사이의 상관 관계를 고려하여 새로운 변수를 생성합니다. 이 새로운 변수들은 원래 변수들의 선형 변환으로 표현됩니다. PCA는 주로 데이터 시각화, 패턴 인식, 데이터 압축 등 다양한 분야에서 활용됩니다.

## 주성분 분석 알고리즘

PCA의 알고리즘은 다음과 같은 절차를 따릅니다.

1. 데이터의 준비: 주성분 분석을 수행하기 위해서는 데이터가 수치형이어야 합니다. 분석을 원하는 변수들을 선택하여 데이터셋을 구성합니다.
2. 데이터의 표준화: 주성분 분석은 변수들의 스케일에 민감하게 반응하므로, 변수들을 표준화하여 동일한 스케일을 갖도록 합니다.
3. 공분산 행렬 계산: 표준화된 데이터셋의 공분산 행렬을 계산합니다.
4. 공분산 행렬의 고유값과 고유벡터 구하기: 공분산 행렬의 고유값과 고유벡터를 계산합니다.
5. 주성분 선정: 고유값이 큰 순서대로 정렬한 후, 주성분을 선정합니다.
6. 주성분 계수 계산: 선택한 주성분으로부터 주성분 계수를 계산합니다. 이 계수는 주성분과 원래 변수들 사이의 선형 관계를 나타냅니다.

## PCA의 활용 예시

PCA는 다양한 분야에서 다양하게 활용될 수 있습니다. 몇 가지 예시를 들어보겠습니다.

### 데이터 시각화

고차원 데이터셋의 경우, 시각화가 어려울 수 있습니다. PCA를 사용하여 데이터의 차원을 줄여 시각화할 수 있습니다. 고유 벡터에 따라 데이터를 변환하면, 새로운 축으로 데이터를 투영할 수 있습니다. 이를 통해 데이터의 패턴이나 경향을 파악할 수 있습니다.

### 패턴 인식

PCA는 주성분의 중요도를 파악할 수 있기 때문에, 패턴 인식 문제에서도 활용됩니다. 예를 들어 얼굴 인식 문제에서, PCA를 사용하여 다양한 얼굴 이미지의 주성분을 추출하고, 분류 작업에 활용할 수 있습니다.

### 데이터 압축

PCA를 사용하여 데이터의 차원을 줄이면, 데이터의 크기가 줄어들게 됩니다. 이는 저장 공간을 절약하고 데이터 전송 속도를 향상시킬 수 있는 장점을 가지고 있습니다.

## 결론

주성분 분석은 데이터의 차원을 줄이는데 사용되는 강력한 기법입니다. 많은 분야에서 데이터 분석에 활용될 수 있으며, 데이터 시각화, 패턴 인식, 데이터 압축 등 다양한 목적으로 활용할 수 있습니다.

> 참고문헌
> - [Wikipedia: Principal Component Analysis](https://en.wikipedia.org/wiki/Principal_component_analysis)
> - Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning: Data Mining, Inference, and Prediction. New York, NY: Springer.