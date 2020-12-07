---
layout: post
title: "[pandas] DataFrame 함수 2"
description: " "
date: 2020-12-04
tags: [pandas]
comments: true
share: true
---


# DataFrame의 분석을 위한 함수들(2)

> `Pandas`에 있는 `DataFrame`에 관한 함수들에 대해서 알아본다.

## 1. sort

> `DataFrame`을 정렬하기 위해서는 두가지 방법만 알아두면 된다.

예제로 다음의 `DataFrame`을 사용한다.

![image-20200913222532257](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913222532257.png?raw=true)

* `sort_index` : `index` 기준(`values`가 아닌)으로 정렬한다. 옵션으로 `axis`와 `ascending`을 줄 수 있다.

```python
display(df.sort_index()) # option default : axis = 0, ascending = True
```

![image-20200913222834178](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913222834178.png?raw=true)

```python
display(df.sort_index(ascending=False)) # 내림차순
```

![image-20200913223007690](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913223007690.png?raw=true)

```python
display(df.sort_index(axis = 1 ,ascending = False)) # column 내림차순
```

![image-20200913224145954](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913224145954.png?raw=true)

* `sort_values`  : `values`기준(`index`가 아닌)으로 정렬한다. 옵션으로 `axis`, `ascending`과 `by`를 줄 수 있다. `index`의 순서는 바뀌지 않는다.

```python
display(df.sort_values(by='B'))  # B 값들의 오름차순 기준으로 정렬한다.
```

![image-20200913224704601](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913224704601.png?raw=true)

```python
display(df.sort_values(by=['B','D'])) # B값 다음으로 D값들의 기준으로 정렬한다.
```

![image-20200913224846149](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913224846149.png?raw=true)



## 2. unique

> `DataFrame`의 행이나 열을 뽑아내 (즉,  `Series`로 뽑아진것)  유일한 성분들을 `list`를 배출한다.

![image-20200913225936117](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913225936117.png?raw=true)

```python
print(df.iloc[1,:].unique())
# [0 1 7]
print(df['B'].unique())
# [8 0 9 2 7]
```



## isin

> `DataFrame`의 행이나 열에 (즉,  `Series`안에) 어떠한 성분들이 들어 있는지 없는지 `True/False`로 구성된 `Series`로 배출한다.

```python
print(df['A'].isin([1]))
# 2020-09-13    False
# 2020-09-14    False
# 2020-09-15    False
# 2020-09-16    False
# 2020-09-17    False
# 2020-09-18     True
# Freq: D, Name: A, dtype: bool
```



## 3. value_counts

> `DataFrame`의 행이나 열을 뽑아내 (즉,  `Series`로 뽑아진것)  성분들의 개수를 `Series`를 배출한다.

![image-20200913225936117](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913225936117.png?raw=true)

```python
print(df.iloc[1].value_counts())
# 0    2
# 7    1
# 1    1
# Name: 2020-09-14 00:00:00, dtype: int64
```