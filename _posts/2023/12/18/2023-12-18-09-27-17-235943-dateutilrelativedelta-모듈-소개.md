---
layout: post
title: "[python] dateutil.relativedelta 모듈 소개"
description: " "
date: 2023-12-18
tags: [python]
comments: true
share: true
---

파이썬에서 날짜와 시간을 다루다 보면 날짜 간의 차이를 계산하거나, 특정한 날짜에 대해 상대적인 날짜를 계산해야 하는 경우가 많습니다. 이러한 작업을 손쉽게 처리할 수 있도록 **dateutil.relativedelta** 모듈이 유용하게 활용됩니다. 이 모듈은 파이썬 내장 모듈인 *datetime*과 함께 사용되며, 상대적인 시간 간격을 다루는 데 도움을 줍니다.

## 모듈 임포트

```python
from dateutil.relativedelta import relativedelta
```

## 기능

**relativedelta** 모듈은 기본 *datetime* 모듈의 **timedelta** 클래스와 유사한 기능을 제공하지만, 더 유연하고 강력한 기능을 제공합니다. 상대적인 날짜 연산을 처리할 때 주로 사용되며, 다음과 같은 기능을 지원합니다.

- 연, 월, 일 단위로 날짜 연산 수행
- 날짜에 변수를 추가하거나 제외하는 유연한 기능 제공
- 날짜 계산 시 반올림 및 버림 설정 가능

## 사용 예시

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()
future_date = now + relativedelta(months=+3, days=+15)
```

위의 예시에서, **relativedelta** 모듈을 사용하여 현재 날짜에 3개월과 15일을 더한 날짜를 계산했습니다.

**relativedelta** 모듈을 이용하면 날짜 및 시간과 관련된 다양한 복잡한 연산을 간편하게 수행할 수 있습니다.

---

참고 문헌:
- [Python dateutil - relativedelta documentation](https://dateutil.readthedocs.io/en/stable/relativedelta.html)