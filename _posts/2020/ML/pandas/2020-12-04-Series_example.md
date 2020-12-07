---
layout: post
title: "[pandas] Series example"
description: " "
date: 2020-12-04
tags: [pandas]
comments: true
share: true
---

# Series example

##### Q1.  A공장의 2020-01-01부터 10일간 생산량을 Series로 저장할 예정이다. 생산량은 평균이 50이고 표준편차가 5인 정규분포에서 랜덤하게 생성하는데 정수로 처리하여라.

##### B공장도 마찬가지로 2020-01-01부터 10일간의 생산량을 Series로 저장할 예정이고 생산량은 평균이 70이고 표준편차가 8인 정규분포에서 램덤하게 생성해 정수로 처리하여라.

##### 날짜별로 모든 공장의 생산량 합계를 구하여 보자!!!!

```python
from datetime import datetime, date, timedelta
import numpy as np
import pandas as pd

start_day = datetime(2020,1,1)
s_a = pd.Series([ int(i) for i in np.random.normal(50,5,(10,))],
                index = [start_day+timedelta(i) for i in range(0,10) ], 
                name = "A공장"  )  
print(s_a)
# 2020-01-01
# 2020-01-01    49
# 2020-01-02    49
# 2020-01-03    41
# 2020-01-04    54
# 2020-01-05    54
# 2020-01-06    42
# 2020-01-07    42
# 2020-01-08    53
# 2020-01-09    56
# 2020-01-10    47
# Name: A공장, dtype: int64
```

```python
s_b = pd.Series([ int(i) for i in np.random.normal(70,8,(10,))],
                index = [start_day+timedelta(i) for i in range(0,10) ], 
                name = "B공장"  )
print(s_b)
# 2020-01-01    67
# 2020-01-02    74
# 2020-01-03    62
# 2020-01-04    76
# 2020-01-05    73
# 2020-01-06    78
# 2020-01-07    75
# 2020-01-08    59
# 2020-01-09    70
# 2020-01-10    74
# Name: B공장, dtype: int64
```

```python
print(s_a + s_b)
# 2020-01-01    116
# 2020-01-02    123
# 2020-01-03    103
# 2020-01-04    130
# 2020-01-05    127
# 2020-01-06    120
# 2020-01-07    117
# 2020-01-08    112
# 2020-01-09    126
# 2020-01-10    121
# dtype: int64
```



##### Q2. 만약 시작날짜가 다르다면 어떻게 될까? B공장의  작업 시작일을 2020-01-05라고 가정하자.

```python
s_b = pd.Series([ int(i) for i in np.random.normal(70,8,(10,))],
                index = [datetime(2020, 1, 5)+timedelta(i) for i in range(0,10) ], 
                name = "B공장"  )
print(s_b)
# # 2020-01-05    67
# 2020-01-06    79
# 2020-01-07    67
# 2020-01-08    81
# 2020-01-09    69
# 2020-01-10    96
# 2020-01-11    65
# 2020-01-12    83
# 2020-01-13    52
# 2020-01-14    78
# Name: B공장, dtype: int64
```

```python
print(s_a+s_b)
# 2020-01-01      NaN
# 2020-01-02      NaN
# 2020-01-03      NaN
# 2020-01-04      NaN
# 2020-01-05    123.0
# 2020-01-06    128.0
# 2020-01-07    113.0
# 2020-01-08    133.0
# 2020-01-09    113.0
# 2020-01-10    154.0
# 2020-01-11      NaN
# 2020-01-12      NaN
# 2020-01-13      NaN
# 2020-01-14      NaN
# dtype: float64
```

* index 가 일치하는 부분에서는 연산이 되지만 둘중에 하나에 index가 없다면 `NaN` 값을 출력한다.




