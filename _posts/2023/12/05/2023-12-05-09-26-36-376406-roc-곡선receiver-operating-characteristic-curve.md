---
layout: post
title: "[python] ROC 곡선(Receiver Operating Characteristic Curve)"
description: " "
date: 2023-12-05
tags: [python]
comments: true
share: true
---

ROC 곡선은 이진 분류 모델의 성능을 평가하는 데 사용되는 도구입니다. 이는 분류 임계값의 변화에 따른 모델의 민감도와 특이도를 시각화하는 방법입니다. ROC 곡선 아래의 면적을 AUC(Area Under the Curve)라고 하며, AUC의 값이 클수록 모델의 성능이 좋다고 판단할 수 있습니다.

## ROC 곡선 그리기

다음은 Python에서 ROC 곡선을 그리는 방법입니다.

```python
import matplotlib.pyplot as plt
from sklearn.metrics import plot_roc_curve

def plot_roc(y_true, y_score):
    # y_true: 실제 클래스 레이블
    # y_score: 모델의 확률 예측값
    
    # ROC 곡선 그리기
    plt.figure(figsize=(8, 6))
    ax = plt.gca()
    roc_auc = plot_roc_curve(model, X_test, y_test, ax=ax)
    
    # 그래프 꾸미기
    plt.plot([0, 1], [0, 1], color='navy', linestyle='--', lw=2)
    plt.title('Receiver Operating Characteristic Curve')
    plt.xlabel('False Positive Rate (1 - Specificity)')
    plt.ylabel('True Positive Rate (Sensitivity)')
    plt.legend(loc='lower right')
    
    plt.show()
```

위의 코드에서 `y_true`는 실제 클래스 레이블을, `y_score`는 모델의 확률 예측값을 가리킵니다. `model`, `X_test`, `y_test`는 각각 이미 학습된 분류 모델, 테스트 데이터의 특성 값, 테스트 데이터의 클래스 레이블을 나타냅니다.

`plot_roc_curve` 함수를 사용하여 ROC 곡선을 그릴 수 있으며, 이를 통해 모델의 성능을 시각화할 수 있습니다. 

## 결론

ROC 곡선은 이진 분류 모델의 성능을 평가하고 시각화하는 방법 중 하나입니다. AUC 값은 모델의 성능을 나타내는 지표로 사용되며, 높을수록 모델의 성능이 우수하다는 것을 의미합니다. ROC 곡선을 활용하여 모델의 분류 성능을 평가하고 비교할 수 있습니다.