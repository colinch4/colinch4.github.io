---
layout: post
title: "[python] Jupyter Notebook에서 데이터 분석 라이브러리 (pandas, numpy 등) 사용하기"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

Jupyter Notebook은 데이터 분석 및 시각화에 매우 유용한 도구입니다. 특히 Python의 데이터 분석 라이브러리인 pandas와 numpy를 사용하면 데이터를 효과적으로 다룰 수 있습니다.

## 1. 패키지 설치 및 불러오기

Jupyter Notebook에서 먼저 필요한 패키지를 설치하고 불러와야 합니다. 아래는 pandas와 numpy 패키지를 설치하고 불러오는 예제 코드입니다.

```python
!pip install pandas numpy
import pandas as pd
import numpy as np
```

## 2. 데이터 불러오기

이제 pandas를 사용하여 데이터를 불러와보겠습니다. CSV 파일을 예시로 들어보겠습니다.

```python
df = pd.read_csv('example.csv')
```

## 3. 데이터 분석 및 시각화

pandas와 numpy를 사용하여 데이터를 분석하고 시각화하는 것이 가능합니다. 예를 들어, 데이터프레임의 특정 열을 선택하여 시각화할 수 있습니다.

```python
import matplotlib.pyplot as plt
plt.plot(df['column1'], df['column2'])
plt.show()
```

이처럼 Jupyter Notebook에서 pandas와 numpy를 활용하여 데이터를 불러오고 분석하는 방법을 알아보았습니다.

더 많은 정보를 원하시면 아래 링크를 참고하시기 바랍니다.

- [Pandas 공식 문서](https://pandas.pydata.org/docs/)
- [NumPy 공식 문서](https://numpy.org/doc/)
- [Jupyter Notebook 공식 문서](https://jupyter-notebook.readthedocs.io/en/stable/)