---
layout: post
title: "[pandas] 중복행 처리"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---


# 중복행 처리

> `duplicated`를 통해 boolean mask를 추출해 중복행 처리하는 방법에 대해서 알아본다. 다음의 예제를 사용한다.

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({'k1':['one']* 3 +['two']*4+['three'],
                   'k2':[1,1,2,3,3,4,4,5]})
display(df)
```

![image-20200917153219940](markdown-images/image-20200917153219940.png)



## 1. duplicated()

> 중복행 추출하는 방법에 대해서 알아본다.

```python
print(df.duplicated())
# 0    False
# 1     True
# 2    False
# 3    False
# 4     True
# 5    False
# 6     True
# 7    False
# dtype: bool

# 1행 부터 내려가면서 중복값이 있었으면 True 없었으면 False 값을 갖는다.
```

```python
display(df.loc[df.duplicated(),:]) # 중복행만 추출한다.
```

![image-20200917153414890](markdown-images/image-20200917153414890.png)



## 2. drop_duplicates()

> 중복행을 제거하는 방법에 대해서 알아본다.

```python
display(df.drop_duplicates())
```

![image-20200917153133432](markdown-images/image-20200917153133432.png)

