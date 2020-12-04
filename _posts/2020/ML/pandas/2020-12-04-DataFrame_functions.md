---
layout: post
title: "[pandas] DataFrame 함수 1"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---

# DataFrame의 분석을 위한 함수들(1)

> `Pandas`에 있는 `DataFrame`에 관한 함수들에 대해서 알아본다.



## 1. np.nan

> `DataFrame`에 `NaN`값을 지정하고 싶을때 사용된다.

```python
data = [[2, np.nan],
       [7,-3],
       [np.nan, np.nan],
       [1, -2]]
df = pd.DataFrame(data,
                  columns=['one', 'two'],
                  index = ['a', 'b', 'c', 'd'])
display(df)
```

![image-20200913211043928](markdown-images/image-20200913211043928.png)



## 2. sum

> Dataframe의 `NaN` 값이 존재할 때의 합계를 다룬다. `ndarray`와 달리 `axis`를 정의하지 않으면 `axis=0`으로 default 된다. 위의 예제를 계속 사용한다.

**덧셈시 `NaN` 값은 0으로 처리되서 제외하고 더해진다.**

* axis = 0

```python
print(df.sum())
# one    10.0
# two    -5.0
# dtype: float64
```

* axis = 1

```python
print(df.sum(axis=1))
# one    10.0
# two    -5.0
# dtype: float64
```

* 원하는 행의 합

```python
print(df.iloc[1:3,:].sum(axis=1))
# b    4.0
# c    0.0
# dtype: float64
```



## 3. date_range

>날짜형식의 값과 기간을 입력하면 그 만큼의 입력날짜의 기간만큼 `DatetimeIndex`가 생성된다.

아래 예제를 보자.

```python
import pandas as pd
import numpy as np

np.random.seed(1)

df.pd.DataFrame(np.random.randint(0, 10, (6, 4)), columns = ['A','B','C','D'])
display(df)
```

![image-20200913203121515](markdown-images/image-20200913203121515.png)

아래와 같이 날짜형식의 `index`를 `date_range`를 이용해 생성 가능하다.

```python
df.index = pd.date_range('20200913',periods=6)
print(df.index)
# DatetimeIndex(['2020-09-13', '2020-09-14', '2020-09-15', '2020-09-16',
#                '2020-09-17', '2020-09-18'],
#               dtype='datetime64[ns]', freq='D')
```

![image-20200913203225377](markdown-images/image-20200913203225377.png)



## 4. reindex

> `reindex`를 통해 쉽게 `index `및 `columns`들의 **순서**만 교체할 수 있다. **(새로운것들로의 정정이 아니다.)** 위의 예제를 계속 사용한다.

* 실제 값을 변경하는게 아니므로 새롭게 정의해 주어야 한다.

```python
df2 = df.reindex(index = np.random.permutation(df.index), columns = ['B','C','D','A'])
display(df2)
```

![image-20200913220444780](markdown-images/image-20200913220444780.png)

* 참고로 `np.random.permutation`에서 `np.random.shuffle`을 사용하면 Error가 발생한다.

```python
np.random.shuffle(df.index)
# TypeError: Index does not support mutable operations
```

