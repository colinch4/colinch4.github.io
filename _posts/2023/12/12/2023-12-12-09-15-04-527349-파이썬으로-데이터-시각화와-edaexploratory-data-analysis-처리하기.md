---
layout: post
title: "[python] 파이썬으로 데이터 시각화와 EDA(Exploratory Data Analysis) 처리하기"
description: " "
date: 2023-12-12
tags: [python]
comments: true
share: true
---

이 글에서는 파이썬을 사용하여 데이터 시각화와 탐색적 데이터 분석(EDA)을 어떻게 수행하는지에 대해 알아보겠습니다.

## 1. 데이터 시각화

데이터 시각화는 데이터를 이해하고 분석하는 데 있어서 중요한 부분입니다. 파이썬에서는 주로 Matplotlib 및 Seaborn 라이브러리를 사용하여 데이터를 시각화합니다.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
data = sns.load_dataset('tips')

# 데이터 시각화
sns.pairplot(data)
plt.show()
```

위 코드는 Seaborn 라이브러리를 이용하여 데이터를 쌍으로(pairwise) 비교하는 그래프를 보여줍니다.

## 2. 탐색적 데이터 분석(EDA)

EDA는 데이터셋을 조사하고 주요 특징을 발견하기 위해 사용되는 분석 기술입니다. 파이썬에서는 Pandas 라이브러리를 통해 EDA를 수행할 수 있습니다.

```python
import pandas as pd

# 데이터 불러오기
data = pd.read_csv('data.csv')

# 데이터 요약 정보 확인
print(data.info())

# 데이터 분포 확인
print(data.describe())
```

위의 코드는 Pandas 라이브러리를 사용하여 데이터를 불러오고, 데이터의 요약 정보 및 분포를 확인합니다.

## 결론

파이썬을 사용하면 데이터를 시각화하고 EDA를 통해 데이터를 효과적으로 분석할 수 있습니다. Matplotlib, Seaborn 및 Pandas와 같은 라이브러리를 익혀두면 데이터 과학 및 분석 작업에 매우 유용합니다.

참고 자료:
- Matplotlib: [matplotlib.org](https://matplotlib.org/)
- Seaborn: [seaborn.pydata.org](https://seaborn.pydata.org/)
- Pandas: [pandas.pydata.org](https://pandas.pydata.org/)