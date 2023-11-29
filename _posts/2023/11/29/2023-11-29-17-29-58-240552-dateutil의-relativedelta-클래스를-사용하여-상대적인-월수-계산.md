---
layout: post
title: "[python] dateutil의 relativedelta 클래스를 사용하여 상대적인 월수 계산"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

파이썬에서는 `dateutil` 라이브러리의 `relativedelta` 클래스를 사용하여 상대적인 날짜 계산을 할 수 있습니다. `relativedelta` 클래스는 두 날짜 간의 차이를 구할 때 유용하게 사용됩니다. 특히, 상대적인 월의 간격을 계산하고 싶을 때 매우 유용합니다.

다음은 `relativedelta` 클래스를 사용하여 상대적인 월수를 계산하는 예제입니다:

```python
from dateutil.relativedelta import relativedelta
from datetime import datetime

start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 3, 1)

delta = relativedelta(end_date, start_date)

months_difference = delta.months + (delta.years * 12)
```

위의 예제에서, `start_date`와 `end_date`는 `datetime` 객체로 지정됩니다. 그런 다음, `relativedelta` 클래스를 사용하여 `end_date`에서 `start_date`를 빼서 두 날짜의 차이를 계산합니다. 날짜의 차이를 구하는 데에는 `months` 속성과 `years` 속성이 사용됩니다.

마지막으로, `months_difference` 변수는 월 수의 차이를 나타냅니다. 이를 계산하기 위해 `months` 속성과 `years` 속성을 조합하여 총 월 수를 계산합니다.

이제, 상대적인 월수를 계산하는 예제를 통해 `dateutil`의 `relativedelta` 클래스의 사용법에 대해 간단히 알아보았습니다. 이러한 기능을 사용하여 날짜 차이를 계산할 때 편리하게 활용할 수 있습니다.

참고 문서: [Python dateutil relativedelta - PyPI](https://pypi.org/project/python-dateutil/)