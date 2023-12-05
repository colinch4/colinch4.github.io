---
layout: post
title: "[python] 합성마이너리티오버샘플링(SMOTE, Synthetic Minority Over-sampling Technique)"
description: " "
date: 2023-12-05
tags: [python]
comments: true
share: true
---

SMOTE(Synthetic Minority Over-sampling Technique)는 불균형한 데이터셋에서 소수 클래스 데이터의 수를 증가시키는 오버샘플링 방법 중 하나입니다. 이 기술은 합성마이너리티오버샘플링으로 알려져 있으며, 데이터 부족 문제를 해결하기 위해 널리 사용됩니다.

## SMOTE 작동 방식

SMOTE는 소수 클래스 샘플에 합성 샘플을 생성합니다. 이는 소수 클래스 샘플들을 이웃들과 가까워지도록 보간하는 방식으로 이뤄집니다. 간단한 SMOTE 알고리즘은 다음과 같은 단계로 진행됩니다.

1. 소수 클래스의 각 샘플에 대해 K개의 최근접 이웃을 찾습니다.
2. 이웃들 중에서 랜덤하게 선택한 이웃과 해당 샘플 사이의 차이를 계산합니다.
3. 차이만큼의 거리를 랜덤하게 선택한 값으로 곱한 다음, 선택된 샘플과 해당 차이를 더하여 합성 샘플을 생성합니다.
4. 이 과정을 반복하여 소수 클래스의 데이터셋을 오버샘플링합니다.

## SMOTE의 장점

SMOTE는 데이터 부족 문제를 해결하여 모델의 성능을 향상시킬 수 있습니다. 이를 통해 정확한 예측 모델을 구축할 수 있습니다. 또한, SMOTE는 데이터를 생성하여 소수 클래스의 정보를 보존하는 효과적인 방법입니다. 이는 합성된 데이터가 원래 데이터에 비해 더 다양한 특징을 가지게 함으로써 모델의 복잡성을 높일 수 있습니다.

## SMOTE의 한계

SMOTE는 간단하고 효과적인 방법이지만 몇 가지 한계점도 있습니다. 첫째, 합성된 데이터는 실제 데이터보다 더 가깝게 분포하게 됩니다. 따라서, 이를 고려하지 않고 모델을 구축하면 오버피팅(Overfitting)의 위험이 있습니다. 둘째, SMOTE는 데이터셋의 소수 클래스 샘플에만 적용될 수 있습니다. 따라서, 다중 클래스 문제나 연속적인 값들에 대해서는 다른 방법을 사용해야 합니다.

## SMOTE의 활용

SMOTE는 불균형한 데이터셋에서 예측 모델의 성능을 향상시키는 데 유용합니다. 특히, 소수 클래스에 관심이 있는 모델에서는 SMOTE를 적용하여 데이터셋을 형성하는 것이 좋습니다. SMOTE는 다양한 분야에서 널리 사용되며, 의료, 금융, 보안 등 다양한 분야에서 활용될 수 있습니다.

## 코드 예제

```python
from imblearn.over_sampling import SMOTE

# SMOTE 객체 생성
smote = SMOTE()

# 소수 클래스 데이터에 대해 SMOTE 적용
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
```

위 예제는 Python의 `imbalanced-learn` 라이브러리를 사용하여 SMOTE를 적용하는 방법을 보여줍니다. `SMOTE` 클래스 객체를 생성하고, `fit_resample` 메소드를 사용하여 소수 클래스 데이터에 대해 SMOTE를 적용합니다.

## 참고 자료

- [Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: synthetic minority over-sampling technique. Journal of artificial intelligence research, 16, 321-357.](https://arxiv.org/abs/1106.1813)
- [imbalanced-learn documentation, "Over-sampling methods"](https://imbalanced-learn.org/stable/over_sampling.html)
- [SMOTE: Synthetic Minority Over-sampling Technique](https://www.geeksforgeeks.org/ml-handling-imbalanced-data-with-smote-and-near-miss-algorithm-in-python/)