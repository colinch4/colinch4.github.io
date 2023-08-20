---
layout: post
title: "[pandas] DataFrame loc"
description: " "
date: 2020-12-04
tags: [pandas]
comments: true
share: true
---

## DataFrame.loc

> 위의 목차에서 [DataFrame의 row와 column 차이](./pandas/r_c_difference.md)를 보면 `DataFrame`의 `row`와 `column`을 다룰 때 작동하는것이 있고 작동하지 않는 방법이 있었다. 이를 해결해 주는 방법이 `pandas` `DataFrame`의 `loc`나 `iloc`를 이용하는 방법이 있다. 여기서는 `loc`에 대해서 다루기로 한다.

* `loc`를 사용함에 있어서 가장 쉽게 생각해는 방법은 2차원으로 생각하는 방법이다.
* 일반적으로 문자로 이루어진 `columns`와 `index`를 이용한다.
* `loc`를 사용하면 `Series` 또는 `DataFrame`으로 불러온다.
* 숫자를 사용한 indexing이나 slicing은 할 수 없다.(이것은 `iloc`를 사용하면 된다.)
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

> 우리가 지정해 둔 `index`를 사용해 indexing을 하면 `DataFrame`이 아닌 다음과 같이 `Series`로 return하게 된다. 이것은 `fancy indexing` 또는 `Boolean indexing`을 사용하면 해결된다.



* 기본 indexing

```python
print(df.loc['three'])      # Series
## 학과     철학
## 이름    홍길동
## 학점    3.1
## 학년      2
## 등급    NaN
## Name: three, dtype: object
```



* fancy indexing

```python
display(df.loc[['three']])  # DataFrame
```

![image-20200913000920671](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913000920671.png?raw=true)



* Boolean indexing

```python
display(df.loc[df['이름']=='홍길동'])
```

![image-20200913000920671](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913000920671.png?raw=true)



## 원하는 열 DataFrame으로 추출하기

> `DataFrame`으로 `column`을 추출하기 위해서는 `row`추출과 마찬가지로 `fancy indexing` 을 사용하면 된다. 

* 기본 indexing

```python
display(df.loc[:,'학점'])    # Series
## one      1.5
## two      2.0
## three    3.1
## four     1.1
## five     2.7
## Name: 학점, dtype: float64
```



* fancy indexing

```python
display(df.loc[:,['학점']])
```

![image-20200913002339558](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913002339558.png?raw=true)



## loc 예제

##### Q1. 학점이 1.5점을 초과하는 학생의 이름과 학점을 DataFrame으로 출력하세요.

```python
display(df.loc[df['학점']>1.5, ['학점','이름']])
```

![image-20200913003615336](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913003615336.png?raw=true)

##### Q2. 이름이 '박동훈'인 사람을 찾아 이름과 학점을 DataFrame으로 출력하세요.

```python
display(df.loc[df['이름']=='박동훈',['학점', '이름']])
```

![image-20200913003848319](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913003848319.png?raw=true)

##### Q2. 이름이 '박동훈'인 사람을 찾아 이름과 학점을 DataFrame으로 출력하세요.

```python
display(df.loc[df['이름']=='박동훈',['학점', '이름']])
```



##### Q3.  학점이 1.5 초과이고 2.5 미만인 모든 사람을 찾아서 학과, 이름, 학점을 DataFrame으로 출력하세요.

```python
display(df.loc[(df['학점']>1.5) & (df['학점']<2.5),'학과':'학점'])
```

![image-20200913004836096](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913004836096.png?raw=true)



##### Q4.  학점이 3.0 초과하는 사람을 찾아서 등급을 'A'로 설정한 후 출력하세요.

```python
df.loc[df['학점']>3.0,'등급']='A'
display(df)
```

![image-20200913005041434](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200913005041434.png?raw=true)