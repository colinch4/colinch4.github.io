---
layout: post
title: "[pandas] DataFrame 기본"
description: " "
date: 2020-12-04
tags: [pandas]
comments: true
share: true
---

# DataFrame

> `DataFrame`은 `Series`의 집합으로 구성된다. 각각의 `column`이 `Series`에 해당한다. 또한 2차원이다.



## Dictionary를 이용한 DataFrame 생성

> dictionary의 `key`값이 `column`이 된다. 다음의 예를 봐보자.

```python
import numpy as np
import pandas as pd

data = {'name' : ['홍길동','김연아','홍길동','강감찬','이순신'],
        'year' : [2015, 2019, 2020, 2013, 2017],
        'point': [3.5, 1.5, 2.0, 3.4, 4.0]  }

# DataFrame 생성
df = pd.DataFrame(data)
print(df)
#  name  year  point
# 0  홍길동  2015    3.5
# 1  김연아  2019    1.5
# 2  홍길동  2020    2.0
# 3  강감찬  2013    3.4
# 4  이순신  2017    4.0  
```

* `DataFrame`을 출력할때 `print`를 사용하면  형태가 별로 좋지 않다.

  `jupyter notebook`에서는 `print` 대신에 `display`  함수를 지원해준다.

	```python
	display(df)
	```

![dict_dataframe](markdown-images/dict_dataframe-1599670078274.PNG)

* `DataFrame`은 기본적인 크기속성 `shape`, `size`, `ndim`을 지닌다.

  ```python
  print(df.shape)     # (5, 3)
  print(df.size)	    # 15
  print(df.ndim)  	# 2
  ```




* `DataFrame`의 구성요소 `index`, `columns`, `values` 값들을 확인해 볼 수 있다.

  ```python
  print(df.index)     # RangeIndex(start=0, stop=5, step=1)
  print(df.columns)   # Index(['name', 'year', 'point'], dtype='object')
  print(df.values)
  # [['홍길동' 2015 3.5]   : 2차원 ndarray 
  #  ['김연아' 2019 1.5]
  #  ['홍길동' 2020 2.0]
  #  ['강감찬' 2013 3.4]
  #  ['이순신' 2017 4.0]]
  ```

* `DataFrame`의 `index`와 `columns`에 `name`속성을 추가할 수 있다.

  ```python
  df.index.name = "학번"
  df.columns.name = "학생정보"
  display(df)
  ```

  ![dict_dataframe1](markdown-images/dict_dataframe1.PNG)



## CSV파일을 이용한 DataFrame 생성

> `csv` 파일을 이용해서 `pandas.DataFrame`을 만들 수 있다. root directory가 `c:/notebook_dir`
>
> 이고 data파일들을 `c:/notebook_dir/data` 에서 관리하므로 이 폴더안에 `student.csv`를 생성한다.

##### 참고 : csv파일의 data는 `,`로 구분한다.

* `csv` 파일에 다음과 같이 입력한다.

	```csv
	이름,입합연도,성적
	아이유,2015,1.5
	김연아,2016,2.0
	홍길동,2019,3.0
	강감찬,2020,3.7
	이순신,2017,3.9
	```

* jupyter notebook에서 `csv`파일을 `pandas`를 이용해 불러오자.

  ```python
  import pandas as pd
  
  df = pd.read_csv('./data/student.csv')
  display(df)
  ```
  
  ![csv_dataframe](markdown-images/csv_dataframe.PNG)

#####  참고 : 자료의 크기가 클때 `display(df.head())`와 `display(df.tail())` 을 이용해 위에서 5개, 아래에서 5개 자료를 확인할 수 있다.



## Database를 이용한 DataFrame 생성