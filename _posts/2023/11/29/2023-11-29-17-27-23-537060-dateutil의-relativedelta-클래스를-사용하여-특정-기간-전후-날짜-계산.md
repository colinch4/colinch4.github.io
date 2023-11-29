---
layout: post
title: "[python] dateutil의 relativedelta 클래스를 사용하여 특정 기간 전후 날짜 계산"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

파이썬을 사용하여 날짜 계산을 수행해야 하는 경우, `dateutil` 라이브러리의 `relativedelta` 클래스를 사용할 수 있습니다. `relativedelta` 클래스는 날짜 기반의 연산을 수행하는 강력한 도구이며, 특정 기간 전후의 날짜를 쉽게 계산할 수 있습니다.

다음은 `relativedelta` 클래스를 사용하여 특정 기간 전후의 날짜를 계산하는 예제입니다.

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 현재 날짜 가져오기
now = datetime.now()

# 1달 전 날짜 계산
one_month_ago = now - relativedelta(months=1)

# 3년 후 날짜 계산
three_years_later = now + relativedelta(years=3)

# 2주 전 날짜 계산
two_weeks_ago = now - relativedelta(weeks=2)

# 5일 후 날짜 계산
five_days_later = now + relativedelta(days=5)

print("1달 전:", one_month_ago)
print("3년 후:", three_years_later)
print("2주 전:", two_weeks_ago)
print("5일 후:", five_days_later)
```

위의 예제에서는 `datetime.now()` 함수를 사용하여 현재 날짜를 얻어온 후, `relativedelta` 클래스를 이용하여 원하는 기간만큼 날짜를 계산합니다. 이때, `months=1`과 같이 인자를 전달하여 원하는 기간을 지정할 수 있습니다.

위의 예제를 실행하면 현재 날짜를 기준으로 1달 전, 3년 후, 2주 전, 5일 후의 날짜가 출력됩니다.

`relativedelta` 클래스를 사용하면 날짜 계산을 쉽고 간편하게 수행할 수 있습니다. `relativedelta` 클래스에 대한 더 자세한 내용은 공식 문서를 참조하시기 바랍니다.

**참고 자료:**
- `dateutil` 공식 문서: [https://dateutil.readthedocs.io/](https://dateutil.readthedocs.io/)
- `datetime` 모듈 공식 문서: [https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)