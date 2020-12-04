---
layout: post
title: "[pandas] DataFrame 함수 3"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---


# DataFrame의 분석을 위한 함수들(3)

> `Pandas`에 있는 `DataFrame`에 관한 함수들에 대해서 알아본다.



## 1. apply

> 직접 정의한 `lambda`를 이용해 `행 ` 또는 `열`에 관한 `Series`를 **return**한다.

![image-20200913231606212](markdown-images/image-20200913231606212.png)

```python
my_func = lambda c : c.max()-c.min()
print(df.apply(my_func,axis=0))
# A    6
# B    9
# C    9
# D    7
# dtype: int64
```

```python
my_func = lambda r : r.max() + r.min()
print(df.apply(my_func,axis=1))
# 2020-01-01    14
# 2020-01-02     7
# 2020-01-03    11
# 2020-01-04     7
# 2020-01-05    13
# 2020-01-06     7
# Freq: D, dtype: int64
```

