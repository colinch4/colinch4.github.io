---
layout: post
title: "[python] scikit-learn을 사용한 Gaussian Mixture Model"
description: " "
date: 2023-12-01
tags: [python]
comments: true
share: true
---

Gaussian Mixture Model(GMM)은 데이터에 대한 혼합 분포를 표현하는 확률 모델입니다. 이 모델은 데이터가 여러 개의 가우시안 분포를 따른다고 가정하며, 각 가우시안 분포의 가중치와 파라미터를 추정하여 모델링합니다. 이번 포스트에서는 scikit-learn 패키지를 사용하여 GMM을 구현하는 방법에 대해 알아보겠습니다.

## 1. 패키지 설치

scikit-learn은 파이썬의 머신러닝 라이브러리로서 GMM 뿐만 아니라 다양한 머신러닝 알고리즘을 제공합니다. 이를 사용하기 위해서는 먼저 scikit-learn 패키지를 설치해야 합니다. 아래의 명령어를 사용하여 설치할 수 있습니다.

```
pip install scikit-learn
```

## 2. 데이터 전처리

GMM을 적용하기 전에 데이터를 적절하게 전처리해야 합니다. scikit-learn에서 제공하는 `StandardScaler`를 사용하여 데이터를 표준화하는 것이 일반적입니다. 예를 들어, 아래와 같이 데이터를 불러오고 표준화할 수 있습니다.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# 데이터 불러오기
data = np.array([[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]])

# 데이터 표준화
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
```

## 3. GMM 모델 학습

데이터 전처리가 완료되면, scikit-learn의 `GaussianMixture` 클래스를 사용하여 GMM 모델을 학습할 수 있습니다. 아래의 예시 코드에서는 2개의 가우시안 분포를 가진 GMM 모델을 만들고, 데이터를 이 모델에 fitting하는 방법을 보여줍니다.

```python
from sklearn.mixture import GaussianMixture

# GMM 모델 생성
gmm = GaussianMixture(n_components=2)

# 데이터 fitting
gmm.fit(scaled_data)
```

## 4. 모델 예측

학습된 GMM 모델을 사용하여 새로운 데이터에 대한 예측을 수행할 수 있습니다. 예측을 위해서는 `predict` 또는 `predict_proba` 메서드를 사용할 수 있습니다. `predict` 메서드는 각 샘플에 대한 예측한 클러스터를 반환하며, `predict_proba` 메서드는 각 샘플이 각 클러스터에 속할 확률을 반환합니다.

```python
# 예측
new_data = np.array([[3, 5], [4, 7]])
scaled_new_data = scaler.transform(new_data)

predictions = gmm.predict(scaled_new_data)
probabilities = gmm.predict_proba(scaled_new_data)

print("Predicted clusters:", predictions)
print("Probabilities:", probabilities)
```

## 5. 결과 시각화

마지막으로, GMM을 사용한 결과를 시각화할 수 있습니다. 이를 위해서는 matplotlib 또는 seaborn과 같은 시각화 라이브러리를 사용할 수 있습니다.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 시각화
sns.scatterplot(x=scaled_data[:, 0], y=scaled_data[:, 1], hue=gmm.predict(scaled_data))

# 예측 결과 시각화
sns.scatterplot(x=scaled_new_data[:, 0], y=scaled_new_data[:, 1], hue=predictions, marker='x')

plt.show()
```

위의 코드에서는 학습된 GMM을 이용하여 새로운 데이터를 클러스터링하고, 결과를 산점도로 시각화하는 방법을 보여줍니다.

이제 여러분은 scikit-learn을 사용하여 Gaussian Mixture Model을 구현하는 방법을 알게 되었습니다. GMM은 클러스터링, 이상치 탐지 및 밀도 추정과 같은 다양한 문제에 널리 사용되는 모델입니다. 따라서 이러한 모델을 잘 이해하고 활용할 수 있다면 여러분의 머신러닝 업무에 큰 도움이 될 것입니다.

## 참고자료

- scikit-learn 공식 문서: <https://scikit-learn.org/stable/modules/mixture.html#gaussian-mixture>
- Python Machine Learning by Sebastian Raschka and Vahid Mirjalili