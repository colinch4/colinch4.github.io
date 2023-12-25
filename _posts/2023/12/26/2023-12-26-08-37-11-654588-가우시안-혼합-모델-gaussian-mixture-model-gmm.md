---
layout: post
title: "[R언어] 가우시안 혼합 모델 (Gaussian Mixture Model, GMM)"
description: " "
date: 2023-12-26
tags: [R언어]
comments: true
share: true
---

가우시안 혼합 모델 (Gaussian Mixture Model, GMM)은 확률 통계 모델 중 하나로, 여러 개의 가우시안 분포를 합쳐서 복잡한 데이터 분포를 모델링하는 데 사용됩니다. GMM은 데이터가 여러 개의 잠재적인 클러스터로부터 생성된 것으로 가정하며, 이를 통해 데이터를 클러스터링하거나 밀도 추정을 수행할 수 있습니다.

## GMM의 개념

GMM은 각 가우시안 분포의 평균 및 분산, 그리고 각 분포의 혼합 가중치로 구성됩니다. 이 가중치는 각 클러스터의 중요성을 나타내며, 새로운 데이터 포인트가 특정 클러스터에서 생성될 확률을 결정하는 데 사용됩니다. GMM은 Expectation-Maximization (EM) 알고리즘을 사용하여 클러스터의 파라미터를 추정하며, 주어진 데이터에 최적으로 맞는 모델을 찾습니다.

## GMM의 활용

GMM은 주로 클러스터링, 이상치 탐지, 차원 축소, 밀도 추정 등의 작업에 적용됩니다. 특히 GMM을 사용하면 복잡한 데이터 세트를 여러 개의 간단한 가우시안 분포로 모델링하여 문제를 해결할 수 있습니다.

```R
# install.packages("mclust")  # 필요한 경우 패키지 설치
library(mclust)

# GMM을 사용한 클러스터링
data <- iris[, -5]  # iris 데이터셋에서 종 속성 제외
model <- Mclust(data, G = 3)  # G=3인 경우 3개의 클러스터로 분류
cluster <- model$classification  # 각 데이터 포인트의 클러스터 할당
```

GMM은 실제 데이터 분석에서 널리 사용되는 모델이며, R 언어를 통해 간단하게 적용할 수 있습니다.

위 내용은 [패키지 매뉴얼](https://cran.r-project.org/web/packages/mclust/mclust.pdf)을 참고하여 작성되었습니다.