---
layout: post
title: "[pandas] DataFrame iloc"
description: " "
date: 2020-12-04
tags: [pandas]
comments: true
share: true
---

## DataFrame.iloc

> `loc`와 달리 `iloc`를 사용하면 숫자 `index`를 사용해서 `DataFrame`의 정보를 불러올 수 있다.

* `iloc`를 사용함에 있어서 가장 쉽게 생각해는 방법은 2차원으로 생각하는 방법이다.

* `iloc`를 사용하면 `Series` 또는 `DataFrame`으로 불러온다.

* `row`와 `column` 동시에 `fancy indexing`이 가능하다.

대부분의 예제로 다음의 `data`를 사용한다.

```python
import pandas as pd
import numpy as np

data = {'이름':['이지은', '박동훈', '홍길동', '강감찬', '오해영'],
        '학과':['컴퓨터', '기계','철학', '컴퓨터', '철학'],
        '학년':[1, 2, 2, 4, 3],
        '학점':[1.5, 2.0, 3.1, 1.1, 2.7]
       }
df = pd.DataFrame(data, 
                  columns = ['학과', '이름', '학점', '학년', '등급'],
                  index = ['one', 'two', 'three', 'four', 'five'])

display(df)
```



## 원하는 행 DataFrame으로 추출하기

> 우리가 `index`를 사용해 indexing을 하면 `DataFrame`이 아닌 다음과 같이 `Series`로 return하게 된다. 이것은 `fancy indexing`을 사용하면 해결된다.



* 기본 indexing


```python
print(df.iloc[1])      # Series
학과     기계
## 이름    박동훈
## 학점      2
## 학년      2
## 등급    NaN
## Name: two, dtype: object
```



* fancy indexing

```python
display(df.iloc[[1]])   # DataFrame
```

![image-20200913012002630](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913012002630.png?raw=true)

## 원하는 열 DataFrame으로 추출하기

> `DataFrame`으로 `column`을 추출하기 위해서는 `row`추출과 마찬가지로 `fancy indexing` 을 사용하면 된다. 

* 기본 indexing

```python
display(df.loc[:,'학점'])    # Series
## # one      이지은
## two      박동훈
## three    홍길동
## four     강감찬
## five     오해영
## Name: 이름, dtype: object
```

* fancy indexing

```python
display(df.loc[:,['학점']])
```

![image-20200913012425896](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913012425896.png?raw=true)