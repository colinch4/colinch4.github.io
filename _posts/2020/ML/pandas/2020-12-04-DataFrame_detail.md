---
layout: post
title: "[pandas] DataFrame 심화 1"
description: " "
date: 2020-12-04
tags: [머신러닝]
comments: true
share: true
---

# 기본 DataFrame column (1)

> `pandas` 의 `DataFrame` 에 관한 `row`와 `column` 추출,수정등에 관한 내용에 대해서 알아본다.

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

![dataFrame_detail](markdown-images/dataFrame_detail.PNG)



## 기본적인 단일 column 추출 방법

> 대체로 두가지 방법이 사용된다.  출력됐을때 `Series`로 추출된다.

```python
print(df['이름'])
# one      이지은
# two      박동훈
# three    홍길동
# four     강감찬
# five     오해영
# Name: 이름, dtype: object
```

```python
print(df.이름)
# one      이지은
# two      박동훈
# three    홍길동
# four     강감찬
# five     오해영
# Name: 이름, dtype: object
```

위의 예제를 살펴보면 `df['이름']` 과 같이 일반적인 방법으로도 `column`을 추출할수 있지만 `df`의 속성으로 생각해 `df.이름`와 같이 입력해서도 추출할 수 있다.

**하지만**, 굳이 `df.이름 ` 를 사용해 추출하는것 보다 `df['이름']`를 사용하는것이 권장된다.



그렇다면, 만약 추출된 `Series`의 값을 변경하면 어떻게 될까?

`Series`의 내용을 변경하면 원래의 `DataFrame` 도 함께 변경된다.

```python
name = df['이름']
name['one'] = '아이유'
display(df)
```

![dataFrame_detail1](markdown-images/dataFrame_detail1.PNG)



## 기본적인 다수 column 추출 방법

column을 추출할때 가능한 방법이 있고 불가능한 방법들이 있다. 또한, `return`시 `DataFrame`으로 추출된다.

* fancy indexing

```python
display(df[['학과','학점']])
```

  ![dataFrame_detail2](markdown-images/dataFrame_detail2.PNG)

* index 명을 이용한 slicing : 가능하지 않다

```python
display(df['학과':'학점'])   # KeyError: '학과'
```



## 단일 column값 수정하는 방법

> column을 추출해 **scalar, array, list**를 이용해서 수정할 수 있다.

![dataFrame_detail](markdown-images/dataFrame_detail.PNG)

위의 `DataFrame`이 계속 주어져 있다고 가정하자.

* 단일값 이용 : `broadcasting` 되서 모두에게 적용된다.

```python
df['등급']='A'
display(df)
```

![dataFrame_detail3](markdown-images/dataFrame_detail3.PNG)



* `numpy`의 `nparray`를 이용 :  알맞은 크기의 `ndarray`를 입력해주면 된다.

```python
df['등급'] = np.array(['A', 'B', 'A', 'D', 'F'])
display(df)
```

![dataFrame_detail4](markdown-images/dataFrame_detail4.PNG)

* python `list`를 이용 : 알맞은 크기의 list를 입력해준다.

```python
df['등급'] = ['A', 'B', 'A', 'D', 'F']
display(df)
```

![dataFrame_detail4](markdown-images/dataFrame_detail4.PNG)



## 다수 column값 수정하는 방법

> 단일 column 수정과 다르지 않다.  마찬가지로 scalar, array, list**를 이용해서 수정할 수 있다.

![dataFrame_detail](markdown-images/dataFrame_detail.PNG)

* 단일값 이용 :  : `broadcasting` 되서 모두에게 적용된다.

```python
df[['학과','등급']] = 'A'
display(df)
```

![dataFrame_detail5](markdown-images/dataFrame_detail5.PNG)

* python `list`를 이용 :  대체로 이중 `list`를 이용한다.

```python
df[['학과','등급']] = [['영어영문','A'],
                       ['철학','C'],
                       ['국어국문','B'],
                       ['화학','F'],
                       ['물리','C']]
display(df)
```

![dataFrame_detail6](markdown-images/dataFrame_detail6.PNG)

* `numpy`의 `ndarray`를 이용

```python
df[['학과','등급']] = np.array([['영어영문','A'],
                       		  ['철학','C'],
	                          ['국어국문','B'],
       		                  ['화학','F'],
              		          ['물리','C']])
display(df)
```

![dataFrame_detail6](markdown-images/dataFrame_detail6.PNG)