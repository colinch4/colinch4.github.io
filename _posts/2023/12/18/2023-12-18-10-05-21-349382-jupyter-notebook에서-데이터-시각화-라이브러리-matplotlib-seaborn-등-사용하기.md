---
layout: post
title: "[python] Jupyter Notebook에서 데이터 시각화 라이브러리 (matplotlib, seaborn 등) 사용하기"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

Jupyter Notebook은 데이터 시각화를 위한 뛰어난 도구로, 함께 사용되는 다양한 라이브러리들이 있습니다. 이번 포스트에서는 주로 활용되는 데이터 시각화 라이브러리인 *matplotlib*와 *seaborn*에 대해 알아보겠습니다.

## Matplotlib 라이브러리

[*Matplotlib*](https://matplotlib.org/)는 파이썬에서 데이터 시각화를 위한 가장 기본적인 도구 중 하나입니다. 다음은 간단한 선 그래프를 *matplotlib*로 그리는 예제 코드입니다.

```python
import matplotlib.pyplot as plt

# 데이터
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# 선 그래프 그리기
plt.plot(x, y)
plt.show()
```

## Seaborn 라이브러리

[*Seaborn*](https://seaborn.pydata.org/)은 *matplotlib*를 기반으로 한 통계 데이터 시각화에 특화된 라이브러리입니다. 아래 예제는 *seaborn*을 사용하여 상자 그림을 그리는 코드입니다.

```python
import seaborn as sns
import pandas as pd

# 데이터 프레임 생성
data = pd.DataFrame({'Category': ['A', 'A', 'B', 'B', 'B', 'C'], 'Value': [1, 2, 3, 4, 5, 6]})

# 상자 그림 그리기
sns.boxplot(x='Category', y='Value', data=data)
```

이상으로 데이터 시각화를 위해 *matplotlib*와 *seaborn*을 Jupyter Notebook에서 활용하는 방법에 대해 살펴보았습니다. 데이터 시각화는 분석 결과를 이해하고 다른 사람에게 전달하는 데 매우 중요한 요소이므로, 이러한 라이브러리들을 잘 활용하여 효과적인 시각화를 구현할 수 있도록 노력해야 합니다.