---
layout: post
title: "[numpy] astype"
description: " "
date: 2020-12-04
tags: [numpy]
comments: true
share: true
---

# Numpy 기타(astype,)

>  `numpy` 에 대한 나머지 사항들에 알아본다.



## astype

> `numpy`의 dtype을 변화시킨다.

```python
arr = np.array([1.5, 2.3, 8.3, 9.8, 7.7], dtype=object)
print(arr)        # [1.5 2.3 8.3 9.8 7.7]
print(arr.dtype)  # object
arr1 = arr.astype(np.int32)  # 다시 정의 해주어야 한다.
print(arr1.dtype) # int32

arr2 = arr.astype(np.float64)
print(arr2.dtype) # float64
```

