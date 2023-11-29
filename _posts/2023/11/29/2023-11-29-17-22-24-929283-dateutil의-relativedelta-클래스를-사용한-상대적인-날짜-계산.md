---
layout: post
title: "[python] dateutil의 relativedelta 클래스를 사용한 상대적인 날짜 계산"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

## 개요
날짜와 시간을 다룰 때 종종 상대적인 날짜 계산이 필요한 경우가 있습니다. 예를 들어, "현재 날짜로부터 2달 후의 날짜는 언제인가?"와 같은 질문에 대한 답을 구할 때 상대적인 날짜 계산이 필요합니다. 이러한 상대적인 날짜 계산을 간편하게 해주는 도구 중 하나가 Python의 `dateutil` 패키지에 포함된 `relativedelta` 클래스입니다. 이번 포스트에서는 `relativedelta` 클래스의 사용법에 대해 알아보겠습니다.

## `relativedelta` 클래스란?
`relativedelta` 클래스는 `dateutil` 패키지에 포함된 클래스로, 날짜와 시간을 상대적으로 계산하는 데 사용됩니다. 이 클래스는 `datetime` 모듈에서 제공하는 `timedelta` 클래스와 유사하지만, 더욱 강력한 상대적인 계산 기능을 제공합니다.

## `relativedelta` 클래스 사용법
`relativedelta` 클래스를 사용하기 위해서는 먼저 `dateutil` 패키지를 설치해야 합니다. 설치는 아래의 커맨드를 사용하여 진행할 수 있습니다.

```python
pip install python-dateutil
```

`dateutil` 패키지를 설치한 후에는 다음과 같은 방법으로 `relativedelta` 클래스를 사용할 수 있습니다.

```python
from dateutil.relativedelta import relativedelta
from datetime import datetime

current_date = datetime.now()
next_date = current_date + relativedelta(months=2)
```

위의 코드에서는 `relativedelta` 클래스의 인스턴스를 생성하여 원하는 상대적인 시간 간격을 지정한 후, 이를 날짜에 더해주는 방식으로 상대적인 날짜 계산을 수행하고 있습니다. 위 코드에서는 현재 날짜로부터 2달 후의 날짜를 `next_date` 변수에 저장하고 있습니다.

## 다양한 상대적인 시간 간격 지정 방법
`relativedelta` 클래스를 사용할 때는 다양한 상대적인 시간 간격을 지정하는 옵션들을 사용할 수 있습니다. 몇 가지 예를 들어보면 다음과 같습니다.

- `years`: 상대적인 연도
- `months`: 상대적인 월
- `weeks`: 상대적인 주
- `days`: 상대적인 일
- `hours`: 상대적인 시간
- `minutes`: 상대적인 분
- `seconds`: 상대적인 초
- `microseconds`: 상대적인 마이크로초

이 외에도 상대적인 날짜 계산에 활용할 수 있는 다양한 옵션들이 있으니 필요에 따라 적절한 옵션을 선택하여 사용하면 됩니다.

## 결론
Python의 `dateutil` 패키지에 포함된 `relativedelta` 클래스를 사용하면 상대적인 날짜 계산을 간편하게 수행할 수 있습니다. 이를 활용하여 날짜와 시간을 다루는 프로그램을 구현할 때 유용하게 활용할 수 있습니다.

## 참고 자료
- `dateutil` 패키지 공식 문서: [https://dateutil.readthedocs.io/](https://dateutil.readthedocs.io/)