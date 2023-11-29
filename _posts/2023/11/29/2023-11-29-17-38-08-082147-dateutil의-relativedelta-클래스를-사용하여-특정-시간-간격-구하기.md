---
layout: post
title: "[python] dateutil의 relativedelta 클래스를 사용하여 특정 시간 간격 구하기"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

하나의 날짜나 시간에서 다른 날짜나 시간까지의 시간 간격을 계산해야 할 때가 있습니다. Python에서는 dateutil 라이브러리의 relativedelta 클래스를 사용하여 이를 수행할 수 있습니다. relativedelta 클래스는 timedelta 클래스와 유사하며, 날짜, 시간의 연산을 보다 쉽게 수행할 수 있도록 도와줍니다.

## dateutil 설치하기
먼저, dateutil 라이브러리를 설치해야 합니다. 다음 명령어를 사용하여 설치할 수 있습니다:

```
pip install python-dateutil
```

## relativedelta로 특정 시간 간격 구하기
relativedelta 클래스는 두 개의 날짜나 시간을 인자로 받아서 그 사이의 시간 간격을 계산합니다. 다음은 relativedelta 클래스를 사용하여 특정 시간 간격을 구하는 예제입니다:

```python
from dateutil.relativedelta import relativedelta
from datetime import datetime

start_date = datetime(2021, 1, 1)
end_date = datetime(2021, 12, 31)

delta = relativedelta(end_date, start_date)

print(delta.years)  # 0
print(delta.months)  # 11
print(delta.days)  # 30
```

위 예제에서는 start_date와 end_date를 datetime 객체로 생성한 후, relativedelta 클래스의 인자로 전달하여 delta 객체를 구합니다. delta 객체에는 years, months, days 등의 속성이 있으며, 이를 통해 특정 시간 간격을 구할 수 있습니다.

## 다양한 시간 간격 계산하기
relativedelta 클래스는 다양한 시간 간격을 계산할 수 있는 속성들을 제공합니다. 아래는 주요 속성들의 목록입니다:

- years: 연 수
- months: 월 수
- days: 일 수
- hours: 시간 수
- minutes: 분 수
- seconds: 초 수
- microseconds: 마이크로초 수

이 속성들을 사용하여 원하는 특정 시간 간격을 계산할 수 있습니다. 예를 들어, 3년 2개월 10일 이후의 날짜를 구하고 싶다면 다음과 같이 코드를 작성할 수 있습니다:

```python
from dateutil.relativedelta import relativedelta
from datetime import datetime

start_date = datetime(2021, 1, 1)

delta = relativedelta(years=3, months=2, days=10)

end_date = start_date + delta

print(end_date)  # 2024-03-11 00:00:00
```

위 코드에서는 start_date에 2021년 1월 1일을 설정한 후, relativedelta 클래스의 인자로 years=3, months=2, days=10을 전달하여 delta 객체를 생성합니다. 그리고 start_date와 delta를 더하여 end_date를 구하고 출력합니다.

## 참고 자료
- dateutil 라이브러리 공식 문서: [https://dateutil.readthedocs.io/en/stable/](https://dateutil.readthedocs.io/en/stable/)
- 파이썬 datetime 모듈 공식 문서: [https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)