---
layout: post
title: "[python] 데이터 차원축소(Dimensionality Reduction) 방법"
description: " "
date: 2023-12-05
tags: [python]
comments: true
share: true
---

데이터 분석이나 머신러닝 과정에서 종종 데이터의 차원이 높아 성능이 저하되는 경우가 발생합니다. 이런 경우에는 차원축소(Dimensionality Reduction) 기법을 사용하여 데이터의 특징을 보존하면서 차원을 줄일 수 있습니다. 차원축소는 데이터의 복잡성을 줄여 연산 비용을 감소시키고, 시각화를 통해 데이터를 이해하기 쉽게 만들어줍니다.

## 1. 주성분 분석(Principal Component Analysis, PCA)
PCA는 가장 일반적으로 사용되는 차원축소 알고리즘입니다. PCA는 고차원 데이터를 가지고 있는 경우, 데이터의 분산을 최대한 보존하는 새로운 주축(Principal Component)를 찾아 데이터를 투영합니다. 이렇게 찾은 주축은 원래 데이터의 차원보다 낮으며, 데이터의 분산을 최대한 보존하기 때문에 원래 데이터의 특성을 잘 보존하면서도 차원을 줄일 수 있습니다.

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)  # 주성분의 개수를 2로 설정
reduced_data = pca.fit_transform(data)
```

## 2. t-SNE(t-Distributed Stochastic Neighbor Embedding)
t-SNE는 고차원의 데이터를 시각화하기 위해 사용되는 차원축소 알고리즘입니다. t-SNE는 고차원 데이터의 국부적 구조를 보존하려고 노력하며, 비슷한 특징을 가진 데이터들을 가깝게 배치시킵니다. 이렇게 배치된 데이터는 시각화를 통해 그룹화되어 있는 패턴을 쉽게 파악할 수 있습니다.

```python
from sklearn.manifold import TSNE
tsne = TSNE(n_components=2)  # 2차원으로 축소
reduced_data = tsne.fit_transform(data)
```

## 3. LLE(Locally Linear Embedding)
LLE는 데이터의 국부 구조를 보존하는 비선형 차원축소 알고리즘입니다. LLE는 각 데이터 포인트를 근접 이웃 데이터 포인트들로 선형적으로 잘 표현할 수 있는 가중치를 찾아 차원을 줄입니다. 이렇게 찾은 가중치를 사용하여 원 데이터를 새로운 공간으로 투영함으로써 차원을 축소합니다.

```python
from sklearn.manifold import LocallyLinearEmbedding
lle = LocallyLinearEmbedding(n_components=2)  # 2차원으로 축소
reduced_data = lle.fit_transform(data)
```

위에서 소개한 방법들은 데이터 차원축소를 위한 대표적인 알고리즘이지만, 다른 방법들도 여러 가지 존재합니다. 특정한 데이터에 적합한 차원축소 방법을 선택하여 사용하는 것이 중요합니다.