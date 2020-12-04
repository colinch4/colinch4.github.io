---
layout: post
title: "[pandas] DataFrame row"
description: " "
date: 2020-12-04
tags: [pandas]
comments: true
share: true
---

# 기본 DataFrame row

> Dataframe의 `row`와 `column` 처리 방법에는 어느정도 차이가 존재한다. 

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

## 기본적인 column 추출 방법

* 단일 `row` indexing : 지원하지 않는다.

```python
print(df['one'])   # Error
print(df[0])	   # Error
```



* slicing : `row`에 관해서 가능하다.

```python
display(df['one':'three'])
```

![image-20200912015639818](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200912015639818.png?raw=true)

```python
display(df[0:3])   # 위와 동일한 값을 추출한다.(column에 대해서 하지 않는다.)
```

![image-20200912015724200](https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/ML/markdown-images/image-20200912015724200.png?raw=true)

* fancy indexing : 지원하지 않는다.

```python
display(df[[0,2]])   # Error
```

