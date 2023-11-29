---
layout: post
title: "[python] dateutil의 relativedelta 클래스를 사용하여 주어진 날짜와의 차이 계산"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Python에서는 날짜 계산을 쉽게 할 수 있는 dateutil이라는 유용한 라이브러리가 있습니다. 이 라이브러리의 `relativedelta` 클래스를 사용하면 주어진 날짜와의 차이를 계산할 수 있습니다. 이 포스트에서는 `relativedelta` 클래스를 사용하여 주어진 날짜와의 차이를 계산하는 방법에 대해 알아보겠습니다.

먼저, `relativedelta` 클래스를 사용하기 위해서는 `dateutil` 모듈을 설치해야 합니다. 아래 명령을 사용하여 설치할 수 있습니다.

```python
pip install python-dateutil
```

`relativedelta` 클래스를 사용하여 날짜와의 차이를 계산하려면 다음과 같은 단계를 따릅니다.

1. `dateutil` 모듈을 가져옵니다.

```python
from dateutil.relativedelta import relativedelta
```

2. 주어진 날짜와 비교할 날짜를 생성합니다.

```python
import datetime

given_date = datetime.datetime(2022, 12, 31)
comparison_date = datetime.datetime(2021, 1, 1)
```

3. `relativedelta` 클래스를 사용하여 주어진 날짜와의 차이를 계산합니다.

```python
difference = relativedelta(given_date, comparison_date)
```

`difference` 객체에는 주어진 날짜와의 차이에 대한 정보가 포함되어 있습니다. 예를 들어, `difference.years`를 사용하면 주어진 날짜와의 차이의 연도 부분을 얻을 수 있습니다. 마찬가지로, `difference.months`, `difference.days`, `difference.hours` 등을 사용하여 다른 차이 정보를 얻을 수 있습니다.

아래는 예제 코드입니다.

```python
from dateutil.relativedelta import relativedelta
import datetime

given_date = datetime.datetime(2022, 12, 31)
comparison_date = datetime.datetime(2021, 1, 1)

difference = relativedelta(given_date, comparison_date)

print(f"Years difference: {difference.years}")
print(f"Months difference: {difference.months}")
print(f"Days difference: {difference.days}")
```

위 코드를 실행하면 다음과 같은 결과를 얻을 수 있습니다.

```
Years difference: 1
Months difference: 11
Days difference: 30
```

이처럼, `relativedelta` 클래스를 사용하면 주어진 날짜와의 차이를 쉽게 계산할 수 있습니다. `relativedelta` 클래스에 대한 자세한 내용은 [공식 문서](https://dateutil.readthedocs.io/en/stable/relativedelta.html)를 참조하십시오.