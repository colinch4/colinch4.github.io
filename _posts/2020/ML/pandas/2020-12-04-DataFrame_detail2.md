---
layout: post
title: "[pandas] DataFrame 심화 2"
description: " "
date: 2020-12-04
tags: [pandas]
comments: true
share: true
---

# 기본 DataFrame column (2)

> `pandas` 의 `DataFrame` 에 관한 `row`와 `column` 추가, 삭제등에 관한 내용에 대해서 알아본다.

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

![dataFrame_detail](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/dataFrame_detail.png?raw=true)



## column 추가( Series를 이용한 추가방법)

> `DataFrame`에 새로운 column을 추가하기 위해서는 추출 및 수정과 같이 `scalar`, `list`, `ndarray`를 사용할 수 있고 추가적으로  `Series` 도 사용할 수 있다. `scalar`, `list`, `ndarray` 는 추출 및 수정과 동일하므로 건너뛴다.

*  Series를 이용한 추가방법

```python
df['나이'] = pd.Series([20, 21, 22, 23, 24])
display(df)
```

![dataFrame_add1](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/dataFrame_add1.png?raw=true)

이렇게 그냥 `Series`값을 대입해 버리면 `NaN` (Not a Number) 값으로 나와버린다.

즉, 제대로 추가가 되지 않는다.  `column`을 제대로 추가하기 위해서는 `index` 값을 지정해주면 제대로 작동한다.

```python
df['나이'] = pd.Series([20, 21, 22, 23, 24],
                      index = ['one', 'two', 'three', 'four', 'five']) 
display(df)
```

![dataFrame_add2](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/dataFrame_add2.png?raw=true)



**그러면** `Series`를 사용하려면 `index`를 추가해야 하므로 `ndarray`나 `list`를 사용하는것보다 귀찮다고 느낄수 있다. **그러나** `Series`를 사용했을때 `ndarray`나 `list`와 달리 값을 주지 않는 곳에  `NaN` 값을 주면서 원하는 `index` 위치에만 값을 줄 수 있다.

```python
df['나이'] = pd.Series([20, 22,  24],
                    index=['one','three','five']) 
display(df)
```

![dataFrame_add3](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/dataFrame_add3.png?raw=true)



## column 추가(연산을 통한 추가방법)

> 연산을 통해 column을 추가 할 수 있다.

```python
print(df['학점'] > 3.0)
# one      False
# two      False
# three     True
# four     False
# five     False
# Name: 학점, dtype: bool     : Series
df['장학생여부'] = df['학점'] > 3.0
display(df)
```

![dataFrame_add4](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/dataFrame_add4.png?raw=true)



## column 삭제

> column 뿐만 아니라 row를 삭제 할때 모두 `drop`이라는 method를 사용한다.
>
> option으로는 `axis`와 `inplace`가 들어간다.
>
> `axis` 로 행과 열을 선택할 수 있고 `inplace` (`False`/`True`)로 원본을 보존하고 삭제된 결과를 새로 만들지(`False`) 아니면 원본을 지울지(`True`)  결정한다.

```python
display(df.drop('등급', axis=1, inplace=False)) # 등급이 사라진다.
```

![dataFrame_add5](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/dataFrame_add5.png?raw=true)

```python
df.drop(['학년', '등급'], axis=1, inplace=True)
display(df)
```

![dataFrame_detail6](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/dataFrame_detail6-1599838174568.png?raw=true)